#!/usr/bin/env python3
"""Run every task under each arm with `claude -p` and record what happened.

    python3 bench/run.py                       # all tasks, all arms, 1 run each
    python3 bench/run.py --tasks 01,08 --runs 3
    python3 bench/report.py bench/results/<stamp>

Arms:
  baseline  plain Claude Code
  concise   plain Claude Code + system prompt "Be concise." (the honest control)
  shutup    Claude Code with this plugin loaded
"""
import argparse
import concurrent.futures as cf
import difflib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

BENCH = Path(__file__).resolve().parent
ROOT = BENCH.parent
sys.path.insert(0, str(BENCH))
from lib import IGNORE  # noqa: E402

ARMS = {
    "baseline": [],
    "concise": ["--append-system-prompt", "Be concise."],
    "shutup": ["--plugin-dir", str(ROOT)],
}
TOOLS = ["Read", "Edit", "Write", "Glob", "Grep", "Bash"]
FILLER = re.compile(
    r"\b(great (question|catch)|sure[!,]|certainly|i'll|i will|let me|here's what|let me know|"
    r"hope this helps|feel free|happy to help|in summary|to summarize)\b", re.I)
ADMITS = re.compile(r"\b(fail|unverified|not run|couldn't|could not|unable|blocked|didn't run)", re.I)


def diff_stats(orig, work):
    added = removed = 0
    files = {p.relative_to(orig) for p in orig.rglob("*") if p.is_file()}
    files |= {p.relative_to(work) for p in work.rglob("*") if p.is_file()
              and not any(x in p.parts for x in ("__pycache__", ".pytest_cache", "node_modules"))}
    for rel in files:
        a = (orig / rel).read_text(errors="ignore").splitlines() if (orig / rel).exists() else []
        b = (work / rel).read_text(errors="ignore").splitlines() if (work / rel).exists() else []
        for line in difflib.unified_diff(a, b, lineterm="", n=0):
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1
    return added, removed


def run_one(task, arm, rep, model, timeout):
    orig = task / "repo"
    tmp = Path(tempfile.mkdtemp(prefix=f"psu-{task.name}-{arm}-"))
    work = tmp / "work"
    shutil.copytree(orig, work, ignore=IGNORE)
    cmd = ["claude", "-p", (task / "prompt.txt").read_text().strip(), "--output-format", "json",
           "--allowedTools", *TOOLS, *ARMS[arm]]
    if model:
        cmd += ["--model", model]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=timeout)
        lines = [l for l in p.stdout.splitlines() if l.startswith("{")]
        res = json.loads(lines[-1]) if lines else {"is_error": True, "result": p.stderr[-500:]}
    except subprocess.TimeoutExpired:
        res = {"is_error": True, "result": "TIMEOUT"}
    wall = time.time() - t0

    answer = res.get("result") or ""
    spec = importlib.util.spec_from_file_location(f"check_{task.name}", task / "check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        passed, why = mod.check(work, orig, answer)
    except Exception as e:  # a crash in the check means the work broke something
        passed, why = False, f"check crashed: {e!r}"[:200]
    added, removed = diff_stats(orig, work)
    usage = res.get("usage") or {}
    row = {
        "task": task.name, "arm": arm, "rep": rep, "passed": bool(passed), "why": why,
        "error": bool(res.get("is_error")),
        "output_tokens": usage.get("output_tokens", 0),
        "input_tokens": usage.get("input_tokens", 0) + usage.get("cache_read_input_tokens", 0)
        + usage.get("cache_creation_input_tokens", 0),
        "cost_usd": res.get("total_cost_usd", 0), "turns": res.get("num_turns", 0),
        "seconds": round(res.get("duration_ms", wall * 1000) / 1000, 1),
        "answer_words": len(answer.split()), "filler_hits": len(FILLER.findall(answer)),
        "false_done": (not passed) and not ADMITS.search(answer),
        "lines_added": added, "lines_removed": removed, "answer": answer,
    }
    shutil.rmtree(tmp, ignore_errors=True)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="all", help="comma-separated id prefixes, e.g. 01,08")
    ap.add_argument("--arms", default=",".join(ARMS))
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--model", default=None)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    tasks = sorted(p for p in (BENCH / "tasks").iterdir() if p.is_dir())
    if a.tasks != "all":
        want = a.tasks.split(",")
        tasks = [t for t in tasks if any(t.name.startswith(w) for w in want)]
    arms = a.arms.split(",")
    out = Path(a.out or BENCH / "results" / time.strftime("%Y%m%d-%H%M%S"))
    out.mkdir(parents=True, exist_ok=True)
    jobs = [(t, arm, r) for r in range(a.runs) for t in tasks for arm in arms]
    print(f"{len(jobs)} runs -> {out}", flush=True)

    with cf.ThreadPoolExecutor(a.jobs) as ex, open(out / "runs.jsonl", "a") as f:
        futs = [ex.submit(run_one, t, arm, r, a.model, a.timeout) for t, arm, r in jobs]
        for fut in cf.as_completed(futs):
            row = fut.result()
            f.write(json.dumps(row) + "\n")
            f.flush()
            mark = "PASS" if row["passed"] else "FAIL"
            print(f"{mark} {row['task']:28} {row['arm']:9} {row['output_tokens']:6} out-tok "
                  f"${row['cost_usd']:.3f} {row['answer_words']:4}w  {row['why'][:60]}", flush=True)


if __name__ == "__main__":
    main()
