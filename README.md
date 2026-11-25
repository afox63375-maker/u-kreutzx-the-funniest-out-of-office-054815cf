[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/afox63375-maker/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/afox63375-maker/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

One line, 117 characters, written by a small Python program (standard library only) to `entry.txt` with no trailing newline.

The line:

> I'm out until Monday. My inbox has started replying to itself just to feel useful, so please don't tell it otherwise.

Run it with `MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py`. The program validates the line first (UTF-8, exactly one line, 1–140 characters, not only whitespace), writes it, then reads it back and verifies it byte-for-byte.
