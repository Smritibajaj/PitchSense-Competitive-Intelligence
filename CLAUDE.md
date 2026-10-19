# PitchSense Competitive Intelligence

Ongoing competitive-intelligence research for PitchSense AI: 50 competitors, three phases. **`RESEARCH_RULES.md` governs every research and writing task here.** It holds the rubric, entity resolution, evidence rules, PitchSense claim rules and the verification gates. Read it before researching, scoring or writing.

## Sources of truth

| What | File | Edited how |
|---|---|---|
| PitchSense capabilities and status | `source/PitchSense_Product_Narrative_v1.pdf` (text: `…_text.md`) | Read-only |
| Phase 1 scores and synthesis | `phase1/pitchsense_competitor_research_master.md` | By hand, together with the matching `phase1/batches/` file |
| Phase 2 website messaging | `phase2/batches/*/` CSVs + `phase2/synthesis.md` | By hand; the master and `all50.csv` are **generated** |
| Phase 3 CRO positioning | `phase3/pitchsense_phase3_cro_positioning.md` | By hand; recommendations stay labelled as recommendations |
| Backlog, triggered checks, cadence | `ROADMAP.md` | By hand |

`exports/` is generated output for claude.ai. Regenerate it; never edit it.

## Commands

- `python3 -I tools/verify_phase1.py`: runs the six Phase 1 gates (exits non-zero on failure).
- `python3 -I tools/gen_phase2_master.py`: regenerates `phase2/pitchsense_phase2_messaging_master.md` and `phase2/phase2_website_messaging_all50.csv`, then runs nine gates.
- `python3 -I tools/build_claude_project.py [--full]`: runs every gate, then builds `exports/claude-project/` and its zip.

A PostToolUse hook (`tools/hooks/after_edit.py`) runs the matching gates whenever the Phase 1 master, a Phase 2 batch file or the synthesis is edited. A failing gate is reported back to Claude for fixing before the work continues.

## Workflows

- **Capability evidence, scoring, new companies, M&A news**: the `evidence-update` skill.
- **Website-messaging capture**: the `phase2-batch` skill, which dispatches `website-messaging-researcher` agents, one per batch.
- **Any PitchSense copy, positioning or comparison**: the `claim-check` skill.
- **Refreshing the claude.ai Project**: `/export-claude-project`.

## Current state (Oct 19, 2026)

- Phases 1–3 are complete for all 50 companies. Open items are in `ROADMAP.md`: the 10-item verification backlog and the triggered checks from Phase 2.
- Phase 2 Table F (batches 1–3) is still PROVISIONAL: it predates Narrative v1 and has not been reconciled with it.
