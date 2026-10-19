# Research Roadmap — Maintenance and Expansion

This Project is the ongoing home of the PitchSense competitive-intelligence research. The master report (`reports/pitchsense_competitor_research_master.md`) is the source of truth; update it (not just the batch files) whenever new evidence lands.

## Frozen rules (do not change without noting a rubric revision)

- Five scoring dimensions, 0-2 each, max 10: Call Intelligence, Deal Intelligence, Content Intelligence, Coaching Intelligence, Shared Memory.
- Shared memory functional test: 1 = retained context in limited scope reused in workflows; 2 = persistent cross-source context used across capabilities. A chatbot, CRM sync, or AI search alone is insufficient; the word "memory" is not required.
- Only documented product evidence; 1 means documented partial capability; uncertain depth/availability is flagged separately, and unverified points are shown as provisional totals (e.g., "2 (+1 unverified)").
- Entity resolution before fetching; dedupe operating companies (Clari+Salesloft; Seismic+Highspot; Showpad+Bigtincan+Brainshark; People.ai→Backstory; ZoomInfo Chorus is a product).
- Programmatic verification gates after every report change: identical company sets across Tables A/B/C, distinct-company count, scores 0-2, totals = sum of components, every Table B row carries evidence URLs, Table A rows have consistent column counts (12 cells).
- Announced vs GA capabilities separated (e.g., Noota Sales Agent "Coming soon"; Mindtickle ElevateOS; Agentforce Long-Horizon Runtime).
- Research dates and per-company "Daily users" fields preserved; inferred values labeled.

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

## Expansion candidates (next batch, when growing beyond 50)

- Companies identified during identity resolution but not scored: monitor for re-entry (BoostUp and SetSail were defunct as of Oct 19, 2026 — verify before any re-add).
- Rising adjacent categories to watch: AI SDR/agent startups, buyer-intelligence layers (Humantic-class), digital sales rooms (Aligned-class), in-person field-sales CI (Siro-class).
- Any newly funded CI/enablement startup competing for the same buying job.

## Maintenance cadence

- Quarterly: re-verify the top 10 and the shared-memory/CRO shortlists; update scores only with new documented evidence; log changes in the master report header.
- Triggered: M&A watch (consolidation is an active theme — Clari/Salesloft, Seismic/Highspot, Showpad/Bigtincan), major product launches by shortlist vendors, defunct/rebrand checks.
- Process: every update runs the programmatic verification gates and a reviewer pass on changed rows before the report is re-shared under the same file name.

## Open synthesis items

- The three gap hypotheses remain testable, not verified absences; validate each against its named partial counterexamples before using in positioning work.
- No PitchSense positioning recommendation exists yet (per the original brief); the evidence base is now complete for that next step.
