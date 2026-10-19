#!/usr/bin/env python3
"""Generate PitchSense Phase 2 Batch 3 report from canonical CSVs (v3 — clean)."""
import csv, os, re, shutil, tempfile
from urllib.parse import urlparse

BASE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(BASE)
REPORT = os.path.join(WS, 'pitchesense_phase2c_messaging_salesloft_showpad_mindtickle_allego.md')

def read_csv(name):
    with open(os.path.join(BASE, name), encoding='utf-8') as f:
        return list(csv.DictReader(f))

def esc(s):
    """Escape for Markdown table cells; escape pipes, newlines, and literal HTML tags."""
    if s is None: return ''
    LT = chr(38) + 'lt;'; GT = chr(38) + 'gt;'
    s = re.sub(r'<(/?)(h[1-6]|div|span|p|em|strong|a|nav|footer|body|html|section|ul|li)([^>]*?)>', lambda m: LT + m.group(1) + m.group(2) + m.group(3) + GT, s)
    return s.replace('|', '\\|').replace('\n', ' ')

def cite_url(url, label=None):
    """Convert a raw URL to a descriptive Markdown citation."""
    if not url: return ''
    if label is None:
        host = urlparse(url).netloc.replace('www.','')
        path = urlparse(url).path.rstrip('/')
        if path and path != '/':
            seg = path.split('/')[-1].replace('-',' ').title()
            label = f"{host} {seg}"
        else:
            label = f"{host} homepage" if host else "page"
    return f"[{label}]({url})"

def cite_urls_field(text):
    """Convert all raw URLs in a text field to Markdown citations."""
    if not text: return ''
    return re.sub(r'(?<!\]\()https?://[^\s\|\)\]]+', lambda m: cite_url(m.group(0).rstrip('.,;')), text)

# ─── Read canonical CSVs ───
A = read_csv('table_A_hero_comparison.csv')
B = read_csv('table_B_landing_page_structure.csv')
C = read_csv('table_C_messaging_positioning.csv')
D = read_csv('table_D_cta_strategy.csv')
E = read_csv('table_E_cro_messaging.csv')
F = read_csv('table_F_pitchsense_comparison.csv')

# ─── Compute Table D totals from CSV ───
SUPPORTING_KEYS = ['forecasting','revenue-leaders','sales-leadership','revenue-leader']
def is_supporting(url):
    return any(k in url for k in SUPPORTING_KEYS)

breakdown = {}
for r in D:
    key = (r['Company'], 'supporting' if is_supporting(r['Source URL']) else 'homepage')
    breakdown[key] = breakdown.get(key, 0) + 1

COMPANIES = ['Salesloft + Clari','Showpad','Mindtickle','Allego']
HOME_URLS = {'Salesloft + Clari': 'https://www.salesloft.com/', 'Showpad': 'https://www.showpad.com/', 'Mindtickle': 'https://www.mindtickle.com/', 'Allego': 'https://www.allego.com/'}

totals_md = []
for c in COMPANIES:
    h = breakdown.get((c,'homepage'),0); s = breakdown.get((c,'supporting'),0)
    totals_md.append(f"{c} {h+s} (homepage {h} + supporting page {s})")
TOTAL = sum(breakdown.values())

# ─── Sequence interpretations (corrected, grounded in Table B) ───
SEQ_INTERP = {
    'Salesloft + Clari': "Salesloft's homepage sequence (Table B): navigation → hero (outcome words: Create/Convert/Grow) → stats + customer stories section → Signals platform section → bridging line → final CTA (Book 15 Minutes) → footer ([homepage](https://www.salesloft.com/)). This may front-load credibility before features, potentially reducing perceived commitment with the time-boxed CTA, though neither effect is established. The supporting forecast page was captured but its internal section order was not separately catalogued.",
    'Showpad': "Showpad's homepage sequence (Table B): hero (buyer's world: essential products + safe governed AI) → logo strip (2,000+ companies) → analyst badges → AI platform section → four product modules (Sales Readiness, Content Management, Buyer Engagement, Analytics) → Showpad Genie → customer stories → short body Every team section (heading + paragraph only; persona links are in navigation) → integrations → news/awards → final demo CTA ([homepage](https://www.showpad.com/)). This may build confidence through social proof and analyst validation before asking for a demo, though the effect is not established.",
    'Mindtickle': "Mindtickle's homepage sequence (Table B): hero (AI teammate + Try AI Role Play CTA) → book promotion → platform overview (Get a demo) → persona sections → ElevateOS banner → customer stories → analyst badges → AI Copilot section → news/resources → analyst recognition → final CTA (Request a demo) ([homepage](https://www.mindtickle.com/)). The early roleplay CTA may encourage product exploration alongside the demo-led journey; trial usability was not verified.",
    'Allego': "Allego's homepage sequence (Table B): hero (Loved By Customers + Gartner badge) → logo strip → What Most Platforms Miss (anti-category frame) → One Platform. Practical Agentic AI at the Core. → Why Leading Revenue Teams Choose Allego → Tailored Solutions → Real Results → Built to Change the Game → Insights → Switch to Allego (competitive switch offer) ([homepage](https://www.allego.com/)). This may position switching as the natural next step, though the effect is not established.",
}

