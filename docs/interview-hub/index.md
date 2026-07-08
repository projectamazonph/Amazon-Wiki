---
title: "Interview Questions Hub"
summary: "How to answer the most common Amazon PPC interview questions — frameworks, strong answers, and red flags to avoid."
last_updated: 2026-07-08
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["interview", "questions", "hiring", "preparation", "acronym"]
---

# Interview Questions Hub

This page covers how to answer the interview questions you're most likely to get when applying for Amazon PPC roles — from junior coordinator to senior manager. For each question, you'll find: why interviewers ask it, what a strong answer sounds like, and the red flags that get candidates rejected.

**Jump to section:**
- [Core Strategy Questions](#core-strategy-questions)
- [Tactical Questions](#tactical-questions)
- [Tool & Process Questions](#tool-and-process-questions)
- [Scenario Questions](#scenario-questions)
- [Curveball Questions](#curveball-questions)

---

## Core Strategy Questions

### "Walk me through how you'd structure a new product launch."

**Why they ask this:** They want to see if you understand the full launch cycle — from keyword research to campaign structure to optimization cadence. They're also testing whether you think about unit economics, not just ACOS.

**Strong answer framework:**
1. **Pre-launch research (1-2 weeks before live):** Keyword research, competitor analysis, ACOS targets based on unit economics. "I calculate the max bid from target ACOS × conversion rate × ASP before touching anything."
2. **Campaign structure:** Auto campaign + 5 exact-match SKAGs. Explain why — auto collects data, SKAGs give control on high-intent terms.
3. **Budget:** Set at 2x steady-state target. Accept higher ACOS in weeks 1-2 as the algorithm learns.
4. **Monitoring cadence:** Daily spend and pacing checks. Weekly search term review. 30-day milestone for structural decisions.
5. **What signals trigger changes:** At what point would you restructure vs. wait? Give specific thresholds.

**Red flags:**
- "I set up an auto campaign and let it run" — too passive
- No mention of unit economics — means you think about ACOS without understanding margin
- No mention of what you'd do if the launch underperforms

---

### "How do you reduce ACOS?"

**Why they ask this:** This is the core optimization question. They want to know if you understand the levers — and whether you know that ACOS isn't always the right metric to optimize.

**Strong answer framework:**
Walk through the diagnostic hierarchy, not just tactics:

1. **Listing quality first:** "I always check the listing before touching bids. If the detail page doesn't convert, no bid change fixes it."
   - Main image quality
   - Bullet points clarity (benefits vs. features)
   - Price competitiveness
   - Review count and rating
2. **Targeting precision:**
   - Are irrelevant search terms eating budget? (Check search term report, add negatives)
   - Are match types correct? (Are you getting phrase/broad queries on exact-match campaigns?)
3. **Bid efficiency:**
   - Are you overbidding on low-converting placements? (Check placement report)
   - Are you bidding differently based on time-of-day or day-of-week patterns?
4. **Structural issues:**
   - Are ASINs with different margin profiles in the same campaign?
   - Are campaigns fragmented with too little spend each to learn?
5. **Strategic context:** "Sometimes ACOS goes up because you're investing in rank-building. I check whether the increased spend is buying rank improvement on high-value terms — if yes, it might be worth it."

**Red flags:**
- "I lower the bids" without any diagnostic — shows pattern-following, not understanding
- No mention of listing quality — common blind spot for junior candidates
- Treating ACOS as the only metric that matters

---

### "What's your experience with automatic vs. manual bidding?"

**Why they ask this:** They want to know if you understand when each approach is appropriate — and whether you've worked with enough campaign volume to have seen the difference.

**Strong answer framework:**

**When I use automatic bidding (Smart Bidding):**
- Campaigns with 100+ monthly conversions (minimum threshold for Smart Bidding to work)
- Lower-priority campaigns where I'm willing to sacrifice granular control for efficiency
- When I don't have time for frequent manual bid management

**When I use manual bidding:**
- New campaigns during the learning period
- Low-volume campaigns that won't give Smart Bidding enough data
- Situations where I need specific bid control by keyword, placement, or time

**What I've learned:**
- Smart Bidding requires patience — it takes 2-4 weeks to stabilize after significant changes
- Manual bidding gives me more control but requires consistent attention
- My current approach: Smart Bidding for 70-80% of spend on high-volume campaigns, manual for the rest

**Red flags:**
- "I always use manual because I don't trust the algorithm" — inflexible
- "I always use Smart Bidding because it's easier" — doesn't understand the requirements
- No mention of the 100-conversion minimum

---

## Tactical Questions

### "Walk me through your keyword research process."

**Why they ask this:** Keyword research is foundational. They want to see whether you have a repeatable, thorough process — not just "I use Helium 10."

**Strong answer framework:**

1. **Seed list generation:** Start with Amazon's own data — Amazon Brand Analytics (for brand-registered sellers), auto campaign search terms, and competitor ASIN reverse lookups.
2. **Expansion:** Use Helium 10 Magnet, Cerebro, or Jungle Scout Keyword Scout to find related terms and long-tail variations.
3. **Volume validation:** Cross-reference with Google Keyword Planner for relative volume, but treat Amazon Brand Analytics numbers as ground truth for Amazon-specific volume.
4. **Intent classification:** Categorize keywords by buyer intent (transactional vs. informational) and match type appropriateness.
5. **Prioritization:** Focus on keywords that appear in both competitor rankings and your own product relevance — the intersection of volume and fit.
6. **Ongoing refinement:** Treat keyword research as a monthly process, not a one-time event. Auto campaigns are always generating new query data.

**Red flags:**
- Only mentions one tool — suggests surface-level understanding
- No mention of how to validate keyword data (vs. just collecting it)
- No process for ongoing keyword refinement

---

### "What's your approach to negative keywords?"

**Why they ask this:** Negative keywords are where ACOS quietly bleeds. They want to see that you're proactive, not reactive.

**Strong answer framework:**

**When I add negatives:**
- Search terms with 5+ clicks and 0 orders in 7 days (adjust threshold based on campaign volume)
- Search terms that are clearly irrelevant to the product (even with 1-2 orders if the ACOS is catastrophically bad)
- My own exact-match winners in broad/phrase campaigns (to prevent self-cannibalization)

**Match type for negatives:**
- Usually exact match for negatives — this blocks only that exact phrase, not broader variations
- Phrase match only when I want to block all queries containing that phrase

**The cadence:**
- Weekly minimum review of search term reports
- Monthly audit of existing negative keyword lists for accumulation (I've seen campaigns with 500+ negatives that have strangled their own reach)

**What I've learned:**
- Being too aggressive with negatives early in a campaign's life kills learning. Give auto campaigns 30 days before heavy negation.
- Being too passive later costs budget. Find the balance by campaign stage.

**Red flags:**
- "I don't really use negative keywords" — disqualifying
- No process for ongoing negative keyword management
- Negatives only added reactively when ACOS spikes

---

### "What tools do you use and why?"

**Why they ask this:** They want to know your tool ecosystem — and whether you understand that tools are decision-support, not decision-making.

**Strong answer framework:**

**Daily drivers:**
- **Amazon Seller Central** — always the source of truth, especially for bulk operations
- **Helium 10** (or equivalent) — for keyword research and competitor analysis
- **Spreadsheets (Excel/Google Sheets)** — for custom bid tracking and campaign change logs

**For specific use cases:**
- [Name the tool] for keyword rank tracking
- [Name the tool] for attribution analysis if working with AMC
- [Name the tool] for automated campaign management if managing 10+ accounts

**The important part:**
"I use tools to gather data faster and spot patterns I'd miss manually. But every automated decision goes through a human review before it runs live."

**Red flags:**
- Lists only tools without explaining what each is used for
- "I let [tool] manage everything automatically" — no human oversight
- Confuses features across tools (says Helium 10 does what it doesn't)

---

## Tool & Process Questions

### "How do you measure campaign performance beyond ACOS?"

**Why they ask this:** ACOS tells you profitability. They want to know if you understand the full performance picture — and whether you know when to use which metric.

**Strong answer framework:**

| Metric | When I use it |
|--------|--------------|
| ACOS | Profitability check on individual campaigns |
| TACOS (total advertising cost of sales) | Overall business impact — ad spend vs. total revenue |
| ROAS | When talking to investors or comparing channels |
| Impression share | Am I winning the auctions I need to win? |
| Click-through rate | Is my targeting and creative resonating? |
| Conversion rate | Is the landing page (detail page) doing its job? |
| Search term performance | Where in the funnel am I losing people? |

"I track ACOS weekly but diagnose with search term performance. If a keyword has high clicks and low orders, the problem is conversion — not the bid."

**Red flags:**
- Only mentions ACOS — tunnel vision
- Can't explain the difference between ACOS and TACOS
- No framework for diagnosing funnel issues

---

### "Describe your weekly optimization routine."

**Why they ask this:** They're hiring someone who will own a process. They want to know if you have one — and whether it's systematic.

**Strong answer:**

"Monday morning I pull the 7-day search term report across all active campaigns. First pass: I add negatives for any term with 5+ clicks and 0 orders. Second pass: I promote exact-match winners (3+ orders, good ACOS) from broad/phrase campaigns. Third pass: I review ACOS vs. targets and flag any campaign more than 5 percentage points above target. I make bid adjustments within a +/- 10% range. Anything larger goes to my manager for approval. I document everything in a change log and send a summary email by Tuesday."

**Red flags:**
- "I check the dashboard and make changes as needed" — no systematic process
- No mention of documentation
- No mention of escalation thresholds

---

## Scenario Questions

### "A campaign's ACOS suddenly jumped 10 percentage points overnight. What do you do?"

**Why they ask this:** They want your diagnostic thinking under pressure.

**Strong answer:**

"First: check whether it's a data reporting lag or a real change. If it's real:

1. Check the search term report — did a new keyword start spending heavily at a bad ACOS?
2. Check the placement report — did impression share shift toward product pages?
3. Check for CPC changes — did competitors start bidding more aggressively on my keywords?
4. Check the listing — did a negative review drop the rating? Did the main image change?
5. Check the product — is it in stock? Did the price change?

I work through these in order of likelihood. Usually it's a new keyword in auto/phrase campaigns spending out of control. If I can't identify the cause quickly, I'll reduce bids on the worst-performing keywords by 10-20% as a hedge while I investigate further."

**Red flags:**
- "I lower the bids right away" without investigation
- No systematic approach to diagnosis
- No mention of checking for non-PPC factors (listing changes, stock issues)

---

### "A product has no reviews. How do you handle PPC for it?"

**Why they ask this:** Products without social proof convert poorly. They want to know if you understand this constraint and adjust accordingly.

**Strong answer:**

"First, I set realistic ACOS expectations — a product with no reviews will convert at roughly half the rate of the same product with 20+ reviews. I adjust my max bid formula to account for a lower conversion rate, which means lower bids.

Second, I focus on high-intent targeting. Without reviews, broad auto campaigns will show my product for loosely related queries where shoppers will click the competitor with reviews instead. I lean on exact-match SKAGs for my strongest keywords and use auto sparingly.

Third, I use Sponsored Display or competitor ASIN targeting to reach people who are already familiar with the product category — they need less convincing than cold traffic.

Fourth, I treat the PPC launch as part of the review-building strategy. The goal isn't profit — it's generating enough sales velocity to accumulate 15-20 reviews as fast as possible, after which I restructure the campaigns."

**Red flags:**
- No adjustment to bid strategy based on conversion rate
- Expects the same ACOS as products with reviews
- Doesn't mention Sponsored Display as an alternative for review-poor products

---

### "How would you handle a client who wants to cut ad spend because of high ACOS, but you believe the spend is building rank?"

**Why they ask this:** This is the classic short-term vs. long-term tension. They want to know if you can advocate for the right strategy while managing client relationships.

**Strong answer:**

"I'd pull the data to make the argument concrete, not just philosophical.

First, I'd show the keyword rank trajectory — are the target terms climbing week-over-week? Second, I'd show whether organic sales (non-PPC) are increasing as a percentage of total sales, which would indicate that paid traffic is building organic visibility. Third, I'd model the tradeoff: if we cut spend and lose rank, what does the recovery cost look like? Usually it's 50-100% more expensive to rebuild rank than to maintain it.

If the client still wants to cut, I'd propose a compromise: reduce spend by X% on lower-priority campaigns while protecting spend on the top 2-3 keywords that are closest to ranking goals. Then set a milestone — at Y rank position, we can reduce spend without losing the benefit."

**Red flags:**
- "I just do what the client says" — no strategic advocacy
- "They don't understand PPC" — no client relationship management
- No data-driven framework for making the case

---

## Curveball Questions

### "What's a campaign metric that most people don't track but should?"

Good answers:
- **Impression share loss due to budget** — you might be leaving money on the table because your budget is too low, not because your bids are wrong
- **Keyword rank velocity** — not just current rank, but how fast you're climbing
- **Blend of search terms by intent level** — are you getting mostly high-intent exact queries, or a lot of low-intent auto queries?
- **Placement roas (by placement type)** — top of search vs. product page ROAS can be 3-4x different

### "If you could only use one PPC metric for the rest of your career, what would it be?"

There is no single correct answer. What they're looking for:
- Do you understand what each metric actually measures?
- Can you reason about tradeoffs?
- Is your answer grounded in your actual experience?

Strong answer: "TACOS, because it measures the impact of advertising on the total business, not just the performance of an individual campaign."

Strong answer: "ACOS by keyword, because it's the most actionable — I can make a specific decision based on it."

Weak answer: "ROAS" — shows you know a metric name but not necessarily when to use it.

### "Tell me about a campaign that failed. What did you learn?"

They ask this to check for intellectual honesty. People who claim they've never had a campaign underperform are either lying or not paying close enough attention.

Strong answer: Describes a specific failure honestly, takes ownership (not "Amazon changed the algorithm"), and extracts a specific lesson. "I over-structured a new product launch with 15 campaigns on day one. Each campaign had too little budget to learn. ACOS was terrible for 6 weeks. I learned to start simple and let the data tell me when to add complexity."

---

## Related Pages

- [Core Metrics Deep Dive](/docs/sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive)
- [New Product Launch](/docs/sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch)
- [Negative Keywords Hub](/docs/sections/09-9-negative-keywords-and-negation-strategy)
- [Search Term Mining SOP](/docs/sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop)
