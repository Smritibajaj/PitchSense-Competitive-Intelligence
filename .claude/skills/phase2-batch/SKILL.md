---
name: phase2-batch
description: Phase 2 website-messaging capture. Use when adding companies to Phase 2, re-capturing changed homepages, or refreshing messaging on the quarterly cadence.
---

# Phase 2 batch

1. **Scope check.** Each company must already be in the Phase 1 master (Table A). If it isn't, stop: it needs Phase 1 scoring first (`evidence-update`), because the Phase 2 gates require the same company set as Phase 1.
2. **Assign batches.** Split the companies into groups of up to 5. Number them from the next free `phase2/batches/batchNN`. A re-capture of a company already covered gets a new batch too; the old batch stays as the dated record.
3. **Dispatch.** Send one `website-messaging-researcher` agent per batch, all in a single message so they run in parallel. Give each one its companies, its `NN`, and today's date.
4. **Supersede, if re-capturing.** The generator finds new `batchNN` folders automatically. When a company is re-captured, the combined table must not list it twice, so remove the superseded row from the older batch CSV, but only after the user agrees. The older batch's `captures/` remain as the dated record.
5. **Regenerate.** Run `python3 -I tools/gen_phase2_master.py`. All gates must PASS.
6. **Synthesis.** Update `phase2/synthesis.md`: counts, examples and implications. Regenerate again.
7. **Flags.** Add ownership changes, rebrands and blocked pages to `ROADMAP.md` under triggered checks. They are not score changes.

You are done when the gates pass, the synthesis counts match the new table, and the user has each agent's summary of Not-verified fields and notable changes.
