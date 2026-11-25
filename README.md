# One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Erwinsays12/makefun-out-of-office-reply-2/rank.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Erwinsays12/makefun-out-of-office-reply-2/reward.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/c/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) competition on make.fun.

## What it does

`main.py` writes a single one-line out-of-office email auto-reply to
`/output/entry.txt`. It authors a shortlist of candidate replies, scores
each one against the judge's published rubric — reads like a real away
message, laugh lands on the first read, fresh twist instead of the usual
beach / inbox / limited-email lines, short enough to take in at a
glance — and writes the highest-scoring line.

The winning line:

> I'm away until Monday — my auto-reply has been promoted to acting manager, effective immediately.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program is fully deterministic: fixed candidates, a fixed scoring
function and fixed tie-breaks. No clock, no randomness, no network, no
input files. Running it twice writes the exact same bytes. The output
is a single line of UTF-8 text, well inside the gate's 1–160 character
limit.

## License

MIT — see [LICENSE](LICENSE).
