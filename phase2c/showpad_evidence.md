# Showpad — Evidence Record (Phase 2, Batch 3)
Research date: October 19, 2026 (Europe/Berlin)
Entity note: Showpad merged with Bigtincan and Brainshark (Phase 1; footer links "Showpad Brainshark" → /brainshark, "Showpad Bigtincan Hub" → /bigtincan-hub, "Showpad Zunos" → /zunos, "Showpad ClearSlide" → /clearslide confirm the suite on the live site).

Sources captured:
- https://www.showpad.com/ (homepage) — phase2c/showpad_home.html (51KB)
- https://www.showpad.com/showpad-for-revenue-leaders (Revenue Leadership page, CRO-relevant) — phase2c/showpad_revleaders.html
- Rendered-page inspection (cloud browser, Oct 19, 2026): hero, nav, announcement bar, persona cards. Screenshots preserved in session history.

## Homepage structure (in HTML order, heading levels from HTML tags)
1. Announcement bar: "Excellence in the Field — New York, Chicago, London, Düsseldorf" + "Request to join" CTA (client-side content — CTA verified in rendered page, not in saved HTML)
2. Nav: Platform | Showpad Genie | Customers | Resources | Pricing | Log in | "Request a demo" → /request-a-demo
3. HERO — H1 (HTML <h1>): "The world relies on what you sell. You can rely on Showpad." Hero paragraph: "Medical devices that save lives. Equipment that powers cities. Your products are essential. But selling them isn't simple. With safe, governed AI, Showpad solves complex business problems that generic enablement can't." CTAs: "Take a tour" (client-side content — verified in rendered page, not in saved HTML) + "Request a demo" (→ /request-a-demo, verified in HTML)
   - Hero media: persona portrait cards with AI pills: Enablement (+AUTHORING AI, "High-impact seller readiness"), Field Sellers (+FIELD SELLER AGENT, "Real-time deal support, anytime, anywhere"), Revenue Leadership (+ROLEPLAY AI, "Sales coaching at scale"), Marketing (+LIBRARY AI, "Exceptional buyer experiences"). Card texts verified in HTML (embedded JSON); AI pill labels client-side (verified in rendered page, not in saved HTML)
4. H3: "2,000+ global companies rely on Showpad." (logo strip) + "Our Customers" → /customers
5. H3: "Built for effectiveness. Recognized for excellence." — analyst badges (Aragon, Gartner, IDC, Forrester) + "Read the report" → /reports/aragon-globe-coaching-2027
6. H2: "AI engineered for the fast lane." — "The revenue effectiveness platform for field teams who can't afford to slow down." + "Explore the platform" → /platform-overview
7. Four modules (H3s, each with paragraph + CTA):
   - "Sales Readiness" — "Learning that creates champions." — "Combine proven skills, practice, and real-time coaching to forge sellers who show up ready for any conversation." — CTA "Explore Sales Readiness" → /sales-readiness
   - "Content Management" — "Content your teams can count on." — "Construct a content engine that turns every seller into a closer — with the right spec sheet, pricing, and proof points to win with confidence." — CTA "Start with Content Management" → /content-management
   - "Buyer Engagement" — "Your entire catalog in every seller's pocket." — "Bring physical products to life with unforgettable digital demos, while collaborative deal rooms keep buying committees moving toward yes with you — not your competition." — CTA "Start with Buyer Engagement" → /buyer-engagement
   - "Analytics & Insights" — "Act smarter. Prove impact." — "Quickly spot the patterns behind top performers and high-converting content, and apply that intel to every seller, deal, and customer interaction." — CTA "Learn about Analytics & Insights" → /analytics-insights
