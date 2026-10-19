# PitchSense Competitive Intelligence

Competitive research for PitchSense AI, a sales AI covering calls, deals, content and coaching on one shared memory. It covers **50 competitors** in three phases. This folder is the one home for the research: open it in Claude Code to work on it, and export it to claude.ai to discuss it.

## Layout

```
RESEARCH_RULES.md        how research is done: rubric, entity rules, evidence rules, claim rules, gates
ROADMAP.md               what's left: verification backlog, triggered checks, expansion, cadence
CLAUDE.md                instructions Claude Code loads automatically
source/                  PitchSense Product Narrative v1 (PDF + text): read-only source of truth
phase1/                  capability research: master report (50 companies, scores) + batch details
phase2/                  website messaging: master report + all-50 CSV (both generated), synthesis.md
  batches/batch01…11/    canonical batch CSVs/reports; batches 06–11 keep their HTML captures
phase3/                  CRO positioning synthesis and landing-page recommendations
tools/                   gate scripts, Phase 2 generator, claude.ai export builder, edit hook
.claude/                 Claude Code setup: settings (permissions + hook), skills, research agent
exports/                 generated claude.ai upload set (rebuild; don't edit)
```

## Working in Claude Code

Ask in plain words. The matching workflow loads on its own:

| You say… | What runs |
|---|---|
| "Verify backlog item 6 (Backstory)" / "Re-score Gong" / "Add company X" | `evidence-update` skill: primary-source evidence, rubric scoring, master + batch edit, gates, changed-row list |
| "Re-capture the top 10 homepages" / "Add X to Phase 2" | `phase2-batch` skill: parallel research agents, regenerated master, gates |
| "Review this landing page copy" / "Write a one-pager" | `claim-check` skill: every PitchSense claim checked against the Narrative's Built / In build / Planned status |
| `/export-claude-project` | rebuilds the claude.ai upload set (only if every gate passes) |

The verification gates run automatically whenever a report or batch file is edited.

## Using it in claude.ai

1. Run `/export-claude-project` in Claude Code.
2. In your claude.ai Project, replace the knowledge files with `exports/claude-project/knowledge/*`. That's 7 files: index, rules, Narrative, the three phase masters, and the roadmap.
3. Paste `exports/claude-project/PROJECT_INSTRUCTIONS.md` into the Project instructions.

Edit only in Claude Code, then re-export. The claude.ai copy is read-only by convention.

## Key results (Oct 19, 2026)

- **Phase 1 top 10 by capability overlap:** Gong 8; Aida, Attention, Outreach, Showpad, Allego, Mindtickle 7; Sybill, Traq.ai, Avoma 6.
  - Shared-memory five: Sybill, Aida, Gong, Backstory, Attention.
  - CRO five: Salesloft + Clari, Gong, Backstory, Attention, Aviso.
- **Phase 2:**
  - No homepage H1 among the 50 leads with "memory", but meeting notetakers now use memory wording in their hero copy.
  - AI-agent language appears in 14 of 50 heroes.
  - A demo CTA appears in 33 of 50 heroes.
- **Phase 3 recommendation:**
  - Lead with "intelligence you can check" (source-linked answers) plus readiness the CRO can see. Both are Built.
  - Hold "shared memory" as the mechanism until memory layers 2–3, deal risks and real-call scoring ship.
