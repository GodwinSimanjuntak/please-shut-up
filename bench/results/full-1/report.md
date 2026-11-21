# Results (60 runs, 20 tasks)

| metric | baseline | concise | shutup |
|---|---|---|---|
| tasks passed (hidden tests) | 20/20 | 20/20 | 20/20 |
| claimed done but failed | 0 | 0 | 0 |
| final message, median words | 142 | 88 | 77 |
| filler phrases (total) | 0 | 0 | 0 |
| output tokens, mean | 1,014 | 763 | 788 |
| input tokens, mean | 118,307 | 115,308 | 118,673 |
| cost per task, mean | $0.136 | $0.128 | $0.145 |
| turns, mean | 4.9 | 4.5 | 4.5 |
| seconds, mean | 20 | 17 | 17 |
| lines added, total | 104 | 86 | 69 |
| lines removed, total | 129 | 127 | 122 |

Change vs baseline:

- concise: final message words -36%
- concise: output tokens -25%
- concise: cost -5%
- shutup: final message words -43%
- shutup: output tokens -22%
- shutup: cost +7%

## By category (passed / median words)

| category | baseline | concise | shutup |
|---|---|---|---|
| bug | 8/8 · 153w | 8/8 · 80w | 8/8 · 72w |
| cleanup | 3/3 · 152w | 3/3 · 92w | 3/3 · 77w |
| feat | 5/5 · 124w | 5/5 · 73w | 5/5 · 74w |
| multi | 1/1 · 134w | 1/1 · 112w | 1/1 · 110w |
| question | 2/2 · 129w | 2/2 · 78w | 2/2 · 61w |
| refactor | 1/1 · 163w | 1/1 · 96w | 1/1 · 79w |

## Failures