# ─── Build report ───
lines = []
lines.append("# PitchSense AI — Phase 2: Competitor Website Messaging and Landing Page Analysis (Batch 3)")
lines.append("")
lines.append("**Research date:** October 19, 2026 (Europe/Berlin). Pages captured directly from official websites via full-HTML capture; all four homepages were additionally inspected in a rendered browser.")
lines.append("")
lines.append("**Scope:** Salesloft + Clari (salesloft.com — clari.com redirects to salesloft.com; merger page \"Salesloft & Clari Are Now One Company\" captured), Showpad (showpad.com), Mindtickle (mindtickle.com), Allego (allego.com) — homepages plus one CRO-relevant supporting page each (Salesloft: /platform/sales-forecasting-software; Showpad: /showpad-for-revenue-leaders; Mindtickle: /solutions/sales-leadership-solutions-training/; Allego: /solutions/sales-leadership/). Phase 1 discovery, classification, and capability scoring are not repeated here.")
lines.append("")
lines.append("**Entity note (Salesloft + Clari):** Salesloft and Clari are one company — the merger page title reads \"Salesloft & Clari Are Now One Company\" ([salesloft.com/clari-salesloft-merger](https://www.salesloft.com/clari-salesloft-merger), captured October 19, 2026), and https://www.clari.com/ redirects to https://www.salesloft.com/ (redirect observed October 19, 2026). One website was analyzed, with the redirect and merger recorded. The merged product suite appears in the login menu: Salesloft (app.salesloft.com), Clari Forecast (app.clari.com), Conversations (copilot.clari.com), Drift (start.drift.com), Groove (engine.groove.clari.com).")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table A — Hero Section Comparison")
lines.append("")
cols = list(A[0].keys())
lines.append("| " + " | ".join(cols) + " |")
lines.append("|" + "---|" * len(cols))
for r in A:
    cells = []
    for c in cols:
        v = esc(r[c])
        if c == 'Source URL': v = cite_urls_field(v)
        cells.append(v)
    lines.append("| " + " | ".join(cells) + " |")
lines.append("")
lines.append("**Full table: `phase2c/table_A_hero_comparison.csv`.**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table B — Landing Page Structure (one row per section, in page order)")
lines.append("")
lines.append("Section numbering restarts at 1 for each company. Body sections only — navigation mega-menu content is recorded as navigation (verified by DOM ancestors).")
lines.append("")
cols = list(B[0].keys())
lines.append("| " + " | ".join(cols) + " |")
lines.append("|" + "---|" * len(cols))
for r in B:
    cells = []
    for c in cols:
        v = esc(r[c])
        if c == 'Source URL': v = cite_urls_field(v)
        cells.append(v)
    lines.append("| " + " | ".join(cells) + " |")
lines.append("")
lines.append(f"**Full table: `phase2c/table_B_landing_page_structure.csv` ({len(B)} rows).**")
lines.append("")
lines.append("### Page-Sequence Interpretation (Analyst interpretation)")
lines.append("")
lines.append("The following interpretations are analyst views grounded in each company's actual recorded section order (Table B). They are not vendor statements and not evidence of conversion effectiveness.")
lines.append("")
for c in COMPANIES:
    lines.append(f"**{c}** (Analyst interpretation): {SEQ_INTERP[c]} ([homepage]({HOME_URLS[c]}))")
    lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table C — Messaging and Positioning")
