#!/usr/bin/env python3
"""PostToolUse hook (Edit|Write): re-run the verification gates when a canonical research file changes.
Exit 2 sends the failing gate output back to Claude so it fixes the file before moving on."""
import json, os, subprocess, sys

WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    path = os.path.relpath(os.path.abspath(json.load(sys.stdin).get('tool_input', {}).get('file_path', '')), WS)
except Exception:
    sys.exit(0)

if path == 'phase1/pitchsense_competitor_research_master.md':
    script = 'tools/verify_phase1.py'
elif path.startswith('phase2/batches/') and path.endswith(('.csv', '.md')) or path == 'phase2/synthesis.md':
    script = 'tools/gen_phase2_master.py'  # regenerates the Phase 2 master + all50 CSV, then gates
else:
    sys.exit(0)

r = subprocess.run([sys.executable, '-I', os.path.join(WS, script)], capture_output=True, text=True)
if r.returncode != 0:
    print(f'Verification gates FAILED after editing {path} ({script}):\n{r.stdout}{r.stderr}', file=sys.stderr)
    sys.exit(2)
print(f'Gates passed after editing {path} ({script}).')
