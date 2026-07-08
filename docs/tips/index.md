---
title: "Pro Tips & Tactics Hub"
summary: "Battle-tested PPC tactics organized by campaign stage — launch, scale, and optimize. Includes the mistakes that kill ACOS."
last_updated: 2026-07-08
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["tips", "tactics", "launch", "scale", "optimize", "mistakes"]
---

# Pro Tips & Tactics Hub

Tactics from running real campaigns. No fluff, no generic advice — this is what actually works and what actually breaks.

**Jump to section:**
- [Launch Phase](#launch-phase)
- [Scale Phase](#scale-phase)
- [Optimize Phase](#optimize-phase)
- [Mistakes That Kill ACOS](#mistakes-that-kill-acos)

---

## Launch Phase

### 1. Let Auto Campaigns Breathe for 30 Days

The single biggest mistake new PPC managers make: pruning the auto campaign too early. Auto targeting campaigns are your data collection engine during launch. They surface search terms you never would have thought of, at the match types Amazon thinks are relevant, from the products Amazon thinks are comparable.

If you start adding negatives after week 1, you starve the algorithm of the signal it needs to learn. Here's the rule: run auto campaigns untouched for 30 days minimum. At day 30, harvest the converting terms and move them to exact-match SKAGs. Then start pruning.

### 2. Seed Exact Match with Your Best Keyword Assumptions

Don't wait for Amazon to discover everything. Pick your top 5-7 keyword hypotheses based on your own product knowledge and competitor analysis. Put each in its own SKAG campaign at a slightly elevated bid (10-20% above your calculated max bid). This gets your best assumptions in front of buyers immediately while auto campaigns gather the long tail.

### 3. Budget the Ramp, Not the Steady State

When launching, your initial ACOS will be ugly. That's normal. What matters is:
- Is the listing converting at a reasonable rate? (aim for >8% conversion on the detail page)
- Are you building keyword rank on your target terms?
- Are you generating real sales velocity?

Set a launch budget that's 2x your steady-state target and accept a 40-50% ACOS for the first 2 weeks. If your listing can't convert at that traffic level, the problem is the listing — not the PPC.

### 4. Monitor SKU-Level Conversion, Not Just Campaign ACOS

Amazon reports campaign-level metrics. But if you're running multiple ASINs in one campaign, the campaign ACOS hides which products are performing. Split campaigns by ASIN margin profile early. A hero product subsidizing a slow-mover in the same campaign looks like a healthy campaign ACOS until the slow-mover tanks your margin.

### 5. Check Placement Report in Week 2

After you have 7-10 days of data, pull the placements report. You want to know: is your ad showing more on product pages or top of search? For most products, top-of-search converts 2-4x better. If you're getting most of your spend on product pages, increase placement bid modifier for top of search by 25-50%.

---

## Scale Phase

### 6. The Negation Cascade

As you scale from auto campaigns to exact match, you will inevitably have overlap. Here's the order of operations:

**Step 1:** At day 30, pull the search term report from your auto campaign. Identify exact-match terms that generated 3+ orders with ACOS below your target.

**Step 2:** Create exact-match SKAGs for those terms. Set bids based on your max bid formula.

**Step 3:** Add those exact-match terms as negatives in your auto campaign — *but only at exact match type*. This prevents auto campaign from bidding on terms you're now targeting manually, without blocking broader relevant queries.

**Step 4:** 30 days later, repeat. This cascade builds out your manual campaign with proven winners while auto handles the discovery.

### 7. Placement Bid Modifier Progression

Don't set placement modifiers on day 1. Do this instead:

- **Weeks 1-2:** Collect baseline data. No modifiers.
- **Weeks 3-4:** If top-of-search ACOS is 20%+ better than overall ACOS, add +50% modifier.
- **Month 2+:** If data is consistent, push to +75% or +100%.

The reason: modifiers amplify your base bid. If your base bid is wrong, the modifier amplifies a wrong number faster.

### 8. Dayparting — Only If You Have the Data

Dayparting (scheduling bids by time of day) is tempting but dangerous if you don't have enough data. You need at least 30 days of consistent data showing a clear pattern before adjusting by time.

What to look for: some products convert 2x better in evening hours than morning. Others spike on weekends. If you see a consistent pattern across 4+ weeks, test a rule-based bid adjustment during peak hours.

Don't daypart on 2 weeks of data. You'll optimize for noise.

### 9. Scale Winning ASINs, Not All ASINs

When scaling spend, add budget only to campaigns where:
- ACOS is at or below target
- Search term report shows diverse, relevant queries (not just one or two terms)
- Placement data is healthy (not over-indexed on product pages)

For campaigns that are just "not bad," hold the budget flat. Allocate growth budget to your proven winners.

### 10. Use Bulk Operations for Bid Changes

If you're managing 50+ campaigns, don't make individual bid changes through the UI. Use the [Bulk Operations](/docs/sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations) spreadsheet workflow. Download the bid change spreadsheet, edit in Excel or Google Sheets, upload. This is 10x faster and reduces error rate.

---

## Optimize Phase

### 11. Weekly Negative Keyword Sweep

This is non-negotiable. Every Monday morning: pull the search term report, look at the past 7 days of search terms with spend but zero orders, add them as negatives. This is where budget quietly bleeds out.

Threshold: if a search term has 5+ clicks and 0 orders, negative it. If it has 3 clicks, 0 orders, and your product clearly can't match that intent, negative it. The rest: let them run.

### 12. The 90-Day Architecture Review

Every 90 days, step back and ask: is my campaign structure still serving the business? Common things that break over time:

- Too many campaigns with too little spend each (Amazon's algorithm needs data to learn; $3/day campaigns never learn)
- Mismatched ACOS targets across ASINs in the same campaign
- Exact match and broad match competing against each other for the same terms
- Old campaigns that were never paused when the product moved to steady state

Fix: export all campaign data, look at spend vs. orders per campaign, and make hard calls. Pausing a $2/day campaign that never converted is not a loss — it's budget recovery.

### 13. Match Type Sequencing

As products mature, move terms through match type sequencing:

**Launch (month 1):** Auto-only. Gather data.

**Month 2:** Add phrase and broad match campaigns. Set them up as separate campaigns, not ad groups within the same campaign.

**Month 3:** Promote exact-match winners from phrase/broad into dedicated SKAG campaigns. Add exact-match negatives to the broader campaigns.

**Month 4+:** Your campaign structure stabilizes. Maintenance mode: weekly negation, monthly bid adjustments, quarterly architecture review.

### 14. Use Search Query Performance, Not Just ACOS

ACOS tells you if a campaign is profitable. Search Query Performance tells you where the funnel is breaking. If a keyword has:
- High impressions, low clicks → visibility problem (bid higher or check relevance)
- High clicks, low orders → conversion problem (check listing, price, reviews)
- Low everything → insufficient data (wait or increase bids)

See [10.1 Core Metrics Deep Dive](/docs/sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive) for the full framework.

---

## Mistakes That Kill ACOS

These are the patterns I see repeatedly destroy ACOS. Avoid them.

### Mistake 1: Over-Structuring from Day 1

New PPC managers create 30 campaigns with 5 SKAGs each on day 1. This is a mistake. Over-structured campaigns mean each campaign gets too little data for Amazon's algorithm to learn. The algorithm then takes longer to optimize, and you end up spending more to gather the same data.

Start simple. Auto campaign + 5 exact-match SKAGs. Add structure as data proves the need for it.

### Mistake 2: Never Adding Negatives

The flip side of the "let auto breathe" advice: never adding negatives is equally dangerous. After the first 30 days, you have data. Use it. The auto campaign should be a disciplined discovery engine, not a budget dump into irrelevant queries.

### Mistake 3: Mixing ASINs with Different Margin Profiles

If Product A has 50% margin and Product B has 15% margin, running them in the same campaign means one of two things: either Product A is subsidizing Product B's unprofitable clicks, or Product B's budget is being crowded out by Product A's better ACOS. Neither is good.

Segment campaigns by margin profile from the start.

### Mistake 4: Using Smart Bidding Without Enough Data

Amazon's Smart Bidding requires 100+ monthly conversions per campaign to function properly. Below that threshold, you'll see 20-30% CPA volatility and extended learning periods. If your campaign is doing 20 conversions a month, use manual bidding. Smart Bidding is not a shortcut — it's a power tool that needs fuel.

See [6.2 Dynamic & Rule-Based Bidding](/docs/sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding) for when to use which strategy.

### Mistake 5: Chasing Low ACOS Instead of Total Profit

A 5% ACOS campaign that generates $200 in revenue is less valuable than a 20% ACOS campaign that generates $5,000 in revenue. Always contextualize ACOS against total spend and revenue. The goal is total profit, and sometimes that means accepting a higher ACOS on a high-revenue campaign.

### Mistake 6: Ignoring the Listing

No amount of PPC optimization fixes a listing that doesn't convert. Before you change a single bid, check: is the main image compelling? Are the bullets clear about the benefits, not just features? Is the price competitive? Does the product have reviews?

Listing quality is upstream of PPC performance. See [15. Listing Optimization](/docs/sections/15-15-listing-optimization) for the full guide.

### Mistake 7: Not Tracking Against a Benchmark

If you don't know what your ACOS was last month, you can't tell if this month is better or worse. Set up a simple tracking system: log campaign ACOS, total spend, and total orders weekly. Plot it over time. The trend matters more than any single data point.

---

## Quick Reference: Tactical Checklist by Phase

**Launch (Days 1-30)**
- [ ] Set up auto campaign + 5 exact-match SKAGs
- [ ] Budget at 2x steady-state target
- [ ] Do NOT add negatives yet
- [ ] Check placement report at day 14
- [ ] Start harvesting converting terms at day 30

**Scale (Months 2-3)**
- [ ] Move proven terms to exact-match SKAGs
- [ ] Add phrase and broad match campaigns
- [ ] Begin negation cascade (exact terms out of auto)
- [ ] Set placement modifiers if data supports it
- [ ] Segment campaigns by ASIN margin profile

**Optimize (Month 4+)**
- [ ] Weekly: negative keyword sweep
- [ ] Monthly: bid adjustments based on 4-week data
- [ ] Quarterly: full architecture review
- [ ] Ongoing: monitor listing quality as upstream lever

---

## Related Pages

- [Negative Keywords Hub](/docs/sections/09-9-negative-keywords-and-negation-strategy)
- [Bid Adjustment Cadence](/docs/sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence)
- [Search Term Mining SOP](/docs/sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop)
- [Listing Optimization](/docs/sections/15-15-listing-optimization)