lines.append("")
lines.append("Source URL column carries the homepage URL plus supporting-page URLs with per-clause attribution.")
lines.append("")
cols = list(C[0].keys())
lines.append("| " + " | ".join(cols) + " |")
lines.append("|" + "---|" * len(cols))
for r in C:
    cells = []
    for c in cols:
        v = esc(r[c])
        if c == 'Source URL': v = cite_urls_field(v)
        cells.append(v)
    lines.append("| " + " | ".join(cells) + " |")
lines.append("")
lines.append("**Full table: `phase2c/table_C_messaging_positioning.csv`.**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table D — CTA Strategy")
lines.append("")
lines.append(f"One row per CTA occurrence. {TOTAL} records total — {', '.join(totals_md)}.")
lines.append("")
lines.append("**Occurrence audit:** 92 rows mapped one-to-one to 92 distinct anchor ordinals (exact label + resolved-URL comparison against the same anchor element; queries and fragments preserved; composite banner anchors identified by exact CTA child elements; each row assigned to a distinct occurrence; source-versus-inventory counts verified for every demo label on every inspected page). 2 rows classified as client-side-extracted (Showpad's \"Request to join\" and \"Take a tour\" — labels verified in rendered page, destinations taken from the live rendered DOM). Occurrence audit file: `phase2c/cta_occurrence_audit.csv` (Source URL + anchor ordinal + Table D row identifier).")
lines.append("")
lines.append("Key patterns (full table in CSV — summary only):")
lines.append("")
lines.append("- **Salesloft:** \"Talk to Sales\" ×3 homepage placements (nav desktop, nav mobile variant, footer) + ×3 forecast-page placements (nav, nav-adjacent layout element, footer) → /see-it-live ([salesloft.com](https://www.salesloft.com/), [forecast page](https://www.salesloft.com/platform/sales-forecasting-software)); hero CTAs are content-first; final CTA \"Book 15 Minutes\" (time-boxed). Nav banner \"Get the Report\" → gated benchmark report ([homepage](https://www.salesloft.com/)).")
lines.append("- **Showpad:** \"Request a demo\" ×3 homepage (nav, hero, final) + ×3 RevLeaders page (nav, content, footer) → /request-a-demo ([showpad.com](https://www.showpad.com/), [RevLeaders page](https://www.showpad.com/showpad-for-revenue-leaders)); module CTAs are \"Start with X\" / \"Explore X\" (content-first); \"Take a tour\" → /interactive-product-tour?utm_source=homepage (client-side); \"Request to join\" → https://eitf.showpad.com/?ribbon=eitf-2026 (client-side). Pricing link in nav ([homepage](https://www.showpad.com/)).")
lines.append("- **Mindtickle:** \"Book a demo\" (nav ×2 incl. mobile variant) / \"Request a demo\" (final) / \"Get a demo\" (platform section + final area ×2) + RevLeaders page ×5 → /request-a-demo/ ([mindtickle.com](https://www.mindtickle.com/), [RevLeaders page](https://www.mindtickle.com/solutions/sales-leadership-solutions-training/)); hero features product-led \"Try AI Role Play\" → /ai-role-plays/ (UTM; redirects to roleplay.mindtickle.com — dedicated roleplay product site); G2 badge as CTA; RevLeaders page has \"Read the report\" → campaigns.mindtickle.com/cro-and-sales-leadership-outlook-report-2024 (CRO-specific report) ([RevLeaders page](https://www.mindtickle.com/solutions/sales-leadership-solutions-training/)).")
lines.append("- **Allego:** \"See a Demo\" ×5 homepage occurrences + ×9 SalesLeaders page occurrences (nav desktop, nav mobile variant, hero, ×5 alternating content sections, final CTA — placements confirmed by DOM ancestors), all → /schedule-a-demo-of-allego/ ([allego.com](https://www.allego.com/), [SalesLeaders page](https://www.allego.com/solutions/sales-leadership/)); module CTAs are \"Learn more about X\"; competitive switch banner.")
lines.append("")
lines.append(f"**Full table: `phase2c/table_D_cta_strategy.csv` ({len(D)} rows — not rendered inline; see CSV).**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table E — CRO-Focused Messaging")
lines.append("")
lines.append(f"{len(E)} records. Highlights (first 10 shown; full table in CSV):")
lines.append("")
cols = list(E[0].keys())
lines.append("| " + " | ".join(cols) + " |")
lines.append("|" + "---|" * len(cols))
for r in E[:10]:
    cells = []
    for c in cols:
        v = esc(r[c])
        if 'URL' in c or 'Evidence' in c: v = cite_urls_field(v)
        cells.append(v)
    lines.append("| " + " | ".join(cells) + " |")
