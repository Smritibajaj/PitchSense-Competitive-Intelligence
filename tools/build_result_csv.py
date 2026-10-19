#!/usr/bin/env python3
"""Generate result/competitors_all50.csv and .xlsx: one 17-column row per competitor.
Takes the messaging columns from phase2/phase2_website_messaging_all50.csv, except Positioning
overrides and Differentiation, which come from result/positioning_differentiation.csv.
PitchSense Category lists the Product Narrative v1 areas (four intelligences on one shared memory) in which
the competitor has documented capability: a Phase 1 Table B score of 1 or 2 in
phase1/pitchsense_competitor_research_master.md. Unverified (starred) points are left out, as in the Phase 1 total.
Usage (from the project root): python3 -I tools/build_result_csv.py"""
import csv, os, re, sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(WS, 'phase2', 'phase2_website_messaging_all50.csv')
FIX = os.path.join(WS, 'result', 'positioning_differentiation.csv')
P1 = os.path.join(WS, 'phase1', 'pitchsense_competitor_research_master.md')
OUT = os.path.join(WS, 'result', 'competitors_all50.csv')
CATS = ['Call Intelligence', 'Deal Intelligence', 'Content Intelligence', 'Coaching Intelligence', 'Shared Memory']
COLS = ['Company', 'Website', 'Category', 'PitchSense Category', 'PitchSense Overlap (of 10)', 'ICP', 'Pain Points', 'H1', 'H2',
        'Hero Description', 'Primary CTA', 'Secondary CTA', 'Section Headings', 'Positioning', 'Differentiation',
        'Source URLs', 'Verification Status']
OUT_XLSX = os.path.join(WS, 'result', 'competitors_all50.xlsx')


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def lines(*vals):
    """Join non-empty values one per line, dropping repeats."""
    out = []
    for v in vals:
        for x in (v or '').splitlines():
            if x.strip() and x.strip() not in out:
                out.append(x.strip())
    return '\n'.join(out)


def key(n):
    """Same company key as tools/gen_phase2_master.py, so Phase 1 and Phase 2 names match."""
    return re.sub(r'[^a-z]', '', n.lower().split('(')[0].split('+')[0].split(' incl')[0])[:6]


def categories(scores):
    """Narrative categories with a confirmed Phase 1 score of 1 or 2 (starred points are unverified)."""
    return ', '.join(c for c, x in zip(CATS, scores) if x.strip() in ('1', '2')) or 'None documented'


def write_xlsx(path, header, data):
    """Minimal .xlsx (stdlib only): frozen header, filters, wrapped text."""
    import zipfile
    from xml.sax.saxutils import escape
    col = lambda i: (col((i // 26) - 1) if i >= 26 else '') + chr(65 + i % 26)
    clean = lambda s: escape(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s)))
    narrow = ('PitchSense Overlap (of 10)',)
    width = {'Company': 24, 'Website': 24, 'Category': 26, 'PitchSense Category': 30, 'PitchSense Overlap (of 10)': 14, 'Verification Status': 70}
    def cell(r, c, v, style):
        ref = f'{col(c)}{r}'
        if isinstance(v, str) and re.fullmatch(r'\d+', v) and COLS[c] == 'PitchSense Overlap (of 10)':
            return f'<c r="{ref}" s="{style}"><v>{v}</v></c>'
        return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{clean(v)}</t></is></c>'
    rows_xml = ['<row r="1">' + ''.join(cell(1, i, h, 1) for i, h in enumerate(header)) + '</row>']
    for n, row in enumerate(data, start=2):
        rows_xml.append(f'<row r="{n}" ht="90" customHeight="1">' + ''.join(cell(n, i, v, 3 if header[i] in narrow else 2) for i, v in enumerate(row)) + '</row>')
    cols_xml = ''.join(f'<col min="{i + 1}" max="{i + 1}" width="{width.get(h, 42)}" customWidth="1"/>' for i, h in enumerate(header))
    end = f'{col(len(header) - 1)}{len(data) + 1}'
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
             f'<dimension ref="A1:{end}"/>'
             '<sheetViews><sheetView workbookViewId="0"><pane xSplit="1" ySplit="1" topLeftCell="B2" activePane="bottomRight" state="frozen"/></sheetView></sheetViews>'
             f'<sheetFormatPr defaultRowHeight="15"/><cols>{cols_xml}</cols><sheetData>{"".join(rows_xml)}</sheetData>'
             f'<autoFilter ref="A1:{end}"/>'
             '</worksheet>')
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
              '<fonts count="2"><font><sz val="10"/><name val="Arial"/></font><font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Arial"/></font></fonts>'
              '<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>'
              '<fill><patternFill patternType="solid"><fgColor rgb="FF1F3864"/><bgColor indexed="64"/></patternFill></fill></fills>'
              '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
              '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
              '<cellXfs count="4"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
              '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>'
              '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>'
              '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment horizontal="center" vertical="top"/></xf></cellXfs>'
              '</styleSheet>')
    parts = {
        '[Content_Types].xml': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/></Types>',
        '_rels/.rels': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>',
        'xl/workbook.xml': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<sheets><sheet name="Competitors" sheetId="1" r:id="rId1"/></sheets>'
            f'<definedNames><definedName name="_xlnm._FilterDatabase" localSheetId="0" hidden="1">Competitors!$A$1:${end.rstrip("0123456789")}${len(data) + 1}</definedName></definedNames></workbook>',
        'xl/_rels/workbook.xml.rels': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>',
        'xl/styles.xml': styles,
        'xl/worksheets/sheet1.xml': sheet,
    }
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, xml in parts.items():
            z.writestr(name, xml)


p1, sec = {}, None
for line in open(P1, encoding='utf-8'):
    if line.startswith('## '): sec = line.startswith('## Table B')
    c = [x.strip() for x in line.split('|')]
    if sec and len(c) > 9 and c[1].isdigit():
        p1[key(c[2])] = [categories(c[3:8]), c[8].replace('*', '')]

rows, fix = rd(SRC), {r['Company']: r for r in rd(FIX)}
nop1 = [r['Company'] for r in rows if key(r['Company']) not in p1]
if nop1 or len(p1) != 50:
    sys.exit(f'FAIL - Phase 1 Table B scores: {len(p1)} rows parsed; no match for {nop1}')
missing = [r['Company'] for r in rows if r['Company'] not in fix]
extra = sorted(set(fix) - {r['Company'] for r in rows})
if missing or extra:
    sys.exit(f'FAIL - company sets differ. Missing from fix file: {missing}; unknown in fix file: {extra}')

data = []
for r in rows:
    x = fix[r['Company']]
    data.append([r['Company'], r['Website'], r['Category']] + p1[key(r['Company'])] + [r['ICP'], r['Pain Point'], r['H1'], r['H2'],
                 r['Hero Description'], r['Primary CTA'], r['Secondary CTA'],
                 lines(r['Section Heading 1'], r['Section Heading 2'], r['Section Heading 3']),
                 x['Positioning'].strip() or r['Positioning'], x['Differentiation'],
                 lines(r['Source URL'], x['Source URLs']),
                 r['Verification'] + '\nPositioning/Differentiation: ' + x['Verification']])
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(COLS)
    w.writerows(data)
write_xlsx(OUT_XLSX, COLS, data)
print(f'PASS - wrote {len(rows)} rows x {len(COLS)} columns to result/competitors_all50.csv and .xlsx')
