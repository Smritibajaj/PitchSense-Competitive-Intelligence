#!/usr/bin/env python3
"""Build the claude.ai Project upload set in exports/claude-project/ (+ a zip).
Usage (from the project root): python3 -I tools/build_claude_project.py [--full]
  default : lean set (rules, Narrative, three masters, roadmap) — best answer quality in claude.ai
  --full  : also every batch report and CSV, for row-level lookups (larger; claude.ai will search it)
Refuses to build if any verification gate fails."""
import os, shutil, subprocess, sys, zipfile, glob

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(WS, 'exports', 'claude-project')
KN = os.path.join(OUT, 'knowledge')
FULL = '--full' in sys.argv

LEAN = [
    ('01_RESEARCH_RULES.md', 'RESEARCH_RULES.md', 'Rubric, entity resolution, evidence rules, PitchSense claim rules, verification gates.'),
    ('02_PitchSense_Product_Narrative_v1.pdf', 'source/PitchSense_Product_Narrative_v1.pdf', 'PitchSense Product Narrative v1 (Sep 30, 2026): what PitchSense does; Appendix = Built / In build / Planned.'),
    ('03_PHASE1_MASTER_capability_scores.md', 'phase1/pitchsense_competitor_research_master.md', 'Phase 1 master: 50 companies, Tables A/B/C, scores, final synthesis, gap hypotheses.'),
    ('04_PHASE2_MASTER_website_messaging.md', 'phase2/pitchsense_phase2_messaging_master.md', 'Phase 2 master: website messaging for all 50, full Tables A–F for 10, synthesis, flags.'),
    ('05_PHASE3_CRO_positioning.md', 'phase3/pitchsense_phase3_cro_positioning.md', 'Phase 3: CRO positioning synthesis and landing-page recommendations (recommendations, not findings).'),
    ('06_ROADMAP.md', 'ROADMAP.md', 'Verification backlog, triggered checks, expansion candidates, maintenance cadence.'),
]

# Gates first: never export an unverified state.
for script in ('tools/verify_phase1.py', 'tools/gen_phase2_master.py'):
    r = subprocess.run([sys.executable, '-I', os.path.join(WS, script)], capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit(f'\nABORTED: {script} reported a failing gate. Fix it before exporting.')

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(KN)
files = list(LEAN)
if FULL:
    for i, p in enumerate(sorted(glob.glob(os.path.join(WS, 'phase1', 'batches', '*.md'))), 1):
        files.append((f'10_phase1_batch{i}_detail.md', os.path.relpath(p, WS), 'Phase 1 batch detail.'))
    for d in sorted(glob.glob(os.path.join(WS, 'phase2', 'batches', 'batch*'))):
        b = os.path.basename(d)[:7]  # batchNN
        for p in sorted(glob.glob(os.path.join(d, '*.md')) + glob.glob(os.path.join(d, '*.csv'))):
            files.append((f'20_phase2_{b}_{os.path.basename(p)}', os.path.relpath(p, WS), 'Phase 2 batch detail.'))

for dst, src, _ in files:
    shutil.copy2(os.path.join(WS, src), os.path.join(KN, dst))
shutil.copy2(os.path.join(WS, 'tools', 'claude_project', 'PROJECT_INSTRUCTIONS.md'), os.path.join(OUT, 'PROJECT_INSTRUCTIONS.md'))

idx = ['# PitchSense Competitive Intelligence — Project Index', '',
       'Generated from the Claude Code project by `tools/build_claude_project.py`' + (' --full' if FULL else '') + '. '
       'Do not edit these files in claude.ai; changes are made in the Claude Code project and re-exported.', '']
idx += [f'- `{dst}` — {desc}' for dst, _, desc in files if not dst.startswith(('10_', '20_'))]
if FULL:
    idx += ['', '## Batch detail', ''] + [f'- `{dst}` (from `{src}`)' for dst, src, _ in files if dst.startswith(('10_', '20_'))]
open(os.path.join(KN, '00_INDEX.md'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')

zpath = os.path.join(WS, 'exports', 'PitchSense-Claude-Project.zip')
with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(OUT):
        for f in fs:
            p = os.path.join(root, f); z.write(p, os.path.relpath(p, os.path.dirname(OUT)))
size = sum(os.path.getsize(os.path.join(KN, f)) for f in os.listdir(KN))
print(f'\nBuilt {len(os.listdir(KN))} knowledge files ({size // 1024} KB) in exports/claude-project/ and {os.path.relpath(zpath, WS)}')
