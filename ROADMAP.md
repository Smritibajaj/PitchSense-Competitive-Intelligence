# Research Roadmap — Maintenance and Expansion

This repository is the ongoing home of the PitchSense competitive-intelligence research. Phase 1 changes go into `phase1/pitchsense_competitor_research_master.md` and its batch file together (see the `evidence-update` skill).

Research rules (rubric, entity resolution, evidence and claim rules, gates) live in `RESEARCH_RULES.md`. This file tracks what is still to do.

## Verification backlog (unresolved flags from the 50-company research)

Priority items to verify against release notes / product docs:

1. Salesforce Agentforce: whether the documented "retain context" Long-Horizon Runtime is reused across sales-agent workflows; SM held at 1 pending this.
2. ~~Wonderway: the call-capture/analysis mechanism behind "Real sales coaching on EVERY. SINGLE. CALL."; AI Coach is in beta.~~ **Resolved Oct 19, 2026:** the AI Coach is now Verity (BTS) and documents scoring of every call through dialer/video/CI integrations, plus transcription; CI 0 (unverified) → 1, SM stays 0.
3. Aviso: whether "conversational intelligence" and "Coaching & Enablement" (capability-list mentions) become documented products.
4. ~~HubSpot Breeze: the Data agent "insights from your CRM, calls, and documents" workflow (CoI held at 1 unverified).~~ **Resolved Oct 19, 2026:** the smart-properties knowledge-base article lists files and documents as a data source; CoI 1 confirmed, total 3.
5. Showpad: Genie's connection to recorded conversations; merged-stack (Bigtincan/Brainshark) integration and GA status.
6. Backstory (ex-People.ai): whether call-content analysis is transcript-level or metadata-only.
7. Mindtickle: ElevateOS availability; clarify "decade of rep behavior data".
8. Gong: newer agent features GA status (Gong Enable).
9. Noota: Sales Agent GA status (currently "Coming soon").
10. Microsoft Copilot for Sales: release-note coverage beyond Microsoft Learn docs (marketing page unfetchable). Oct 19, 2026: docs now title it "Sales agent"; the What's new page has no feature entries and points to the M365 roadmap; rename date still unverified. Still open. Also review whether GA confirm-before-save CRM field writes justify DI 2.

## Triggered checks raised by Phase 2 batches 6–11 — resolved Oct 19, 2026

All checked against primary sources; changes logged in the Phase 1 master header. No shortlist position changed.

- PathFactory: acquired by Kaltura April 1, 2026 (Kaltura 10-Q). Brand live; scores unchanged.
- Fathom: acquired by Superhuman (formerly Grammarly), announced Sep 14, 2026; product unchanged; scores unchanged.
- Wonderway: BTS-owned since June 2024; AI Coach renamed Verity. CI 0* → 1 (see backlog item 2).
- Microsoft Copilot for Sales: docs now titled "Sales agent"; evidence re-verified; scores unchanged.
- Hyperbound: Perform/Kota Activate (GA) document native recording and deal risks. CI 1 → 2, DI 0 → 1, total 6.
- Regie.ai: RegieGO is the product; dialer records calls with transcript recaps. CI 0 → 1, total 2.
- Wording drift: quotes refreshed for Circleback, Quantified, PitchMonster, HubSpot Breeze, Humantic AI; scores unchanged except HubSpot CoI confirmed.

## Triggered checks to watch (opened Oct 19, 2026)

- Quantified Field AI: beta, release scheduled Q4 2026; at GA it would document real-visit analysis (CI 0 → 1 candidate).
- Hyperbound private-preview agents (Deal Strategist, Live Call Coaching, Agentic Enablement): at GA, re-check DI (structured CRM writes) and CoI (live battlecards); SM 2 candidate from Kota.
- Fathom: whether it stays standalone or folds into Superhuman.
- ~~PathFactory: Kaltura/eSelf integration GA.~~ **Closed Oct 20, 2026:** removed from scope in the second swap.
- Wonderway: brand direction under BTS (Wonderway vs. Verity); Phase 2 homepage may need re-capture under Verity.
- Circleback DI 1: HubSpot integration describes activity logging on deals; review whether this exceeds CRM sync.

## Triggered checks raised by the Phase 2 full-format upgrade (batches 4–11, opened Oct 19, 2026)

Observations from the captured pages, not score changes. Verify against primary sources before touching the Phase 1 master.

