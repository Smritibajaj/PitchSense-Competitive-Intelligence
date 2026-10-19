# Salesloft + Clari — Evidence Record (Phase 2, Batch 3)
Research date: October 19, 2026 (Europe/Berlin)
Entity note: Salesloft and Clari are one company — merger page title "Salesloft & Clari Are Now One Company" (https://www.salesloft.com/clari-salesloft-merger, captured). https://www.clari.com/ redirects to https://www.salesloft.com/ (redirect observed Oct 19, 2026). One website analyzed (salesloft.com) with the redirect and merger recorded. Login menu shows the merged product suite: "Log in to Salesloft" (app.salesloft.com), "Log in to Clari Forecast" (app.clari.com), "Log in to Conversations" (copilot.clari.com), "Log in to Drift" (start.drift.com), "Log in to Groove" (engine.groove.clari.com).

Sources captured:
- https://www.salesloft.com/ (homepage) — phase2c/salesloft_home.html (29KB)
- https://www.salesloft.com/platform/sales-forecasting-software (Clari Forecast page, CRO-relevant) — phase2c/salesloft_forecast.html
- https://www.salesloft.com/clari-salesloft-merger (merger announcement) — phase2c/salesloft_merger.html
- Rendered-page inspection (cloud browser, Oct 19, 2026): hero, nav, feature tabs, signal-stream pills. Privacy overlay present (not dismissed; does not obscure main content). Screenshots preserved in session history.

## Homepage structure (in HTML order, heading levels from HTML tags)
1. Nav: PLATFORM | SOLUTIONS | RESOURCES | COMPANY | LOGIN (dropdown: Salesloft / Clari Forecast / Conversations / Drift / Groove) | "Talk to Sales" → /see-it-live. Mega-menu: For Account Teams (Cadence — "Build & nurture sales pipeline"; Conversation Intelligence — "Get insights about buyers & sellers"; Deals — "Manage & close opportunities"; Rhythm — "Prioritize your workflow") / For Executive & Revops Teams (Clari Forecast — "Improve forecast accuracy"; Inspect — "Get full pipeline visibility"; Revenue Cadences — "Keep teams aligned & accountable"; Analytics — "Turn data into action") / By Outcome (Create Sales Pipeline / Convert & Close Deals / Grow & Retain Customers) / By Industry / For Customers / Learn & Connect / Company / People. Banner: "2026 Revenue Benchmark Report Get the Report" → /resources/guides/revenue-benchmark-report-us
2. HERO — H1 (HTML <h1>): "Create . Convert . Grow ." (rendered as "Create. Convert. Grow." with a green dot; HTML has spaces around periods). Eyebrow: "THE PREDICTIVE REVENUE SYSTEM". Hero CTAs: "How it Works" (→ #outcomes-in-action, on-page anchor) + "See the Platform" (→ /platform-overview). Hero sub-tabs (feature bullets): "Prioritize seller actions" / "Understand deal risks" / "Drive predictable revenue" / "Fill your sales funnel faster" (4th partially cut in rendered capture; full text verified in HTML)
   - Hero media (rendered): floating UI pills showing an activity/signal stream ("Engaged with Rhythm", "Opened data sources", "Attended LinkedIn Live", "Invited to event") — signal-stream visualization; no video
3. H2: "The numbers behind our customers' success ." — stats: "50% Higher conversion rate" / "60% Less time to close a deal" / "100% Pipeline visibility" / "30% Higher sales efficiency" (01-04). Customer-story carousel with testimonials:
   - "The ability to standardize and automate processes across our teams delivers value to current sellers and brings new employees up to speed fast." — Jason Amidon, Director, US & Canada Sales Operations
   - "I don't call it a sales tool anymore. It's our go-to-market engine — the more teams use it, the smarter it gets." — Adelle Bonavire, Senior Director, GTM Process & Execution
   - "Salesloft rolled up their sleeves and became a true extension of our team." — Brian Fretschel, VP of Digital Selling Excellence
   - "Conversion rates on our trials have increased from being touched in 10 minutes at a rate of 1% to now 20%." — Kaycee Decker, Sales Operations Analyst
   - CTA "Read the Full Story" (Wrike case study link)
4. H2: "Capture every signal . Then act on them ." — "Salesloft captures every revenue signal across your stack, separates the ones that drive outcomes from the noise, and turns them into your next move — grounded in your data, not guesswork." + persona demo modules (H3s "CRO" and "Account team"; "Customized to your specific revenue motion and data"). CTA "See How Signals Become Revenue" → /signals
5. H3: "Sales teams hit their number, quarter after quarter with Salesloft."
6. FINAL CTA — H2: "The system behind your next win ." — CTAs: "Book 15 Minutes" (→ /see-it-live) + phone +1 (770) 756-8022 + "Talk to Sales" (→ /see-it-live) + "Get Updates" (→ /sign-up)
7. Footer — full sitemap: Platform (Overview, Tour Platform, AI Agents, Product Launch Hub, Partner Integrations, Signals, Consulting Services, Cadence, Clari Forecast, Conversation Intelligence, Deals, Inspect, Revenue Cadences, Rhythm) / Solutions / Resources (Community, Customer Education/academy, Office Hours, Find a Partner/marketplace, Product Release Notes, Resource Center, Research Guides & Reports, Events) / Company (About, Why Salesloft, Leadership, Newsroom, Become a Partner, Careers, Diversity) / Security (/security-compliance), Privacy, Trust Center (trust.salesloft.com), Platform Status

## Forecast page (/platform/sales-forecasting-software)
- Title: "Sales Forecasting Software Built to Act On"
- H1: "Sales Forecasting Software Built to Act On ."
- "Know your number" — "The market's most complete, AI-validated sales forecast, so you can call a number you can stand behind."
- "Catch risk early" — "Act early on slipping deals, stalled buying activity, and execution gaps."
- "Predict, then act" — "The only sales forecasting tool connected to your system of action, so you can make your number, not just predict it."
- Capabilities (H3s): "Forecast for your business goals" / "A unified dashboard" / "Track pipeline momentum" / "AI that validates your number" ("Forecast AI is trained on your historical data and predicts outcomes based on deal size, stage, and velocity.")
- H2: "Raise your expectations ." — "We've built the market's most accurate revenue forecasting software. Because stale data and gut feelings won't help you defend a number to the board."
- H3s: "Commit to a number you can trust" ("The AI Forecast Agent analyzes all your historical deal data and live rep activity, so your forecast accuracy is grounded in facts, not feelings.") / "Stop risks in their tracks" / "Drive more than just reporting" ("Risks, gaps, and opportunities automatically trigger next best actions in the seller workflow, so your team is held accountable to your number.")
- Resources: "Content designed for revenue leaders who would rather do than read."
- FAQ answers: "Salesloft's AI is trained on your historical deal data and layered with live rep and activity signals, so your forecast is grounded in fact, not gut feel." / "Salesloft lets anyone ask plain-language questions about revenue data and get instant answers — no RevOps ticket or stale report required." / "Salesloft is the only platform that combines AI-powered revenue forecasting, real-time deal tracking, and integrated execution in one place."

## CTA inventory (verified, one record per occurrence; placements confirmed by DOM ancestor classes)
- Nav (desktop): "Talk to Sales" → /see-it-live
- Nav (mobile variant, hidden on desktop): "Talk to Sales" → /see-it-live
- Nav banner (composite anchor "2026 Revenue Benchmark ReportGet the Report"): → /resources/guides/revenue-benchmark-report-us
- Hero: "How it Works" → #outcomes-in-action (on-page anchor) + "See the Platform" → /platform-overview
- Customer stories: "Read the Full Story" → /resources/case-studies/wrike-finds-an-operational-soulmate-for-closing-the-gap-between-buyers-and-sellers (one occurrence in HTML — Wrike case study; full URL recovered from source)
- Signals section (inside persona demo module): "See How Signals Become Revenue" → /signals
- Final CTA section (dark section, confirmed by ancestors): "Book 15 Minutes" → /see-it-live (+ phone number)
- Footer: "Talk to Sales" → /see-it-live + "Get Updates" → /sign-up
- Forecast page CTAs (one record per occurrence): "Talk to Sales" → /see-it-live (nav + footer, 2 occurrences); "See Platform Capabilities" → #tabbed-features (on-page anchor); "Book 15 Minutes" → /see-it-live (final CTA); "Get Updates" → /sign-up (footer); "Tour Platform" → /take-a-tour

## Trust/credibility observed
- Stats: 50% higher conversion rate, 60% less time to close, 100% pipeline visibility, 30% higher sales efficiency (homepage)
- Named testimonials with roles: Jason Amidon (Director, US & Canada Sales Operations), Adelle Bonavire (Senior Director, GTM Process & Execution), Brian Fretschel (VP of Digital Selling Excellence), Kaycee Decker (Sales Operations Analyst)
- Security/Privacy/Trust Center/Platform Status links in footer
- 2026 Revenue Benchmark Report (gated resource)

## Notes
- H1 stylization: HTML text "Create . Convert . Grow ." renders as "Create. Convert. Grow." (period spacing differs; both recorded)
- The "Signals" concept (→ /signals) is the platform's unifying framing: "captures every revenue signal across your stack, separates the ones that drive outcomes from the noise, and turns them into your next move"
- No pricing link in nav; no visible homepage free-trial entry observed (page-scoped observation — operating model not inferred)
- Homepage has no dedicated persona-targeted section (persona demos appear inside the Signals module: CRO / Account team tabs)
- "Sales teams hit their number, quarter after quarter with Salesloft." (H3) is a standalone bridging element in main — not wrapped in a section with its own CTA
- No coaching/roleplay or content-library proposition observed on the inspected homepage and forecast page (page-scoped observation only — no product-capability claim)
