# Benchmark

20 small, realistic coding tasks, each run in a fresh copy of its repo with `claude -p`. A task counts as passed only if **hidden tests** pass. The agent never sees those tests, so it can't game them.

| arm | what it is |
|---|---|
| `baseline` | plain Claude Code |
| `concise` | plain Claude Code + system prompt `Be concise.` (the honest control: "would just asking for brevity do the same?") |
| `shutup` | Claude Code with this plugin (`--plugin-dir .`) |

Tasks: 8 bug fixes (Python and JS), 5 features, 3 cleanups/deletions, 1 refactor, 1 multi-bug "make the suite pass", and 2 questions where the files must stay untouched.

## Run it

```bash
python3 bench/run.py --jobs 8
```

```bash
python3 bench/report.py bench/results/<stamp>
```

Options: `--tasks 01,08` runs a subset, `--runs 3` repeats each task, and `--model <id>` pins a model. One full pass is 60 runs, about $10 on Opus.

## What's measured

- **passed**: hidden tests pass (or, for questions, the answer names the cause and no file changed).
- **claimed done but failed**: the task failed and the final message doesn't admit it.
- **final message words**, **filler phrases**, **output/input tokens**, **cost**, **turns**, **time**.
- **lines added/removed** in the diff.

## Caveats

- Cost is noisy. Runs execute in parallel, so whichever run writes the prompt cache first pays for it. Output tokens are the cleaner number.
- Your own `~/.claude` setup (skills, CLAUDE.md, plugins) loads in every arm. It's the same for all three, but numbers will shift a bit between machines.
- These are small tasks. A single pass has variance, so use `--runs 3` before quoting numbers.
