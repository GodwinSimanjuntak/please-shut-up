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

## Benchmark (iteration 1, 3 tasks)

| | with skill | without |
|---|---|---|
| Assertions passed | 100% | 79% |
| Final message length | 46–55 words | 68–155 words |
| States how it was verified | 3/3 | 1/3 |

The test cases are in `skills/please-shut-up/evals/`. Run them with `claude plugin eval skills/please-shut-up --allow-tools Write,Edit,Bash --scaffold`.
