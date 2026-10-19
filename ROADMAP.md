# Research Roadmap — Maintenance and Expansion

This repository is the ongoing home of the PitchSense competitive-intelligence research. Phase 1 changes go into `phase1/pitchsense_competitor_research_master.md` and its batch file together (see the `evidence-update` skill).

Research rules (rubric, entity resolution, evidence and claim rules, gates) live in `RESEARCH_RULES.md`. This file tracks what is still to do.

## Verification backlog (unresolved flags from the 50-company research)

Priority items to verify against release notes / product docs:

1. Salesforce Agentforce: whether the documented "retain context" Long-Horizon Runtime is reused across sales-agent workflows; SM held at 1 pending this.
2. Wonderway: the call-capture/analysis mechanism behind "Real sales coaching on EVERY. SINGLE. CALL."; AI Coach is in beta.
3. Aviso: whether "conversational intelligence" and "Coaching & Enablement" (capability-list mentions) become documented products.
4. HubSpot Breeze: the Data agent "insights from your CRM, calls, and documents" workflow (CoI held at 1 unverified).
5. Showpad: Genie's connection to recorded conversations; merged-stack (Bigtincan/Brainshark) integration and GA status.
6. Backstory (ex-People.ai): whether call-content analysis is transcript-level or metadata-only.
7. Mindtickle: ElevateOS availability; clarify "decade of rep behavior data".
8. Gong: newer agent features GA status (Gong Enable).
9. Noota: Sales Agent GA status (currently "Coming soon").
10. Microsoft Copilot for Sales: release-note coverage beyond Microsoft Learn docs (marketing page unfetchable).

## Triggered checks raised by Phase 2 batches 6–11 (Oct 19, 2026 homepage captures — verify before changing Master Report)

- PathFactory: homepage banner states acquisition by Kaltura.
- Fathom: site-wide banner "FATHOM IS NOW PART OF SUPERHUMAN".
- Wonderway: page references "Verity by BTS" (possible rebrand; relationship not stated); AI Coach still labeled beta.
- Microsoft Copilot for Sales: H1 now "Sales solution in Microsoft Copilot" (adoption page; marketing page still bot-blocked).
- Hyperbound: "AI-Powered Roleplay Platform" framing replaced by Practice / Perform / Kota Activate.
- Regie.ai: product now "RegieGO" ("agentic sales workspace").
- Wording drift vs. Master Report quotes: Circleback "Company Brain" (now title-only), Quantified ("one audit trail"), PitchMonster ("300K+ reps" vs 30,000+), HubSpot Breeze, Humantic AI ("Miia, Pi & Signals").

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
- Phase 3 CRO positioning exists (`phase3/`). Revisit its hero direction when deal risks, commitments, or real-call scoring ship (Narrative v1 status).
- Reconcile Phase 2 Table F (batches 1–3) with Narrative v1 and review its PROVISIONAL label.