8. H2: "Showpad Genie" + H3 "Deal winning expertise, made standard practice" — "Showpad Genie is the platform's AI core that learns how your company wins — powering instant answers, better decisions, and governed automation across every deal." — CTA "Explore Showpad Genie" → /showpad-genie
9. H2: "What reliable revenue effectiveness looks like." — customer-story carousel + "See all stories" → /customers
10. H2: "Every team that owns revenue. One platform they can rely on." — BODY SECTION ONLY: H2 + paragraph ("When your products are essential, your revenue team needs tools that are, too." — verified from saved HTML). Persona links (Marketing / Field Sellers / Enablement / Revenue Leadership / Revenue Operations / Channel Selling) and industry links are in the NAV MEGA-MENU, not in the body section (verified by DOM ancestors).
11. H2: "The foundation for how you win — connected to every tool you use" — "Showpad holds what no other system has: the content, coaching signals, and deal-stage context that defines how your company wins. Connect your stack, and that foundation flows everywhere it needs to go." — CTA "Explore integrations" → /platform-overview/integrations
12. H2: "Fuel for revenue leaders" — news cards (H3s): "Close the revenue effectiveness gap: Showpad Summer Release '26" ("Check it out" → /blog/summer-26-release) / "Excellence in Action customer awards are back — nominate your team today" ("Apply now" → https://eia.showpad.com/) / "Showpad recognized as a Customers' Choice in the Gartner Peer Insights Report" ("Read the report" → /reports/gartner-peer-insights-revenue-enableme[nt])
13. FINAL CTA — H2: "Power revenue effectiveness for your team." — CTA "Request a demo" → /request-a-demo
14. Footer — sitemap: Products (Content Management, Sales Readiness, Buyer Engagement, Analytics & Insights, Roleplay AI, Field Seller Agent, Authoring AI, Experiences & Collections, Courses & Paths, Shared Spaces, Showpad Genie, Data + Trust, Integrations, Brainshark, Bigtincan Hub, Zunos, ClearSlide) / persona pages / industries / Resources / Company / comparison pages ("Showpad vs. Seismic" → /seismic-competitors, "Showpad vs. Highspot" → /lp/showpad-vs-highspot/, "Showpad vs. Allego" → /lp/switch-from-allego) / legal / "Hey AI, learn about us" → /llm-info

## Revenue Leadership page (/showpad-for-revenue-leaders)
- Title: "Showpad for Revenue Leaders Teams"
- H1: "Showpad for Revenue Leaders"
- H2: "For those accountable for the bottomline — and every seller behind it." — "Your forecast is met or missed based on what happens between the strategy deck and the customer meeting. Showpad turns top-performer behavior into the standard across every rep, territory, and quarter — so predictable revenue stops being an ambition and becomes how your team operates every day."
- H3: "Showpad supports thousands of revenue leaders globally."
- H2: "The forecast is yours to defend. Build the field that makes hitting it predictable."
- H2: "Make your top 20% the standard. With AI trained by your best." — "Your top sellers show you what the other 80% are capable of. Genie — the intelligent core of Showpad — turns their winning behaviors into a system every rep can execute. All while being grounded in your data, content, and methodology, not a general-purpose model that might hallucinate in front of a buyer." (full sentence verified against page text; continues: "The result: deals that move on signals, reps who show up ready, and a clearer answer to...")
- H3s with descriptions:
  - "Roleplay AI" — "Consistent coaching, every rep, every region — no manager capacity required. Sellers practice scenarios that show up in your real deals. Scoring is structured and consistent, so readiness is something you can gauge and correct across the field."
  - "Genie Assistant" — "All sellers get the knowledge of your best performer. Plain-language questions in, verified answers out — so sellers handle complexity and objections without escalating up the chain."
  - "Field Seller Agent" — "Every meeting captured. Every CRM update submitted — automatically. Your pipeline reflects what happened in the room, not what reps remembered to log. So you see the buy signs and warning lights across every geo, product line, and deal stage."
- H2: "CROs and CSOs rely on Showpad to plan with precision, execute with consistency, and prove what's working."
- H2: "Built for the manager. Felt by the seller. Visible for leadership." — "Your front-line sales managers are the difference between a revenue plan that lands and one that erodes. Showpad gives them the visibility, tools, and coaching workflows to develop their teams, spot risk early, and drive reliable performance across every rep."
- H2: "The revenue engine leaders rely on." — case studies (H3s): "From 96% attainment to 102% — how an eyecare innovator turned one region's playbook into £2.8M in incremental revenue" / "ABB's robotics sellers were spending 70% of their time not selling; leadership built a system to change that" / "How Just Eat reclaims 300 productive hours per week and makes every business review an upsell opportunity" / "27% higher deal value and 150% more pipeline — what happened when IFF stopped leaving cross-sells on the table" / "How GF's sales leadership got 60k products into every seller's hands and every customer conversation" / "100+ stores. 1,300 associates. One platform that propelled cohesive training into consistent revenue"
- H2: "Your revenue stack, fully monetized." — "Showpad integrates with your CRM, BI tools, and collaboration platforms so every interaction is captured, every insight is actionable, and your tech investments compound instead of compete."
- H2: "Your boardroom-ready battlecards." — includes H3 "Showpad named a Leader in the 2025 Gartner® Magic Quadrant™ for Revenue Enablement Platforms" + H3 "Confident sellers at scale: Customer insights on Roleplay AI" + H3 "Most AI is built for a seller who's not in your organization"
- H2: "Frequently asked questions" — answers include: "Showpad connects seller activity, buyer engagement, and content usage to pipeline data in your CRM. You get real-time visibility into which deals are progressing, which are stalling, and which behaviors and content correlate with closed-won outcomes. Your forecast is built on signals, not self-repor[ting]" (truncated at clipping point) / "Customers report cutting onboarding time by up to 50%." / "Showpad's Question-Based Analytics and CRM integrations tie readiness, content, and coaching activity directly to win rates, deal size, and cycle length. You get answer-focused dashboards built for board-level conversations — connecting every dollar spent to measurable revenue impact." / "Showpad is built for field-first organizations selling complex portfolios — medical devices, industrial equipment, financial services, consumer goods."
- H2: "Power revenue effectiveness for your team." (final CTA)

## CTA inventory (verified, one record per occurrence)
- Announcement bar: "Request to join" → https://eitf.showpad.com/?ribbon=eitf-2026 (client-side content — verified in rendered page; destination extracted from live rendered DOM Oct 19, 2026: event site)
- Nav: "Request a demo" → /request-a-demo
- Hero: "Request a demo" → /request-a-demo (verified in HTML) + "Take a tour" → https://www.showpad.com/interactive-product-tour?utm_source=homepage (client-side content — verified in rendered page; destination extracted from live rendered DOM Oct 19, 2026: interactive product tour)
- H3 logo strip: "Our Customers" → /customers
- Analyst badges: "Read the report" → /reports/aragon-globe-coaching-2027
- AI section: "Explore the platform" → /platform-overview
- Four module CTAs: "Explore Sales Readiness" → /sales-readiness; "Start with Content Management" → /content-management; "Start with Buyer Engagement" → /buyer-engagement; "Learn about Analytics & Insights" → /analytics-insights
- Genie: "Explore Showpad Genie" → /showpad-genie
- Stories: "See all stories" → /customers
- Integrations: "Explore integrations" → /platform-overview/integrations
- News: "Check it out" → /blog/summer-26-release; "Apply now" → https://eia.showpad.com/; "Read the report" → /reports/gartner-peer-insights-revenue-enablement-2026 (full URL recovered from source)
- Final: "Request a demo" → /request-a-demo

## Trust/credibility observed
- "2,000+ global companies rely on Showpad" (homepage logo strip)
- Analyst badges: Aragon (Leader, Enterprise Coaching 2027 Globe), Gartner, IDC, Forrester
- "Showpad named a Leader in the 2025 Gartner® Magic Quadrant™ for Revenue Enablement Platforms" (RevLeaders page)
- "Showpad recognized as a Customers' Choice in the Gartner Peer Insights Report" (homepage news card)
- Quantified case studies: ABB (70% of time not selling), Just Eat (300 productive hours/week), IFF (27% higher deal value, 150% more pipeline), eyecare innovator (96%→102% attainment, £2.8M incremental revenue), GF (60k products), 100+ stores/1,300 associates
- "Customers report cutting onboarding time by up to 50%" (RevLeaders FAQ)

## Notes
- Key memory-adjacent claim (homepage): "Showpad holds what no other system has: the content, coaching signals, and deal-stage context that defines how your company wins. Connect your stack, and that foundation flows everywhere it needs to go."
- Governance positioning in hero: "safe, governed AI"; Genie: "governed automation across every deal"
- Grounding claim (RevLeaders): "grounded in your data, content, and methodology, not a general-purpose model that might hallucinate in front of a [customer]"
- Verified-answers claim (RevLeaders): "Plain-language questions in, verified answers out"
- Roleplay AI featured: homepage footer product link + RevLeaders page section + hero card pill (client-side); dedicated page exists (/showpad-genie/roleplay-ai)
- Field-sales vertical framing: "field teams who can't afford to slow down"; industries: medical devices, industrial equipment, financial services, consumer goods
- Pricing link in nav; demo-gated conversion ("Request a demo" — no visible free-trial entry on homepage)
- "Hey AI, learn about us" → /llm-info (LLM-visibility page in footer)
- Announcement bar and two CTAs are client-side (labeled per convention)
- Comparison pages vs. Seismic, Highspot, Allego in footer
