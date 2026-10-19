---
name: export-claude-project
description: Rebuild the claude.ai Project upload set from this repo.
disable-model-invocation: true
---

# Export to claude.ai

1. Run `python3 -I tools/build_claude_project.py` (lean, recommended), or add `--full` to include every batch file. The script refuses to build if any gate fails.
2. Tell the user:
   - In their claude.ai Project, replace the knowledge files with everything in `exports/claude-project/knowledge/`. Remove any old files that aren't in the new set.
   - Paste `exports/claude-project/PROJECT_INSTRUCTIONS.md` into the Project instructions.
   - The zip is at `exports/PitchSense-Claude-Project.zip`.
