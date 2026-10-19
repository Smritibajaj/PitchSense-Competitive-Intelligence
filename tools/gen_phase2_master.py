#!/usr/bin/env python3
"""Generate phase2/pitchsense_phase2_messaging_master.md from the batch CSVs.
Usage (from the project root): python3 -I tools/gen_phase2_master.py"""
import csv, os, re, sys, collections

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYN = os.path.join(WS, 'phase2', 'synthesis.md')
OUT = os.path.join(WS, 'phase2', 'pitchsense_phase2_messaging_master.md')
B = 'phase2/batches/'
FULL = [(1, B + 'batch01_sybill_aida_gong'), (2, B + 'batch02_attention_backstory_outreach'),
        (3, B + 'batch03_salesloft_showpad_mindtickle_allego')]
# Light-format batches are discovered: phase2/batches/batchNN/website_messaging_batchN.csv (NN >= 4)
LIGHT = {}
for _d in sorted(os.listdir(os.path.join(WS, B))):
    _m = re.fullmatch(r'batch(\d{2})', _d)
    if _m and int(_m.group(1)) >= 4:
        LIGHT[int(_m.group(1))] = f'{B}{_d}/website_messaging_batch{int(_m.group(1))}.csv'


def rd(p):
    with open(os.path.join(WS, p), encoding='utf-8') as f:
        return list(csv.DictReader(f))


def esc(s):
    if s is None: return ''
    s = re.sub(r'<(/?[a-zA-Z][^>]*)>', lambda m: '&lt;' + m.group(1) + '&gt;', s)
    return s.replace('|', '\\|').replace('\r', ' ').replace('\n', ' ').strip()


def link(u):
    m = re.search(r'https?://[^\s)\]|]+', u or '')
    if not m: return esc(u)
    u = m.group(0)
    host = re.sub(r'^www\.', '', u.split('/')[2])
    path = '/'.join(u.split('/')[3:]).strip('/')
    label = host + ('/' + path if path else '')
    if len(label) > 60: label = label[:57] + '…'
    return f'[{label}]({u})'


