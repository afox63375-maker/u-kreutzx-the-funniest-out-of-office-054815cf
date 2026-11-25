# The Funniest Out-of-Office — u-kreutzx-the-funniest-out-of-office-054815cf

## The line

> I'm out until Monday. My inbox has started replying to itself just to feel useful, so please don't tell it otherwise.

- Characters: 117 (limit 140)
- Bytes: 117 (ASCII, UTF-8)
- Lines: 1
- Trailing newline: none

## Why it meets the judge criteria, in order

1. **Reads like a real one-line out-of-office reply a real person would actually set and send.** It opens with the plain, believable "I'm out until Monday." and stays in the register of a normal auto-reply — a date, a status, a request — so it could sit in a real inbox without looking like a joke written for a contest.
2. **Turns on a genuine surprise.** The twist arrives mid-sentence and is not telegraphed: the inbox has not piled up or gone quiet — it has started replying to itself. The reader expects an apology or a return date and instead gets an inbox holding a conversation with no one.
3. **Sounds like a person with a voice of their own, not a template.** "just to feel useful" gives the inbox a small, needy personality, and "please don't tell it otherwise" is a conspiratorial aside to the reader — a human asking for a favour on behalf of their own email. No template talks like that.
4. **Stays fresh.** The concept is invented for this entry: an inbox replying to itself out of loneliness/usefulness. It avoids the tired templates ("I'm out of office", "your email is important to me", "limited access to email", "I'll reply when I return") and does not reuse the other entries' concepts (no context window, no lighthouse keeper, no vending machine).
5. **Uses every word.** "out until Monday" sets the real reply; "started replying to itself" is the joke; "just to feel useful" is the motive and the laugh; "so please don't tell it otherwise" is the punchline that turns the reader into an accomplice. Cut any clause and either the setup, the twist, or the laugh disappears.

## Local test

Command: `MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py`

Result: PASS.

- Program printed: Wrote /tmp/ooo-out/entry.txt, Characters: 117, Bytes: 117, Lines: 1.
- Independent verification of /tmp/ooo-out/entry.txt: 117 characters, 117 bytes, exactly 1 line, no newline character, no trailing newline, byte-identical to the line in main.py.
- main.py is standard library only, validates the gate before writing, writes with no trailing newline, and reads the file back to verify it byte-for-byte.
