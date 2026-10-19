---
name: evidence-update
description: Phase 1 capability evidence and scoring. Use when verifying a ROADMAP backlog item, re-scoring a company, adding a new company, or acting on M&A/rebrand news.
---

# Evidence update (Phase 1)

1. **Resolve identity.** Apply `RESEARCH_RULES.md` §2 before fetching anything.
2. **Gather evidence.** Use primary sources in this order: release notes, product docs, then official product pages. Record the URL and the research date for every claim. Separate GA from announced.
3. **Score.** Apply the rubric (`RESEARCH_RULES.md` §1) to each dimension. A change needs documented evidence. Mark unverified points with a star.
4. **Edit both records.** Update `phase1/pitchsense_competitor_research_master.md` (Tables A, B and C, plus any synthesis the change touches) **and** the relevant `phase1/batches/` file. Then add a dated line to the master header that names the change and its evidence.
5. **Gates.** The edit hook runs `tools/verify_phase1.py`. If it didn't fire, run it yourself. All six gates must PASS.
6. **Close the loop.** Mark the ROADMAP backlog item resolved (with the date and the finding) or still open (with what is missing). If a top-10, shared-memory or CRO shortlist position changed, say so explicitly.
7. **Hand back.** List every changed row (company, dimension, old → new, evidence URL) for the reviewer pass.

You are done when the gates pass and every changed row is listed with its evidence.
