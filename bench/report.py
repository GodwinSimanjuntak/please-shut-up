#!/usr/bin/env python3
"""Summarize a results dir: python3 bench/report.py bench/results/<stamp>"""
import json
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

d = Path(sys.argv[1])
rows = [json.loads(l) for l in open(d / "runs.jsonl")]
arms = [a for a in ("baseline", "concise", "shutup") if any(r["arm"] == a for r in rows)]
by = defaultdict(list)
for r in rows:
    by[r["arm"]].append(r)


def mean(xs):
    return st.mean(xs) if xs else 0


def cat(task):
    return task.split("-")[1]


out = [f"# Results ({len(rows)} runs, {len({r['task'] for r in rows})} tasks)", ""]
out += ["| metric | " + " | ".join(arms) + " |", "|---|" + "---|" * len(arms)]
metrics = [
    ("tasks passed (hidden tests)", lambda rs: f"{sum(r['passed'] for r in rs)}/{len(rs)}"),
    ("claimed done but failed", lambda rs: str(sum(r["false_done"] for r in rs))),
    ("final message, median words", lambda rs: f"{st.median([r['answer_words'] for r in rs]):.0f}"),
    ("filler phrases (total)", lambda rs: str(sum(r["filler_hits"] for r in rs))),
    ("output tokens, mean", lambda rs: f"{mean([r['output_tokens'] for r in rs]):,.0f}"),
    ("input tokens, mean", lambda rs: f"{mean([r['input_tokens'] for r in rs]):,.0f}"),
    ("cost per task, mean", lambda rs: f"${mean([r['cost_usd'] for r in rs]):.3f}"),
    ("turns, mean", lambda rs: f"{mean([r['turns'] for r in rs]):.1f}"),
    ("seconds, mean", lambda rs: f"{mean([r['seconds'] for r in rs]):.0f}"),
    ("lines added, total", lambda rs: str(sum(r["lines_added"] for r in rs))),
    ("lines removed, total", lambda rs: str(sum(r["lines_removed"] for r in rs))),
]
for name, fn in metrics:
    out.append(f"| {name} | " + " | ".join(fn(by[a]) for a in arms) + " |")

if "baseline" in arms:
    out += ["", "Change vs baseline:", ""]
    for a in arms:
        if a == "baseline":
            continue
        for key, label in [("answer_words", "final message words"), ("output_tokens", "output tokens"),
                           ("cost_usd", "cost")]:
            b, x = mean([r[key] for r in by["baseline"]]), mean([r[key] for r in by[a]])
            if b:
                out.append(f"- {a}: {label} {100 * (x - b) / b:+.0f}%")

out += ["", "## By category (passed / median words)", "",
        "| category | " + " | ".join(arms) + " |", "|---|" + "---|" * len(arms)]
for c in sorted({cat(r["task"]) for r in rows}):
    cells = []
    for a in arms:
        rs = [r for r in by[a] if cat(r["task"]) == c]
        cells.append(f"{sum(r['passed'] for r in rs)}/{len(rs)} · {st.median([r['answer_words'] for r in rs]):.0f}w"
                     if rs else "–")
    out.append(f"| {c} | " + " | ".join(cells) + " |")

out += ["", "## Failures", ""]
for r in sorted(rows, key=lambda r: (r["task"], r["arm"])):
    if not r["passed"]:
        out.append(f"- `{r['task']}` / {r['arm']}: {r['why']}")

text = "\n".join(out) + "\n"
(d / "report.md").write_text(text)
print(text)
