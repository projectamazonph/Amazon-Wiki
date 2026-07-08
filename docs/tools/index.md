---
title: "Tools & Automation Hub"
summary: "The complete landscape of Amazon PPC tools — all-in-one suites, point solutions, build vs. buy framework, and a free tool stack that actually works."
last_updated: 2026-07-08
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["tools", "automation", "software", "spreadsheets", "browser-extensions"]
---

# Tools & Automation Hub

Every tool you'll need for Amazon PPC, organized by what it actually does. This page covers the full ecosystem — from free spreadsheet templates to enterprise suites — with a framework for deciding what to use when.

**Jump to section:**
- [Existing Tool Pages](#existing-tool-pages)
- [Build vs. Buy Framework](#build-vs-buy-framework)
- [Free Tool Stack](#free-tool-stack)
- [Spreadsheet Templates](#spreadsheet-templates)
- [Browser Extensions](#browser-extensions)
- [Tool Evaluation Checklist](#tool-evaluation-checklist)

---

## Existing Tool Pages

The wiki has detailed pages on the tool ecosystem. Start here for context:

- [17.1 All-in-One Suites](/docs/sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites) — Helium 10, Sellics, Perpetua, and others
- [17.2 Point Solutions](/docs/sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions) — tools focused on one specific task
- [17.3 Build vs. Buy](/docs/sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy) — when to build internal tools vs. subscribe to SaaS
- [17.4 Tool Evaluation Framework](/docs/sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework) — structured rubric for evaluating tools

**Automation-specific pages:**
- [16.1 Native Amazon Automation](/docs/sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation) — rules built into Amazon's console
- [16.2 Bulk Operations](/docs/sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations) — spreadsheet-based bulk management
- [16.3 Custom Scripts & API-Based Automation](/docs/sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation) — programmatic control
- [16.4 AI-Augmented PPC Management](/docs/sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management) — AI-assisted campaign management

---

## Build vs. Buy Framework

Before you pay for another tool subscription, work through this decision tree.

### Questions to Ask

**1. How many accounts are you managing?**
- 1-3 accounts: SaaS tools almost always win on cost and setup time
- 5+ accounts with consistent structure: custom tooling may pay off at scale

**2. How specific is the use case?**
- Generic campaign management: use an all-in-one suite
- One specific workflow (e.g., just search term mining): use a point solution
- Unique internal process that SaaS can't replicate: consider building

**3. What's your team's technical capacity?**
- No-code team: SaaS tools. Custom scripts require maintenance.
- Have a developer: API-based automation with custom dashboards scales better.
- Have a data analyst: build internal reporting on top of the Amazon Advertising API.

**4. What's the true cost?**

SaaS costs are visible. Build costs are hidden. A $300/month tool subscription looks expensive until you count:
- Developer time to build and maintain (even a "simple" script needs debugging)
- Opportunity cost of that developer not working on product or growth
- Cost of errors when a custom script misbehaves

Rule of thumb: if a SaaS tool saves 2+ hours per week of manual work and costs less than $100/month, it's almost always worth it.

### When to Build

- You need a workflow that SaaS tools don't support (e.g., profit-linked bid adjustments using your actual COGS data)
- You're managing 10+ accounts with identical structures and need bulk operations at scale
- You have data that can't leave your systems for compliance reasons
- You have a developer who's already on payroll with spare capacity

### When to Buy

- You're a small team with limited technical capacity
- Your workflow is well-served by existing tools
- You need fast setup (SaaS tools: days. Custom build: weeks to months)
- You want automatic updates as Amazon's platform evolves

---

## Free Tool Stack

These tools are free or have generous free tiers. Together they cover 80% of what most sellers need.

### Keyword Research

**Helium 10 Magnet (Free: 30 queries/month)**
- Reverse ASIN lookup: enter a competitor's ASIN, get the keywords they're ranking for
- Good for gap analysis: what keywords do competitors rank for that you're not targeting?
- URL: helium10.com

**Amazon Brand Analytics (Free: for brand-registered sellers)**
- Amazon's own search frequency rank data
- Most accurate keyword volume data available
- Download up to 90 days of data
- URL: Seller Central > Reports > Brand Analytics

**Google Keyword Planner (Free with Google account)**
- Not Amazon-specific, but useful for volume estimates and related keyword ideas
- Useful for international markets where Amazon keyword tools are thin
- Combine with Amazon auto campaign data for a fuller picture

### Campaign Management

**Amazon Sponsored Products Console (Free)**
- Native tool. Always start here.
- Bulk operations spreadsheet downloads/uploads
- Rule-based automation
- Less sophisticated than third-party tools, but zero cost and always accurate

**Amazon Advertising API (Free: apply for access)**
- For technical teams: direct data access for custom dashboards and automation
- Rate limits apply but sufficient for most use cases
- Apply at: advertiser-conditions.amazon.com

### Analytics & Reporting

**Amazon Marketing Cloud (AMC) (Free: for brands with significant ad spend)**
- SQL-based ad analytics on Amazon's data
- Attribution analysis, audience overlap, incrementality
- Requires SQL knowledge and data warehouse setup
- See [AMC SQL Basics](/docs/sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics)

**Google Data Studio / Looker Studio (Free)**
- Connect to Amazon data via third-party connectors or API
- Build custom dashboards
- Share with clients or team members
- Great for multi-account consolidated reporting

### Competitive Intelligence

**Jungle Scout (Free: limited Chrome extension)**
- Chrome extension shows estimated sales, revenue, and reviews for any Amazon product
- Good for quick competitive checks without a paid subscription

**Helium 10 Cerebro (Free: 30 searches/month)**
- Reverse ASIN keyword research
- Shows organic rank vs. sponsored rank

---

## Spreadsheet Templates

These Google Sheets templates cover the most common PPC workflows. Copy them to your own Drive and customize.

### Automatic Ruler / Campaign Structure Builder

Build campaigns in bulk using a spreadsheet. Enter keywords, match types, and bids in one sheet, then export to Amazon's bulk upload format.

**What it does:**
- Keyword list → structured campaign hierarchy (campaign > ad group > keyword)
- Auto-generates campaign naming convention
- Calculates estimated max bids from ACOS target + conversion rate + ASP
- Outputs bulk upload spreadsheet ready for Seller Central

**Setup:** Create a new Google Sheet, copy the template structure from [27.2 Downloadable Templates](/docs/sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates), and customize for your naming convention.

**Key columns:**
| Column | Purpose |
|--------|---------|
| Campaign Name | Consistent naming: `[Brand]_[Product]_[MatchType]_[Date]` |
| Ad Group Name | Group tightly themed keywords together |
| Keyword | The search term |
| Match Type | exact / phrase / broad |
| Bid | Start with calculated max bid, adjust based on competition |
| Campaign Daily Budget | Start at 10x your target bid |
| Campaign Type | sponsored-products / sponsored-brands |

### Keyword Harvester / Search Term Processor

Process your search term report and turn raw data into actionable campaign changes.

**What it does:**
- Paste raw search term report
- Auto-calculate ACOS, orders, and spend per term
- Flag terms for negation (0 orders, high spend)
- Flag terms for promotion to exact match (3+ orders, good ACOS)
- Generate negative keyword list for bulk upload

**Weekly workflow:**
1. Download search term report from Seller Central
2. Paste into the "Raw Data" tab
3. Review the "Action" column (Negate / Promote / Monitor)
4. Copy negation list to bulk upload spreadsheet
5. Upload to Seller Central

### Bid Management Tracker

Track bid changes and their impact over time.

**What it does:**
- Log each bid change with date, campaign, old bid, new bid, reason
- Track ACOS in the 7 days before and after the change
- Calculate whether the bid change improved or worsened performance
- Build a "bid history" for each campaign over time

This is especially useful for manual bidding campaigns where you're making regular adjustments. The pattern over time reveals what actually works for your specific product and market.

### ACOS Tracker

Simple weekly log of campaign performance.

| Week | Campaign | Spend | Revenue | ACOS | Orders | Notes |
|------|----------|-------|---------|------|--------|-------|
| W26 | SP-Auto | $423 | $1,540 | 27.5% | 42 | Added 5 negatives |
| W27 | SP-Auto | $398 | $1,610 | 24.7% | 47 | ACOS improving |

Plot this over time. A trend line tells you more than any single week.

---

## Browser Extensions

These run in Chrome and give you instant data while browsing Amazon or Seller Central.

### For Sellers (while browsing Amazon as a customer)

**Helium 10 Chrome Extension (Free tier available)**
- Shows BSR, estimated revenue, number of reviews, and FBA fees on any Amazon product page
- Useful for competitive research during keyword discovery

**Jungle Scout Extension**
- Similar to Helium 10: sales estimates, review counts, listing quality score
- Both tools are useful; try both and pick your preference

**Keepa (Free: limited / $15/month full)**
- Price history charts going back years
- Essential for understanding pricing trends and competitive landscape
- The free tier covers what most people need

### For PPC Managers (while in Seller Central)

**Amazon PPC Dashboard Chrome extensions** are limited — most good tools are web-based. The most useful browser-level tool is actually Seller Central itself with keyboard shortcuts:
- Use the bulk operations interface (Campaign Manager > Bulk Operations)
- Use filter views to save common searches
- Use the search term report with column customization to see ACOS, spend, and orders simultaneously

---

## Tool Evaluation Checklist

Before subscribing to any tool, run it through this checklist:

**Data Accuracy**
- [ ] Does the tool's keyword volume data match Amazon Brand Analytics (if you have access)?
- [ ] Does the tool's ACOS/spend data match Seller Central when pulled on the same day?
- [ ] Are historical data points consistent across sessions?

**Feature Fit**
- [ ] Does it support your campaign structure (SKAGs, single ASIN campaigns, etc.)?
- [ ] Does it handle all the ad types you use (SP, SB, SD, DSP)?
- [ ] Does it support bulk operations for your scale?

**Integration**
- [ ] Can it connect to your existing tools (Google Sheets, BI dashboards, etc.)?
- [ ] Does it export data in formats you can work with?
- [ ] Is there an API if you need programmatic access?

**Support**
- [ ] Is there a free trial (minimum 14 days)?
- [ ] What's the actual support response time — not the SLA on paper, but what people report?
- [ ] Is there an active community or knowledge base?

**Cost vs. Value**
- [ ] Does the monthly cost equal less than 5% of your ad spend?
- [ ] Does it save at least 2 hours per week of manual work?
- [ ] What's the churn rate — if other users are leaving, find out why before joining

**AI Tools (2026 additions)**
- [ ] If the tool claims AI features, test them with your actual products before committing
- [ ] Check whether AI outputs require human review before deployment
- [ ] Verify that AI recommendations are based on your data, not generic patterns

---

## Related Pages

- [All-in-One Suites](/docs/sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites)
- [Point Solutions](/docs/sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions)
- [Bulk Operations Guide](/docs/sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations)
- [Custom Scripts & API Automation](/docs/sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation)
- [Downloadable Templates](/docs/sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates)
