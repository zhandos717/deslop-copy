#!/usr/bin/env python3
"""Flag common AI-writing tells in EN/RU copy. Usage: detect.py <files|dirs|-> ..."""
import os, re, sys

PATTERNS = {
    'em-dash': r'\s—\s',
    'en-filler': r"(?i)\b(know exactly|in one go|seamless(ly)?|effortless(ly)?|whether you're|take the guesswork|look no further|unlock|elevate|ultimate guide|fast-paced world|it'?s important to note|dive into|game[- ]changer|comprehensive|hassle[- ]free|with ease|say goodbye|navigate the|in conclusion|not just .{1,40} but)\b",
    'en-allows-you': r'(?i)\ballows? you to\b',
    'ru-filler': r'(?i)(в современном мире|не секрет, что|важно отметить|давайте разбер|идеальн\w+ решени|быстро и удобно|в пару кликов|без лишних хлопот|уникальн\w+|широк\w+ спектр|на сегодняшний день|подводя итог|это не просто)',
    'ru-bureaucratic': r'(?i)\b(является|являются|осуществля\w+|данн(ый|ая|ое|ые|ого|ой)|позволяет вам)\b',
    'rhetorical-opener': r'(?i)(wondering (how|what|if)|you\'re not alone|задумывались ли вы)',
}
EXT = {'.md', '.mdx', '.html', '.astro', '.txt', '.ts', '.tsx', '.js', '.jsx', '.json', '.vue', '.svelte'}
SKIP = {'node_modules', 'dist', '.git', '.astro', 'build', '.next'}


def files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, fs in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP]
                yield from (os.path.join(root, f) for f in fs if os.path.splitext(f)[1] in EXT)
        else:
            yield p


def scan(name, text):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for tag, rx in PATTERNS.items():
            for m in re.finditer(rx, line):
                hits.append((i, tag, m.group(0).strip()))
    words = max(1, len(re.findall(r'\w+', text)))
    for i, tag, frag in hits:
        print(f'{name}:{i}: [{tag}] {frag}')
    if hits:
        print(f'== {name}: {len(hits)} hits, {len(hits) * 1000 / words:.1f} per 1000 words\n')
    return len(hits)


def main():
    args = sys.argv[1:] or ['-']
    total = 0
    for a in args:
        if a == '-':
            total += scan('<stdin>', sys.stdin.read())
            continue
        for f in files([a]):
            try:
                total += scan(f, open(f, encoding='utf-8').read())
            except (UnicodeDecodeError, OSError):
                pass
    print(f'TOTAL: {total} hits')


if __name__ == '__main__':
    main()