def table(headers, rows):
    out = ['| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)]
    out += ['| ' + ' | '.join(r) + ' |' for r in rows]
    return '\n'.join(out)


def key(n):
    return re.sub(r'[^a-z]', '', n.lower().split('(')[0].split('+')[0].split(' incl')[0])[:6]


# ---- Phase 1 cross-reference (master Tables A/B/C) ----
p1 = collections.defaultdict(dict)
sec = None
for line in open(os.path.join(WS, 'phase1/pitchsense_competitor_research_master.md'), encoding='utf-8'):
    if line.startswith('## Table A'): sec = 'A'
    elif line.startswith('## Table B'): sec = 'B'
    elif line.startswith('## Table C'): sec = 'C'
    elif line.startswith('## '): sec = None
    c = [x.strip() for x in line.split('|')]
    if not sec or len(c) < 5 or c[1] in ('#', 'Company') or c[1].startswith('-'): continue
    strip = lambda s: re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    if sec == 'A' and c[1].isdigit(): p1[key(c[2])].update(num=int(c[1]), cat=strip(c[4]))
    if sec == 'B' and c[1].isdigit(): p1[key(c[2])].update(total=c[8].strip('*'))
    if sec == 'C': p1[key(c[1])].update(prio=c[2])

# ---- load data ----
light_hdr = next(csv.reader(open(os.path.join(WS, LIGHT[4]), encoding='utf-8')))
light = []
for b, f in LIGHT.items():
    for r in rd(f):
        r['Batch'] = b; light.append(r)
fullA, fullB, fullC, fullD, fullE, fullF = [], [], [], [], [], []
for b, d in FULL:
    for name, acc in [('A_hero_comparison', fullA), ('B_landing_page_structure', fullB),
                      ('C_messaging_positioning', fullC), ('D_cta_strategy', fullD),
                      ('E_cro_messaging', fullE)]:
        for r in rd(f'{d}/table_{name}.csv'):
            r['Batch'] = b; acc.append(r)
    with open(os.path.join(WS, d, 'table_F_pitchsense_comparison.csv'), encoding='utf-8') as fh:
        rows = list(csv.reader(fh))
    fullF.append((b, rows[0], rows[1:]))


# ---- build phase2/phase2_website_messaging_all50.csv (light rows verbatim; full-format rows derived) ----
def derive_full_rows():
    out = []
    for b, d in FULL:
        A = [r for r in fullA if r['Batch'] == b]
        Bt = [r for r in fullB if r['Batch'] == b]
        Ct = {r['Company']: r for r in fullC if r['Batch'] == b}
        for a in A:
            n = a['Company']; url = (re.search(r'https?://[^\s)\]|]+', a['Source URL']) or [a['Source URL']])[0]
            secs = [r['Exact Heading'] for r in Bt if r['Company'] == n and r['Exact Heading']
                    and not re.search(r'hero|nav|footer|announcement|banner|logo', r['Section Type'], re.I)
                    and (re.search(r'https?://[^\s)\]|]+', r['Source URL']) or [''])[0] == url][:3]
            secs += ['Not verified'] * (3 - len(secs))
            out.append({'Batch': str(b), 'Company': n, 'Website': re.sub(r'https?://(www\.)?', '', url).strip('/'),
                        'Category': p1.get(key(n), {}).get('cat', 'Not verified'), 'H1': a['H1'], 'H2': a['H2'] or 'Not present',
                        'Hero Description': a['Hero Supporting Copy'], 'Primary CTA': a['Primary CTA'], 'Secondary CTA': a['Secondary CTA'] or 'Not present',
                        'Section Heading 1': secs[0], 'Section Heading 2': secs[1], 'Section Heading 3': secs[2],
                        'Positioning': 'ANALYST SUMMARY (not verbatim): ' + a['Main Promise'], 'ICP': 'ANALYST SUMMARY: ' + a['Target Buyer'],
                        'Pain Point': 'ANALYST SUMMARY: ' + Ct.get(n, {}).get('Problem Framing', 'Not verified'), 'Source URL': url,
                        'Verification': f'Derived from Phase 2 batch {b} full-format Tables A/B/C (verbatim H1/H2/hero/CTAs/section headings per those tables; Positioning/ICP/Pain are analyst summaries, not homepage quotes). See batch {b} report for verification detail.'})
    return out

all50 = derive_full_rows() + [dict(r, Batch=str(r['Batch'])) for r in light]
all50.sort(key=lambda r: int(r['Batch']))
with open(os.path.join(WS, 'phase2', 'phase2_website_messaging_all50.csv'), 'w', encoding='utf-8', newline='') as fh:
    wr = csv.DictWriter(fh, fieldnames=['Batch'] + light_hdr); wr.writeheader(); wr.writerows(all50)

# ---- verification gates ----
gates = []
names50 = [r['Company'] for r in all50]
p1keys = {k for k, v in p1.items() if 'num' in v}
gates.append(('Combined table has 50 rows and 50 distinct companies', len(all50) == 50 and len(set(names50)) == 50, f'{len(all50)} rows, {len(set(names50))} distinct'))
gates.append(('Company set identical to Phase 1 master Table A', {key(n) for n in names50} == p1keys, f'{len({key(n) for n in names50} & p1keys)}/50 matched'))
bad = [f for b, f in LIGHT.items() if next(csv.reader(open(os.path.join(WS, f), encoding='utf-8'))) != light_hdr]
gates.append(('Light-format batch CSVs (4–11) share the identical 16-column header', not bad, 'all identical' if not bad else ', '.join(bad)))
cols = [r['Company'] for r in light if len([k for k in r if k != 'Batch']) != 16]
gates.append(('Every light-format row has 16 cells', not cols, f'{len(light)} rows checked'))
nourl = [r['Company'] for r in all50 if not r['Source URL'].startswith('http')]
gates.append(('Every company row carries a Source URL', not nourl, 'all present' if not nourl else ', '.join(nourl)))
setA = {r['Company'] for r in fullA}; setC = {r['Company'] for r in fullC}; setE = {r['Company'] for r in fullE}; setB = {r['Company'] for r in fullB}; setD = {r['Company'] for r in fullD}
gates.append(('Full-format Tables A/B/C/D/E contain identical company sets (10)', setA == setB == setC == setD == setE and len(setA) == 10, f'{len(setA)} companies'))
a12 = all(len([k for k in r if k != 'Batch']) == 12 for r in fullA)
gates.append(('Full-format Table A rows have 12 cells', a12, f'{len(fullA)} rows checked'))
eurl = [r['Company'] for r in fullE if not r['Evidence URL'].startswith('http') and r['Exact Supporting Claim'].lower().startswith('not observed') is False]
gates.append(('Every Table E claim (excluding "Not observed" rows) carries an evidence URL', not eurl, f'{len(fullE)} rows checked'))
ver = [r['Company'] for r in light if 'Homepage researched October 19, 2026' not in r['Verification'] and 'October 19, 2026' not in r['Verification']]
gates.append(('Every light-format Verification cell carries the research date', not ver, 'all dated' if not ver else ', '.join(ver)))

# ---- not-verified tallies ----
NVF = ['H1', 'H2', 'Hero Description', 'Primary CTA', 'Secondary CTA', 'Section Heading 1', 'Section Heading 2', 'Section Heading 3', 'Positioning', 'ICP', 'Pain Point']
nv = collections.Counter()
nv_by = {}
for r in light:
    miss = [k for k in NVF if r[k].strip().lower().startswith('not verified')]
    nv.update(miss); nv_by[r['Company']] = miss

# ---- build document ----
D = []
w = D.append
w('# PitchSense AI — Phase 2 Master Report: Competitor Website Messaging & Landing-Page Analysis (50 Companies)\n')
w('**Research dates:** October 19, 2026 (Europe/Berlin), all 11 batches. **Consolidated:** October 19, 2026. '
  '**Scope:** the same 50 companies as the Phase 1 master report (`phase1/pitchsense_competitor_research_master.md`). Phase 1 discovery, classification and capability scoring are not repeated here.\n')
w('**Source of truth.** This report consolidates Phase 2. Canonical data stays in the batch CSVs it is generated from. When evidence changes, update the batch CSV, regenerate this file, and re-run the verification gates below.\n')
w('**Two research depths.**')
w('- **Full format (batches 1–3, 10 companies):** Sybill, Aida, Gong; Attention, Backstory, Outreach; Salesloft + Clari, Showpad, Mindtickle, Allego. Homepage plus one CRO-relevant page each. Tables A (hero), B (landing-page structure), C (messaging and positioning), D (CTA strategy), E (CRO messaging) and F (PitchSense comparison). Rendered-browser checks were done in addition to HTML capture.')
w('- **Light format (batches 4–11, 40 companies):** homepage (or product landing page for large-vendor products) captured as HTML. One 16-field row per company: H1, H2, hero description, two CTAs, three section headings, positioning, ICP, pain point, source and verification notes.\n')
w('**Method rules (all batches).** Heading levels verified against HTML tags. Nav, mega-menu, footer, tab and responsive duplicates are excluded and the exclusions noted. Copy is quoted verbatim. Anything not found or not verifiable is written "Not verified" with the reason. Vendor metrics and analyst badges are recorded as vendor claims, not verified facts. CTA frequency is observed page structure, not evidence of conversion effectiveness. Messaging emphasis is not evidence that a product capability is missing.\n')
w('**Change log.**')
w('- Oct 19, 2026: batches 1–3 (full format) and 4–5 (light format).')
w('- Oct 19, 2026: batches 6–11 (light format, 30 companies) completed the 50-company scope, and this master report was consolidated.')
w('- Product Narrative v1 (Sep 30, 2026) was located after batches 1–3. Table F was reconciled against it on Oct 19, 2026: its PitchSense column gives Appendix status, and each interpretation ends with a reconciliation note. Phase 3 (`phase3/pitchsense_phase3_cro_positioning.md`) uses it.\n')
w('---\n')

# Coverage
w('## Coverage — 50 companies\n')
w('Phase 1 columns (#, primary category, capability total out of 10, priority) are cross-referenced from the Phase 1 master report.\n')
rows = []
for r in sorted(all50, key=lambda r: p1.get(key(r['Company']), {}).get('num', 99)):
    k = p1.get(key(r['Company']), {})
    b = int(r['Batch'])
    rows.append([str(k.get('num', '')), esc(r['Company']), esc(k.get('cat', '')), esc(k.get('total', '')), esc(k.get('prio', '')),
                 str(b), 'Full' if b <= 3 else 'Light', link(r['Source URL'])])
w(table(['P1 #', 'Company', 'Phase 1 category', 'P1 total', 'Priority', 'P2 batch', 'Format', 'Page analysed'], rows) + '\n')
w('---\n')

# Part A
w('## Part A — Detailed analysis of the 10 full-format companies (batches 1–3)\n')
w('Full row-level detail, including per-row verification notes, Table B section rows and the Table D anchor audit, is in the batch reports and CSVs: '
  '`phase2/batches/batch01_sybill_aida_gong/`, `batch02_attention_backstory_outreach/` and `batch03_salesloft_showpad_mindtickle_allego/` (report `.md` plus `table_*.csv` in each).\n')

w('### Table A — Hero section comparison\n')
w(table(['Company', 'H1', 'H2', 'Hero supporting copy', 'Primary CTA', 'Secondary CTA', 'Hero media', 'Main promise (analyst)', 'Target buyer', 'Source'],
        [[esc(r['Company']), esc(r['H1']), esc(r['H2']) or '—', esc(r['Hero Supporting Copy']), esc(r['Primary CTA']), esc(r['Secondary CTA']) or '—',
          esc(r['Hero Media Type']), esc(r['Main Promise']), esc(r['Target Buyer']), link(r['Source URL'])] for r in fullA]) + '\n')

w('### Table B — Landing-page section sequence (homepages)\n')
seq = collections.OrderedDict()
home = {r['Company']: (re.search(r'https?://[^\s)\]|]+', r['Source URL']) or [''])[0] for r in fullA}
for r in fullB:
    u = (re.search(r'https?://[^\s)\]|]+', r['Source URL']) or [''])[0]
    if u.rstrip('/') == home[r['Company']].rstrip('/'):
        seq.setdefault(r['Company'], []).append(r['Section Type'])
w(table(['Company', 'Sections in page order (Section Type, Table B)', 'Sections'],
        [[esc(c), esc(' → '.join(s)), str(len(s))] for c, s in seq.items()]) + '\n')

w('### Table C — Messaging and positioning\n')
w(table(['Company', 'Problem framing', 'Urgency language', 'Solution framing', 'Main benefit', 'Differentiator', 'Proof point', 'Source'],
        [[esc(r['Company']), esc(r['Problem Framing']), esc(r['Urgency Language']), esc(r['Solution Framing']), esc(r['Main Benefit']),
          esc(r['Differentiator']), esc(r['Proof Point']), link(r['Source URL'])] for r in fullC]) + '\n')

w('### Table D — CTA strategy summary\n')
w('Count of CTA records per company in Table D, grouped by exact wording (case-insensitive). The full location and destination audit is in each batch\'s `table_D_cta_strategy.csv`; batch 3 adds `cta_occurrence_audit.csv`.\n')
drows = []
for c in [r['Company'] for r in fullA]:
    recs = [r for r in fullD if r['Company'] == c]
    cnt = collections.Counter(r['Exact CTA'].strip().lower() for r in recs)
    disp = {}
    for r in recs: disp.setdefault(r['Exact CTA'].strip().lower(), r['Exact CTA'].strip())
    ctype = collections.Counter(r['Conversion Type'].strip() for r in recs if r['Conversion Type'].strip())
    drows.append([esc(c), str(len(recs)), esc('; '.join(f'{disp[k]} ×{v}' for k, v in cnt.most_common(5))), esc('; '.join(f'{k} ×{v}' for k, v in ctype.most_common(3)))])
w(table(['Company', 'CTA records', 'Most frequent CTA wording', 'Most frequent conversion types'], drows) + '\n')

w('### Table E — CRO messaging (all claims)\n')
w(table(['Company', 'CRO pain point', 'Exact supporting claim', 'Location on page', 'Promised business outcome', 'Evidence'],
        [[esc(r['Company']), esc(r['CRO Pain Point']), esc(r['Exact Supporting Claim']), esc(r['Location on Page']), esc(r['Promised Business Outcome']),
          link(r['Evidence URL']) if r['Evidence URL'].startswith('http') else esc(r['Evidence URL'])] for r in fullE]) + '\n')

w('### Table F — PitchSense narrative comparison (reconciled with Narrative v1)\n')
w('Batches 1–3 were written before PitchSense Product Narrative v1 was located, using the positioning in the research brief. On Oct 19, 2026 they were reconciled with Narrative v1: the PitchSense column now gives Appendix status (Built / In build / Planned), and each interpretation ends with a reconciliation note. The last column is analyst interpretation, not a capability claim.\n')
for b, hdr, rows in fullF:
    comp = [h for h in hdr[1:-2]]
    w(f'**Batch {b}** ({", ".join(h.replace(" Evidence", "") for h in comp)})\n')
    w(table([esc(h) for h in hdr], [[esc(x) for x in r] for r in rows]) + '\n')
w('---\n')

# Part B
w('## Part B — Website messaging, all 50 companies\n')
w('One row per company. Rows from batches 4–11 are verbatim homepage fields. For batches 1–3, H1, H2, hero copy, CTAs and section headings come verbatim from the full-format tables; '
  'Positioning, ICP and Pain Point in those 10 rows are **analyst summaries** (labelled) drawn from Tables A and C, not homepage quotes. Verification notes for every row follow in Part B2.\n')
cols = ['H1', 'H2', 'Hero Description', 'Primary CTA', 'Secondary CTA', 'Section Heading 1', 'Section Heading 2', 'Section Heading 3', 'Positioning', 'ICP', 'Pain Point']
w(table(['Batch', 'Company', 'Category (P1)'] + ['Hero description' if c == 'Hero Description' else c for c in cols] + ['Source'],
        [[r['Batch'], esc(r['Company']), esc(r['Category'])] + [esc(r[c]) for c in cols] + [link(r['Source URL'])] for r in all50]) + '\n')

w('### Part B2 — Verification notes (per company)\n')
for r in all50:
    w(f'- **{esc(r["Company"])}** (batch {r["Batch"]}): {esc(r["Verification"])}')
w('\n---\n')

# Part C synthesis
w('## Part C — Cross-batch synthesis (all 50)\n')
with open(SYN, encoding='utf-8') as fh:
    w(fh.read().strip() + '\n')
w('---\n')

# Part D flags
w('## Part D — Flags carried forward\n')
w('### D1 — Fields not verified (light-format batches 4–11, 40 companies)\n')
w(table(['Field', 'Companies marked Not verified'], [[k, str(nv.get(k, 0))] for k in NVF]) + '\n')
w(table(['Company', 'Not-verified fields'], [[esc(c), esc(', '.join(m))] for c, m in nv_by.items() if m]) + '\n')
w('### D2 — Fetch substitutions, ownership changes and wording drift (Oct 19, 2026 captures)\n')
w('These are observations from the captured pages. Verify before changing the Phase 1 master report; they are also listed in `ROADMAP.md`.\n')
for s in [
    '**Microsoft (Copilot for Sales):** the microsoft.com marketing page served a bot-block page. The official adoption page was used instead. The H1 now reads "Sales solution in Microsoft Copilot".',
    '**Dropbox (DocSend):** docsend.com returned a Cloudflare 403. The official dropbox.com/docsend page was used instead; docsend.com messaging may differ.',
    '**PathFactory:** a homepage banner states the company has been acquired by Kaltura.',
    '**Fathom:** a site-wide banner reads "FATHOM IS NOW PART OF SUPERHUMAN".',
    '**Wonderway:** the page references "Verity by BTS" (possible rebrand, relationship not stated). The AI Coach section is still labelled beta. Most CTAs are hidden by the site\'s own CSS.',
    '**Hyperbound:** the "AI-Powered Roleplay Platform" framing has been replaced by Practice / Perform / Kota Activate.',
    '**Regie.ai:** the product is now "RegieGO", an "agentic sales workspace".',
    '**Salesforce (Agentforce):** the landing-page hero is about customer service, not sales. The large headline renders client-side, so only the "Agentforce" H1 label was recorded.',
    '**Uniphore:** there is no `<h1>` on the page. The hero is a rotating carousel led by a report promotion.',
    '**Rotating or client-side H1s:** Gong, Otter.ai, Aviso, Balto and Yoodli. Consensus\'s H1 carries a `data-lp-replace` attribute, so some visitors may see different text.',
    '**Wording changed since Phase 1 quotes:** Circleback ("Company Brain" is now only in the page title), Quantified ("one audit trail"), PitchMonster ("300K+ reps" vs. 30,000+), HubSpot Breeze, Humantic AI ("Miia, Pi & Signals"), Zoom Revenue Accelerator.',
]:
    w(f'- {s}')
w('')
w('---\n')

# Gates
w('## Verification gates (programmatic, run at generation)\n')
w(table(['Gate', 'Result', 'Detail'], [[g, 'PASS' if ok else 'FAIL', esc(d)] for g, ok, d in gates]) + '\n')
w('Regenerate after any change to a batch CSV or `phase2/synthesis.md`: `python3 -I tools/gen_phase2_master.py`. Do not hand-edit this file.\n')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(D))
print(OUT, os.path.getsize(OUT), 'bytes')
for g, ok, d in gates: print('PASS' if ok else 'FAIL', '-', g, '-', d)
sys.exit(0 if all(ok for _, ok, _ in gates) else 1)
