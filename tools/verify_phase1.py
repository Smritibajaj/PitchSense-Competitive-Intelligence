#!/usr/bin/env python3
"""Run the Phase 1 verification gates on phase1/pitchsense_competitor_research_master.md.
Usage (from the project root): python3 -I tools/verify_phase1.py
Exit code 0 = every gate passes; 1 = at least one gate fails (details printed)."""
import os, re, sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(WS, 'phase1', 'pitchsense_competitor_research_master.md')
EXPECTED = 50  # distinct operating companies in scope; change only with a scope change


def tables(path):
    """Return {'A': rows, 'B': rows, 'C': rows}; each row is a list of cell strings."""
    out, sec = {'A': [], 'B': [], 'C': []}, None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'## Table ([ABC])\b', line)
        if m: sec = m.group(1); continue
        if line.startswith('## '): sec = None; continue
        if sec and line.startswith('|') and not re.match(r'\|\s*[-#]|\|\s*Company\s*\|', line):
            # split on unescaped pipes; drop the empty edges
            cells = re.split(r'(?<!\\)\|', line.rstrip('\n'))[1:-1]
            out[sec].append([c.strip() for c in cells])
    return out


def name(c):
    return re.sub(r'\s+', ' ', re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', c)).strip()


T = tables(MASTER)
A = {name(r[1]): r for r in T['A']}
B = {name(r[1]): r for r in T['B']}
C = {name(r[0]): r for r in T['C']}
results = []


def gate(label, failures):
    results.append((label, failures))


gate('Tables A, B and C contain identical company sets',
     [f'only in {t}: {sorted(s - (set(A) & set(B) & set(C)))}' for t, s in (('A', set(A)), ('B', set(B)), ('C', set(C))) if s != set(A) & set(B) & set(C)])
gate(f'Distinct-company count is {EXPECTED} (and no duplicate rows)',
     ([f'Table {t}: {len(set(d))} distinct, {len(T[t])} rows' for t, d in (('A', A), ('B', B), ('C', C)) if len(set(d)) != EXPECTED or len(T[t]) != EXPECTED]))

score_fail, total_fail = [], []
for n, r in B.items():
    dims = r[2:7]
    confirmed, unverified = 0, 0
    for d in dims:
        m = re.fullmatch(r'([0-2])(\*?)', d)
        if not m: score_fail.append(f'{n}: "{d}"'); continue
        if m.group(2): unverified += int(m.group(1))
        else: confirmed += int(m.group(1))
    t = re.fullmatch(r'\*\*(\d+)\*\*(?:\s*\(\+(\d+) unverified\))?', r[7])
    if not t:
        total_fail.append(f'{n}: total cell "{r[7]}" not in **N** or **N** (+K unverified) form'); continue
    if int(t.group(1)) != confirmed or int(t.group(2) or 0) != unverified:
        total_fail.append(f'{n}: total {r[7]} but components give {confirmed} confirmed + {unverified} unverified')
gate('Every dimension score is 0–2 (a trailing * marks an unverified point)', score_fail)
gate('Each total equals the sum of its confirmed components; starred points appear as (+K unverified)', total_fail)
gate('Every Table B row includes an evidence URL', [n for n, r in B.items() if 'http' not in ' '.join(r)])
gate('Every Table A row has 12 cells', [f'{n}: {len(r)} cells' for n, r in A.items() if len(r) != 12])

ok = True
for label, fails in results:
    print(('PASS' if not fails else 'FAIL') + ' - ' + label)
    for f in fails: print('       ' + f)
    ok &= not fails
sys.exit(0 if ok else 1)
