# please-shut-up

A Claude Code plugin that makes Claude stop yapping and do the work.

| | caveman | ponytail | rtk | **please-shut-up** |
|---|---|---|---|---|
| Shorter replies | ✅ (broken grammar) | – | – | ✅ (normal grammar) |
| Less code, deletes dead code | – | ✅ | – | ✅ |
| Smaller tool output | – | – | ✅ (Rust binary) | ✅ (behavior only, nothing to install) |
| Asks only blocking questions, with defaults | – | – | – | ✅ |
| Proves code runs before saying "done" | – | – | – | ✅ |
| Never drops risks or assumptions to save words | – | – | – | ✅ |
| Always on, no command needed | needs `/caveman` | hooks (needs node) | hook | ✅ SessionStart hook (`awk`) |

## Install

```bash
claude plugin marketplace add GodwinSimanjuntak/please-shut-up
```

```bash
claude plugin install please-shut-up@please-shut-up
```

Or copy just the skill:

```bash
cp -r skills/please-shut-up ~/.claude/skills/
```

## What it does

- **Talk:** Puts the result first. Uses a fixed 3-line report: what changed, how it was verified, and any real risk. No openers, recaps or "let me know".
- **Ask:** Asks only when the answer changes the code and the repo can't answer it. Questions come in one batch, each with a default, so you can just reply "defaults".
- **Code:** Makes the smallest diff that works. Deletes code first. Removes anything the change orphans. No speculative abstractions or unrequested extras.
- **Work:** "Done" means it ran. If it can't run, it says "unverified".
- **Tool output:** Greps before reading, uses quiet flags, never dumps logs.

Say "explain" or "why" any time to get the long version.

## Benchmark

20 tasks, hidden tests, 1 run per arm, Opus. Raw data is in `bench/results/full-1/`, and you can reproduce it with `python3 bench/run.py`.

| | baseline | `Be concise.` | **please-shut-up** |
|---|---|---|---|
| Tasks passed | 20/20 | 20/20 | 20/20 |
| Final message, median words | 142 | 88 | **77** |
| Says how the change was verified | 5/18 | 3/18 | **18/18** |
| Net lines changed | −25 | −41 | **−53** |
| Output tokens, mean | 1,014 | **763** | 788 |
| Cost per task | $0.136 | **$0.128** | $0.145 |

Compared with just saying "Be concise.", please-shut-up writes slightly shorter reports and smaller diffs. The real difference is that it always tells you what it ran to prove the change works. It doesn't save money: the skill text adds about 7% cost per task. See `bench/README.md` for the method.
