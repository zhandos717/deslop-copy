---
name: deslop-copy
description: Rewrite website, SEO, landing-page, product and blog copy (English or Russian) so it stops reading like AI output and sounds like a practitioner wrote it. Use whenever the user says "deslop", "убери AI-слоп", "сделай текст органичным/живым/человеческим", "текст звучит как ChatGPT", asks to audit or clean up site copy, FAQ, meta descriptions, or before submitting a site to AdSense / publishing articles — even if they only say "почисти тексты на сайте". Not for code cleanup (use ai-slop-cleaner for that).
---

# deslop-copy

Readers and Google's quality raters recognize AI copy in seconds, and on content sites that recognition costs trust, rankings and AdSense approval. The cure isn't synonyms — it's replacing generic claims with specific, checkable information and the plain rhythm of someone who has done the work.

## Workflow

1. **Scan.** Run the detector on the files or text:
   ```bash
   python3 ~/.claude/skills/deslop-copy/scripts/detect.py <files or dirs>   # or: echo "text" | detect.py -
   ```
   It prints each hit with file:line and the pattern name, plus a per-file score. It only finds surface tells; you still read the copy yourself.
2. **Read every string a visitor sees** (titles, leads, buttons, FAQ, meta descriptions, alt text) and judge it against the patterns below — the script misses structural slop.
3. **Rewrite** in place. Keep facts, numbers, formulas, keywords that matter for SEO, and the file's syntax (watch quotes/apostrophes inside JS/TS string literals — use ’ in single-quoted strings).
   - **Treat title, meta description and h1 wording as keywords.** Those phrases ("актуальный курс", "loan calculator") are usually what people search for. Remove filler around them; don't swap the phrase itself for a synonym unless you know it isn't a target query.
   - **A rewrite must not be longer than the original** unless it adds a concrete fact. If your version needs an extra sentence to say the same thing, keep the original.
   - **Don't add advice or claims that weren't there** ("check with your bank", "updated hourly"). Cutting is safe; adding needs a source on the same page.
   - Leave legal/disclaimer wording ("справочный характер", "not financial advice") at least as strong as it was.
4. **Fact-check anything you touch.** If a sentence contains a number, recompute or verify it. Deslopping must never introduce a wrong figure; flag numbers you can't verify instead of inventing them.
5. **Rebuild / re-run the detector** and report: what changed (2–3 before→after examples), remaining hits you left on purpose, and what only the owner can add (see "Experience gap").

## What to remove or rewrite

**Punctuation & rhythm**
- Em dashes (—) used as a dramatic pause. Replace with a period, comma, colon or parentheses. One per page is fine; ten is a fingerprint. Russian copy: the dash is grammatical in «X — это Y», keep those; cut the decorative ones.
- Triplets everywhere ("fast, simple, and reliable"). Use the number of items the facts require.
- Every sentence the same length. Mix short ones in.

**Empty promises and filler** — sentences that would fit any website:
- EN: "Know exactly…", "in one go", "seamless", "effortless", "whether you're a beginner or a pro", "take the guesswork out", "look no further", "unlock", "elevate", "ultimate guide", "in today's fast-paced world", "it's important to note", "dive into", "game-changer", "comprehensive", "hassle-free", "with ease", "say goodbye to".
- RU: «в современном мире», «не секрет, что», «важно отметить», «давайте разберёмся», «идеальное решение», «быстро и удобно», «всего в пару кликов», «без лишних хлопот», «уникальный», «широкий спектр», «является», «осуществлять», «данный», «позволяет вам», «на сегодняшний день».
- Rhetorical question + answer openers ("Wondering how much mulch you need? You're not alone.").
- Closing summaries that repeat the page ("In conclusion…", «Подводя итог…»).

**Structure**
- "Not just X, but Y" / «это не просто X, а Y».
- Every paragraph starting with the topic noun.
- Bold-label bullet lists where prose would do.
- Hedging stacks ("can potentially help to").

## What to put instead

Prefer, in this order:
1. **A concrete fact** the reader can act on: a number, unit, threshold, product size. "Past about 3 yards, bulk delivery is cheaper than bags" beats "Find out whether bulk makes more sense."
2. **The real constraint or trade-off** a practitioner would mention ("Many plants charge a short-load fee under 3–4 yd³").
3. **Plain verbs, second person, present tense.** "Enter the slab size." Not "This tool allows you to calculate…".
4. **Headings phrased like real searches** ("How much do I need?", «Сколько нужно мешков?»), not slogans.

Example rewrites:
- "Find out how many bags of mulch to buy — or whether a bulk delivery makes more sense." → "Bags or bulk: past about 3 yards, bulk delivery usually wins on price."
- «Наш калькулятор позволяет быстро и удобно рассчитать платёж всего в пару кликов.» → «Введите сумму, ставку и срок — платёж и переплата посчитаются сразу.» (dash here is grammatical-ish; a colon also works)

## Experience gap

Some "organic" signals can't be written by a model and must not be faked: first-hand photos, the author's name and background, prices checked on a date, "I tried X and Y happened". Never invent personal experience, testimonials, reviews or credentials. Instead, end your report with a short list of specific things the owner could add (e.g. "photo of the 80 lb bag label showing 0.6 ft³ yield").
