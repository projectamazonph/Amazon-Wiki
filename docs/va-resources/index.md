---
title: "VA Resources Hub"
summary: "Onboarding guide, SOPs, checklists, and communication templates for VAs managing Amazon PPC campaigns."
last_updated: 2026-07-08
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["va", "virtual-assistant", "sop", "onboarding", "checklist", "templates"]
---

# VA Resources Hub

This hub is for two audiences: VAs who are new to Amazon PPC, and the people who hire and manage them. Everything VAs need to get up to speed and run campaigns correctly — and everything managers need to set expectations and review work quality.

**Jump to section:**
- [Onboarding Guide](#onboarding-guide)
- [Standard Operating Procedures](#standard-operating-procedures)
- [Task Checklists](#task-checklists)
- [Communication Templates](#communication-templates)
- [Tools VAs Should Know](#tools-vas-should-know)
- [Quality Assurance Checklist](#quality-assurance-checklist)

---

## Onboarding Guide

### Before You Start: What You'll Need Access To

Your manager should provision these before your first day:

- [ ] **Amazon Seller Central access** — at minimum, Campaign Manager view access (read-only) for initial training
- [ ] **Reporting access** — ability to download search term reports, campaign performance reports
- [ ] **Communication channel** — Slack, Discord, or email for daily/weekly check-ins
- [ ] **Tool access** — whatever tool the team uses (Helium 10, Sellics, Perpetua, etc.)
- [ ] **Shared drive** — Google Drive or Dropbox for templates, reports, and campaign documentation

If any of these aren't ready on day 1, flag it immediately. Running PPC without proper access leads to mistakes.

### Week 1: Learning the Account

**Day 1-2:** Read these wiki pages in order:
1. [What is Amazon PPC](/docs/sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc)
2. [The Amazon Advertising Ecosystem](/docs/sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem)
3. [Account and Campaign Architecture](/docs/sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-and-amazon-ads-ui)
4. [Core Metrics Deep Dive](/docs/sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive)

**Day 3-4:** Shadow your manager or senior team member. Watch them navigate Seller Central, pull reports, and make a bid change. Take notes. Ask why they make each decision.

**Day 5:** Run through the [Daily Checklist](#daily-checklist) on the account. Start with observation — note what you see without changing anything yet.

### Week 2: Your First Tasks

Start with supervised tasks only. Your manager reviews everything before changes go live.

**Task 1:** Pull the search term report for the past 7 days. Identify:
- Top 10 search terms by spend
- Any search terms with 5+ clicks and 0 orders (flag for negation)
- Any search terms with 3+ orders and ACOS below target (flag for exact-match promotion)

**Task 2:** Pull the placement performance report. Identify:
- Which campaigns are getting most of their spend on product pages vs. top of search
- Whether placement modifiers should be adjusted

**Task 3:** Check campaign budget pacing. Which campaigns are at risk of running out of budget mid-day?

### Week 3+: Graduated Independence

After two weeks, you can start making changes independently — but only within pre-approved parameters your manager has set:

- **Bid adjustments:** +/- 10% maximum per change, within established bid ranges
- **Negative keywords:** Can add negatives directly; must flag removals for manager approval
- **Budget changes:** Must get manager approval
- **Campaign structure changes:** Must get manager approval

As you build trust (and make fewer errors), these parameters can expand.

---

## Standard Operating Procedures

### SOP 1: Weekly Campaign Optimization

**Purpose:** Maintain campaign health every week.

**Time required:** 30-60 minutes per account

**Steps:**
1. Pull search term report (last 7 days) for all active campaigns
2. Add negative keywords for search terms with 5+ clicks, 0 orders
3. Add exact-match keywords for search terms with 3+ orders, good ACOS
4. Review ACOS vs. targets — flag campaigns more than 5% above target
5. Review placement performance — note any campaigns needing bid modifier review
6. Check budget pacing — note campaigns running out before end of day
7. Log all changes in the campaign change log
8. Send summary to manager

### SOP 2: Monthly Campaign Architecture Review

**Purpose:** Ensure campaign structure still serves the business.

**Time required:** 2-3 hours per account

**Steps:**
1. Export campaign performance summary for the past 30 days
2. Identify campaigns with:
   - Less than $50 total spend (likely not learning properly)
   - Zero orders in 30 days (needs review or pause)
   - ACOS more than 10 percentage points above target (needs restructuring)
3. Identify duplicate targeting (same keywords in multiple campaigns bidding against each other)
4. Review ASIN segmentation — are products with different margin profiles still in the same campaigns?
5. Prepare a summary with recommendations for manager review

### SOP 3: New Product Launch Support

**Purpose:** Set up new product campaigns correctly from day 1.

**Steps:**
1. Get product ASIN, margin, target ACOS, and launch timeline from manager
2. Set up campaign structure per the [New Product Launch SOP](/docs/sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint):
   - Auto targeting campaign
   - Exact-match SKAG campaign (manager provides keyword list)
   - Initial daily budget
3. Create campaign naming convention following the team's standard
4. Document all campaign settings in the shared campaign log
5. Set up a 30-day milestone review (flag to manager at day 15 and day 30)
6. Establish ACOS target (typically 35-45% during launch ramp)

---

## Task Checklists

### Daily Checklist

Time: ~15 minutes per account

- [ ] Pull campaign performance summary (spend, revenue, ACOS) for yesterday
- [ ] Check for campaigns that hit daily budget before 6 PM
- [ ] Check for any unusual CPC spikes (>20% above normal for same day-of-week)
- [ ] Confirm product is in stock (pause Sponsored Products ads if product goes out of stock)
- [ ] Log any issues or anomalies in the campaign log
- [ ] Send daily summary to manager (if required by your setup)

### Weekly Checklist

Time: ~45-60 minutes per account

- [ ] Pull 7-day search term report
- [ ] Add negative keywords for irrelevant 0-order terms
- [ ] Promote high-performing terms to exact-match
- [ ] Review ACOS vs. targets for all campaigns
- [ ] Check placement performance
- [ ] Review budget pacing projections
- [ ] Document all changes in campaign change log
- [ ] Send weekly summary to manager

### Monthly Checklist

Time: ~2-3 hours per account

- [ ] Full 30-day performance review
- [ ] Architecture audit (campaigns with <$50 spend, zero orders, extreme ACOS)
- [ ] Keyword rank tracking review (where available)
- [ ] Competitor activity review (keyword gaps, new competitors)
- [ ] Listing quality check (has anything changed that might affect conversion?)
- [ ] Present findings and recommendations to manager

---

## Communication Templates

### Template 1: Weekly Report

```
Subject: [Account Name] Weekly PPC Report — Week of [Date]

Hi [Manager Name],

Here's the weekly PPC summary for [Account Name].

**Account Performance (7-day)**
- Total Spend: $[amount]
- Total Revenue: $[amount]
- Blended ACOS: [X]% (target: [X]%)
- Total Orders: [N]

**Campaigns Needing Attention**
- [Campaign Name]: ACOS [X]% vs. target [Y]%. [Action taken / Recommendation]
- [Campaign Name]: Budget exhausted at [time]. [Action taken / Recommendation]

**Search Term Changes Made**
- Added negatives: [list terms]
- Promoted to exact match: [list terms]

**Questions / Decisions Needed**
- [Question 1]
- [Question 2]

Let me know if you want me to take any different actions before the weekend.

Best,
[Your Name]
```

### Template 2: Bid Change Request

```
Subject: Bid Change Request — [Campaign Name] — [Date]

Campaign: [Campaign Name]
Current Bid: $[X.XX]
Proposed Bid: $[X.XX]
Change: [+/- X%]

Reason: ACOS is [X]% over the past 14 days with [N] orders. Reducing bid by 10% to bring ACOS closer to the [Y]% target.

Current Performance (14-day):
- Spend: $[amount]
- Revenue: $[amount]
- ACOS: [X]%
- Orders: [N]

Please confirm before I apply this change.
```

### Template 3: New Keyword Brief

```
Subject: Keyword Request — [Product Name] — [Date]

Product: [ASIN and product name]
Campaign: [Campaign Name]
Priority: [Normal / Urgent — we're losing rank on these terms]

Requested Keywords:
1. [keyword] — [reason: competitor is dominating this term]
2. [keyword] — [reason: converting well in auto campaign, want exact control]
3. [keyword] — [reason: seasonal, entering peak period]

Match types: [Exact / Phrase / Broad — or specify per keyword]

Target bid: Based on unit economics (ACOS [X]%, CVR [Y]%, ASP $[Z]) = $[bid]
Max I'm approved to bid: $[ceiling]

Let me know if you'd like different match types or bids.
```

### Template 4: Escalation Alert

```
Subject: ⚠️ [URGENT] Account Issue — [Account Name] — [Date/Time]

Issue: [One-sentence description]
Campaign Affected: [Campaign Name]
Impact: [Spend at risk / Revenue lost / Other]

What I see:
- [Specific data point]
- [Specific data point]

What I've done so far: [Action taken]
What I'm asking you to decide: [Specific decision needed]

Need your response by: [Time — give at least 2 hours]
```

---

## Tools VAs Should Know

### Must-Know (You'll use daily)

**Amazon Seller Central**
- Pulling search term reports
- Pulling campaign performance reports
- Making bulk bid changes
- Navigating the Campaign Manager interface

**Spreadsheet Software (Excel or Google Sheets)**
- VLOOKUP/INDEX-MATCH for matching data across reports
- Pivot tables for campaign performance summaries
- Filtering and sorting for search term analysis

### Should-Know (You'll use weekly)

**Helium 10 (or equivalent suite)**
- Keyword research and reverse ASIN lookup
- Keyword tracking and rank monitoring
- Cerebro for competitor keyword analysis

**Bulk Operations in Seller Central**
- Download bid change templates
- Upload bulk changes
- Validate before submitting

### Nice-to-Know (Adds Value)

**Amazon Marketing Cloud (AMC)**
- Basic SQL queries for attribution analysis
- Building custom audience segments

**Perpetua / Scale Insights / Teikametrics**
- Automated campaign management tools
- Understand how rules-based automation works

**Google Data Studio / Looker Studio**
- Building client-facing dashboards
- Consolidating multi-account data

---

## Quality Assurance Checklist

Your manager will use this checklist when reviewing your work. Know it so you can self-check before submitting.

### Before Submitting Any Change

- [ ] I have checked the current bid against the approved range
- [ ] I have logged the change in the campaign change log
- [ ] I have confirmed the campaign name and ID match what I intended to change
- [ ] I have noted any downstream effects (e.g., pausing this campaign means no coverage for these keywords)

### Before Sending Weekly Report

- [ ] Numbers add up (spend ÷ revenue = ACOS)
- [ ] I've included context for any unusual metrics (seasonal, new product launch, etc.)
- [ ] I've highlighted what's different from last week
- [ ] I've flagged decisions that need manager input, not just reported data

### Common Errors to Catch Before Submitting

1. **Wrong campaign targeted** — Always confirm the campaign name and ID before making any change
2. **Bid entered as dollar amount vs. percentage** — Amazon's bulk upload can be confusing; verify format
3. **Negative keyword match type wrong** — Exact negatives block only that exact phrase; phrase negatives block anything containing the phrase
4. **Bid ceiling exceeded** — If your bid change puts a keyword above its max bid cap, the change will be rejected or capped
5. **Decimal point in wrong place** — $0.10 vs $1.00 is a 10x difference. Always double-check.

---

## Related Pages

- [New Product Launch Blueprint](/docs/sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint)
- [Search Term Mining SOP](/docs/sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop)
- [Bulk Upload QA Checklist](/docs/sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist)
- [Negative Keywords Hub](/docs/sections/09-9-negative-keywords-and-negation-strategy)
- [Bid Adjustment Cadence](/docs/sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence)