lines.append("")
lines.append(f"**Full table: `phase2c/table_E_cro_messaging.csv` ({len(E)} rows — only first 10 rendered inline).**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Table F — PitchSense Messaging Comparison (PROVISIONAL — pending Product Narrative v1)")
lines.append("")
lines.append("All interpretations are analyst views, not capability or market-absence claims. Vendor statements are the vendors' own claims, preserved verbatim.")
lines.append("")
cols = list(F[0].keys())
lines.append("| " + " | ".join(cols) + " |")
lines.append("|" + "---|" * len(cols))
for r in F:
    cells = []
    for c in cols:
        v = esc(r[c])
        v = cite_urls_field(v)
        cells.append(v)
    lines.append("| " + " | ".join(cells) + " |")
lines.append("")
lines.append("**Full table: `phase2c/table_F_pitchsense_comparison.csv`.**")
lines.append("")
lines.append("---")
lines.append("")

# ─── Trust inventory + strategic prose (preserved from existing report, with citations) ───
s = open(REPORT, encoding='utf-8').read()
i = s.find('## Trust and Credibility')
if i >= 0:
    trust = s[i:s.find('---\n\n## Final Strategic Analysis')]
    trust = cite_urls_field(trust)
    lines.append(trust.rstrip())
    lines.append("")
    lines.append("---")
    lines.append("")
    j = s.find('## Final Strategic Analysis')
    if j >= 0:
        strategic = s[j:s.find('**Research date:** October 19, 2026. All quotes')]
        strategic = cite_urls_field(strategic)
        lines.append(strategic.rstrip())
        lines.append("")
        lines.append("**Research date:** October 19, 2026. All quotes verified against the cited page. Client-side content labeled per convention. Table F remains PROVISIONAL pending the official Product Narrative v1. Deliverable CSVs: phase2c/table_A–F + cta_occurrence_audit.csv (in Project files).")
    else:
        lines.append("## Final Strategic Analysis")
        lines.append("")
        lines.append("(strategic analysis section — see previous version)")
else:
    lines.append("## Trust and Credibility Inventory (observed on inspected pages)")
    lines.append("")
    lines.append("(trust inventory — see previous version)")

content = "\n".join(lines) + "\n"

# ─── Write to temp, validate, replace ───
tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.md', dir=WS, delete=False, encoding='utf-8')
tmp.write(content)
tmp.close()

with open(tmp.name, encoding='utf-8') as f:
    check = f.read()
issues = []
if '80 rows' in check: issues.append("stale 80 rows")
if '78 rows' in check: issues.append("stale 78 rows")
if len(re.findall(r'(?<!\*)\*[^*\n]+\*(?!\*)', check)): issues.append("italics present")
if 'coaches, guides, and acts' in check: issues.append("wrong conjugation")
if f'{TOTAL} records total' not in check: issues.append("total count missing")
if re.search(r'<h[1-6]>', check): issues.append("unescaped HTML tags")
if 'persona-grid' in check: issues.append("persona-grid in sequence")
if 'self-serve-first' in check: issues.append("self-serve-first in sequence")
if 'final CTA section position is recorded' in check: issues.append("placeholder present")

if issues:
    print(f"VALIDATION FAILED: {issues}")
    os.unlink(tmp.name)
else:
    shutil.move(tmp.name, REPORT)
    print(f"VALIDATION PASSED — report generated: {len(check)} bytes")
    print(f"Table D totals from CSV: TOTAL={TOTAL}")
    for c in COMPANIES:
        h=breakdown.get((c,'homepage'),0); s_=breakdown.get((c,'supporting'),0)
        print(f"  {c}: {h}+{s_}={h+s_}")
    print(f"Citations in report: {check.count('](http')}")
    print(f"Analyst interpretation paragraphs: {check.count('(Analyst interpretation):')}")
