# Claude Project Instructions

This repository contains the ongoing PitchSense competitive-intelligence research. Follow these instructions whenever researching competitors or editing research files.

## Source of truth

The consolidated master report, [`reports/pitchsense_competitor_research_master.md`](reports/pitchsense_competitor_research_master.md), is the source of truth. When new evidence is added, update the master report as well as any relevant batch files; do not update batch files alone.

## Frozen research rubric

Do not change the rubric without explicitly noting a rubric revision.

- Score five dimensions from 0 to 2 each, for a maximum total of 10: Call Intelligence, Deal Intelligence, Content Intelligence, Coaching Intelligence, and Shared Memory.
- Apply the Shared Memory functional test:
  - **1:** retained context in a limited scope is reused in workflows.
  - **2:** persistent context across sources is used across capabilities.
  - A chatbot, CRM sync, or AI search alone is insufficient. The product does not need to use the word “memory.”
- Use documented product evidence only. A score of 1 represents a documented partial capability. Flag uncertain depth or availability separately; show unverified points as provisional (for example, `2 (+1 unverified)`).
- Resolve company identities before fetching evidence and deduplicate operating companies:
  - Clari + Salesloft
  - Seismic + Highspot
  - Showpad + Bigtincan + Brainshark
  - People.ai → Backstory
  - ZoomInfo Chorus is a product, not a separate operating company.
- Separate announced capabilities from generally available (GA) capabilities. Examples requiring this distinction include Noota Sales Agent (“Coming soon”), Mindtickle ElevateOS, and Agentforce Long-Horizon Runtime.
- Preserve research dates and each company’s “Daily users” field. Label inferred values as inferred.

## Required verification after report changes

Run the available programmatic verification gates after every report change, and check that:

1. Tables A, B, and C contain identical company sets.
2. The distinct-company count is correct.
3. Every dimension score is between 0 and 2.
4. Each total equals the sum of its component scores.
5. Every Table B row includes evidence URLs.
6. Every Table A row has a consistent 12-cell column count.

Review changed rows after running the gates. Do not re-share the report until both checks are complete.

## Verification backlog

These are unresolved flags from the 50-company research. Prioritize release notes and product documentation when verifying them; update the master report with any findings.

1. **Salesforce Agentforce:** Verify whether the documented “retain context” Long-Horizon Runtime is reused across sales-agent workflows. Shared Memory remains at 1 pending verification.
2. **Wonderway:** Verify the call-capture and analysis mechanism behind “Real sales coaching on EVERY. SINGLE. CALL.” AI Coach is in beta.
3. **Aviso:** Verify whether “conversational intelligence” and “Coaching & Enablement” capability-list mentions are documented products.
4. **HubSpot Breeze:** Verify the Data agent workflow for “insights from your CRM, calls, and documents.” Call Intelligence remains at 1, with the additional point unverified.
5. **Showpad:** Verify Genie’s connection to recorded conversations, merged-stack (Bigtincan/Brainshark) integration, and GA status.
6. **Backstory (formerly People.ai):** Verify whether call-content analysis is transcript-level or metadata-only.
7. **Mindtickle:** Verify ElevateOS availability and clarify the “decade of rep behavior data” claim.
8. **Gong:** Verify the GA status of newer agent features, including Gong Enable.
9. **Noota:** Verify Sales Agent GA status; it is currently described as “Coming soon.”
10. **Microsoft Copilot for Sales:** Check release-note coverage beyond Microsoft Learn documentation; the marketing page was unfetchable.

## Expansion candidates

When expanding beyond 50 companies:

- Recheck companies found during identity resolution but not scored. BoostUp and SetSail were reported defunct as of October 19, 2026; verify their current status before re-adding them.
- Watch adjacent categories: AI SDR/agent startups, buyer-intelligence layers (Humantic-class), digital sales rooms (Aligned-class), and in-person field-sales conversation intelligence (Siro-class).
- Include newly funded conversation-intelligence or enablement startups when they compete for the same buying job.

## Maintenance cadence

- **Quarterly:** Re-verify the top 10 and the Shared Memory/CRO shortlists. Change scores only when new documented evidence supports the change, and log changes in the master report header.
- **Triggered:** Check M&A and consolidation (including Clari/Salesloft, Seismic/Highspot, and Showpad/Bigtincan), major product launches by shortlist vendors, and defunct or rebrand status.
- For every update, run the programmatic verification gates and have a reviewer check changed rows before sharing the report under the same file name.

## Open synthesis items

- Treat the three gap hypotheses as testable, not as verified absences. Validate each against its named partial counterexamples before using it in positioning work.
- The research does not yet contain a PitchSense positioning recommendation. The evidence base is ready for that next step; do not present a recommendation as an existing research conclusion.
