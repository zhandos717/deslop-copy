# deslop-copy

A Claude skill that rewrites website, SEO and marketing copy so it stops reading like AI output. Works in English and Russian.

It does two things:

1. **Finds the tells.** `scripts/detect.py` flags decorative em dashes, stock phrases ("seamless", "in one go", "в пару кликов"), bureaucratic Russian («является», «данный»), "allows you to" and rhetorical openers. Output is `file:line [pattern] match` plus hits per 1,000 words.
2. **Rewrites with rules, not synonyms.** Generic promises become specific facts or real trade-offs, headings become real search queries, and every number the rewrite touches gets re-checked.

It will not invent first-hand experience, reviews or credentials. It lists what only the site owner can add (photos, author, dated prices) instead.

## Before / after

> Find out how many bags of mulch to buy — or whether a bulk delivery makes more sense.

> Bags or bulk: past about 3 yards, bulk delivery usually wins on price.

## Install

**Claude Code**

```
/plugin marketplace add zhandos717/deslop-copy
/plugin install deslop-copy@deslop-copy
```

**claude.ai** — download `deslop-copy.skill` from [Releases](https://github.com/zhandos717/deslop-copy/releases), then Settings → Capabilities → Skills → Upload skill.

**Manual** — copy `skills/deslop-copy` to `~/.claude/skills/`.

## Use

Ask Claude something like "deslop the copy in src/pages", "убери AI-слоп из текстов сайта" or "this landing page sounds like ChatGPT, fix it".

The detector also runs on its own:

```
python3 skills/deslop-copy/scripts/detect.py src/
echo "Our seamless tool allows you to..." | python3 skills/deslop-copy/scripts/detect.py -
```

No dependencies beyond Python 3.

## License

MIT
