"""Helpers shared by the task checks. Checks run hidden tests on a copy of the
agent's work, so the agent can't see or edit them."""
import filecmp
import shutil
import subprocess
import tempfile
from pathlib import Path

IGNORE = shutil.ignore_patterns("__pycache__", ".pytest_cache", "node_modules", ".git")


def sh(cmd, cwd, timeout=60):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def _hidden(work, name, src, cmd):
    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(work, t, dirs_exist_ok=True, ignore=IGNORE)
        Path(t, name).write_text(src)
        code, out = sh(cmd, t)
        last = (out.strip().splitlines() or [""])[-1]
        return code == 0, last[:200]


def pytest_hidden(work, src):
    return _hidden(work, "test_zz_hidden.py", src, "python3 -m pytest -q -p no:cacheprovider test_zz_hidden.py")


def node_hidden(work, src):
    return _hidden(work, "zz_hidden.js", src, "node zz_hidden.js")


def code_lines(path):
    """Non-blank, non-comment lines."""
    return sum(1 for l in Path(path).read_text().splitlines() if l.strip() and not l.strip().startswith("#"))


def unchanged(work, orig):
    cmp = filecmp.dircmp(orig, work, ignore=["__pycache__", ".pytest_cache"])

    def walk(c):
        if c.left_only or c.diff_files or c.funny_files:
            return False
        return all(walk(s) for s in c.subdirs.values())

    # new files the agent left behind (other than caches) also count as a change
    return walk(cmp) and not [f for f in cmp.right_only if not f.startswith(".")]