- Momentum: homepage banner "Momentum is now part of Salesforce!" links to a Salesforce news story about a definitive agreement to acquire it. Re-check entity resolution (RESEARCH_RULES §2) and close date.
- ~~Observe.AI: review SM evidence for its "Shared memory and connective tissue" layer.~~ **Closed Oct 20, 2026:** removed from scope in the swap (contact-centre tool outside the Narrative's buyer).
- Hyperbound: "Calls, roleplays, email, CRM, and Slack — connected through your buyers, deals, and reps" (screen-reader-only text). Adds to the existing SM 2 watch item.
- Salesforce (Agentforce): FAQ describes Sales Coach role-play tailored to specific deals; check whether it is GA and in scope for CoI.
- Wonderway: the AI coach is marketed as "Verity by BTS"; its sales-intelligence page carries an old template (lorem ipsum, /old-home link).
- Microsoft (Copilot for Sales): the linked /sales-solution/ page returns "Page not found"; still no usable CRO page.
- Data quality notes for anyone quoting metrics: conflicting figures on Quantified (80%/48 hours vs. 100%/five days) and Jiminny (37% vs. 62%). (Consensus, also flagged, left the scope on Oct 20, 2026.)

## Scope swap of Oct 20, 2026, and watch items for the new companies

Removed (all P4 weak fits): Uniphore, Level AI, Observe.AI, Reprise, Consensus, Dropbox DocSend. Added (Phase 1 Batch 5, Phase 2 batches 12–13): Granola, Read AI, Day AI, Oliv.ai, Glean, Spekit. Their earlier records stay in git history and in the dated batch reports.

- Granola: DI 1* and ChI 1* unverified (deal sync is note logging; coaching is prompt-based). Re-check DI when the native Salesforce connector (early access) is GA. Also a Built transcript source for PitchSense: watch for partnership vs. competition.
- Read AI: DI 2 depth partly rests on a vendor article on its own site; confirm CRM Copilot deal predictions and field writes in product docs.
- Glean: DI 1* rests on agent-library templates only; Meeting Coach is in beta. Re-check DI and ChI at GA.
- Spekit: ChI 2 rests on AI Role Play launched on Oct 20, 2026; confirm availability by plan. SM 2 candidate (governed knowledge reused across features).
- Second swap (Oct 20, 2026), from a screen of seven user-named candidates (record: `phase1/batches/pitchsense_competitor_research_batch6.md`): Balto and PathFactory out; Revenue Grid and Weflow in (Phase 2 batch 14). Weflow CoI 1* and SM 1* unverified; re-check when its content features or a persistence layer beyond Salesforce objects are documented.
- **Watch, not in scope:** MaxIQ (getmaxiq.com; 5 +2 unverified; "AI Coach" and "Context Graph" not yet documented as GA; site says some features are still being built; re-screen when they are). 6sense (2 +1 unverified; marketing intent data; its "context for your team and agents" messaging echoes PitchSense; re-screen if it adds conversation capture, deal risk or team memory).
- **Open decisions (screened Oct 20, 2026; record in `phase1/batches/pitchsense_competitor_research_batch6.md`):** add Tribble (8 +1 unverified, P1; AI RFP/sales agent with call recorder, CRM write-back and one knowledge layer; evidence from marketing pages only), Attio (7, P2; AI-native CRM with call recording and shared context) and Nooks (6 +1 unverified, P2; AI dialer with roleplays from real calls and call scoring)? Suggested replacements: Salesforce (Agentforce) (0 +1 unverified), Humantic AI (2), Regie.ai (2). Scratchpad (2; partial pivot to Clearskies, a "context layer for revenue AI") to watch. Guru (3) excluded: general knowledge base, slot covered by Glean.
- **Excluded after screening (Oct 20, 2026):** Forecastio (HubSpot-only forecasting, 2), DealHub AI / DealHub.io (quote-to-revenue, 2), MarketBetter (pre-conversation ABM/SDR playbooks, 2 +1 unverified).
- Day AI and Oliv.ai: both P1 and in the shared-memory five; add to the quarterly top-10 re-verification and to the next Phase 3 head-to-head set.

## Expansion candidates (next batch, when growing beyond 50)

- Companies identified during identity resolution but not scored: monitor for re-entry (BoostUp and SetSail were defunct as of Oct 19, 2026 — verify before any re-add).
- Rising adjacent categories to watch: AI SDR/agent startups, buyer-intelligence layers (Humantic-class), digital sales rooms (Aligned-class), in-person field-sales CI (Siro-class).
- Any newly funded CI/enablement startup competing for the same buying job.

## Maintenance cadence

- Quarterly: re-verify the top 10 and the shared-memory/CRO shortlists; update scores only with new documented evidence; log changes in the master report header.
- Triggered: M&A watch (consolidation is an active theme — Clari/Salesloft, Seismic/Highspot, Showpad/Bigtincan), major product launches by shortlist vendors, defunct/rebrand checks.
- Process: every update runs the gates (the edit hook does this automatically) and a reviewer pass on changed rows, then `/export-claude-project` refreshes claude.ai.
- Quarterly also: re-capture Phase 2 messaging for the top 10 (`phase2-batch` skill).

## Open synthesis items

- The three gap hypotheses remain testable, not verified absences; validate each against its named partial counterexamples before using in positioning work.
- Phase 3 CRO positioning is complete (`phase3/`; all-50 check and claim check added Oct 19, 2026). Revisit its hero direction when deal risks, commitments, or real-call scoring ship (Narrative v1 status), or if a coaching-led vendor (Hyperbound) adds source evidence and a CRO frame.
- Review Phase 3 Direction A (source-backed answers) against the counterexamples in Phase 2 synthesis C7: Noota, Read AI, Siro, Humantic AI, Quantified and Hyperbound (plus Balto, removed Oct 20) make source- or evidence-link claims, in addition to Backstory and Attention.
- Before public use of the Phase 3 page: confirm "Admins see adoption, never scores" and "company-owned data" with the product owner (Narrative-stated, not on the status list).
- ~~Reconcile Phase 2 Table F (batches 1–3) with Narrative v1 and review its PROVISIONAL label.~~ Done Oct 19, 2026: PitchSense column now gives Appendix status; reconciliation notes added; the "approved-content governance" nuance is Not in Narrative.
