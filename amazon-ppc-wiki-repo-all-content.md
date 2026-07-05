# Amazon PPC Wiki Repo - Complete Markdown Export

This file combines the text-based contents of the repo into one Markdown document. Binary source files are listed, not embedded.

## Repository Tree

```text
.github/workflows/validate.yml
.gitignore
CHANGELOG.md
CONTRIBUTING.md
README.md
VALIDATION_NOTE.md
data/formulas.json
data/glossary.json
data/page_index.generated.json
data/pages.json
data/prerequisites.json
data/quizzes.sample.json
data/scenarios.sample.json
docs/app-layer/index.md
docs/appendix/formulas-calculators.md
docs/complete-data-filled-guide.md
docs/glossary/index.md
docs/index.md
docs/sections/00-0-front-matter/0-1-0-1-home-landing-page.md
docs/sections/00-0-front-matter/0-2-0-2-how-to-use-this-wiki.md
docs/sections/00-0-front-matter/0-3-0-3-contributor-maintenance-guide.md
docs/sections/00-0-front-matter/index.md
docs/sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md
docs/sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.md
docs/sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md
docs/sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.md
docs/sections/01-1-foundations-and-fundamentals/index.md
docs/sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.md
docs/sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md
docs/sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.md
docs/sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.md
docs/sections/02-2-account-and-campaign-architecture/index.md
docs/sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md
docs/sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md
docs/sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md
docs/sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.md
docs/sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md
docs/sections/03-3-campaign-types/3-6-3-6-cross-campaign-type-strategy.md
docs/sections/03-3-campaign-types/index.md
docs/sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md
docs/sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md
docs/sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md
docs/sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.md
docs/sections/04-4-targeting-and-match-types/index.md
docs/sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.md
docs/sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.md
docs/sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.md
docs/sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.md
docs/sections/05-5-keyword-research-and-search-term-mining/index.md
docs/sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md
docs/sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md
docs/sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md
docs/sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md
docs/sections/06-6-bidding-strategies-and-bid-management/index.md
docs/sections/07-7-budget-management-and-pacing/7-1-7-1-budget-allocation-frameworks.md
docs/sections/07-7-budget-management-and-pacing/7-2-7-2-pacing-and-ran-out-of-budget-diagnostics.md
docs/sections/07-7-budget-management-and-pacing/7-3-7-3-seasonal-budget-planning.md
docs/sections/07-7-budget-management-and-pacing/index.md
docs/sections/08-8-placements-and-placement-optimization/8-1-8-1-placement-types-explained.md
docs/sections/08-8-placements-and-placement-optimization/8-2-8-2-placement-reporting-and-diagnosis.md
docs/sections/08-8-placements-and-placement-optimization/index.md
docs/sections/09-9-negative-keywords-and-negation-strategy/9-1-9-1-negative-match-types.md
docs/sections/09-9-negative-keywords-and-negation-strategy/9-2-9-2-negation-strategy-by-campaign-structure.md
docs/sections/09-9-negative-keywords-and-negation-strategy/9-3-9-3-common-negation-mistakes.md
docs/sections/09-9-negative-keywords-and-negation-strategy/index.md
docs/sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive.md
docs/sections/10-10-metrics-kpis-and-analytics/10-2-10-2-advanced-metrics.md
docs/sections/10-10-metrics-kpis-and-analytics/10-3-10-3-health-check-frameworks.md
docs/sections/10-10-metrics-kpis-and-analytics/10-4-10-4-benchmarking.md
docs/sections/10-10-metrics-kpis-and-analytics/index.md
docs/sections/11-11-reporting-and-data-analysis/11-1-11-1-native-amazon-reports.md
docs/sections/11-11-reporting-and-data-analysis/11-2-11-2-brand-analytics.md
docs/sections/11-11-reporting-and-data-analysis/11-3-11-3-custom-reporting-and-dashboards.md
docs/sections/11-11-reporting-and-data-analysis/11-4-11-4-data-storytelling.md
docs/sections/11-11-reporting-and-data-analysis/index.md
docs/sections/12-12-amazon-marketing-cloud/12-1-12-1-what-amc-is-and-who-needs-it.md
docs/sections/12-12-amazon-marketing-cloud/12-2-12-2-amc-use-cases.md
docs/sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics.md
docs/sections/12-12-amazon-marketing-cloud/index.md
docs/sections/13-13-amazon-dsp/13-1-13-1-dsp-fundamentals.md
docs/sections/13-13-amazon-dsp/13-2-13-2-dsp-campaign-types.md
docs/sections/13-13-amazon-dsp/13-3-13-3-dsp-audience-building.md
docs/sections/13-13-amazon-dsp/13-4-13-4-dsp-plus-sponsored-ads-synergy.md
docs/sections/13-13-amazon-dsp/index.md
docs/sections/14-14-brand-presence-and-content-tie-ins/14-1-14-1-brand-registry.md
docs/sections/14-14-brand-presence-and-content-tie-ins/14-2-14-2-brand-store.md
docs/sections/14-14-brand-presence-and-content-tie-ins/14-3-14-3-aplus-content-premium-aplus.md
docs/sections/14-14-brand-presence-and-content-tie-ins/index.md
docs/sections/15-15-listing-optimization/15-1-15-1-why-listing-quality-gates-ppc-performance.md
docs/sections/15-15-listing-optimization/15-2-15-2-title-bullet-backend-keyword-optimization.md
docs/sections/15-15-listing-optimization/15-3-15-3-image-and-video-impact-on-ctr-cvr.md
docs/sections/15-15-listing-optimization/15-4-15-4-pricing-and-promotions-interplay-with-ppc.md
docs/sections/15-15-listing-optimization/index.md
docs/sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation.md
docs/sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations.md
docs/sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation.md
docs/sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management.md
docs/sections/16-16-automation-rules-and-scripts/index.md
docs/sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites.md
docs/sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions.md
docs/sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy.md
docs/sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework.md
docs/sections/17-17-software-and-tools-ecosystem/index.md
docs/sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch.md
docs/sections/18-18-strategy-by-business-lifecycle-stage/18-2-18-2-growth-stage.md
docs/sections/18-18-strategy-by-business-lifecycle-stage/18-3-18-3-mature-steady-state.md
docs/sections/18-18-strategy-by-business-lifecycle-stage/18-4-18-4-decline-sunset.md
docs/sections/18-18-strategy-by-business-lifecycle-stage/index.md
docs/sections/19-19-strategy-by-product-category/19-1-19-1-high-consideration-high-price-categories.md
docs/sections/19-19-strategy-by-product-category/19-2-19-2-low-price-impulse-categories.md
docs/sections/19-19-strategy-by-product-category/19-3-19-3-seasonal-gift-categories.md
docs/sections/19-19-strategy-by-product-category/19-4-19-4-regulated-categories.md
docs/sections/19-19-strategy-by-product-category/index.md
docs/sections/20-20-seasonal-and-event-planning/20-1-20-1-prime-day-playbook.md
docs/sections/20-20-seasonal-and-event-planning/20-2-20-2-q4-holiday-playbook.md
docs/sections/20-20-seasonal-and-event-planning/20-3-20-3-other-key-dates.md
docs/sections/20-20-seasonal-and-event-planning/index.md
docs/sections/21-21-international-and-multi-marketplace-ppc/21-1-21-1-marketplace-differences.md
docs/sections/21-21-international-and-multi-marketplace-ppc/21-2-21-2-cross-marketplace-account-structure.md
docs/sections/21-21-international-and-multi-marketplace-ppc/21-3-21-3-localization-considerations.md
docs/sections/21-21-international-and-multi-marketplace-ppc/index.md
docs/sections/22-22-agency-and-team-operations/22-1-22-1-team-roles-and-raci.md
docs/sections/22-22-agency-and-team-operations/22-2-22-2-sops-and-workflow-documentation.md
docs/sections/22-22-agency-and-team-operations/22-3-22-3-va-training-and-enablement.md
docs/sections/22-22-agency-and-team-operations/22-4-22-4-qa-and-review-process.md
docs/sections/22-22-agency-and-team-operations/index.md
docs/sections/23-23-client-and-stakeholder-communication/23-1-23-1-reporting-cadence.md
docs/sections/23-23-client-and-stakeholder-communication/23-2-23-2-setting-expectations.md
docs/sections/23-23-client-and-stakeholder-communication/23-3-23-3-handling-difficult-conversations.md
docs/sections/23-23-client-and-stakeholder-communication/index.md
docs/sections/24-24-compliance-policy-and-account-health/24-1-24-1-advertising-policy-basics.md
docs/sections/24-24-compliance-policy-and-account-health/24-2-24-2-account-health-interplay.md
docs/sections/24-24-compliance-policy-and-account-health/24-3-24-3-competitor-and-ethical-boundaries.md
docs/sections/24-24-compliance-policy-and-account-health/index.md
docs/sections/25-25-advanced-and-emerging-topics/25-1-25-1-retail-media-network-trends.md
docs/sections/25-25-advanced-and-emerging-topics/25-2-25-2-ai-s-growing-role-in-amazon-ads.md
docs/sections/25-25-advanced-and-emerging-topics/25-3-25-3-privacy-and-signal-loss.md
docs/sections/25-25-advanced-and-emerging-topics/index.md
docs/sections/26-26-career-certification-and-learning/26-1-26-1-certifications.md
docs/sections/26-26-career-certification-and-learning/26-2-26-2-career-pathing.md
docs/sections/26-26-career-certification-and-learning/26-3-26-3-continuing-education.md
docs/sections/26-26-career-certification-and-learning/index.md
docs/sections/27-27-case-studies-and-templates/27-1-27-1-case-study-template.md
docs/sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates.md
docs/sections/27-27-case-studies-and-templates/27-3-27-3-real-case-studies.md
docs/sections/27-27-case-studies-and-templates/index.md
docs/sections/28-28-glossary-and-acronyms/index.md
docs/sections/29-29-appendix-formulas-and-calculators/index.md
docs/sections/30-30-meta-changelog/30-30-meta-changelog.md
docs/sections/30-30-meta-changelog/index.md
docs/sections/31-31-training-layer-template/31-1-31-1-learning-aid.md
docs/sections/31-31-training-layer-template/31-2-31-2-quiz.md
docs/sections/31-31-training-layer-template/31-3-31-3-teaching-guide.md
docs/sections/31-31-training-layer-template/31-4-31-4-handout.md
docs/sections/31-31-training-layer-template/31-5-31-5-tagging-and-assembly-system.md
docs/sections/31-31-training-layer-template/31-6-31-6-rollout-priority.md
docs/sections/31-31-training-layer-template/31-7-31-7-assessment-and-certification-tie-in.md
docs/sections/31-31-training-layer-template/index.md
docs/sections/32-32-app-building-layer/32-1-32-1-content-as-data-separation.md
docs/sections/32-32-app-building-layer/32-2-32-2-standardized-schemas.md
docs/sections/32-32-app-building-layer/32-3-32-3-simulator-scenario-bank.md
docs/sections/32-32-app-building-layer/32-4-32-4-asset-library-with-naming-convention.md
docs/sections/32-32-app-building-layer/32-5-32-5-content-versioning-and-sync-contract.md
docs/sections/32-32-app-building-layer/32-6-32-6-api-export-layer.md
docs/sections/32-32-app-building-layer/32-7-32-7-difficulty-and-progression-graph.md
docs/sections/32-32-app-building-layer/32-8-32-8-multi-consumer-design.md
docs/sections/32-32-app-building-layer/index.md
docs/sections/zz-capstone-practice-scenarios/index.md
docs/sections/zz-deep-operational-playbooks/index.md
docs/sections/zz-deep-operational-playbooks/playbook-a-a-ppc-diagnostic-framework.md
docs/sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop.md
docs/sections/zz-deep-operational-playbooks/playbook-c-c-bid-and-budget-decision-matrix.md
docs/sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint.md
docs/sections/zz-deep-operational-playbooks/playbook-e-e-client-reporting-narrative-builder.md
docs/sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist.md
docs/sections/zz-deep-operational-playbooks/playbook-g-g-wiki-to-app-data-schemas.md
docs/sections/zz-how-this-expanded-version-is-different/index.md
docs/sections/zz-official-source-checklist-for-maintenance/index.md
docs/sections/zz-reusable-training-assets/index.md
docs/sections/zz-start-here-paths/index.md
docs/training/index.md
mkdocs.yml
requirements.txt
schemas/glossary.schema.json
schemas/learner-progress.schema.json
schemas/quiz.schema.json
schemas/scenario.schema.json
scripts/build_page_index.py
scripts/validate_content.py
source/Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx [binary listed only]
source/Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.pdf [binary listed only]
templates/changelog-template.md
templates/quiz-template.json
templates/scenario-template.json
templates/wiki-page-template.md
```

## Binary Files Listed Only

- `source/Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx` (93,815 bytes)
- `source/Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.pdf` (2,367,997 bytes)

## Text File Contents


---

## File: `.github/workflows/validate.yml`

```yaml
name: Validate Wiki Content
on:
  pull_request:
  push:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python scripts/validate_content.py
      - run: mkdocs build --strict
```

---

## File: `.gitignore`

```text
.venv/
site/
__pycache__/
.DS_Store
*.tmp
```

---

## File: `CHANGELOG.md`

```markdown

## 2.5.0 - 2026-07-05

- Merged the Complete Data-Filled Guide into numbered wiki section pages.
- Added consolidated guide page at `docs/complete-data-filled-guide.md`.
- Updated glossary, formulas, sample quizzes, and simulator scenarios.
- Added operator checklists to section pages for beginner-safe execution.

# Changelog

## 1.0.0 - 2026-07-05

- Initial wiki-style repository generated from the expanded Amazon PPC guide.
- Added Markdown docs, schemas, sample data, validation scripts, and MkDocs config.
```

---

## File: `CONTRIBUTING.md`

```markdown
# Contributing

Use `templates/wiki-page-template.md` for new pages. Keep language beginner-friendly. Every change that affects live workflow must include a `last_verified_against_live_console` date after checking Amazon Ads Console.

Before opening a PR, run:

``​`bash
python scripts/validate_content.py
``​`
```

---

## File: `README.md`

```markdown
# The Amazon PPC Wiki

A beginner-friendly, operator-ready knowledge base for Amazon PPC training, agency operations, and future app integration.

This repo was generated from the expanded Amazon PPC Wiki manual and is designed to work as:

- a GitHub wiki-style documentation repo,
- a MkDocs static knowledge base,
- a training library for VAs and junior strategists,
- a structured data source for simulators, quizzes, and future tools.

## Start here by role

- **Beginner VA:** Start with Sections 1-4, then 5-11, then 22.
- **Junior Strategist:** Read Sections 1-11, then 14-15, 18, 22-23.
- **Senior Strategist:** Read the core sections, then 12-13, 17, 21, 25, and 32.
- **Brand Owner:** Read Sections 1, 3, 10, 14-15, 18, 20, and 23.
- **Agency Owner:** Read Sections 2, 10-11, 16-17, 22-23, 26-27, and 32.

## Repo map

- `docs/sections/` - all wiki pages as Markdown.
- `docs/glossary/` - A-Z PPC terms and acronyms.
- `docs/appendix/` - formulas, calculators, and reference material.
- `docs/training/` - learning aids, quiz model, teaching guide model, handout model.
- `docs/app-layer/` - content-as-data and simulator integration notes.
- `data/` - machine-readable page index, glossary, formulas, quizzes, scenarios, and prerequisite graph.
- `schemas/` - JSON Schemas for app-facing content.
- `templates/` - reusable wiki page, changelog, quiz, and scenario templates.
- `scripts/` - validation and export helpers.

## Naming convention

Every page should keep these fields in YAML frontmatter:

``​`yaml
page_id: "1-1"
title: "What is Amazon PPC"
learner_level: "Foundational"
topic_tags: ["amazon-ppc", "foundations"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
``​`

## Local preview

``​`bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
``​`

Open the local URL MkDocs prints in your terminal.

## Generated source

Built from `Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx`.


## Complete Data-Filled Guide merge

This repo now includes the beginner-friendly complete guide content merged into the numbered wiki section pages. A consolidated copy lives at `docs/complete-data-filled-guide.md`, while the operational content is split across `docs/sections/*` for normal wiki navigation.

Key additions:

- Detailed beginner explanations by section
- Practical workflows and operator checklists
- Expanded glossary and formulas
- Sample quizzes and simulator scenarios
- Versioned content notes for app/LMS reuse
```

---

## File: `VALIDATION_NOTE.md`

```markdown
mkdocs strict build attempted after data merge. Review note: [Errno 2] No such file or directory: 'mkdocs'
```

---

## File: `data/formulas.json`

```json
[
  {
    "id": "acos",
    "name": "ACOS",
    "formula": "ad_spend / ad_sales",
    "plain_english": "How much ad spend was needed to create ad-attributed revenue."
  },
  {
    "id": "roas",
    "name": "ROAS",
    "formula": "ad_sales / ad_spend",
    "plain_english": "How many dollars of ad revenue you earned per dollar spent."
  },
  {
    "id": "tacos",
    "name": "TACOS",
    "formula": "ad_spend / total_sales",
    "plain_english": "How much total business revenue is supported by advertising spend."
  },
  {
    "id": "break_even_acos",
    "name": "Break-even ACOS",
    "formula": "gross_profit / price",
    "plain_english": "Highest ACOS before ads likely become unprofitable before strategic exceptions."
  },
  {
    "id": "target_bid",
    "name": "Target Bid",
    "formula": "price * conversion_rate * target_acos",
    "plain_english": "A simple safe bid estimate based on price, conversion rate, and target efficiency."
  }
]
```

---

## File: `data/glossary.json`

```json
[
  {
    "term": "ACOS",
    "short_def": "Advertising Cost of Sales. Ad spend divided by ad-attributed sales.",
    "long_def": "Advertising Cost of Sales. Ad spend divided by ad-attributed sales.",
    "related_terms": [
      "ROAS",
      "TACOS"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Ad Group",
    "short_def": "A focused group inside a campaign containing ads and targets.",
    "long_def": "A focused group inside a campaign containing ads and targets.",
    "related_terms": [
      "Campaign",
      "Keyword"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "ASIN",
    "short_def": "Amazon Standard Identification Number. A unique product identifier.",
    "long_def": "Amazon Standard Identification Number. A unique product identifier.",
    "related_terms": [
      "Product Targeting"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Attribution Window",
    "short_def": "The time Amazon uses to credit sales after an ad click or view.",
    "long_def": "The time Amazon uses to credit sales after an ad click or view.",
    "related_terms": [
      "ROAS",
      "Reporting"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Auto Campaign",
    "short_def": "A Sponsored Products campaign where Amazon chooses targets from listing data.",
    "long_def": "A Sponsored Products campaign where Amazon chooses targets from listing data.",
    "related_terms": [
      "Close Match",
      "Loose Match"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Brand Registry",
    "short_def": "Amazon program for brand owners that unlocks advanced brand and ad features.",
    "long_def": "Amazon program for brand owners that unlocks advanced brand and ad features.",
    "related_terms": [
      "Sponsored Brands",
      "A+ Content"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Broad Match",
    "short_def": "Keyword match type that reaches wide variations of the keyword.",
    "long_def": "Keyword match type that reaches wide variations of the keyword.",
    "related_terms": [
      "Phrase Match",
      "Exact Match"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Buy Box",
    "short_def": "The purchase box on a listing. Sponsored Products usually require Buy Box eligibility.",
    "long_def": "The purchase box on a listing. Sponsored Products usually require Buy Box eligibility.",
    "related_terms": [
      "Eligibility"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "CPC",
    "short_def": "Cost per click. Ad spend divided by clicks.",
    "long_def": "Cost per click. Ad spend divided by clicks.",
    "related_terms": [
      "Bid",
      "CTR"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "CTR",
    "short_def": "Click-through rate. Clicks divided by impressions.",
    "long_def": "Click-through rate. Clicks divided by impressions.",
    "related_terms": [
      "Impressions",
      "Clicks"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "CVR",
    "short_def": "Conversion rate. Orders divided by clicks.",
    "long_def": "Conversion rate. Orders divided by clicks.",
    "related_terms": [
      "Orders",
      "Listing Optimization"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "DSP",
    "short_def": "Demand Side Platform. Amazon's programmatic platform for display, video, audio, and TV ads.",
    "long_def": "Demand Side Platform. Amazon's programmatic platform for display, video, audio, and TV ads.",
    "related_terms": [
      "AMC",
      "Sponsored Display"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Exact Match",
    "short_def": "Keyword match type focused on exact or close variations.",
    "long_def": "Keyword match type focused on exact or close variations.",
    "related_terms": [
      "Broad Match",
      "Phrase Match"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Negative Keyword",
    "short_def": "A term that prevents ads from showing for unwanted searches.",
    "long_def": "A term that prevents ads from showing for unwanted searches.",
    "related_terms": [
      "Negative Exact",
      "Negative Phrase"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "Portfolio",
    "short_def": "A campaign grouping tool that can help reporting and budget control.",
    "long_def": "A campaign grouping tool that can help reporting and budget control.",
    "related_terms": [
      "Budget"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "ROAS",
    "short_def": "Return on ad spend. Ad revenue divided by ad spend.",
    "long_def": "Return on ad spend. Ad revenue divided by ad spend.",
    "related_terms": [
      "ACOS"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  },
  {
    "term": "TACOS",
    "short_def": "Total advertising cost of sales. Ad spend divided by total sales.",
    "long_def": "Total advertising cost of sales. Ad spend divided by total sales.",
    "related_terms": [
      "ACOS",
      "Organic Sales"
    ],
    "first_appears_in_section": "1.3",
    "version": "2.5"
  }
]
```

---

## File: `data/page_index.generated.json`

```json
[
  {
    "title": "App-Building Layer",
    "path": "app-layer/index.md"
  },
  {
    "title": "Formula Appendix",
    "path": "appendix/formulas-calculators.md"
  },
  {
    "title": "Glossary & Acronyms",
    "path": "glossary/index.md"
  },
  {
    "title": "Amazon PPC Wiki",
    "path": "index.md"
  },
  {
    "title": "0.1 Home / Landing Page",
    "path": "sections/00-0-front-matter/0-1-0-1-home-landing-page.md"
  },
  {
    "title": "0.2 How to Use This Wiki",
    "path": "sections/00-0-front-matter/0-2-0-2-how-to-use-this-wiki.md"
  },
  {
    "title": "0.3 Contributor / Maintenance Guide",
    "path": "sections/00-0-front-matter/0-3-0-3-contributor-maintenance-guide.md"
  },
  {
    "title": "0. Front Matter",
    "path": "sections/00-0-front-matter/index.md"
  },
  {
    "title": "1.1 What is Amazon PPC",
    "path": "sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md"
  },
  {
    "title": "1.2 The Amazon Advertising Ecosystem",
    "path": "sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.md"
  },
  {
    "title": "1.3 Core Terminology Primer",
    "path": "sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md"
  },
  {
    "title": "1.4 Eligibility & Prerequisites",
    "path": "sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.md"
  },
  {
    "title": "1. Foundations & Fundamentals",
    "path": "sections/01-1-foundations-and-fundamentals/index.md"
  },
  {
    "title": "2.1 Account Structure Philosophy",
    "path": "sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.md"
  },
  {
    "title": "2.2 Campaign Structuring Models",
    "path": "sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md"
  },
  {
    "title": "2.3 Ad Group Best Practices",
    "path": "sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.md"
  },
  {
    "title": "2.4 Portfolio & Budget Grouping",
    "path": "sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.md"
  },
  {
    "title": "2. Account & Campaign Architecture",
    "path": "sections/02-2-account-and-campaign-architecture/index.md"
  },
  {
    "title": "3.1 Sponsored Products (SP)",
    "path": "sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md"
  },
  {
    "title": "3.2 Sponsored Brands (SB)",
    "path": "sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md"
  },
  {
    "title": "3.3 Sponsored Display (SD)",
    "path": "sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md"
  },
  {
    "title": "3.4 Sponsored TV / Streaming TV Ads",
    "path": "sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.md"
  },
  {
    "title": "3.5 Amazon DSP",
    "path": "sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md"
  },
  {
    "title": "3.6 Cross-Campaign-Type Strategy",
    "path": "sections/03-3-campaign-types/3-6-3-6-cross-campaign-type-strategy.md"
  },
  {
    "title": "3. Campaign Types",
    "path": "sections/03-3-campaign-types/index.md"
  },
  {
    "title": "4.1 Keyword Match Types",
    "path": "sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md"
  },
  {
    "title": "4.2 Product Targeting",
    "path": "sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md"
  },
  {
    "title": "4.3 Audience Targeting",
    "path": "sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md"
  },
  {
    "title": "4.4 Auto-Targeting Categories",
    "path": "sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.md"
  },
  {
    "title": "4. Targeting & Match Types",
    "path": "sections/04-4-targeting-and-match-types/index.md"
  },
  {
    "title": "5.1 Research Methodology",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.md"
  },
  {
    "title": "5.2 Keyword Research Tools",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.md"
  },
  {
    "title": "5.3 Search Term Harvesting Workflow",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.md"
  },
  {
    "title": "5.4 Long-Tail vs. Head Term Strategy",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.md"
  },
  {
    "title": "5. Keyword Research & Search Term Mining",
    "path": "sections/05-5-keyword-research-and-search-term-mining/index.md"
  },
  {
    "title": "6.1 Manual Bidding Fundamentals",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md"
  },
  {
    "title": "6.2 Dynamic & Rule-Based Bidding",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md"
  },
  {
    "title": "6.3 Bid Adjustment Cadence",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md"
  },
  {
    "title": "6.4 Placement Bid Modifiers",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md"
  },
  {
    "title": "6. Bidding Strategies & Bid Management",
    "path": "sections/06-6-bidding-strategies-and-bid-management/index.md"
  },
  {
    "title": "7.1 Budget Allocation Frameworks",
    "path": "sections/07-7-budget-management-and-pacing/7-1-7-1-budget-allocation-frameworks.md"
  },
  {
    "title": "7.2 Pacing and Ran Out of Budget Diagnostics",
    "path": "sections/07-7-budget-management-and-pacing/7-2-7-2-pacing-and-ran-out-of-budget-diagnostics.md"
  },
  {
    "title": "7.3 Seasonal Budget Planning",
    "path": "sections/07-7-budget-management-and-pacing/7-3-7-3-seasonal-budget-planning.md"
  },
  {
    "title": "7. Budget Management & Pacing",
    "path": "sections/07-7-budget-management-and-pacing/index.md"
  },
  {
    "title": "8.1 Placement Types Explained",
    "path": "sections/08-8-placements-and-placement-optimization/8-1-8-1-placement-types-explained.md"
  },
  {
    "title": "8.2 Placement Reporting & Diagnosis",
    "path": "sections/08-8-placements-and-placement-optimization/8-2-8-2-placement-reporting-and-diagnosis.md"
  },
  {
    "title": "8. Placements & Placement Optimization",
    "path": "sections/08-8-placements-and-placement-optimization/index.md"
  },
  {
    "title": "9.1 Negative Match Types",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-1-9-1-negative-match-types.md"
  },
  {
    "title": "9.2 Negation Strategy by Campaign Structure",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-2-9-2-negation-strategy-by-campaign-structure.md"
  },
  {
    "title": "9.3 Common Negation Mistakes",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-3-9-3-common-negation-mistakes.md"
  },
  {
    "title": "9. Negative Keywords & Negation Strategy",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/index.md"
  },
  {
    "title": "10.1 Core Metrics Deep Dive",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive.md"
  },
  {
    "title": "10.2 Advanced Metrics",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-2-10-2-advanced-metrics.md"
  },
  {
    "title": "10.3 Health Check Frameworks",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-3-10-3-health-check-frameworks.md"
  },
  {
    "title": "10.4 Benchmarking",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-4-10-4-benchmarking.md"
  },
  {
    "title": "10. Metrics, KPIs & Analytics",
    "path": "sections/10-10-metrics-kpis-and-analytics/index.md"
  },
  {
    "title": "11.1 Native Amazon Reports",
    "path": "sections/11-11-reporting-and-data-analysis/11-1-11-1-native-amazon-reports.md"
  },
  {
    "title": "11.2 Brand Analytics",
    "path": "sections/11-11-reporting-and-data-analysis/11-2-11-2-brand-analytics.md"
  },
  {
    "title": "11.3 Custom Reporting & Dashboards",
    "path": "sections/11-11-reporting-and-data-analysis/11-3-11-3-custom-reporting-and-dashboards.md"
  },
  {
    "title": "11.4 Data Storytelling",
    "path": "sections/11-11-reporting-and-data-analysis/11-4-11-4-data-storytelling.md"
  },
  {
    "title": "11. Reporting & Data Analysis",
    "path": "sections/11-11-reporting-and-data-analysis/index.md"
  },
  {
    "title": "12.1 What AMC Is and Who Needs It",
    "path": "sections/12-12-amazon-marketing-cloud/12-1-12-1-what-amc-is-and-who-needs-it.md"
  },
  {
    "title": "12.2 AMC Use Cases",
    "path": "sections/12-12-amazon-marketing-cloud/12-2-12-2-amc-use-cases.md"
  },
  {
    "title": "12.3 AMC SQL Basics",
    "path": "sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics.md"
  },
  {
    "title": "12. Amazon Marketing Cloud",
    "path": "sections/12-12-amazon-marketing-cloud/index.md"
  },
  {
    "title": "13.1 DSP Fundamentals",
    "path": "sections/13-13-amazon-dsp/13-1-13-1-dsp-fundamentals.md"
  },
  {
    "title": "13.2 DSP Campaign Types",
    "path": "sections/13-13-amazon-dsp/13-2-13-2-dsp-campaign-types.md"
  },
  {
    "title": "13.3 DSP Audience Building",
    "path": "sections/13-13-amazon-dsp/13-3-13-3-dsp-audience-building.md"
  },
  {
    "title": "13.4 DSP + Sponsored Ads Synergy",
    "path": "sections/13-13-amazon-dsp/13-4-13-4-dsp-plus-sponsored-ads-synergy.md"
  },
  {
    "title": "13. Amazon DSP",
    "path": "sections/13-13-amazon-dsp/index.md"
  },
  {
    "title": "14.1 Brand Registry",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-1-14-1-brand-registry.md"
  },
  {
    "title": "14.2 Brand Store",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-2-14-2-brand-store.md"
  },
  {
    "title": "14.3 A+ Content / Premium A+",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-3-14-3-aplus-content-premium-aplus.md"
  },
  {
    "title": "14. Brand Presence & Content Tie-Ins",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/index.md"
  },
  {
    "title": "15.1 Why Listing Quality Gates PPC Performance",
    "path": "sections/15-15-listing-optimization/15-1-15-1-why-listing-quality-gates-ppc-performance.md"
  },
  {
    "title": "15.2 Title, Bullet, Backend Keyword Optimization",
    "path": "sections/15-15-listing-optimization/15-2-15-2-title-bullet-backend-keyword-optimization.md"
  },
  {
    "title": "15.3 Image & Video Impact on CTR/CVR",
    "path": "sections/15-15-listing-optimization/15-3-15-3-image-and-video-impact-on-ctr-cvr.md"
  },
  {
    "title": "15.4 Pricing & Promotions Interplay with PPC",
    "path": "sections/15-15-listing-optimization/15-4-15-4-pricing-and-promotions-interplay-with-ppc.md"
  },
  {
    "title": "15. Listing Optimization",
    "path": "sections/15-15-listing-optimization/index.md"
  },
  {
    "title": "16.1 Native Amazon Automation",
    "path": "sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation.md"
  },
  {
    "title": "16.2 Bulk Operations",
    "path": "sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations.md"
  },
  {
    "title": "16.3 Custom Scripts & API-Based Automation",
    "path": "sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation.md"
  },
  {
    "title": "16.4 AI-Augmented PPC Management",
    "path": "sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management.md"
  },
  {
    "title": "16. Automation, Rules & Scripts",
    "path": "sections/16-16-automation-rules-and-scripts/index.md"
  },
  {
    "title": "17.1 All-in-One Suites",
    "path": "sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites.md"
  },
  {
    "title": "17.2 Point Solutions",
    "path": "sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions.md"
  },
  {
    "title": "17.3 Build vs. Buy",
    "path": "sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy.md"
  },
  {
    "title": "17.4 Tool Evaluation Framework",
    "path": "sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework.md"
  },
  {
    "title": "17. Software & Tools Ecosystem",
    "path": "sections/17-17-software-and-tools-ecosystem/index.md"
  },
  {
    "title": "18.1 New Product Launch",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch.md"
  },
  {
    "title": "18.2 Growth Stage",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-2-18-2-growth-stage.md"
  },
  {
    "title": "18.3 Mature/Steady-State",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-3-18-3-mature-steady-state.md"
  },
  {
    "title": "18.4 Decline/Sunset",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-4-18-4-decline-sunset.md"
  },
  {
    "title": "18. Strategy by Business Lifecycle Stage",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/index.md"
  },
  {
    "title": "19.1 High-Consideration / High-Price Categories",
    "path": "sections/19-19-strategy-by-product-category/19-1-19-1-high-consideration-high-price-categories.md"
  },
  {
    "title": "19.2 Low-Price / Impulse Categories",
    "path": "sections/19-19-strategy-by-product-category/19-2-19-2-low-price-impulse-categories.md"
  },
  {
    "title": "19.3 Seasonal/Gift Categories",
    "path": "sections/19-19-strategy-by-product-category/19-3-19-3-seasonal-gift-categories.md"
  },
  {
    "title": "19.4 Regulated Categories",
    "path": "sections/19-19-strategy-by-product-category/19-4-19-4-regulated-categories.md"
  },
  {
    "title": "19. Strategy by Product Category",
    "path": "sections/19-19-strategy-by-product-category/index.md"
  },
  {
    "title": "20.1 Prime Day Playbook",
    "path": "sections/20-20-seasonal-and-event-planning/20-1-20-1-prime-day-playbook.md"
  },
  {
    "title": "20.2 Q4 / Holiday Playbook",
    "path": "sections/20-20-seasonal-and-event-planning/20-2-20-2-q4-holiday-playbook.md"
  },
  {
    "title": "20.3 Other Key Dates",
    "path": "sections/20-20-seasonal-and-event-planning/20-3-20-3-other-key-dates.md"
  },
  {
    "title": "20. Seasonal & Event Planning",
    "path": "sections/20-20-seasonal-and-event-planning/index.md"
  },
  {
    "title": "21.1 Marketplace Differences",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-1-21-1-marketplace-differences.md"
  },
  {
    "title": "21.2 Cross-Marketplace Account Structure",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-2-21-2-cross-marketplace-account-structure.md"
  },
  {
    "title": "21.3 Localization Considerations",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-3-21-3-localization-considerations.md"
  },
  {
    "title": "21. International & Multi-Marketplace PPC",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/index.md"
  },
  {
    "title": "22.1 Team Roles & RACI",
    "path": "sections/22-22-agency-and-team-operations/22-1-22-1-team-roles-and-raci.md"
  },
  {
    "title": "22.2 SOPs & Workflow Documentation",
    "path": "sections/22-22-agency-and-team-operations/22-2-22-2-sops-and-workflow-documentation.md"
  },
  {
    "title": "22.3 VA Training & Enablement",
    "path": "sections/22-22-agency-and-team-operations/22-3-22-3-va-training-and-enablement.md"
  },
  {
    "title": "22.4 QA & Review Process",
    "path": "sections/22-22-agency-and-team-operations/22-4-22-4-qa-and-review-process.md"
  },
  {
    "title": "22. Agency & Team Operations",
    "path": "sections/22-22-agency-and-team-operations/index.md"
  },
  {
    "title": "23.1 Reporting Cadence",
    "path": "sections/23-23-client-and-stakeholder-communication/23-1-23-1-reporting-cadence.md"
  },
  {
    "title": "23.2 Setting Expectations",
    "path": "sections/23-23-client-and-stakeholder-communication/23-2-23-2-setting-expectations.md"
  },
  {
    "title": "23.3 Handling Difficult Conversations",
    "path": "sections/23-23-client-and-stakeholder-communication/23-3-23-3-handling-difficult-conversations.md"
  },
  {
    "title": "23. Client & Stakeholder Communication",
    "path": "sections/23-23-client-and-stakeholder-communication/index.md"
  },
  {
    "title": "24.1 Advertising Policy Basics",
    "path": "sections/24-24-compliance-policy-and-account-health/24-1-24-1-advertising-policy-basics.md"
  },
  {
    "title": "24.2 Account Health Interplay",
    "path": "sections/24-24-compliance-policy-and-account-health/24-2-24-2-account-health-interplay.md"
  },
  {
    "title": "24.3 Competitor & Ethical Boundaries",
    "path": "sections/24-24-compliance-policy-and-account-health/24-3-24-3-competitor-and-ethical-boundaries.md"
  },
  {
    "title": "24. Compliance, Policy & Account Health",
    "path": "sections/24-24-compliance-policy-and-account-health/index.md"
  },
  {
    "title": "25.1 Retail Media Network Trends",
    "path": "sections/25-25-advanced-and-emerging-topics/25-1-25-1-retail-media-network-trends.md"
  },
  {
    "title": "25.2 AI's Growing Role in Amazon Ads",
    "path": "sections/25-25-advanced-and-emerging-topics/25-2-25-2-ai-s-growing-role-in-amazon-ads.md"
  },
  {
    "title": "25.3 Privacy & Signal Loss",
    "path": "sections/25-25-advanced-and-emerging-topics/25-3-25-3-privacy-and-signal-loss.md"
  },
  {
    "title": "25. Advanced & Emerging Topics",
    "path": "sections/25-25-advanced-and-emerging-topics/index.md"
  },
  {
    "title": "26.1 Certifications",
    "path": "sections/26-26-career-certification-and-learning/26-1-26-1-certifications.md"
  },
  {
    "title": "26.2 Career Pathing",
    "path": "sections/26-26-career-certification-and-learning/26-2-26-2-career-pathing.md"
  },
  {
    "title": "26.3 Continuing Education",
    "path": "sections/26-26-career-certification-and-learning/26-3-26-3-continuing-education.md"
  },
  {
    "title": "26. Career, Certification & Learning",
    "path": "sections/26-26-career-certification-and-learning/index.md"
  },
  {
    "title": "27.1 Case Study Template",
    "path": "sections/27-27-case-studies-and-templates/27-1-27-1-case-study-template.md"
  },
  {
    "title": "27.2 Downloadable Templates",
    "path": "sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates.md"
  },
  {
    "title": "27.3 Real Case Studies",
    "path": "sections/27-27-case-studies-and-templates/27-3-27-3-real-case-studies.md"
  },
  {
    "title": "27. Case Studies & Templates",
    "path": "sections/27-27-case-studies-and-templates/index.md"
  },
  {
    "title": "28. Glossary & Acronyms",
    "path": "sections/28-28-glossary-and-acronyms/index.md"
  },
  {
    "title": "29. Appendix: Formulas & Calculators",
    "path": "sections/29-29-appendix-formulas-and-calculators/index.md"
  },
  {
    "title": "30. Meta / Changelog",
    "path": "sections/30-30-meta-changelog/30-30-meta-changelog.md"
  },
  {
    "title": "30. Meta / Changelog",
    "path": "sections/30-30-meta-changelog/index.md"
  },
  {
    "title": "31.1 Learning Aid",
    "path": "sections/31-31-training-layer-template/31-1-31-1-learning-aid.md"
  },
  {
    "title": "31.2 Quiz",
    "path": "sections/31-31-training-layer-template/31-2-31-2-quiz.md"
  },
  {
    "title": "31.3 Teaching Guide",
    "path": "sections/31-31-training-layer-template/31-3-31-3-teaching-guide.md"
  },
  {
    "title": "31.4 Handout",
    "path": "sections/31-31-training-layer-template/31-4-31-4-handout.md"
  },
  {
    "title": "31.5 Tagging & Assembly System",
    "path": "sections/31-31-training-layer-template/31-5-31-5-tagging-and-assembly-system.md"
  },
  {
    "title": "31.6 Rollout Priority",
    "path": "sections/31-31-training-layer-template/31-6-31-6-rollout-priority.md"
  },
  {
    "title": "31.7 Assessment & Certification Tie-In",
    "path": "sections/31-31-training-layer-template/31-7-31-7-assessment-and-certification-tie-in.md"
  },
  {
    "title": "31. Training Layer Template",
    "path": "sections/31-31-training-layer-template/index.md"
  },
  {
    "title": "32.1 Content-as-Data Separation",
    "path": "sections/32-32-app-building-layer/32-1-32-1-content-as-data-separation.md"
  },
  {
    "title": "32.2 Standardized Schemas",
    "path": "sections/32-32-app-building-layer/32-2-32-2-standardized-schemas.md"
  },
  {
    "title": "32.3 Simulator Scenario Bank",
    "path": "sections/32-32-app-building-layer/32-3-32-3-simulator-scenario-bank.md"
  },
  {
    "title": "32.4 Asset Library with Naming Convention",
    "path": "sections/32-32-app-building-layer/32-4-32-4-asset-library-with-naming-convention.md"
  },
  {
    "title": "32.5 Content Versioning & Sync Contract",
    "path": "sections/32-32-app-building-layer/32-5-32-5-content-versioning-and-sync-contract.md"
  },
  {
    "title": "32.6 API/Export Layer",
    "path": "sections/32-32-app-building-layer/32-6-32-6-api-export-layer.md"
  },
  {
    "title": "32.7 Difficulty & Progression Graph",
    "path": "sections/32-32-app-building-layer/32-7-32-7-difficulty-and-progression-graph.md"
  },
  {
    "title": "32.8 Multi-Consumer Design",
    "path": "sections/32-32-app-building-layer/32-8-32-8-multi-consumer-design.md"
  },
  {
    "title": "32. App-Building Layer",
    "path": "sections/32-32-app-building-layer/index.md"
  },
  {
    "title": "Capstone Practice Scenarios",
    "path": "sections/zz-capstone-practice-scenarios/index.md"
  },
  {
    "title": "Deep Operational Playbooks",
    "path": "sections/zz-deep-operational-playbooks/index.md"
  },
  {
    "title": "A. PPC Diagnostic Framework",
    "path": "sections/zz-deep-operational-playbooks/playbook-a-a-ppc-diagnostic-framework.md"
  },
  {
    "title": "B. Search Term Mining SOP",
    "path": "sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop.md"
  },
  {
    "title": "C. Bid and Budget Decision Matrix",
    "path": "sections/zz-deep-operational-playbooks/playbook-c-c-bid-and-budget-decision-matrix.md"
  },
  {
    "title": "D. New Product Launch Blueprint",
    "path": "sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint.md"
  },
  {
    "title": "E. Client Reporting Narrative Builder",
    "path": "sections/zz-deep-operational-playbooks/playbook-e-e-client-reporting-narrative-builder.md"
  },
  {
    "title": "F. Bulk Upload and Change QA Checklist",
    "path": "sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist.md"
  },
  {
    "title": "G. Wiki-to-App Data Schemas",
    "path": "sections/zz-deep-operational-playbooks/playbook-g-g-wiki-to-app-data-schemas.md"
  },
  {
    "title": "How this expanded version is different",
    "path": "sections/zz-how-this-expanded-version-is-different/index.md"
  },
  {
    "title": "Official Source Checklist for Maintenance",
    "path": "sections/zz-official-source-checklist-for-maintenance/index.md"
  },
  {
    "title": "Reusable Training Assets",
    "path": "sections/zz-reusable-training-assets/index.md"
  },
  {
    "title": "Start Here Paths",
    "path": "sections/zz-start-here-paths/index.md"
  },
  {
    "title": "Training Layer",
    "path": "training/index.md"
  }
]
```

---

## File: `data/pages.json`

```json
[
  {
    "title": "0.1 Home / Landing Page",
    "page_id": "0-1",
    "section": "0. Front Matter",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/00-0-front-matter/0-1-0-1-home-landing-page.md"
  },
  {
    "title": "0.2 How to Use This Wiki",
    "page_id": "0-2",
    "section": "0. Front Matter",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/00-0-front-matter/0-2-0-2-how-to-use-this-wiki.md"
  },
  {
    "title": "0.3 Contributor / Maintenance Guide",
    "page_id": "0-3",
    "section": "0. Front Matter",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/00-0-front-matter/0-3-0-3-contributor-maintenance-guide.md"
  },
  {
    "title": "1.1 What is Amazon PPC",
    "page_id": "1-1",
    "section": "1. Foundations & Fundamentals",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md"
  },
  {
    "title": "1.2 The Amazon Advertising Ecosystem",
    "page_id": "1-2",
    "section": "1. Foundations & Fundamentals",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.md"
  },
  {
    "title": "1.3 Core Terminology Primer",
    "page_id": "1-3",
    "section": "1. Foundations & Fundamentals",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md"
  },
  {
    "title": "1.4 Eligibility & Prerequisites",
    "page_id": "1-4",
    "section": "1. Foundations & Fundamentals",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.md"
  },
  {
    "title": "2.1 Account Structure Philosophy",
    "page_id": "2-1",
    "section": "2. Account & Campaign Architecture",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.md"
  },
  {
    "title": "2.2 Campaign Structuring Models",
    "page_id": "2-2",
    "section": "2. Account & Campaign Architecture",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md"
  },
  {
    "title": "2.3 Ad Group Best Practices",
    "page_id": "2-3",
    "section": "2. Account & Campaign Architecture",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.md"
  },
  {
    "title": "2.4 Portfolio & Budget Grouping",
    "page_id": "2-4",
    "section": "2. Account & Campaign Architecture",
    "learner_level": "Foundational",
    "topic_tags": [
      "budget"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.md"
  },
  {
    "title": "3.1 Sponsored Products (SP)",
    "page_id": "3-1",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "sponsored-products"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md"
  },
  {
    "title": "3.2 Sponsored Brands (SB)",
    "page_id": "3-2",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "brand",
      "sponsored-brands"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md"
  },
  {
    "title": "3.3 Sponsored Display (SD)",
    "page_id": "3-3",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "sponsored-display"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md"
  },
  {
    "title": "3.4 Sponsored TV / Streaming TV Ads",
    "page_id": "3-4",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.md"
  },
  {
    "title": "3.5 Amazon DSP",
    "page_id": "3-5",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "dsp"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md"
  },
  {
    "title": "3.6 Cross-Campaign-Type Strategy",
    "page_id": "3-6",
    "section": "3. Campaign Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/03-3-campaign-types/3-6-3-6-cross-campaign-type-strategy.md"
  },
  {
    "title": "4.1 Keyword Match Types",
    "page_id": "4-1",
    "section": "4. Targeting & Match Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords",
      "targeting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md"
  },
  {
    "title": "4.2 Product Targeting",
    "page_id": "4-2",
    "section": "4. Targeting & Match Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "targeting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md"
  },
  {
    "title": "4.3 Audience Targeting",
    "page_id": "4-3",
    "section": "4. Targeting & Match Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "targeting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md"
  },
  {
    "title": "4.4 Auto-Targeting Categories",
    "page_id": "4-4",
    "section": "4. Targeting & Match Types",
    "learner_level": "Foundational",
    "topic_tags": [
      "targeting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.md"
  },
  {
    "title": "5.1 Research Methodology",
    "page_id": "5-1",
    "section": "5. Keyword Research & Search Term Mining",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.md"
  },
  {
    "title": "5.2 Keyword Research Tools",
    "page_id": "5-2",
    "section": "5. Keyword Research & Search Term Mining",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords",
      "tools"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.md"
  },
  {
    "title": "5.3 Search Term Harvesting Workflow",
    "page_id": "5-3",
    "section": "5. Keyword Research & Search Term Mining",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.md"
  },
  {
    "title": "5.4 Long-Tail vs. Head Term Strategy",
    "page_id": "5-4",
    "section": "5. Keyword Research & Search Term Mining",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.md"
  },
  {
    "title": "6.1 Manual Bidding Fundamentals",
    "page_id": "6-1",
    "section": "6. Bidding Strategies & Bid Management",
    "learner_level": "Foundational",
    "topic_tags": [
      "bidding"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md"
  },
  {
    "title": "6.2 Dynamic & Rule-Based Bidding",
    "page_id": "6-2",
    "section": "6. Bidding Strategies & Bid Management",
    "learner_level": "Foundational",
    "topic_tags": [
      "bidding"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md"
  },
  {
    "title": "6.3 Bid Adjustment Cadence",
    "page_id": "6-3",
    "section": "6. Bidding Strategies & Bid Management",
    "learner_level": "Foundational",
    "topic_tags": [
      "bidding"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md"
  },
  {
    "title": "6.4 Placement Bid Modifiers",
    "page_id": "6-4",
    "section": "6. Bidding Strategies & Bid Management",
    "learner_level": "Foundational",
    "topic_tags": [
      "bidding"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md"
  },
  {
    "title": "7.1 Budget Allocation Frameworks",
    "page_id": "7-1",
    "section": "7. Budget Management & Pacing",
    "learner_level": "Foundational",
    "topic_tags": [
      "budget"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/07-7-budget-management-and-pacing/7-1-7-1-budget-allocation-frameworks.md"
  },
  {
    "title": "7.2 Pacing and Ran Out of Budget Diagnostics",
    "page_id": "7-2",
    "section": "7. Budget Management & Pacing",
    "learner_level": "Foundational",
    "topic_tags": [
      "budget"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/07-7-budget-management-and-pacing/7-2-7-2-pacing-and-ran-out-of-budget-diagnostics.md"
  },
  {
    "title": "7.3 Seasonal Budget Planning",
    "page_id": "7-3",
    "section": "7. Budget Management & Pacing",
    "learner_level": "Foundational",
    "topic_tags": [
      "budget"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/07-7-budget-management-and-pacing/7-3-7-3-seasonal-budget-planning.md"
  },
  {
    "title": "8.1 Placement Types Explained",
    "page_id": "8-1",
    "section": "8. Placements & Placement Optimization",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/08-8-placements-and-placement-optimization/8-1-8-1-placement-types-explained.md"
  },
  {
    "title": "8.2 Placement Reporting & Diagnosis",
    "page_id": "8-2",
    "section": "8. Placements & Placement Optimization",
    "learner_level": "Foundational",
    "topic_tags": [
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/08-8-placements-and-placement-optimization/8-2-8-2-placement-reporting-and-diagnosis.md"
  },
  {
    "title": "9.1 Negative Match Types",
    "page_id": "9-1",
    "section": "9. Negative Keywords & Negation Strategy",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-1-9-1-negative-match-types.md"
  },
  {
    "title": "9.2 Negation Strategy by Campaign Structure",
    "page_id": "9-2",
    "section": "9. Negative Keywords & Negation Strategy",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-2-9-2-negation-strategy-by-campaign-structure.md"
  },
  {
    "title": "9.3 Common Negation Mistakes",
    "page_id": "9-3",
    "section": "9. Negative Keywords & Negation Strategy",
    "learner_level": "Foundational",
    "topic_tags": [
      "keywords"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/09-9-negative-keywords-and-negation-strategy/9-3-9-3-common-negation-mistakes.md"
  },
  {
    "title": "10.1 Core Metrics Deep Dive",
    "page_id": "10-1",
    "section": "10. Metrics, KPIs & Analytics",
    "learner_level": "Foundational",
    "topic_tags": [
      "metrics"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive.md"
  },
  {
    "title": "10.2 Advanced Metrics",
    "page_id": "10-2",
    "section": "10. Metrics, KPIs & Analytics",
    "learner_level": "Foundational",
    "topic_tags": [
      "metrics"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-2-10-2-advanced-metrics.md"
  },
  {
    "title": "10.3 Health Check Frameworks",
    "page_id": "10-3",
    "section": "10. Metrics, KPIs & Analytics",
    "learner_level": "Foundational",
    "topic_tags": [
      "metrics"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-3-10-3-health-check-frameworks.md"
  },
  {
    "title": "10.4 Benchmarking",
    "page_id": "10-4",
    "section": "10. Metrics, KPIs & Analytics",
    "learner_level": "Foundational",
    "topic_tags": [
      "metrics"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/10-10-metrics-kpis-and-analytics/10-4-10-4-benchmarking.md"
  },
  {
    "title": "11.1 Native Amazon Reports",
    "page_id": "11-1",
    "section": "11. Reporting & Data Analysis",
    "learner_level": "Foundational",
    "topic_tags": [
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/11-11-reporting-and-data-analysis/11-1-11-1-native-amazon-reports.md"
  },
  {
    "title": "11.2 Brand Analytics",
    "page_id": "11-2",
    "section": "11. Reporting & Data Analysis",
    "learner_level": "Foundational",
    "topic_tags": [
      "brand",
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/11-11-reporting-and-data-analysis/11-2-11-2-brand-analytics.md"
  },
  {
    "title": "11.3 Custom Reporting & Dashboards",
    "page_id": "11-3",
    "section": "11. Reporting & Data Analysis",
    "learner_level": "Foundational",
    "topic_tags": [
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/11-11-reporting-and-data-analysis/11-3-11-3-custom-reporting-and-dashboards.md"
  },
  {
    "title": "11.4 Data Storytelling",
    "page_id": "11-4",
    "section": "11. Reporting & Data Analysis",
    "learner_level": "Foundational",
    "topic_tags": [
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/11-11-reporting-and-data-analysis/11-4-11-4-data-storytelling.md"
  },
  {
    "title": "12.1 What AMC Is and Who Needs It",
    "page_id": "12-1",
    "section": "12. Amazon Marketing Cloud",
    "learner_level": "Applied",
    "topic_tags": [
      "amc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/12-12-amazon-marketing-cloud/12-1-12-1-what-amc-is-and-who-needs-it.md"
  },
  {
    "title": "12.2 AMC Use Cases",
    "page_id": "12-2",
    "section": "12. Amazon Marketing Cloud",
    "learner_level": "Applied",
    "topic_tags": [
      "amc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/12-12-amazon-marketing-cloud/12-2-12-2-amc-use-cases.md"
  },
  {
    "title": "12.3 AMC SQL Basics",
    "page_id": "12-3",
    "section": "12. Amazon Marketing Cloud",
    "learner_level": "Applied",
    "topic_tags": [
      "amc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics.md"
  },
  {
    "title": "13.1 DSP Fundamentals",
    "page_id": "13-1",
    "section": "13. Amazon DSP",
    "learner_level": "Applied",
    "topic_tags": [
      "dsp"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/13-13-amazon-dsp/13-1-13-1-dsp-fundamentals.md"
  },
  {
    "title": "13.2 DSP Campaign Types",
    "page_id": "13-2",
    "section": "13. Amazon DSP",
    "learner_level": "Applied",
    "topic_tags": [
      "dsp"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/13-13-amazon-dsp/13-2-13-2-dsp-campaign-types.md"
  },
  {
    "title": "13.3 DSP Audience Building",
    "page_id": "13-3",
    "section": "13. Amazon DSP",
    "learner_level": "Applied",
    "topic_tags": [
      "dsp"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/13-13-amazon-dsp/13-3-13-3-dsp-audience-building.md"
  },
  {
    "title": "13.4 DSP + Sponsored Ads Synergy",
    "page_id": "13-4",
    "section": "13. Amazon DSP",
    "learner_level": "Applied",
    "topic_tags": [
      "dsp"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/13-13-amazon-dsp/13-4-13-4-dsp-plus-sponsored-ads-synergy.md"
  },
  {
    "title": "14.1 Brand Registry",
    "page_id": "14-1",
    "section": "14. Brand Presence & Content Tie-Ins",
    "learner_level": "Applied",
    "topic_tags": [
      "brand"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-1-14-1-brand-registry.md"
  },
  {
    "title": "14.2 Brand Store",
    "page_id": "14-2",
    "section": "14. Brand Presence & Content Tie-Ins",
    "learner_level": "Applied",
    "topic_tags": [
      "brand"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-2-14-2-brand-store.md"
  },
  {
    "title": "14.3 A+ Content / Premium A+",
    "page_id": "14-3",
    "section": "14. Brand Presence & Content Tie-Ins",
    "learner_level": "Applied",
    "topic_tags": [
      "brand"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/14-14-brand-presence-and-content-tie-ins/14-3-14-3-aplus-content-premium-aplus.md"
  },
  {
    "title": "15.1 Why Listing Quality Gates PPC Performance",
    "page_id": "15-1",
    "section": "15. Listing Optimization",
    "learner_level": "Applied",
    "topic_tags": [
      "listing"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/15-15-listing-optimization/15-1-15-1-why-listing-quality-gates-ppc-performance.md"
  },
  {
    "title": "15.2 Title, Bullet, Backend Keyword Optimization",
    "page_id": "15-2",
    "section": "15. Listing Optimization",
    "learner_level": "Applied",
    "topic_tags": [
      "keywords",
      "listing"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/15-15-listing-optimization/15-2-15-2-title-bullet-backend-keyword-optimization.md"
  },
  {
    "title": "15.3 Image & Video Impact on CTR/CVR",
    "page_id": "15-3",
    "section": "15. Listing Optimization",
    "learner_level": "Applied",
    "topic_tags": [
      "listing"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/15-15-listing-optimization/15-3-15-3-image-and-video-impact-on-ctr-cvr.md"
  },
  {
    "title": "15.4 Pricing & Promotions Interplay with PPC",
    "page_id": "15-4",
    "section": "15. Listing Optimization",
    "learner_level": "Applied",
    "topic_tags": [
      "listing"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/15-15-listing-optimization/15-4-15-4-pricing-and-promotions-interplay-with-ppc.md"
  },
  {
    "title": "16.1 Native Amazon Automation",
    "page_id": "16-1",
    "section": "16. Automation, Rules & Scripts",
    "learner_level": "Applied",
    "topic_tags": [
      "automation"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation.md"
  },
  {
    "title": "16.2 Bulk Operations",
    "page_id": "16-2",
    "section": "16. Automation, Rules & Scripts",
    "learner_level": "Applied",
    "topic_tags": [
      "automation"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations.md"
  },
  {
    "title": "16.3 Custom Scripts & API-Based Automation",
    "page_id": "16-3",
    "section": "16. Automation, Rules & Scripts",
    "learner_level": "Applied",
    "topic_tags": [
      "automation"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation.md"
  },
  {
    "title": "16.4 AI-Augmented PPC Management",
    "page_id": "16-4",
    "section": "16. Automation, Rules & Scripts",
    "learner_level": "Applied",
    "topic_tags": [
      "automation"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management.md"
  },
  {
    "title": "17.1 All-in-One Suites",
    "page_id": "17-1",
    "section": "17. Software & Tools Ecosystem",
    "learner_level": "Applied",
    "topic_tags": [
      "tools"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites.md"
  },
  {
    "title": "17.2 Point Solutions",
    "page_id": "17-2",
    "section": "17. Software & Tools Ecosystem",
    "learner_level": "Applied",
    "topic_tags": [
      "tools"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions.md"
  },
  {
    "title": "17.3 Build vs. Buy",
    "page_id": "17-3",
    "section": "17. Software & Tools Ecosystem",
    "learner_level": "Applied",
    "topic_tags": [
      "tools"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy.md"
  },
  {
    "title": "17.4 Tool Evaluation Framework",
    "page_id": "17-4",
    "section": "17. Software & Tools Ecosystem",
    "learner_level": "Applied",
    "topic_tags": [
      "tools"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework.md"
  },
  {
    "title": "18.1 New Product Launch",
    "page_id": "18-1",
    "section": "18. Strategy by Business Lifecycle Stage",
    "learner_level": "Advanced",
    "topic_tags": [
      "launch"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch.md"
  },
  {
    "title": "18.2 Growth Stage",
    "page_id": "18-2",
    "section": "18. Strategy by Business Lifecycle Stage",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-2-18-2-growth-stage.md"
  },
  {
    "title": "18.3 Mature/Steady-State",
    "page_id": "18-3",
    "section": "18. Strategy by Business Lifecycle Stage",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-3-18-3-mature-steady-state.md"
  },
  {
    "title": "18.4 Decline/Sunset",
    "page_id": "18-4",
    "section": "18. Strategy by Business Lifecycle Stage",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/18-18-strategy-by-business-lifecycle-stage/18-4-18-4-decline-sunset.md"
  },
  {
    "title": "19.1 High-Consideration / High-Price Categories",
    "page_id": "19-1",
    "section": "19. Strategy by Product Category",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/19-19-strategy-by-product-category/19-1-19-1-high-consideration-high-price-categories.md"
  },
  {
    "title": "19.2 Low-Price / Impulse Categories",
    "page_id": "19-2",
    "section": "19. Strategy by Product Category",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/19-19-strategy-by-product-category/19-2-19-2-low-price-impulse-categories.md"
  },
  {
    "title": "19.3 Seasonal/Gift Categories",
    "page_id": "19-3",
    "section": "19. Strategy by Product Category",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/19-19-strategy-by-product-category/19-3-19-3-seasonal-gift-categories.md"
  },
  {
    "title": "19.4 Regulated Categories",
    "page_id": "19-4",
    "section": "19. Strategy by Product Category",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/19-19-strategy-by-product-category/19-4-19-4-regulated-categories.md"
  },
  {
    "title": "20.1 Prime Day Playbook",
    "page_id": "20-1",
    "section": "20. Seasonal & Event Planning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/20-20-seasonal-and-event-planning/20-1-20-1-prime-day-playbook.md"
  },
  {
    "title": "20.2 Q4 / Holiday Playbook",
    "page_id": "20-2",
    "section": "20. Seasonal & Event Planning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/20-20-seasonal-and-event-planning/20-2-20-2-q4-holiday-playbook.md"
  },
  {
    "title": "20.3 Other Key Dates",
    "page_id": "20-3",
    "section": "20. Seasonal & Event Planning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/20-20-seasonal-and-event-planning/20-3-20-3-other-key-dates.md"
  },
  {
    "title": "21.1 Marketplace Differences",
    "page_id": "21-1",
    "section": "21. International & Multi-Marketplace PPC",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-1-21-1-marketplace-differences.md"
  },
  {
    "title": "21.2 Cross-Marketplace Account Structure",
    "page_id": "21-2",
    "section": "21. International & Multi-Marketplace PPC",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-2-21-2-cross-marketplace-account-structure.md"
  },
  {
    "title": "21.3 Localization Considerations",
    "page_id": "21-3",
    "section": "21. International & Multi-Marketplace PPC",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/21-21-international-and-multi-marketplace-ppc/21-3-21-3-localization-considerations.md"
  },
  {
    "title": "22.1 Team Roles & RACI",
    "page_id": "22-1",
    "section": "22. Agency & Team Operations",
    "learner_level": "Foundational",
    "topic_tags": [
      "operations"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/22-22-agency-and-team-operations/22-1-22-1-team-roles-and-raci.md"
  },
  {
    "title": "22.2 SOPs & Workflow Documentation",
    "page_id": "22-2",
    "section": "22. Agency & Team Operations",
    "learner_level": "Foundational",
    "topic_tags": [
      "operations"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/22-22-agency-and-team-operations/22-2-22-2-sops-and-workflow-documentation.md"
  },
  {
    "title": "22.3 VA Training & Enablement",
    "page_id": "22-3",
    "section": "22. Agency & Team Operations",
    "learner_level": "Foundational",
    "topic_tags": [
      "operations"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/22-22-agency-and-team-operations/22-3-22-3-va-training-and-enablement.md"
  },
  {
    "title": "22.4 QA & Review Process",
    "page_id": "22-4",
    "section": "22. Agency & Team Operations",
    "learner_level": "Foundational",
    "topic_tags": [
      "operations"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/22-22-agency-and-team-operations/22-4-22-4-qa-and-review-process.md"
  },
  {
    "title": "23.1 Reporting Cadence",
    "page_id": "23-1",
    "section": "23. Client & Stakeholder Communication",
    "learner_level": "Foundational",
    "topic_tags": [
      "communication",
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/23-23-client-and-stakeholder-communication/23-1-23-1-reporting-cadence.md"
  },
  {
    "title": "23.2 Setting Expectations",
    "page_id": "23-2",
    "section": "23. Client & Stakeholder Communication",
    "learner_level": "Foundational",
    "topic_tags": [
      "communication"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/23-23-client-and-stakeholder-communication/23-2-23-2-setting-expectations.md"
  },
  {
    "title": "23.3 Handling Difficult Conversations",
    "page_id": "23-3",
    "section": "23. Client & Stakeholder Communication",
    "learner_level": "Foundational",
    "topic_tags": [
      "communication"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/23-23-client-and-stakeholder-communication/23-3-23-3-handling-difficult-conversations.md"
  },
  {
    "title": "24.1 Advertising Policy Basics",
    "page_id": "24-1",
    "section": "24. Compliance, Policy & Account Health",
    "learner_level": "Advanced",
    "topic_tags": [
      "policy"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/24-24-compliance-policy-and-account-health/24-1-24-1-advertising-policy-basics.md"
  },
  {
    "title": "24.2 Account Health Interplay",
    "page_id": "24-2",
    "section": "24. Compliance, Policy & Account Health",
    "learner_level": "Advanced",
    "topic_tags": [
      "policy"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/24-24-compliance-policy-and-account-health/24-2-24-2-account-health-interplay.md"
  },
  {
    "title": "24.3 Competitor & Ethical Boundaries",
    "page_id": "24-3",
    "section": "24. Compliance, Policy & Account Health",
    "learner_level": "Advanced",
    "topic_tags": [
      "policy"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/24-24-compliance-policy-and-account-health/24-3-24-3-competitor-and-ethical-boundaries.md"
  },
  {
    "title": "25.1 Retail Media Network Trends",
    "page_id": "25-1",
    "section": "25. Advanced & Emerging Topics",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/25-25-advanced-and-emerging-topics/25-1-25-1-retail-media-network-trends.md"
  },
  {
    "title": "25.2 AI's Growing Role in Amazon Ads",
    "page_id": "25-2",
    "section": "25. Advanced & Emerging Topics",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/25-25-advanced-and-emerging-topics/25-2-25-2-ai-s-growing-role-in-amazon-ads.md"
  },
  {
    "title": "25.3 Privacy & Signal Loss",
    "page_id": "25-3",
    "section": "25. Advanced & Emerging Topics",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/25-25-advanced-and-emerging-topics/25-3-25-3-privacy-and-signal-loss.md"
  },
  {
    "title": "26.1 Certifications",
    "page_id": "26-1",
    "section": "26. Career, Certification & Learning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/26-26-career-certification-and-learning/26-1-26-1-certifications.md"
  },
  {
    "title": "26.2 Career Pathing",
    "page_id": "26-2",
    "section": "26. Career, Certification & Learning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/26-26-career-certification-and-learning/26-2-26-2-career-pathing.md"
  },
  {
    "title": "26.3 Continuing Education",
    "page_id": "26-3",
    "section": "26. Career, Certification & Learning",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/26-26-career-certification-and-learning/26-3-26-3-continuing-education.md"
  },
  {
    "title": "27.1 Case Study Template",
    "page_id": "27-1",
    "section": "27. Case Studies & Templates",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/27-27-case-studies-and-templates/27-1-27-1-case-study-template.md"
  },
  {
    "title": "27.2 Downloadable Templates",
    "page_id": "27-2",
    "section": "27. Case Studies & Templates",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates.md"
  },
  {
    "title": "27.3 Real Case Studies",
    "page_id": "27-3",
    "section": "27. Case Studies & Templates",
    "learner_level": "Advanced",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/27-27-case-studies-and-templates/27-3-27-3-real-case-studies.md"
  },
  {
    "title": "30. Meta / Changelog",
    "page_id": "30",
    "section": "30. Meta / Changelog",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/30-30-meta-changelog/30-30-meta-changelog.md"
  },
  {
    "title": "31.1 Learning Aid",
    "page_id": "31-1",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-1-31-1-learning-aid.md"
  },
  {
    "title": "31.2 Quiz",
    "page_id": "31-2",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-2-31-2-quiz.md"
  },
  {
    "title": "31.3 Teaching Guide",
    "page_id": "31-3",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-3-31-3-teaching-guide.md"
  },
  {
    "title": "31.4 Handout",
    "page_id": "31-4",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-4-31-4-handout.md"
  },
  {
    "title": "31.5 Tagging & Assembly System",
    "page_id": "31-5",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-5-31-5-tagging-and-assembly-system.md"
  },
  {
    "title": "31.6 Rollout Priority",
    "page_id": "31-6",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-6-31-6-rollout-priority.md"
  },
  {
    "title": "31.7 Assessment & Certification Tie-In",
    "page_id": "31-7",
    "section": "31. Training Layer Template",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/31-31-training-layer-template/31-7-31-7-assessment-and-certification-tie-in.md"
  },
  {
    "title": "32.1 Content-as-Data Separation",
    "page_id": "32-1",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-1-32-1-content-as-data-separation.md"
  },
  {
    "title": "32.2 Standardized Schemas",
    "page_id": "32-2",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-2-32-2-standardized-schemas.md"
  },
  {
    "title": "32.3 Simulator Scenario Bank",
    "page_id": "32-3",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-3-32-3-simulator-scenario-bank.md"
  },
  {
    "title": "32.4 Asset Library with Naming Convention",
    "page_id": "32-4",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-4-32-4-asset-library-with-naming-convention.md"
  },
  {
    "title": "32.5 Content Versioning & Sync Contract",
    "page_id": "32-5",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-5-32-5-content-versioning-and-sync-contract.md"
  },
  {
    "title": "32.6 API/Export Layer",
    "page_id": "32-6",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-6-32-6-api-export-layer.md"
  },
  {
    "title": "32.7 Difficulty & Progression Graph",
    "page_id": "32-7",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-7-32-7-difficulty-and-progression-graph.md"
  },
  {
    "title": "32.8 Multi-Consumer Design",
    "page_id": "32-8",
    "section": "32. App-Building Layer",
    "learner_level": "Foundational",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/32-32-app-building-layer/32-8-32-8-multi-consumer-design.md"
  },
  {
    "title": "A. PPC Diagnostic Framework",
    "page_id": "playbook-a",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-a-a-ppc-diagnostic-framework.md"
  },
  {
    "title": "B. Search Term Mining SOP",
    "page_id": "playbook-b",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop.md"
  },
  {
    "title": "C. Bid and Budget Decision Matrix",
    "page_id": "playbook-c",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "bidding",
      "budget"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-c-c-bid-and-budget-decision-matrix.md"
  },
  {
    "title": "D. New Product Launch Blueprint",
    "page_id": "playbook-d",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "launch"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint.md"
  },
  {
    "title": "E. Client Reporting Narrative Builder",
    "page_id": "playbook-e",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "communication",
      "reporting"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-e-e-client-reporting-narrative-builder.md"
  },
  {
    "title": "F. Bulk Upload and Change QA Checklist",
    "page_id": "playbook-f",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist.md"
  },
  {
    "title": "G. Wiki-to-App Data Schemas",
    "page_id": "playbook-g",
    "section": "Deep Operational Playbooks",
    "learner_level": "Applied",
    "topic_tags": [
      "amazon-ppc"
    ],
    "delivery_format": [
      "self-paced",
      "instructor-led"
    ],
    "estimated_time_minutes": 15,
    "owner": "PPC Training Team",
    "review_cycle": "Quarterly",
    "last_verified_against_live_console": null,
    "source_doc": "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx",
    "status": "draft-ready",
    "path": "sections/zz-deep-operational-playbooks/playbook-g-g-wiki-to-app-data-schemas.md"
  }
]
```

---

## File: `data/prerequisites.json`

```json
[
  {
    "topic_id": "0-1",
    "prerequisite_ids": []
  },
  {
    "topic_id": "0-2",
    "prerequisite_ids": []
  },
  {
    "topic_id": "0-3",
    "prerequisite_ids": []
  },
  {
    "topic_id": "1-1",
    "prerequisite_ids": []
  },
  {
    "topic_id": "1-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "1-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "1-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "2-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "2-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "2-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "2-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-5",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "3-6",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "4-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "4-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "4-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "4-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "5-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "5-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "5-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "5-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "6-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "6-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "6-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "6-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "7-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "7-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "7-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "8-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "8-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "9-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "9-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "9-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "10-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "10-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "10-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "10-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "11-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "11-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "11-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "11-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "12-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "12-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "12-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "13-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "13-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "13-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "13-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "14-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "14-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "14-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "15-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "15-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "15-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "15-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "16-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "16-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "16-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "16-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "17-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "17-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "17-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "17-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "18-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "18-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "18-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "18-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "19-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "19-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "19-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "19-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "20-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "20-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "20-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "21-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "21-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "21-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "22-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "22-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "22-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "22-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "23-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "23-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "23-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "24-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "24-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "24-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "25-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "25-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "25-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "26-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "26-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "26-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "27-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "27-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "27-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "30",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-5",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-6",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "31-7",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-1",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-2",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-3",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-4",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-5",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-6",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-7",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "32-8",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-a",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-b",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-c",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-d",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-e",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-f",
    "prerequisite_ids": [
      "1-1"
    ]
  },
  {
    "topic_id": "playbook-g",
    "prerequisite_ids": [
      "1-1"
    ]
  }
]
```

---

## File: `data/quizzes.sample.json`

```json
[
  {
    "id": "quiz-4-1-1",
    "topic_tag": [
      "match-types"
    ],
    "difficulty": "L1",
    "question": "Which match type usually gives the most impressions?",
    "options": [
      "Exact Match",
      "Phrase Match",
      "Broad Match",
      "Negative Exact"
    ],
    "correct_answer": "Broad Match",
    "explanation": "Broad match can trigger for the widest range of related search terms."
  },
  {
    "id": "quiz-10-1-1",
    "topic_tag": [
      "metrics"
    ],
    "difficulty": "L1",
    "question": "What does ACOS measure?",
    "options": [
      "Ad spend divided by ad sales",
      "Total sales divided by clicks",
      "Clicks divided by impressions",
      "Orders divided by clicks"
    ],
    "correct_answer": "Ad spend divided by ad sales",
    "explanation": "ACOS tells you ad efficiency against ad-attributed revenue."
  },
  {
    "id": "quiz-5-3-1",
    "topic_tag": [
      "harvesting"
    ],
    "difficulty": "L2",
    "question": "After moving a winning search term from Broad to Exact, what should you usually do in the source campaign?",
    "options": [
      "Increase broad bid",
      "Add it as Negative Exact",
      "Pause the whole campaign",
      "Delete the search term report"
    ],
    "correct_answer": "Add it as Negative Exact",
    "explanation": "This helps prevent duplicate spend and keeps the source campaign focused on discovery."
  },
  {
    "id": "quiz-7-2-1",
    "topic_tag": [
      "budget-pacing"
    ],
    "difficulty": "L2",
    "question": "A campaign runs out of budget by 10 AM. What is the safest first diagnostic step?",
    "options": [
      "Double budget immediately",
      "Check ACOS, terms, inventory, and bids",
      "Pause all keywords",
      "Switch to DSP"
    ],
    "correct_answer": "Check ACOS, terms, inventory, and bids",
    "explanation": "Running out of budget is only good if the spend is efficient and supported by inventory."
  }
]
```

---

## File: `data/scenarios.sample.json`

```json
[
  {
    "scenario_id": "scenario-broad-waste",
    "topic_tags": [
      "negative-keywords",
      "search-term-mining"
    ],
    "campaign_type": "Sponsored Products Broad",
    "starting_state": {
      "budget": 100,
      "keyword": "running shoes",
      "spend": 75,
      "orders": 3,
      "acos": 45
    },
    "problem": "Irrelevant searches are spending budget.",
    "correct_actions": [
      "Download Search Term Report",
      "Add irrelevant terms as negatives",
      "Harvest converting terms",
      "Review bids after enough data"
    ],
    "common_mistakes": [
      "Pausing the whole campaign too early",
      "Increasing bids despite weak terms",
      "Negating proven terms"
    ],
    "scoring_rubric": {
      "diagnosis": 30,
      "negatives": 35,
      "harvesting": 20,
      "documentation": 15
    }
  },
  {
    "scenario_id": "scenario-budget-starvation",
    "topic_tags": [
      "budget",
      "pacing"
    ],
    "campaign_type": "Sponsored Products Exact",
    "starting_state": {
      "budget": 50,
      "spend_time": "budget exhausted by 10 AM",
      "acos": 18,
      "target_acos": 25
    },
    "problem": "A profitable campaign cannot stay live all day.",
    "correct_actions": [
      "Confirm inventory and margin",
      "Increase budget or reallocate from weak campaigns",
      "Monitor placement CPC",
      "Log the budget change"
    ],
    "common_mistakes": [
      "Ignoring inventory",
      "Increasing bids instead of budget",
      "Moving budget from another profitable campaign without checking"
    ],
    "scoring_rubric": {
      "profit_check": 30,
      "budget_action": 30,
      "risk_check": 25,
      "documentation": 15
    }
  }
]
```

---

## File: `docs/app-layer/index.md`

```markdown
---
title: "App-Building Layer"
page_type: hub
---

# App-Building Layer

This wiki is structured so apps can consume it. Store human-readable pages in `docs/`, machine-readable records in `data/`, and validation rules in `schemas/`.

Consumers can include a Console Simulator, quiz app, interview lab, reporting assistant, and onboarding LMS.
```

---

## File: `docs/appendix/formulas-calculators.md`

```markdown
---
title: "Formula Appendix"
page_type: reference
---

# Formula Appendix

## ACOS

**Formula:** `Ad Spend / Ad Sales`

**Example:** $200 spend / $1,000 ad sales = 20% ACOS

## ROAS

**Formula:** `Ad Sales / Ad Spend`

**Example:** $1,000 ad sales / $200 spend = 5.0 ROAS

## TACOS

**Formula:** `Ad Spend / Total Sales`

**Example:** $200 spend / $2,000 total sales = 10% TACOS

## Break-even ACOS

**Formula:** `Gross Margin %`

**Example:** If margin is 35%, break-even ACOS is about 35% before other costs.

## Target CPC

**Formula:** `Price x Target ACOS x Conversion Rate`

**Example:** $20 price x 25% target ACOS x 10% CVR = $0.50 target CPC
```

---

## File: `docs/complete-data-filled-guide.md`

```markdown
---
title: Complete Data-Filled Guide
---

# The Amazon PPC Wiki — Complete Data-Filled Guide

This page is the consolidated source page for the new beginner-friendly data added across the wiki section pages. The same material is split into the numbered section pages under `docs/sections`.

## Section 0
## Merged beginner guide content

This wiki is the operating manual for learning Amazon PPC from zero. It is written for fresh graduates, virtual assistants, junior strategists, brand owners, and agency teams. A new learner should start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. Operators who need a quick win should jump to [[9. Negative Keywords & Negation Strategy]] because wasted spend is often the fastest thing to fix.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

## Section 1
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

## Section 2
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

## Section 3
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

## Section 4
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

## Section 5
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

## Section 6
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

## Section 7
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

## Section 8
## Complete data-filled section notes

Placement optimization controls where your ads appear. The three main Sponsored Products placements are Top of Search, Rest of Search, and Product Detail Pages.

| Placement | Typical behavior | Operator note |
|---|---|---|
| Top of Search | High visibility, high CPC, often high CVR | Worth bidding up only when efficient |
| Rest of Search | Middle ground | Often stable and scalable |
| Product Detail Pages | Lower intent, cheaper clicks | Useful for conquesting and cross-sell |

### Diagnosis workflow

1. Pull the Placement Report.
2. Compare ACOS, CTR, CVR, CPC, and sales by placement.
3. Increase modifier where ACOS is below target and volume is limited.
4. Reduce modifier where CPC is high and CVR is weak.
5. Recheck after enough data, not the next morning.

### Worked example

If Top of Search ACOS is 25%, Rest of Search is 35%, and Product Pages is 45%, increase Top of Search modestly, leave Rest alone, and reduce Product Pages or keep it conservative.

## Section 9
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

## Section 10
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

## Section 11
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

## Section 12
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

## Section 13
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

## Section 14
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

## Section 15
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

## Section 16
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

## Section 17
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

## Section 18
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

## Section 19
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

## Section 20
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

## Section 21
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

## Section 22
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

## Section 23
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

## Section 24
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

## Section 25
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

## Section 26
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

## Section 27
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

## Section 28
## Complete data-filled section notes

The glossary is the beginner's decoder ring. Every acronym should have a short definition, long definition, related terms, and first appearance.

### Core acronyms

| Term | Meaning |
|---|---|
| ACOS | Advertising Cost of Sales: Spend / Ad Sales |
| TACOS | Total Advertising Cost of Sales: Spend / Total Sales |
| ROAS | Return on Ad Spend: Ad Sales / Spend |
| CTR | Click-Through Rate: Clicks / Impressions |
| CVR | Conversion Rate: Orders / Clicks |
| CPC | Cost Per Click: Spend / Clicks |
| SP | Sponsored Products |
| SB | Sponsored Brands |
| SD | Sponsored Display |
| STV | Sponsored TV |
| DSP | Demand Side Platform |
| AMC | Amazon Marketing Cloud |
| SQP | Search Query Performance |

### Beginner rule

Define every acronym the first time it appears on a page. Do not make a fresh graduate play acronym bingo.

## Section 29
## Complete data-filled section notes

Formulas turn PPC into controllable math. Every calculator should show inputs, formula, example, and interpretation.

### Key formulas

`ACOS = Ad Spend / Ad Sales`

`ROAS = Ad Sales / Ad Spend`

`TACOS = Ad Spend / Total Sales`

`Break-even ACOS = Gross Profit / Price`

`Target Bid = Price x Conversion Rate x Target ACOS`

### Harvesting rule starter

Harvest a search term when it has enough clicks, enough orders, and ACOS at or below target. A starter rule is 50+ clicks, 5+ orders, and ACOS under target, but the threshold should change by price, category, and conversion rate.

## Section 30
## Complete data-filled section notes

The changelog protects trust. Amazon changes features, policies, reports, and console layouts often. Track changes so learners know what is current.

### Version history example

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-07-05 | Merged complete data-filled guide into section pages |
| 2.4 | 2026-07-05 | Added complete sections, examples, and schemas |
| 2.0 | 2026-01-01 | Major rewrite and training layer added |
| 1.0 | 2025-07-01 | Initial version |

### Update policy

Every page that describes a live console workflow should include a verification date. If unsure, tag it `[Stale?]` and assign review.

## Section 31
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

## Section 32
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.
```

---

## File: `docs/glossary/index.md`

```markdown
---
title: "Glossary & Acronyms"
page_type: hub
---

# Glossary & Acronyms

## ACOS

Advertising Cost of Sales. Ad spend divided by ad-attributed sales. Use it to judge ad efficiency.

Related pages: search this repo for `[[ACOS]]`.

## TACOS

Total Advertising Cost of Sales. Ad spend divided by total sales. Use it to judge business-level ad impact.

Related pages: search this repo for `[[TACOS]]`.

## ROAS

Return on Ad Spend. Ad sales divided by ad spend. Higher is usually better.

Related pages: search this repo for `[[ROAS]]`.

## CTR

Click-through rate. Clicks divided by impressions. It tells you if shoppers are interested enough to click.

Related pages: search this repo for `[[CTR]]`.

## CVR

Conversion rate. Orders divided by clicks. It tells you if shoppers buy after clicking.

Related pages: search this repo for `[[CVR]]`.

## CPC

Cost per click. Ad spend divided by clicks.

Related pages: search this repo for `[[CPC]]`.

## SP

Sponsored Products. Ads for individual products on Amazon.

Related pages: search this repo for `[[SP]]`.

## SB

Sponsored Brands. Brand-focused ads that may show product collection, store spotlight, or video creative.

Related pages: search this repo for `[[SB]]`.

## SD

Sponsored Display. Display ads using contextual or audience targeting.

Related pages: search this repo for `[[SD]]`.

## DSP

Demand Side Platform. Amazon programmatic ads for display, video, audio, OTT, retargeting, and prospecting.

Related pages: search this repo for `[[DSP]]`.

## AMC

Amazon Marketing Cloud. A clean-room analytics tool for advanced attribution and audience analysis.

Related pages: search this repo for `[[AMC]]`.

## Search Term

The actual shopper query that triggered an ad.

Related pages: search this repo for `[[Search Term]]`.

## Keyword

The word or phrase the advertiser bids on in a manual keyword campaign.

Related pages: search this repo for `[[Keyword]]`.

## Negative Keyword

A term blocked from triggering ads.

Related pages: search this repo for `[[Negative Keyword]]`.

## Placement Modifier

A bid adjustment for placements like Top of Search or Product Pages.

Related pages: search this repo for `[[Placement Modifier]]`.

## Portfolio

A grouping container for campaigns, often used for budget or P&L organization.

Related pages: search this repo for `[[Portfolio]]`.

## Buy Box

The offer position that lets shoppers add to cart quickly. Sponsored Products generally depend on offer eligibility.

Related pages: search this repo for `[[Buy Box]]`.
```

---

## File: `docs/index.md`

```markdown
---
title: Amazon PPC Wiki
page_type: landing
version: 1.0.0
---

# The Amazon PPC Wiki

A beginner-friendly, operator-ready knowledge base for Amazon PPC training, agency operations, and future app integration.

This repo was generated from the expanded Amazon PPC Wiki manual and is designed to work as:

- a GitHub wiki-style documentation repo,
- a MkDocs static knowledge base,
- a training library for VAs and junior strategists,
- a structured data source for simulators, quizzes, and future tools.

## Start here by role

- **Beginner VA:** Start with Sections 1-4, then 5-11, then 22.
- **Junior Strategist:** Read Sections 1-11, then 14-15, 18, 22-23.
- **Senior Strategist:** Read the core sections, then 12-13, 17, 21, 25, and 32.
- **Brand Owner:** Read Sections 1, 3, 10, 14-15, 18, 20, and 23.
- **Agency Owner:** Read Sections 2, 10-11, 16-17, 22-23, 26-27, and 32.

## Repo map

- `docs/sections/` - all wiki pages as Markdown.
- `docs/glossary/` - A-Z PPC terms and acronyms.
- `docs/appendix/` - formulas, calculators, and reference material.
- `docs/training/` - learning aids, quiz model, teaching guide model, handout model.
- `docs/app-layer/` - content-as-data and simulator integration notes.
- `data/` - machine-readable page index, glossary, formulas, quizzes, scenarios, and prerequisite graph.
- `schemas/` - JSON Schemas for app-facing content.
- `templates/` - reusable wiki page, changelog, quiz, and scenario templates.
- `scripts/` - validation and export helpers.

## Naming convention

Every page should keep these fields in YAML frontmatter:

``​`yaml
page_id: "1-1"
title: "What is Amazon PPC"
learner_level: "Foundational"
topic_tags: ["amazon-ppc", "foundations"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
``​`

## Local preview

``​`bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
``​`

Open the local URL MkDocs prints in your terminal.
```

---

## File: `docs/sections/00-0-front-matter/0-1-0-1-home-landing-page.md`

```markdown
---
title: "0.1 Home / Landing Page"
page_id: "0-1"
section: "0. Front Matter"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 0.1 Home / Landing Page

**What this page teaches:** This is the front door of the wiki. It tells a new reader what Amazon PPC is, who the wiki is for, and where to start based on role.

**Explain it to a fresh graduate:** A fresh graduate should not start with bidding formulas. Start with the map. Think of this page like the reception desk in a big office building.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Add role paths: Beginner VA, Junior Strategist, Senior Strategist, Brand Owner, Agency Owner. Put the link map here and update the version log every time the wiki changes.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Merged beginner guide content

This wiki is the operating manual for learning Amazon PPC from zero. It is written for fresh graduates, virtual assistants, junior strategists, brand owners, and agency teams. A new learner should start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. Operators who need a quick win should jump to [[9. Negative Keywords & Negation Strategy]] because wasted spend is often the fastest thing to fix.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/00-0-front-matter/0-2-0-2-how-to-use-this-wiki.md`

```markdown
---
title: "0.2 How to Use This Wiki"
page_id: "0-2"
section: "0. Front Matter"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 0.2 How to Use This Wiki

**What this page teaches:** This page explains reading order, notation, examples, and where to find definitions.

**Explain it to a fresh graduate:** New people get lost when every page uses abbreviations. Put [[Glossary]] and [[Formula Appendix]] up front so nobody has to pretend they know what [[TACOS]] means.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use a suggested order: Foundations, Campaign Types, Targeting, Keywords, Bidding, Budgets, Metrics, Reporting, then advanced topics.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Merged beginner guide content

This wiki is the operating manual for learning Amazon PPC from zero. It is written for fresh graduates, virtual assistants, junior strategists, brand owners, and agency teams. A new learner should start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. Operators who need a quick win should jump to [[9. Negative Keywords & Negation Strategy]] because wasted spend is often the fastest thing to fix.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/00-0-front-matter/0-3-0-3-contributor-maintenance-guide.md`

```markdown
---
title: "0.3 Contributor / Maintenance Guide"
page_id: "0-3"
section: "0. Front Matter"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 0.3 Contributor / Maintenance Guide

**What this page teaches:** This explains how team members add, review, update, and retire pages.

**Explain it to a fresh graduate:** Amazon changes often. A stale PPC wiki is like a map with old roads. It still looks official, but it gets people lost.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use page owners, review dates, stale flags, and an approval checklist. Add a changelog template for every update.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Merged beginner guide content

This wiki is the operating manual for learning Amazon PPC from zero. It is written for fresh graduates, virtual assistants, junior strategists, brand owners, and agency teams. A new learner should start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. Operators who need a quick win should jump to [[9. Negative Keywords & Negation Strategy]] because wasted spend is often the fastest thing to fix.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/00-0-front-matter/index.md`

```markdown
---
title: "0. Front Matter"
page_type: section_overview
section_id: "0"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 0. Front Matter

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[0.1 Home / Landing Page]]
- [[0.2 How to Use This Wiki]]
- [[0.3 Contributor / Maintenance Guide]]

---

## Merged from Complete Data-Filled Guide
## Merged beginner guide content

This wiki is the operating manual for learning Amazon PPC from zero. It is written for fresh graduates, virtual assistants, junior strategists, brand owners, and agency teams. A new learner should start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. Operators who need a quick win should jump to [[9. Negative Keywords & Negation Strategy]] because wasted spend is often the fastest thing to fix.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md`

```markdown
---
title: "1.1 What is Amazon PPC"
page_id: "1-1"
section: "1. Foundations & Fundamentals"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 1.1 What is Amazon PPC

**What this page teaches:** Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks your ad, not simply when the ad appears.

**Explain it to a fresh graduate:** Imagine placing your product on a shelf near the entrance of a store. You pay only when someone picks up the product to inspect it. PPC helps products get seen while organic ranking is still growing.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Teach the flywheel: paid clicks can create sales; sales can help ranking; ranking can create more organic sales; better conversion makes ads cheaper to run.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

### Data-filled beginner explanation

Amazon PPC is Amazon's advertising system where the seller pays only after a shopper clicks. It is useful because it creates immediate visibility, gathers search-term data, and can support organic ranking when paid sales help the product gain momentum.

### Auction analogy

Think of it as a silent auction for shelf space. Sellers bid for visibility, but Amazon also considers relevance and conversion likelihood. A higher bid helps, but a bad fit can still lose.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.md`

```markdown
---
title: "1.2 The Amazon Advertising Ecosystem"
page_id: "1-2"
section: "1. Foundations & Fundamentals"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 1.2 The Amazon Advertising Ecosystem

**What this page teaches:** Amazon Ads includes the Ads Console, Seller Central or Vendor Central access, ad products, reports, API access, and learning resources.

**Explain it to a fresh graduate:** Seller Central is usually for third-party sellers. Vendor Central is usually for brands selling wholesale to Amazon. The Ads Console is where campaigns are built and managed.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Show the account access flow: login, account switcher, campaign manager, reports, brand store, billing, permissions.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

### Data table

| Area | Beginner explanation |
|---|---|
| Seller Central | Used by third-party sellers who sell on Amazon's marketplace |
| Vendor Central | Used by first-party suppliers that sell wholesale to Amazon |
| Advertising Console | Main place to create, manage, and report on ads |
| Ads API | Programmatic access for tools, scripts, and automation |

| Ad type | Shows | Best for |
|---|---|---|
| Sponsored Products | Search and product pages | Direct sales |
| Sponsored Brands | Top search and brand placements | Brand visibility |
| Sponsored Display | Amazon and external placements | Remarketing and audiences |
| DSP | Amazon and external inventory | Advanced full-funnel advertising |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md`

```markdown
---
title: "1.3 Core Terminology Primer"
page_id: "1-3"
section: "1. Foundations & Fundamentals"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 1.3 Core Terminology Primer

**What this page teaches:** This page introduces basic words like impressions, clicks, [[CTR]], [[CVR]], [[CPC]], [[ACOS]], [[TACOS]], [[ROAS]], campaign, ad group, keyword, and target.

**Explain it to a fresh graduate:** Do not memorize everything at once. Learn the hierarchy first: campaign is the folder, ad group is the subfolder, target is what tells Amazon where to show the ad.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Link every term to [[Glossary]]. Add tiny examples: 1,000 impressions, 20 clicks, 2 orders means 2% [[CTR]] and 10% [[CVR]].

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

### Metrics starter pack

- Impressions: how many times the ad showed.
- Clicks: how many times shoppers clicked.
- CTR: clicks divided by impressions.
- CVR: orders divided by clicks.
- ACOS: ad spend divided by ad revenue.
- ROAS: ad revenue divided by ad spend.
- TACOS: ad spend divided by total revenue.

### Hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword/Target`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.md`

```markdown
---
title: "1.4 Eligibility & Prerequisites"
page_id: "1-4"
section: "1. Foundations & Fundamentals"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 1.4 Eligibility & Prerequisites

**What this page teaches:** Not every product can advertise. Amazon may require an active account, eligible listings, Featured Offer or Buy Box eligibility, Brand Registry for some ad types, and good account standing.

**Explain it to a fresh graduate:** Before blaming PPC, check if the product is even allowed to show ads. Sometimes the campaign is fine and the listing is the problem.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Create a pre-flight checklist: active listing, inventory, price, shipping, Buy Box or Featured Offer, category approval, policy compliance, Brand Registry if needed.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

### Pre-flight checklist

- Professional account active.
- Buy Box active for the advertised product.
- Account health is good.
- Inventory is available.
- Brand Registry is active if using SB, SD, Brand Store, or A+ Content.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/01-1-foundations-and-fundamentals/index.md`

```markdown
---
title: "1. Foundations & Fundamentals"
page_type: section_overview
section_id: "1"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 1. Foundations & Fundamentals

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[1.1 What is Amazon PPC]]
- [[1.2 The Amazon Advertising Ecosystem]]
- [[1.3 Core Terminology Primer]]
- [[1.4 Eligibility & Prerequisites]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. For a beginner, imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

New operators often think ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.md`

```markdown
---
title: "2.1 Account Structure Philosophy"
page_id: "2-1"
section: "2. Account & Campaign Architecture"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 2.1 Account Structure Philosophy

**What this page teaches:** This defines how accounts, portfolios, campaigns, and naming conventions should be organized.

**Explain it to a fresh graduate:** Good structure makes the account easy to audit. Bad structure turns every optimization into a treasure hunt, but with worse music.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use a standard naming format such as Brand | Parent ASIN | Country | Ad Type | Strategy | Target Type | Match | Theme.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md`

```markdown
---
title: "2.2 Campaign Structuring Models"
page_id: "2-2"
section: "2. Account & Campaign Architecture"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 2.2 Campaign Structuring Models

**What this page teaches:** Campaigns can be grouped by SKU, category, match type, funnel stage, defense or offense, launch stage, and maturity stage.

**Explain it to a fresh graduate:** There is no one perfect structure. The best structure makes reporting clear and keeps budgets controlled.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Separate research from performance. Separate branded defense from non-branded growth. Separate auto, broad, phrase, exact, and product targeting when control matters.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.md`

```markdown
---
title: "2.3 Ad Group Best Practices"
page_id: "2-3"
section: "2. Account & Campaign Architecture"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 2.3 Ad Group Best Practices

**What this page teaches:** Ad groups should hold tightly related products and targets. One-theme-per-ad-group keeps data clean.

**Explain it to a fresh graduate:** If an ad group mixes baby bottles, hiking bags, and gaming keyboards, the data will be useless. Amazon may still spend, but you will not know why.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use SKAGs only when you need very tight bid and budget control. Otherwise, use small themed ad groups.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.md`

```markdown
---
title: "2.4 Portfolio & Budget Grouping"
page_id: "2-4"
section: "2. Account & Campaign Architecture"
learner_level: "Foundational"
topic_tags: ["budget"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 2.4 Portfolio & Budget Grouping

**What this page teaches:** Portfolios group campaigns for reporting and budget caps.

**Explain it to a fresh graduate:** A portfolio is like a department budget. It helps you see spend by product line, brand, season, or owner.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use portfolios for product lines, major ASIN groups, seasonal campaigns, or P&L ownership. Avoid creating too many tiny portfolios.

**Operator view:** Budgets control how much opportunity a campaign can capture. A good budget protects cash while feeding proven performers.

**Practical workflow:**
- Check whether the campaign runs out of budget.
- Separate strong campaigns from testing campaigns.
- Increase budget on campaigns with profitable or strategic performance.
- Reduce budget on campaigns that waste spend or lack strategic purpose.
- Review pacing before seasonal events.

**Worked mini-example:** A campaign with 20% [[ACOS]] and frequent budget-outs deserves review for a budget increase. A campaign with 90% [[ACOS]] and no strategic purpose needs diagnosis before more spend.

**Common beginner mistakes:**
- Giving equal budget to every campaign.
- Starving a campaign that already proves it can sell efficiently.
- Scaling spend without checking inventory and margin.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/02-2-account-and-campaign-architecture/index.md`

```markdown
---
title: "2. Account & Campaign Architecture"
page_type: section_overview
section_id: "2"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 2. Account & Campaign Architecture

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[2.1 Account Structure Philosophy]]
- [[2.2 Campaign Structuring Models]]
- [[2.3 Ad Group Best Practices]]
- [[2.4 Portfolio & Budget Grouping]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md`

```markdown
---
title: "3.1 Sponsored Products (SP)"
page_id: "3-1"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["sponsored-products"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.1 Sponsored Products (SP)

**What this page teaches:** [[Sponsored Products]] promote individual listings. They are usually the main workhorse for Amazon PPC and often send clicks to the product detail page.

**Explain it to a fresh graduate:** If Amazon ads were a team, [[Sponsored Products]] would be the reliable operations person who shows up every day with a spreadsheet.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Teach Auto, Manual Keyword, Manual Product Targeting, bidding strategies, and placements: Top of Search, Rest of Search, Product Pages.

**Operator view:** [[Sponsored Products]] are usually the daily optimization core. They are closest to conversion and product-level demand capture.

**Practical workflow:**
- Confirm advertised products are eligible and in stock.
- Choose auto, manual keyword, product targeting, or category targeting.
- Set daily budget, bid strategy, and starting bids.
- Monitor search terms, placements, budget status, and target performance.
- Harvest, negate, and adjust bids based on data.

**Worked mini-example:** A launch structure may use Auto for discovery, Broad for expansion, Exact for control, and Product Targeting for competitor and defensive placements.

**Common beginner mistakes:**
- Treating auto campaigns as set-and-forget.
- Mixing too many unrelated products in one ad group.
- Ignoring placement performance.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md`

```markdown
---
title: "3.2 Sponsored Brands (SB)"
page_id: "3-2"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["brand", "sponsored-brands"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.2 Sponsored Brands (SB)

**What this page teaches:** [[Sponsored Brands]] promote a brand using product collections, Store spotlight, or video formats. They usually need Brand Registry or vendor access.

**Explain it to a fresh graduate:** SB is less about one product only and more about making shoppers recognize the brand. It is useful for discovery, defense, video, and Store traffic.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use SB when the brand has a strong store, good creative, and products that make sense together.

**Operator view:** [[Sponsored Brands]] help shape brand discovery. They need stronger creative and a clear landing destination.

**Practical workflow:**
- Confirm Brand Registry or eligibility.
- Choose Product Collection, Store Spotlight, or Video.
- Select landing page, products, headline, and creative.
- Separate branded defense from non-branded growth.
- Review [[CTR]], [[CVR]], new-to-brand metrics, and Store impact.

**Worked mini-example:** A [[Sponsored Brands]] Video campaign can introduce a product on high-intent category keywords while Product Collection ads defend branded searches.

**Common beginner mistakes:**
- Running SB before the Store or listings are ready.
- Using generic headlines.
- Expecting every SB campaign to behave like bottom-funnel SP exact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md`

```markdown
---
title: "3.3 Sponsored Display (SD)"
page_id: "3-3"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["sponsored-display"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.3 Sponsored Display (SD)

**What this page teaches:** [[Sponsored Display]] reaches shoppers using product targeting and audience targeting such as remarketing or in-market audiences.

**Explain it to a fresh graduate:** SD is useful when you want to follow up with shoppers who viewed or considered products. Think of it as the polite reminder ad.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use SD for product detail page defense, competitor targeting, remarketing, and audience expansion.

**Operator view:** [[Sponsored Display]] supports product page defense, competitor visibility, and audience remarketing.

**Practical workflow:**
- Choose product targeting or audience targeting.
- Define defense, conquesting, remarketing, or expansion purpose.
- Check creative and product readiness.
- Start with controlled budgets.
- Review view-through and click-attributed performance carefully.

**Worked mini-example:** A brand can target its own ASINs to defend detail pages, then target competitor ASINs with better-rated or lower-priced alternatives.

**Common beginner mistakes:**
- Judging upper-funnel display only by immediate [[ACOS]].
- Targeting too broadly with small budgets.
- Using weak images or uncompetitive listings.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.md`

```markdown
---
title: "3.4 Sponsored TV / Streaming TV Ads"
page_id: "3-4"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.4 Sponsored TV / Streaming TV Ads

**What this page teaches:** Sponsored TV and streaming video help brands reach shoppers through video inventory and upper-funnel placements.

**Explain it to a fresh graduate:** This is not usually the first tool for a tiny budget. It is for awareness and brand recall, not instant keyword harvesting.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Check eligibility, creative specs, minimums, and measurement plan before recommending it.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md`

```markdown
---
title: "3.5 Amazon DSP"
page_id: "3-5"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["dsp"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.5 Amazon DSP

**What this page teaches:** [[Amazon DSP]] is a demand-side platform for programmatic display, video, audio, and streaming ads across Amazon and third-party inventory.

**Explain it to a fresh graduate:** DSP is the advanced machine. It can be powerful, but you need audience strategy, budget, creative, and measurement discipline.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use DSP when Sponsored Ads are mature and the brand needs retargeting, prospecting, or full-funnel measurement.

**Operator view:** DSP is for advanced audience strategy across display, video, audio, and streaming placements. It needs stronger planning than basic Sponsored Ads.

**Practical workflow:**
- Define audience and funnel stage.
- Confirm budget, creative, and measurement plan.
- Separate prospecting from retargeting.
- Use [[Amazon Marketing Cloud]] or reporting to evaluate overlap and path to purchase.
- Coordinate DSP learnings with Sponsored Ads strategy.

**Worked mini-example:** DSP prospecting may build audience reach while SP exact captures purchase intent. Together they can support a full-funnel plan.

**Common beginner mistakes:**
- Launching DSP without enough budget or creative.
- Comparing DSP prospecting directly against SP exact [[ACOS]].
- Ignoring frequency and audience overlap.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/3-6-3-6-cross-campaign-type-strategy.md`

```markdown
---
title: "3.6 Cross-Campaign-Type Strategy"
page_id: "3-6"
section: "3. Campaign Types"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 3.6 Cross-Campaign-Type Strategy

**What this page teaches:** This maps SP, SB, SD, STV, and DSP across the shopper journey.

**Explain it to a fresh graduate:** Different ad types do different jobs. Do not ask a hammer to cook rice.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Map campaigns by funnel: awareness, consideration, conversion, defense, retention. Budget by brand maturity and margin.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/03-3-campaign-types/index.md`

```markdown
---
title: "3. Campaign Types"
page_type: section_overview
section_id: "3"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 3. Campaign Types

This cluster contains 6 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[3.1 Sponsored Products (SP)]]
- [[3.2 Sponsored Brands (SB)]]
- [[3.3 Sponsored Display (SD)]]
- [[3.4 Sponsored TV / Streaming TV Ads]]
- [[3.5 Amazon DSP]]
- [[3.6 Cross-Campaign-Type Strategy]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type beginners learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md`

```markdown
---
title: "4.1 Keyword Match Types"
page_id: "4-1"
section: "4. Targeting & Match Types"
learner_level: "Foundational"
topic_tags: ["keywords", "targeting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 4.1 Keyword Match Types

**What this page teaches:** Broad, phrase, and exact control how closely a shopper search must match your keyword.

**Explain it to a fresh graduate:** Broad explores. Phrase narrows. Exact controls. Broad is the scout, phrase is the filter, exact is the sniper.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Run broad and phrase for discovery, then harvest proven search terms into exact campaigns.

**Operator view:** Keywords and search terms reveal shopper language. Your job is to separate discovery from control.

**Practical workflow:**
- Collect seed keywords from listings, competitors, autocomplete, tools, and reports.
- Launch discovery campaigns with controlled budgets.
- Mine search terms after enough clicks or spend.
- Promote proven terms into exact campaigns.
- Negate waste or harvested terms based on structure.

**Worked mini-example:** The keyword "beer bong" may match the search term "beer bong funnel for party." If that search term gets orders at target [[ACOS]], harvest it into exact match.

**Common beginner mistakes:**
- Confusing keyword with customer search term.
- Promoting terms too early from one lucky sale.
- Adding negatives without checking whether another campaign needs the traffic.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

### Match type quick reference

| Match type | Example keyword | Can match | Best role |
|---|---|---|---|
| Broad | running shoes | best men's running shoes sale | Discovery |
| Phrase | "running shoes" | cheap running shoes | Refinement |
| Exact | [running shoes] | running shoes | Scaling winners |

### Common mistake

Starting with only Exact Match can feel safe, but it blocks discovery. Starting with only Broad can gather data, but it can waste money without negatives.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md`

```markdown
---
title: "4.2 Product Targeting"
page_id: "4-2"
section: "4. Targeting & Match Types"
learner_level: "Foundational"
topic_tags: ["targeting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 4.2 Product Targeting

**What this page teaches:** Product targeting lets you advertise on specific ASINs or categories, including competitor products or your own product pages.

**Explain it to a fresh graduate:** Instead of targeting a word shoppers type, you target a product page they visit.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use own-ASIN targeting for defense and competitor ASIN targeting for conquesting. Use category refinements for price, rating, brand, and Prime eligibility.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md`

```markdown
---
title: "4.3 Audience Targeting"
page_id: "4-3"
section: "4. Targeting & Match Types"
learner_level: "Foundational"
topic_tags: ["targeting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 4.3 Audience Targeting

**What this page teaches:** Audience targeting uses shopper behavior signals such as views, purchases, lifestyle, or in-market interest.

**Explain it to a fresh graduate:** This is closer to saying, 'show ads to people who behaved like potential buyers,' instead of 'show ads when someone types this keyword.'

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use audience targeting in [[Sponsored Display]] and DSP for remarketing and upper-funnel expansion.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.md`

```markdown
---
title: "4.4 Auto-Targeting Categories"
page_id: "4-4"
section: "4. Targeting & Match Types"
learner_level: "Foundational"
topic_tags: ["targeting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 4.4 Auto-Targeting Categories

**What this page teaches:** Auto campaigns can use close match, loose match, substitutes, and complements.

**Explain it to a fresh graduate:** Auto campaigns let Amazon explore where your product may fit. They are helpful, but not magic. They need mining and negatives.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use auto as a discovery engine. Pull converting search terms into manual campaigns and negate waste.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/04-4-targeting-and-match-types/index.md`

```markdown
---
title: "4. Targeting & Match Types"
page_type: section_overview
section_id: "4"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 4. Targeting & Match Types

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[4.1 Keyword Match Types]]
- [[4.2 Product Targeting]]
- [[4.3 Audience Targeting]]
- [[4.4 Auto-Targeting Categories]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.md`

```markdown
---
title: "5.1 Research Methodology"
page_id: "5-1"
section: "5. Keyword Research & Search Term Mining"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 5.1 Research Methodology

**What this page teaches:** Keyword research finds how customers search. Sources include brainstorming, competitor listings, autocomplete, search term reports, reverse ASIN tools, and Brand Analytics.

**Explain it to a fresh graduate:** Do not start with what the brand calls the product. Start with what customers type when they want to buy it.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build a seed list, expand it, score relevance, group by intent, then map keywords to campaigns.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.md`

```markdown
---
title: "5.2 Keyword Research Tools"
page_id: "5-2"
section: "5. Keyword Research & Search Term Mining"
learner_level: "Foundational"
topic_tags: ["keywords", "tools"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 5.2 Keyword Research Tools

**What this page teaches:** Tools like Helium 10, Data Dive, Brand Analytics, and Amazon reports help find keyword opportunities.

**Explain it to a fresh graduate:** Tools do not replace judgment. A keyword with volume but weak relevance can burn money very efficiently. Fancy bonfire, still a bonfire.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use tools to collect data, then human review to judge relevance, intent, and campaign fit.

**Operator view:** Keywords and search terms reveal shopper language. Your job is to separate discovery from control.

**Practical workflow:**
- Collect seed keywords from listings, competitors, autocomplete, tools, and reports.
- Launch discovery campaigns with controlled budgets.
- Mine search terms after enough clicks or spend.
- Promote proven terms into exact campaigns.
- Negate waste or harvested terms based on structure.

**Worked mini-example:** The keyword "beer bong" may match the search term "beer bong funnel for party." If that search term gets orders at target [[ACOS]], harvest it into exact match.

**Common beginner mistakes:**
- Confusing keyword with customer search term.
- Promoting terms too early from one lucky sale.
- Adding negatives without checking whether another campaign needs the traffic.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.md`

```markdown
---
title: "5.3 Search Term Harvesting Workflow"
page_id: "5-3"
section: "5. Keyword Research & Search Term Mining"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 5.3 Search Term Harvesting Workflow

**What this page teaches:** Harvesting means moving search terms that prove performance into stronger manual control, usually exact match.

**Explain it to a fresh graduate:** If a search term makes sales, promote it. If it wastes spend, negate it. That is the heartbeat of PPC operations.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use rules such as: promote terms with orders and acceptable [[ACOS]]; negate terms with enough clicks and zero sales; review before applying.

**Operator view:** Keywords and search terms reveal shopper language. Your job is to separate discovery from control.

**Practical workflow:**
- Collect seed keywords from listings, competitors, autocomplete, tools, and reports.
- Launch discovery campaigns with controlled budgets.
- Mine search terms after enough clicks or spend.
- Promote proven terms into exact campaigns.
- Negate waste or harvested terms based on structure.

**Worked mini-example:** The keyword "beer bong" may match the search term "beer bong funnel for party." If that search term gets orders at target [[ACOS]], harvest it into exact match.

**Common beginner mistakes:**
- Confusing keyword with customer search term.
- Promoting terms too early from one lucky sale.
- Adding negatives without checking whether another campaign needs the traffic.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

### Harvesting SOP

1. Launch Auto and Broad campaigns.
2. Let data collect for 2 to 4 weeks, depending on spend.
3. Download the Search Term Report.
4. Promote terms with 50+ clicks, 5+ orders, and ACOS below target.
5. Add those terms to Exact campaigns.
6. Add them as Negative Exact in the source campaign.
7. Increase bids only after the Exact campaign proves itself.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.md`

```markdown
---
title: "5.4 Long-Tail vs. Head Term Strategy"
page_id: "5-4"
section: "5. Keyword Research & Search Term Mining"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 5.4 Long-Tail vs. Head Term Strategy

**What this page teaches:** Head terms are short and high-volume. Long-tail terms are longer, more specific, and often cheaper or more conversion-friendly.

**Explain it to a fresh graduate:** 'Shoes' is a head term. 'women waterproof hiking shoes size 8' is long-tail. The second tells you much more about buyer intent.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Bid more carefully on head terms. Use long-tail terms for efficient scaling and cleaner search intent.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/05-5-keyword-research-and-search-term-mining/index.md`

```markdown
---
title: "5. Keyword Research & Search Term Mining"
page_type: section_overview
section_id: "5"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 5. Keyword Research & Search Term Mining

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[5.1 Research Methodology]]
- [[5.2 Keyword Research Tools]]
- [[5.3 Search Term Harvesting Workflow]]
- [[5.4 Long-Tail vs. Head Term Strategy]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Keyword research is how you learn the language customers use. A beginner should not guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md`

```markdown
---
title: "6.1 Manual Bidding Fundamentals"
page_id: "6-1"
section: "6. Bidding Strategies & Bid Management"
learner_level: "Foundational"
topic_tags: ["bidding"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 6.1 Manual Bidding Fundamentals

**What this page teaches:** Bids decide how much you are willing to pay for a click. Formulas help keep bids aligned with price, conversion rate, and target [[ACOS]].

**Explain it to a fresh graduate:** A bid is not a guess. It should connect to what a click is worth. If every sale gives little profit, you cannot bid like a billionaire raccoon.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use [[CPC]] max = Price x Target [[ACOS]] x Conversion Rate. Compare to Amazon suggested bids, then start conservatively when data is limited.

**Operator view:** Bids control how aggressively you enter auctions. Bid changes should follow evidence, not mood, caffeine, or panic.

**Practical workflow:**
- Confirm the target [[ACOS]] or [[ROAS]].
- Calculate a safe [[CPC]] from price, conversion rate, and target [[ACOS]].
- Check clicks, orders, spend, and placement before changing the bid.
- Increase bids only where relevance and conversion justify more traffic.
- Decrease bids where spend is inefficient but the target is still relevant.

**Worked mini-example:** If price is $20, target [[ACOS]] is 25%, and [[CVR]] is 10%, the target [[CPC]] is $20 x 25% x 10% = $0.50. A $1.20 bid may be too aggressive unless conversion is much higher.

**Common beginner mistakes:**
- Raising bids on keywords with weak conversion.
- Cutting bids too early before enough clicks exist.
- Ignoring placement modifiers that may be causing high [[CPC]].

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

### Bid calculation example

If price is $50, conversion rate is 10%, and target ACOS is 25%, target bid is:

`$50 x 0.10 x 0.25 = $1.25`

This means paying much more than $1.25 per click may push ACOS above target unless CVR or price improves.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md`

```markdown
---
title: "6.2 Dynamic & Rule-Based Bidding"
page_id: "6-2"
section: "6. Bidding Strategies & Bid Management"
learner_level: "Foundational"
topic_tags: ["bidding"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 6.2 Dynamic & Rule-Based Bidding

**What this page teaches:** Amazon can adjust bids using dynamic bids down only, up and down, or fixed bids. Tools can also automate bid changes with rules.

**Explain it to a fresh graduate:** Dynamic bidding means Amazon may lower or raise bids depending on estimated conversion chance. It is helpful, but it should not replace account strategy.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use Down Only for controlled testing, Up and Down for proven high-converting campaigns, Fixed when you need strict control.

**Operator view:** Bids control how aggressively you enter auctions. Bid changes should follow evidence, not mood, caffeine, or panic.

**Practical workflow:**
- Confirm the target [[ACOS]] or [[ROAS]].
- Calculate a safe [[CPC]] from price, conversion rate, and target [[ACOS]].
- Check clicks, orders, spend, and placement before changing the bid.
- Increase bids only where relevance and conversion justify more traffic.
- Decrease bids where spend is inefficient but the target is still relevant.

**Worked mini-example:** If price is $20, target [[ACOS]] is 25%, and [[CVR]] is 10%, the target [[CPC]] is $20 x 25% x 10% = $0.50. A $1.20 bid may be too aggressive unless conversion is much higher.

**Common beginner mistakes:**
- Raising bids on keywords with weak conversion.
- Cutting bids too early before enough clicks exist.
- Ignoring placement modifiers that may be causing high [[CPC]].

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md`

```markdown
---
title: "6.3 Bid Adjustment Cadence"
page_id: "6-3"
section: "6. Bidding Strategies & Bid Management"
learner_level: "Foundational"
topic_tags: ["bidding"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 6.3 Bid Adjustment Cadence

**What this page teaches:** Bids should be reviewed on a rhythm, not every time one click happens.

**Explain it to a fresh graduate:** One bad click is not a trend. Changing bids too early is like changing your college major because of one quiz.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use daily checks for spend leaks, weekly for optimization, monthly for strategy. Wait for enough clicks, spend, or orders before major changes.

**Operator view:** Bids control how aggressively you enter auctions. Bid changes should follow evidence, not mood, caffeine, or panic.

**Practical workflow:**
- Confirm the target [[ACOS]] or [[ROAS]].
- Calculate a safe [[CPC]] from price, conversion rate, and target [[ACOS]].
- Check clicks, orders, spend, and placement before changing the bid.
- Increase bids only where relevance and conversion justify more traffic.
- Decrease bids where spend is inefficient but the target is still relevant.

**Worked mini-example:** If price is $20, target [[ACOS]] is 25%, and [[CVR]] is 10%, the target [[CPC]] is $20 x 25% x 10% = $0.50. A $1.20 bid may be too aggressive unless conversion is much higher.

**Common beginner mistakes:**
- Raising bids on keywords with weak conversion.
- Cutting bids too early before enough clicks exist.
- Ignoring placement modifiers that may be causing high [[CPC]].

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md`

```markdown
---
title: "6.4 Placement Bid Modifiers"
page_id: "6-4"
section: "6. Bidding Strategies & Bid Management"
learner_level: "Foundational"
topic_tags: ["bidding"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 6.4 Placement Bid Modifiers

**What this page teaches:** Placement modifiers increase bids for Top of Search or Product Pages placements.

**Explain it to a fresh graduate:** Top of Search can convert well, but it can also get expensive. Treat modifiers like seasoning. Too much and the whole dish becomes chaos.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Increase modifiers only when placement data proves better performance and the campaign has enough budget.

**Operator view:** Bids control how aggressively you enter auctions. Bid changes should follow evidence, not mood, caffeine, or panic.

**Practical workflow:**
- Confirm the target [[ACOS]] or [[ROAS]].
- Calculate a safe [[CPC]] from price, conversion rate, and target [[ACOS]].
- Check clicks, orders, spend, and placement before changing the bid.
- Increase bids only where relevance and conversion justify more traffic.
- Decrease bids where spend is inefficient but the target is still relevant.

**Worked mini-example:** If price is $20, target [[ACOS]] is 25%, and [[CVR]] is 10%, the target [[CPC]] is $20 x 25% x 10% = $0.50. A $1.20 bid may be too aggressive unless conversion is much higher.

**Common beginner mistakes:**
- Raising bids on keywords with weak conversion.
- Cutting bids too early before enough clicks exist.
- Ignoring placement modifiers that may be causing high [[CPC]].

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/06-6-bidding-strategies-and-bid-management/index.md`

```markdown
---
title: "6. Bidding Strategies & Bid Management"
page_type: section_overview
section_id: "6"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 6. Bidding Strategies & Bid Management

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[6.1 Manual Bidding Fundamentals]]
- [[6.2 Dynamic & Rule-Based Bidding]]
- [[6.3 Bid Adjustment Cadence]]
- [[6.4 Placement Bid Modifiers]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/07-7-budget-management-and-pacing/7-1-7-1-budget-allocation-frameworks.md`

```markdown
---
title: "7.1 Budget Allocation Frameworks"
page_id: "7-1"
section: "7. Budget Management & Pacing"
learner_level: "Foundational"
topic_tags: ["budget"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 7.1 Budget Allocation Frameworks

**What this page teaches:** Budgets can be set from the top down as a spend target or bottom up by SKU opportunity and margin.

**Explain it to a fresh graduate:** Budget is not just money available. It is a decision about where growth is allowed to happen.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Protect budget for winners, reserve testing budget for discovery, and avoid spreading small budgets across too many campaigns.

**Operator view:** Budgets control how much opportunity a campaign can capture. A good budget protects cash while feeding proven performers.

**Practical workflow:**
- Check whether the campaign runs out of budget.
- Separate strong campaigns from testing campaigns.
- Increase budget on campaigns with profitable or strategic performance.
- Reduce budget on campaigns that waste spend or lack strategic purpose.
- Review pacing before seasonal events.

**Worked mini-example:** A campaign with 20% [[ACOS]] and frequent budget-outs deserves review for a budget increase. A campaign with 90% [[ACOS]] and no strategic purpose needs diagnosis before more spend.

**Common beginner mistakes:**
- Giving equal budget to every campaign.
- Starving a campaign that already proves it can sell efficiently.
- Scaling spend without checking inventory and margin.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/07-7-budget-management-and-pacing/7-2-7-2-pacing-and-ran-out-of-budget-diagnostics.md`

```markdown
---
title: "7.2 Pacing and Ran Out of Budget Diagnostics"
page_id: "7-2"
section: "7. Budget Management & Pacing"
learner_level: "Foundational"
topic_tags: ["budget"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 7.2 Pacing and Ran Out of Budget Diagnostics

**What this page teaches:** Pacing checks whether campaigns run out of budget too early or underspend despite opportunity.

**Explain it to a fresh graduate:** If a strong campaign runs out by lunch, the best hours may be gone before shoppers even arrive after work.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Check budget status, hourly spend, lost opportunity, [[ACOS]], and campaign importance before increasing budgets.

**Operator view:** Budgets control how much opportunity a campaign can capture. A good budget protects cash while feeding proven performers.

**Practical workflow:**
- Check whether the campaign runs out of budget.
- Separate strong campaigns from testing campaigns.
- Increase budget on campaigns with profitable or strategic performance.
- Reduce budget on campaigns that waste spend or lack strategic purpose.
- Review pacing before seasonal events.

**Worked mini-example:** A campaign with 20% [[ACOS]] and frequent budget-outs deserves review for a budget increase. A campaign with 90% [[ACOS]] and no strategic purpose needs diagnosis before more spend.

**Common beginner mistakes:**
- Giving equal budget to every campaign.
- Starving a campaign that already proves it can sell efficiently.
- Scaling spend without checking inventory and margin.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

### Pacing diagnosis

If a campaign runs out of budget in the first few hours, ask:

1. Is ACOS profitable?
2. Is the campaign spending on good search terms?
3. Is inventory healthy?
4. Are bids too high?
5. Should budget increase, or should waste be removed first?

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/07-7-budget-management-and-pacing/7-3-7-3-seasonal-budget-planning.md`

```markdown
---
title: "7.3 Seasonal Budget Planning"
page_id: "7-3"
section: "7. Budget Management & Pacing"
learner_level: "Foundational"
topic_tags: ["budget"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 7.3 Seasonal Budget Planning

**What this page teaches:** Seasonal planning prepares budgets for Prime Day, Q4, Black Friday, Cyber Monday, holidays, and category peaks.

**Explain it to a fresh graduate:** During big events, normal budgets can collapse faster than a cheap umbrella in a typhoon.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Plan pre-event ramp, event-day scale, and post-event wind-down. Tie budget to inventory and promo calendar.

**Operator view:** Budgets control how much opportunity a campaign can capture. A good budget protects cash while feeding proven performers.

**Practical workflow:**
- Check whether the campaign runs out of budget.
- Separate strong campaigns from testing campaigns.
- Increase budget on campaigns with profitable or strategic performance.
- Reduce budget on campaigns that waste spend or lack strategic purpose.
- Review pacing before seasonal events.

**Worked mini-example:** A campaign with 20% [[ACOS]] and frequent budget-outs deserves review for a budget increase. A campaign with 90% [[ACOS]] and no strategic purpose needs diagnosis before more spend.

**Common beginner mistakes:**
- Giving equal budget to every campaign.
- Starving a campaign that already proves it can sell efficiently.
- Scaling spend without checking inventory and margin.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/07-7-budget-management-and-pacing/index.md`

```markdown
---
title: "7. Budget Management & Pacing"
page_type: section_overview
section_id: "7"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 7. Budget Management & Pacing

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[7.1 Budget Allocation Frameworks]]
- [[7.2 Pacing and Ran Out of Budget Diagnostics]]
- [[7.3 Seasonal Budget Planning]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/08-8-placements-and-placement-optimization/8-1-8-1-placement-types-explained.md`

```markdown
---
title: "8.1 Placement Types Explained"
page_id: "8-1"
section: "8. Placements & Placement Optimization"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 8.1 Placement Types Explained

**What this page teaches:** [[Sponsored Products]] placements include Top of Search, Rest of Search, and Product Pages.

**Explain it to a fresh graduate:** Placement means where the ad appears. Same campaign, different shelf location, different buyer behavior.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use Top of Search for high-intent visibility, Product Pages for comparison shopping, and Rest of Search for broader reach.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Placement optimization controls where your ads appear. The three main Sponsored Products placements are Top of Search, Rest of Search, and Product Detail Pages.

| Placement | Typical behavior | Operator note |
|---|---|---|
| Top of Search | High visibility, high CPC, often high CVR | Worth bidding up only when efficient |
| Rest of Search | Middle ground | Often stable and scalable |
| Product Detail Pages | Lower intent, cheaper clicks | Useful for conquesting and cross-sell |

### Diagnosis workflow

1. Pull the Placement Report.
2. Compare ACOS, CTR, CVR, CPC, and sales by placement.
3. Increase modifier where ACOS is below target and volume is limited.
4. Reduce modifier where CPC is high and CVR is weak.
5. Recheck after enough data, not the next morning.

### Worked example

If Top of Search ACOS is 25%, Rest of Search is 35%, and Product Pages is 45%, increase Top of Search modestly, leave Rest alone, and reduce Product Pages or keep it conservative.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/08-8-placements-and-placement-optimization/8-2-8-2-placement-reporting-and-diagnosis.md`

```markdown
---
title: "8.2 Placement Reporting & Diagnosis"
page_id: "8-2"
section: "8. Placements & Placement Optimization"
learner_level: "Foundational"
topic_tags: ["reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 8.2 Placement Reporting & Diagnosis

**What this page teaches:** Placement reports show performance by placement so you can adjust modifiers.

**Explain it to a fresh graduate:** Do not assume Top of Search is always best. Let the placement report be the referee.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Raise modifiers where [[CVR]] and [[ACOS]] support it. Reduce or remove modifiers when spend rises without profitable sales.

**Operator view:** Reports turn raw PPC activity into decisions. The best report explains what happened, why it happened, and what happens next.

**Practical workflow:**
- Choose the right report for the question.
- Clean and label the data.
- Compare against target and previous period.
- Find the root cause, not only the metric movement.
- Write the action plan with owner and deadline.

**Worked mini-example:** Instead of saying [[ACOS]] rose from 25% to 32%, explain that [[CPC]] rose on two non-branded exact campaigns while conversion dropped after price increased.

**Common beginner mistakes:**
- Sending tables without interpretation.
- Mixing attribution windows or date ranges.
- Reporting only ad metrics when stakeholders need business impact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Placement optimization controls where your ads appear. The three main Sponsored Products placements are Top of Search, Rest of Search, and Product Detail Pages.

| Placement | Typical behavior | Operator note |
|---|---|---|
| Top of Search | High visibility, high CPC, often high CVR | Worth bidding up only when efficient |
| Rest of Search | Middle ground | Often stable and scalable |
| Product Detail Pages | Lower intent, cheaper clicks | Useful for conquesting and cross-sell |

### Diagnosis workflow

1. Pull the Placement Report.
2. Compare ACOS, CTR, CVR, CPC, and sales by placement.
3. Increase modifier where ACOS is below target and volume is limited.
4. Reduce modifier where CPC is high and CVR is weak.
5. Recheck after enough data, not the next morning.

### Worked example

If Top of Search ACOS is 25%, Rest of Search is 35%, and Product Pages is 45%, increase Top of Search modestly, leave Rest alone, and reduce Product Pages or keep it conservative.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/08-8-placements-and-placement-optimization/index.md`

```markdown
---
title: "8. Placements & Placement Optimization"
page_type: section_overview
section_id: "8"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 8. Placements & Placement Optimization

This cluster contains 2 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[8.1 Placement Types Explained]]
- [[8.2 Placement Reporting & Diagnosis]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Placement optimization controls where your ads appear. The three main Sponsored Products placements are Top of Search, Rest of Search, and Product Detail Pages.

| Placement | Typical behavior | Operator note |
|---|---|---|
| Top of Search | High visibility, high CPC, often high CVR | Worth bidding up only when efficient |
| Rest of Search | Middle ground | Often stable and scalable |
| Product Detail Pages | Lower intent, cheaper clicks | Useful for conquesting and cross-sell |

### Diagnosis workflow

1. Pull the Placement Report.
2. Compare ACOS, CTR, CVR, CPC, and sales by placement.
3. Increase modifier where ACOS is below target and volume is limited.
4. Reduce modifier where CPC is high and CVR is weak.
5. Recheck after enough data, not the next morning.

### Worked example

If Top of Search ACOS is 25%, Rest of Search is 35%, and Product Pages is 45%, increase Top of Search modestly, leave Rest alone, and reduce Product Pages or keep it conservative.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/09-9-negative-keywords-and-negation-strategy/9-1-9-1-negative-match-types.md`

```markdown
---
title: "9.1 Negative Match Types"
page_id: "9-1"
section: "9. Negative Keywords & Negation Strategy"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 9.1 Negative Match Types

**What this page teaches:** Negative exact blocks one exact query. Negative phrase blocks searches containing that phrase. Negative product targeting blocks specific ASIN targets.

**Explain it to a fresh graduate:** Negatives tell Amazon where not to show the ad. They are the brakes of the account.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use negative exact for precise waste. Use negative phrase for clearly irrelevant word groups. Use product negatives for bad ASIN placements.

**Operator view:** Negative keywords prevent spend on bad traffic or protect clean campaign structure.

**Practical workflow:**
- Review search terms by spend, clicks, orders, [[ACOS]], and relevance.
- Mark terms as irrelevant, inefficient, harvested, or still testing.
- Use negative exact for precise blocking.
- Use negative phrase only when the entire phrase family is unwanted.
- Check conflicts before uploading negatives.

**Worked mini-example:** If a premium leather wallet campaign spends on "cheap plastic wallet," the term may be negated. If "brown leather wallet" spent $8 with no sale but only 6 clicks, keep testing unless thresholds are met.

**Common beginner mistakes:**
- Using negative phrase too aggressively.
- Negating a term that performs in another campaign.
- Blocking discovery before the campaign has enough data.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

### Negative keyword examples

- Use Negative Exact for one bad search term: `[used running shoes]`.
- Use Negative Phrase for a bad concept: `"free"` or `"used"` when those concepts never fit.
- Use product exclusions when a competitor ASIN or category segment wastes spend.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/09-9-negative-keywords-and-negation-strategy/9-2-9-2-negation-strategy-by-campaign-structure.md`

```markdown
---
title: "9.2 Negation Strategy by Campaign Structure"
page_id: "9-2"
section: "9. Negative Keywords & Negation Strategy"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 9.2 Negation Strategy by Campaign Structure

**What this page teaches:** Negatives prevent waste and protect clean campaign segmentation.

**Explain it to a fresh graduate:** If a term is harvested into exact, you may negate it in broad or auto so data moves to the controlled campaign.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Apply cross-campaign negatives carefully. Keep a change log so you know why terms were blocked.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/09-9-negative-keywords-and-negation-strategy/9-3-9-3-common-negation-mistakes.md`

```markdown
---
title: "9.3 Common Negation Mistakes"
page_id: "9-3"
section: "9. Negative Keywords & Negation Strategy"
learner_level: "Foundational"
topic_tags: ["keywords"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 9.3 Common Negation Mistakes

**What this page teaches:** Common errors include over-negating, blocking good terms, creating conflicts, and negating too early.

**Explain it to a fresh graduate:** Negatives are powerful. The wrong negative can quietly kill sales and sit there like a tiny villain in a spreadsheet.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Review search volume, sales history, relevance, and positive targets before applying broad negative phrase rules.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/09-9-negative-keywords-and-negation-strategy/index.md`

```markdown
---
title: "9. Negative Keywords & Negation Strategy"
page_type: section_overview
section_id: "9"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 9. Negative Keywords & Negation Strategy

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[9.1 Negative Match Types]]
- [[9.2 Negation Strategy by Campaign Structure]]
- [[9.3 Common Negation Mistakes]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive.md`

```markdown
---
title: "10.1 Core Metrics Deep Dive"
page_id: "10-1"
section: "10. Metrics, KPIs & Analytics"
learner_level: "Foundational"
topic_tags: ["metrics"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 10.1 Core Metrics Deep Dive

**What this page teaches:** Core metrics include impressions, clicks, [[CTR]], [[CPC]], [[CVR]], spend, sales, [[ACOS]], [[TACOS]], and [[ROAS]].

**Explain it to a fresh graduate:** Metrics are the dashboard lights. They do not fix the car, but they tell you where to inspect.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Teach formulas: [[CTR]] = clicks/impressions; [[CVR]] = orders/clicks; [[ACOS]] = ad spend/ad sales; [[ROAS]] = ad sales/ad spend; [[TACOS]] = ad spend/total sales.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

### Metric interpretation

Low CTR usually means poor relevance, weak main image, or uncompetitive offer. Low CVR usually points to listing, price, reviews, shipping, or mismatch between keyword and product. High CPC means competition or aggressive placement/bid settings.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/10-10-metrics-kpis-and-analytics/10-2-10-2-advanced-metrics.md`

```markdown
---
title: "10.2 Advanced Metrics"
page_id: "10-2"
section: "10. Metrics, KPIs & Analytics"
learner_level: "Foundational"
topic_tags: ["metrics"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 10.2 Advanced Metrics

**What this page teaches:** Advanced metrics include new-to-brand, halo sales, attribution windows, brand halo, and cross-channel impact.

**Explain it to a fresh graduate:** Not all value appears as same-SKU immediate sales. Some ads introduce new customers or influence later purchases.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use advanced metrics for SB, SD, DSP, [[Amazon Marketing Cloud]], and stakeholder reporting beyond basic [[ACOS]].

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/10-10-metrics-kpis-and-analytics/10-3-10-3-health-check-frameworks.md`

```markdown
---
title: "10.3 Health Check Frameworks"
page_id: "10-3"
section: "10. Metrics, KPIs & Analytics"
learner_level: "Foundational"
topic_tags: ["metrics"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 10.3 Health Check Frameworks

**What this page teaches:** A health scorecard quickly shows what is healthy, risky, or broken in the account.

**Explain it to a fresh graduate:** A beginner should not stare at 50 columns and panic. Use a simple red-yellow-green system.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Score spend, sales, [[ACOS]], [[TACOS]], [[CTR]], [[CVR]], budget status, search term waste, and scaling opportunities.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/10-10-metrics-kpis-and-analytics/10-4-10-4-benchmarking.md`

```markdown
---
title: "10.4 Benchmarking"
page_id: "10-4"
section: "10. Metrics, KPIs & Analytics"
learner_level: "Foundational"
topic_tags: ["metrics"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 10.4 Benchmarking

**What this page teaches:** Benchmarks compare performance against category, account history, margin, and business goal.

**Explain it to a fresh graduate:** There is no universal 'good [[ACOS]].' A 35% [[ACOS]] may be great for launch and bad for a low-margin mature product.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Calculate break-even [[ACOS]] from margin. Use category benchmarks only as directional guidance.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/10-10-metrics-kpis-and-analytics/index.md`

```markdown
---
title: "10. Metrics, KPIs & Analytics"
page_type: section_overview
section_id: "10"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 10. Metrics, KPIs & Analytics

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[10.1 Core Metrics Deep Dive]]
- [[10.2 Advanced Metrics]]
- [[10.3 Health Check Frameworks]]
- [[10.4 Benchmarking]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/11-11-reporting-and-data-analysis/11-1-11-1-native-amazon-reports.md`

```markdown
---
title: "11.1 Native Amazon Reports"
page_id: "11-1"
section: "11. Reporting & Data Analysis"
learner_level: "Foundational"
topic_tags: ["reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 11.1 Native Amazon Reports

**What this page teaches:** Key reports include Search Term, Targeting, Placement, Advertised Product, Purchased Product, Budget, and Bulk files.

**Explain it to a fresh graduate:** Reports are where the account tells the truth. The console summary is useful, but reports reveal the details.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Teach where each report lives, what question it answers, and how often to use it.

**Operator view:** Reports turn raw PPC activity into decisions. The best report explains what happened, why it happened, and what happens next.

**Practical workflow:**
- Choose the right report for the question.
- Clean and label the data.
- Compare against target and previous period.
- Find the root cause, not only the metric movement.
- Write the action plan with owner and deadline.

**Worked mini-example:** Instead of saying [[ACOS]] rose from 25% to 32%, explain that [[CPC]] rose on two non-branded exact campaigns while conversion dropped after price increased.

**Common beginner mistakes:**
- Sending tables without interpretation.
- Mixing attribution windows or date ranges.
- Reporting only ad metrics when stakeholders need business impact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/11-11-reporting-and-data-analysis/11-2-11-2-brand-analytics.md`

```markdown
---
title: "11.2 Brand Analytics"
page_id: "11-2"
section: "11. Reporting & Data Analysis"
learner_level: "Foundational"
topic_tags: ["brand", "reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 11.2 Brand Analytics

**What this page teaches:** Brand Analytics includes tools such as Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase reports where available.

**Explain it to a fresh graduate:** Brand Analytics helps you see market behavior, not just your ad clicks.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use SQP to compare query-level impressions, clicks, cart adds, purchases, and share trends.

**Operator view:** Reports turn raw PPC activity into decisions. The best report explains what happened, why it happened, and what happens next.

**Practical workflow:**
- Choose the right report for the question.
- Clean and label the data.
- Compare against target and previous period.
- Find the root cause, not only the metric movement.
- Write the action plan with owner and deadline.

**Worked mini-example:** Instead of saying [[ACOS]] rose from 25% to 32%, explain that [[CPC]] rose on two non-branded exact campaigns while conversion dropped after price increased.

**Common beginner mistakes:**
- Sending tables without interpretation.
- Mixing attribution windows or date ranges.
- Reporting only ad metrics when stakeholders need business impact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/11-11-reporting-and-data-analysis/11-3-11-3-custom-reporting-and-dashboards.md`

```markdown
---
title: "11.3 Custom Reporting & Dashboards"
page_id: "11-3"
section: "11. Reporting & Data Analysis"
learner_level: "Foundational"
topic_tags: ["reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 11.3 Custom Reporting & Dashboards

**What this page teaches:** Custom dashboards translate raw data into views for operators, strategists, clients, and executives.

**Explain it to a fresh graduate:** An operator needs details. A CEO needs the story. Do not give both the same 47-column spreadsheet unless you enjoy meetings with sighing.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build dashboard layers: executive summary, growth drivers, waste, keyword opportunities, budget pacing, action log.

**Operator view:** Reports turn raw PPC activity into decisions. The best report explains what happened, why it happened, and what happens next.

**Practical workflow:**
- Choose the right report for the question.
- Clean and label the data.
- Compare against target and previous period.
- Find the root cause, not only the metric movement.
- Write the action plan with owner and deadline.

**Worked mini-example:** Instead of saying [[ACOS]] rose from 25% to 32%, explain that [[CPC]] rose on two non-branded exact campaigns while conversion dropped after price increased.

**Common beginner mistakes:**
- Sending tables without interpretation.
- Mixing attribution windows or date ranges.
- Reporting only ad metrics when stakeholders need business impact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/11-11-reporting-and-data-analysis/11-4-11-4-data-storytelling.md`

```markdown
---
title: "11.4 Data Storytelling"
page_id: "11-4"
section: "11. Reporting & Data Analysis"
learner_level: "Foundational"
topic_tags: ["reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 11.4 Data Storytelling

**What this page teaches:** Data storytelling explains what happened, why it happened, what you will do, and what result you expect.

**Explain it to a fresh graduate:** Numbers alone do not persuade. A good PPC report turns data into business decisions.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use a simple format: headline, evidence, cause, action, expected impact, owner, deadline.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

### Client narrative template

`What happened:` Ad efficiency changed this month.

`Why it happened:` CPC rose, CVR dropped, budget shifted, or competition changed.

`What we are doing:` Adjust bids, add negatives, harvest winners, shift budget, or improve listing readiness.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/11-11-reporting-and-data-analysis/index.md`

```markdown
---
title: "11. Reporting & Data Analysis"
page_type: section_overview
section_id: "11"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 11. Reporting & Data Analysis

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[11.1 Native Amazon Reports]]
- [[11.2 Brand Analytics]]
- [[11.3 Custom Reporting & Dashboards]]
- [[11.4 Data Storytelling]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/12-12-amazon-marketing-cloud/12-1-12-1-what-amc-is-and-who-needs-it.md`

```markdown
---
title: "12.1 What AMC Is and Who Needs It"
page_id: "12-1"
section: "12. Amazon Marketing Cloud"
learner_level: "Applied"
topic_tags: ["amc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 12.1 What AMC Is and Who Needs It

**What this page teaches:** Amazon Marketing Cloud is a privacy-safe clean room used for deeper analytics and audience building across Amazon Ads signals and advertiser inputs.

**Explain it to a fresh graduate:** [[Amazon Marketing Cloud]] is for advanced measurement. It helps answer questions the normal console cannot answer cleanly.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use [[Amazon Marketing Cloud]] when the brand has enough media activity, wants cross-channel attribution, or needs custom audience logic.

**Operator view:** [[Amazon Marketing Cloud]] is a clean-room analytics tool for advanced measurement and audience building. It is not a beginner campaign manager screen.

**Practical workflow:**
- Define the business question.
- Confirm available signals and privacy constraints.
- Run or request a query.
- Interpret results for overlap, path to conversion, or audience creation.
- Translate the insight into media action.

**Worked mini-example:** [[Amazon Marketing Cloud]] can help answer whether shoppers exposed to DSP and Sponsored Ads convert differently from shoppers exposed to only one channel.

**Common beginner mistakes:**
- Using [[Amazon Marketing Cloud]] without a clear question.
- Expecting it to replace daily campaign reports.
- Sharing or exporting data outside allowed privacy rules.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/12-12-amazon-marketing-cloud/12-2-12-2-amc-use-cases.md`

```markdown
---
title: "12.2 AMC Use Cases"
page_id: "12-2"
section: "12. Amazon Marketing Cloud"
learner_level: "Applied"
topic_tags: ["amc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 12.2 AMC Use Cases

**What this page teaches:** [[Amazon Marketing Cloud]] can support overlap analysis, path-to-purchase analysis, cross-channel attribution, frequency analysis, and audience creation.

**Explain it to a fresh graduate:** It helps answer questions like: Did DSP exposure improve Sponsored Ads conversion? Are we showing too many ads to the same shoppers?

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Start with business questions before writing queries. Do not run SQL just because it sounds senior.

**Operator view:** [[Amazon Marketing Cloud]] is a clean-room analytics tool for advanced measurement and audience building. It is not a beginner campaign manager screen.

**Practical workflow:**
- Define the business question.
- Confirm available signals and privacy constraints.
- Run or request a query.
- Interpret results for overlap, path to conversion, or audience creation.
- Translate the insight into media action.

**Worked mini-example:** [[Amazon Marketing Cloud]] can help answer whether shoppers exposed to DSP and Sponsored Ads convert differently from shoppers exposed to only one channel.

**Common beginner mistakes:**
- Using [[Amazon Marketing Cloud]] without a clear question.
- Expecting it to replace daily campaign reports.
- Sharing or exporting data outside allowed privacy rules.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics.md`

```markdown
---
title: "12.3 AMC SQL Basics"
page_id: "12-3"
section: "12. Amazon Marketing Cloud"
learner_level: "Applied"
topic_tags: ["amc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 12.3 AMC SQL Basics

**What this page teaches:** [[Amazon Marketing Cloud]] uses SQL-style queries on permitted data tables to create aggregated insights.

**Explain it to a fresh graduate:** SQL is a way to ask structured questions of data. It is less scary once you see it as filtered spreadsheet logic.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Teach SELECT, FROM, WHERE, GROUP BY, date windows, privacy thresholds, and template queries.

**Operator view:** [[Amazon Marketing Cloud]] is a clean-room analytics tool for advanced measurement and audience building. It is not a beginner campaign manager screen.

**Practical workflow:**
- Define the business question.
- Confirm available signals and privacy constraints.
- Run or request a query.
- Interpret results for overlap, path to conversion, or audience creation.
- Translate the insight into media action.

**Worked mini-example:** [[Amazon Marketing Cloud]] can help answer whether shoppers exposed to DSP and Sponsored Ads convert differently from shoppers exposed to only one channel.

**Common beginner mistakes:**
- Using [[Amazon Marketing Cloud]] without a clear question.
- Expecting it to replace daily campaign reports.
- Sharing or exporting data outside allowed privacy rules.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/12-12-amazon-marketing-cloud/index.md`

```markdown
---
title: "12. Amazon Marketing Cloud"
page_type: section_overview
section_id: "12"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 12. Amazon Marketing Cloud

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[12.1 What AMC Is and Who Needs It]]
- [[12.2 AMC Use Cases]]
- [[12.3 AMC SQL Basics]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/13-13-amazon-dsp/13-1-13-1-dsp-fundamentals.md`

```markdown
---
title: "13.1 DSP Fundamentals"
page_id: "13-1"
section: "13. Amazon DSP"
learner_level: "Applied"
topic_tags: ["dsp"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 13.1 DSP Fundamentals

**What this page teaches:** [[Amazon DSP]] allows programmatic buying across display, video, audio, and streaming inventory using Amazon audience signals.

**Explain it to a fresh graduate:** Sponsored Ads often capture demand. DSP can create and re-engage demand across more placements.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Explain managed service vs. self-service, budget expectations, audience strategy, creative, and measurement.

**Operator view:** DSP is for advanced audience strategy across display, video, audio, and streaming placements. It needs stronger planning than basic Sponsored Ads.

**Practical workflow:**
- Define audience and funnel stage.
- Confirm budget, creative, and measurement plan.
- Separate prospecting from retargeting.
- Use [[Amazon Marketing Cloud]] or reporting to evaluate overlap and path to purchase.
- Coordinate DSP learnings with Sponsored Ads strategy.

**Worked mini-example:** DSP prospecting may build audience reach while SP exact captures purchase intent. Together they can support a full-funnel plan.

**Common beginner mistakes:**
- Launching DSP without enough budget or creative.
- Comparing DSP prospecting directly against SP exact [[ACOS]].
- Ignoring frequency and audience overlap.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/13-13-amazon-dsp/13-2-13-2-dsp-campaign-types.md`

```markdown
---
title: "13.2 DSP Campaign Types"
page_id: "13-2"
section: "13. Amazon DSP"
learner_level: "Applied"
topic_tags: ["dsp"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 13.2 DSP Campaign Types

**What this page teaches:** DSP campaigns can include display, online video, audio, over-the-top/streaming TV, retargeting, and prospecting.

**Explain it to a fresh graduate:** Retargeting talks to people who already showed interest. Prospecting looks for new likely buyers.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Map campaign type to objective: awareness, consideration, retargeting, loyalty, or category expansion.

**Operator view:** DSP is for advanced audience strategy across display, video, audio, and streaming placements. It needs stronger planning than basic Sponsored Ads.

**Practical workflow:**
- Define audience and funnel stage.
- Confirm budget, creative, and measurement plan.
- Separate prospecting from retargeting.
- Use [[Amazon Marketing Cloud]] or reporting to evaluate overlap and path to purchase.
- Coordinate DSP learnings with Sponsored Ads strategy.

**Worked mini-example:** DSP prospecting may build audience reach while SP exact captures purchase intent. Together they can support a full-funnel plan.

**Common beginner mistakes:**
- Launching DSP without enough budget or creative.
- Comparing DSP prospecting directly against SP exact [[ACOS]].
- Ignoring frequency and audience overlap.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/13-13-amazon-dsp/13-3-13-3-dsp-audience-building.md`

```markdown
---
title: "13.3 DSP Audience Building"
page_id: "13-3"
section: "13. Amazon DSP"
learner_level: "Applied"
topic_tags: ["dsp"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 13.3 DSP Audience Building

**What this page teaches:** Audiences can use Amazon segments, remarketing pools, first-party data, and lookalikes where available.

**Explain it to a fresh graduate:** The audience is the 'who.' Bad audience targeting can waste even beautiful creative.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Document audience source, logic, exclusions, frequency cap, and expected behavior.

**Operator view:** DSP is for advanced audience strategy across display, video, audio, and streaming placements. It needs stronger planning than basic Sponsored Ads.

**Practical workflow:**
- Define audience and funnel stage.
- Confirm budget, creative, and measurement plan.
- Separate prospecting from retargeting.
- Use [[Amazon Marketing Cloud]] or reporting to evaluate overlap and path to purchase.
- Coordinate DSP learnings with Sponsored Ads strategy.

**Worked mini-example:** DSP prospecting may build audience reach while SP exact captures purchase intent. Together they can support a full-funnel plan.

**Common beginner mistakes:**
- Launching DSP without enough budget or creative.
- Comparing DSP prospecting directly against SP exact [[ACOS]].
- Ignoring frequency and audience overlap.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/13-13-amazon-dsp/13-4-13-4-dsp-plus-sponsored-ads-synergy.md`

```markdown
---
title: "13.4 DSP + Sponsored Ads Synergy"
page_id: "13-4"
section: "13. Amazon DSP"
learner_level: "Applied"
topic_tags: ["dsp"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 13.4 DSP + Sponsored Ads Synergy

**What this page teaches:** DSP and Sponsored Ads work best when budgets, audiences, and search coverage support each other.

**Explain it to a fresh graduate:** A shopper may see a video, later search Amazon, click SP, then buy. Good reporting should respect that journey.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use full-funnel planning: DSP builds reach, SD retargets, SB shapes brand consideration, SP captures purchase intent.

**Operator view:** DSP is for advanced audience strategy across display, video, audio, and streaming placements. It needs stronger planning than basic Sponsored Ads.

**Practical workflow:**
- Define audience and funnel stage.
- Confirm budget, creative, and measurement plan.
- Separate prospecting from retargeting.
- Use [[Amazon Marketing Cloud]] or reporting to evaluate overlap and path to purchase.
- Coordinate DSP learnings with Sponsored Ads strategy.

**Worked mini-example:** DSP prospecting may build audience reach while SP exact captures purchase intent. Together they can support a full-funnel plan.

**Common beginner mistakes:**
- Launching DSP without enough budget or creative.
- Comparing DSP prospecting directly against SP exact [[ACOS]].
- Ignoring frequency and audience overlap.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/13-13-amazon-dsp/index.md`

```markdown
---
title: "13. Amazon DSP"
page_type: section_overview
section_id: "13"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 13. Amazon DSP

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[13.1 DSP Fundamentals]]
- [[13.2 DSP Campaign Types]]
- [[13.3 DSP Audience Building]]
- [[13.4 DSP + Sponsored Ads Synergy]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/14-14-brand-presence-and-content-tie-ins/14-1-14-1-brand-registry.md`

```markdown
---
title: "14.1 Brand Registry"
page_id: "14-1"
section: "14. Brand Presence & Content Tie-Ins"
learner_level: "Applied"
topic_tags: ["brand"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 14.1 Brand Registry

**What this page teaches:** Brand Registry unlocks or improves access to brand features like [[Sponsored Brands]], Stores, brand assets, and A+ Content.

**Explain it to a fresh graduate:** Brand Registry proves you control the brand. Without it, some brand-building ad tools may not be available.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Check trademark, brand ownership, store readiness, and user permissions before planning SB-heavy strategies.

**Operator view:** Brand assets influence trust, conversion, and ad formats available to the account.

**Practical workflow:**
- Confirm Brand Registry or eligibility.
- Audit Store, A+ Content, images, video, and brand messaging.
- Map SB and SD campaigns to brand assets.
- Measure Store and product detail page performance.
- Refresh creative when performance decays.

**Worked mini-example:** A strong Brand Store can turn [[Sponsored Brands]] traffic into multi-product discovery instead of sending every shopper to one listing.

**Common beginner mistakes:**
- Sending SB traffic to a weak Store.
- Using inconsistent product messaging.
- Ignoring creative fatigue.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/14-14-brand-presence-and-content-tie-ins/14-2-14-2-brand-store.md`

```markdown
---
title: "14.2 Brand Store"
page_id: "14-2"
section: "14. Brand Presence & Content Tie-Ins"
learner_level: "Applied"
topic_tags: ["brand"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 14.2 Brand Store

**What this page teaches:** A Brand Store is a branded landing space inside Amazon with pages for product lines, collections, and campaigns.

**Explain it to a fresh graduate:** Think of it as a mini website inside Amazon. SB ads often send traffic there.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build pages by shopper intent: best sellers, categories, use cases, bundles, seasonal offers.

**Operator view:** Brand assets influence trust, conversion, and ad formats available to the account.

**Practical workflow:**
- Confirm Brand Registry or eligibility.
- Audit Store, A+ Content, images, video, and brand messaging.
- Map SB and SD campaigns to brand assets.
- Measure Store and product detail page performance.
- Refresh creative when performance decays.

**Worked mini-example:** A strong Brand Store can turn [[Sponsored Brands]] traffic into multi-product discovery instead of sending every shopper to one listing.

**Common beginner mistakes:**
- Sending SB traffic to a weak Store.
- Using inconsistent product messaging.
- Ignoring creative fatigue.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/14-14-brand-presence-and-content-tie-ins/14-3-14-3-aplus-content-premium-aplus.md`

```markdown
---
title: "14.3 A+ Content / Premium A+"
page_id: "14-3"
section: "14. Brand Presence & Content Tie-Ins"
learner_level: "Applied"
topic_tags: ["brand"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 14.3 A+ Content / Premium A+

**What this page teaches:** A+ Content improves product detail pages with richer images, comparison charts, and brand storytelling.

**Explain it to a fresh graduate:** Ads bring shoppers to the page. A+ helps convince them once they arrive.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Audit A+ before scaling traffic. Weak content lowers [[CVR]] and makes every click feel expensive.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/14-14-brand-presence-and-content-tie-ins/index.md`

```markdown
---
title: "14. Brand Presence & Content Tie-Ins"
page_type: section_overview
section_id: "14"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 14. Brand Presence & Content Tie-Ins

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[14.1 Brand Registry]]
- [[14.2 Brand Store]]
- [[14.3 A+ Content / Premium A+]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/15-15-listing-optimization/15-1-15-1-why-listing-quality-gates-ppc-performance.md`

```markdown
---
title: "15.1 Why Listing Quality Gates PPC Performance"
page_id: "15-1"
section: "15. Listing Optimization"
learner_level: "Applied"
topic_tags: ["listing"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 15.1 Why Listing Quality Gates PPC Performance

**What this page teaches:** PPC performance depends on listing conversion rate. A weak listing limits what ads can achieve.

**Explain it to a fresh graduate:** If the product page does not persuade shoppers, buying more traffic just buys more disappointment.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Check title, images, reviews, rating, price, coupon, inventory, A+ content, and competitor comparison before scaling.

**Operator view:** Listings set the ceiling for PPC performance. Ads can bring traffic, but the page must convert that traffic.

**Practical workflow:**
- Audit title, images, bullets, A+ Content, price, reviews, inventory, and offers.
- Compare against top competitors.
- Check [[CVR]] and unit session percentage trends.
- Fix major listing issues before scaling bids.
- Test images, titles, and promotions when possible.

**Worked mini-example:** If [[CTR]] is strong but [[CVR]] is weak, the ad may be attracting shoppers but the listing may fail to convince them.

**Common beginner mistakes:**
- Blaming PPC for a weak product page.
- Scaling spend while reviews, price, or images are uncompetitive.
- Ignoring mobile listing experience.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/15-15-listing-optimization/15-2-15-2-title-bullet-backend-keyword-optimization.md`

```markdown
---
title: "15.2 Title, Bullet, Backend Keyword Optimization"
page_id: "15-2"
section: "15. Listing Optimization"
learner_level: "Applied"
topic_tags: ["keywords", "listing"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 15.2 Title, Bullet, Backend Keyword Optimization

**What this page teaches:** Listings should place important keywords in title, bullets, description/A+, and backend search terms based on relevance and policy.

**Explain it to a fresh graduate:** Keywords help Amazon understand the product. But keyword stuffing makes listings ugly and can hurt trust.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use high-relevance terms naturally. Avoid claims or terms that violate Amazon policy.

**Operator view:** Keywords and search terms reveal shopper language. Your job is to separate discovery from control.

**Practical workflow:**
- Collect seed keywords from listings, competitors, autocomplete, tools, and reports.
- Launch discovery campaigns with controlled budgets.
- Mine search terms after enough clicks or spend.
- Promote proven terms into exact campaigns.
- Negate waste or harvested terms based on structure.

**Worked mini-example:** The keyword "beer bong" may match the search term "beer bong funnel for party." If that search term gets orders at target [[ACOS]], harvest it into exact match.

**Common beginner mistakes:**
- Confusing keyword with customer search term.
- Promoting terms too early from one lucky sale.
- Adding negatives without checking whether another campaign needs the traffic.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/15-15-listing-optimization/15-3-15-3-image-and-video-impact-on-ctr-cvr.md`

```markdown
---
title: "15.3 Image & Video Impact on CTR/CVR"
page_id: "15-3"
section: "15. Listing Optimization"
learner_level: "Applied"
topic_tags: ["listing"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 15.3 Image & Video Impact on CTR/CVR

**What this page teaches:** Main images affect click-through. Secondary images and videos affect conversion.

**Explain it to a fresh graduate:** A great ad cannot rescue a confusing main image. The shopper scrolls fast and judges faster.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use image testing, competitor comparison, lifestyle images, infographics, and video where available.

**Operator view:** Use metrics to diagnose performance before touching bids or budgets. Metrics are symptoms first, decisions second.

**Practical workflow:**
- Check the date range and confirm enough data exists.
- Separate traffic metrics such as impressions, clicks, [[CTR]], and [[CPC]] from outcome metrics such as [[CVR]], orders, [[ACOS]], [[ROAS]], and [[TACOS]].
- Compare the metric against target, margin, previous period, and campaign purpose.
- Decide whether the issue is traffic, conversion, cost, or structure.
- Write the recommendation in plain business language.

**Worked mini-example:** A campaign has 1,000 impressions, 20 clicks, 1 order, $20 spend, and $40 ad sales. [[CTR]] is 2%, [[CVR]] is 5%, [[CPC]] is $1, [[ACOS]] is 50%, and [[ROAS]] is 2.0. The operator checks margin before deciding whether 50% [[ACOS]] is acceptable.

**Common beginner mistakes:**
- Judging a campaign from one day of data.
- Treating [[ACOS]] as the only success metric.
- Ignoring total sales, margin, inventory, and launch stage.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/15-15-listing-optimization/15-4-15-4-pricing-and-promotions-interplay-with-ppc.md`

```markdown
---
title: "15.4 Pricing & Promotions Interplay with PPC"
page_id: "15-4"
section: "15. Listing Optimization"
learner_level: "Applied"
topic_tags: ["listing"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 15.4 Pricing & Promotions Interplay with PPC

**What this page teaches:** Price, coupons, deals, and discounts change ad conversion and competitiveness.

**Explain it to a fresh graduate:** A coupon can lift [[CVR]]. A bad price can sink PPC even with good keywords.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Coordinate PPC with promo calendar, Prime eligibility, inventory, and margin.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/15-15-listing-optimization/index.md`

```markdown
---
title: "15. Listing Optimization"
page_type: section_overview
section_id: "15"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 15. Listing Optimization

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[15.1 Why Listing Quality Gates PPC Performance]]
- [[15.2 Title, Bullet, Backend Keyword Optimization]]
- [[15.3 Image & Video Impact on CTR/CVR]]
- [[15.4 Pricing & Promotions Interplay with PPC]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation.md`

```markdown
---
title: "16.1 Native Amazon Automation"
page_id: "16-1"
section: "16. Automation, Rules & Scripts"
learner_level: "Applied"
topic_tags: ["automation"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 16.1 Native Amazon Automation

**What this page teaches:** Amazon offers rule-based options for budgets and bids in some areas of the console.

**Explain it to a fresh graduate:** Rules are useful for repeatable tasks. They should not run wild without guardrails.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Document trigger, condition, action, cap, owner, and review date for every rule.

**Operator view:** Automation should apply rules consistently, but humans must set the strategy and guardrails.

**Practical workflow:**
- Define the exact decision rule.
- Set data thresholds and max change limits.
- Test on a low-risk scope.
- Review logs and exceptions.
- Keep human approval for high-impact actions.

**Worked mini-example:** A rule can lower bids when spend exceeds threshold and orders are zero, but it should not touch launch campaigns that are intentionally gathering data.

**Common beginner mistakes:**
- Automating before the process is understood.
- Letting rules fight each other.
- Changing bids too often without enough data.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations.md`

```markdown
---
title: "16.2 Bulk Operations"
page_id: "16-2"
section: "16. Automation, Rules & Scripts"
learner_level: "Applied"
topic_tags: ["automation"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 16.2 Bulk Operations

**What this page teaches:** Bulk files let you create and edit many campaigns, ad groups, keywords, targets, budgets, bids, and negatives at once.

**Explain it to a fresh graduate:** Bulk operations are powerful and mildly terrifying. One wrong upload can change hundreds of campaigns.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use backup downloads, versioned files, QA columns, small test uploads, and clear change logs.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation.md`

```markdown
---
title: "16.3 Custom Scripts & API-Based Automation"
page_id: "16-3"
section: "16. Automation, Rules & Scripts"
learner_level: "Applied"
topic_tags: ["automation"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 16.3 Custom Scripts & API-Based Automation

**What this page teaches:** The Amazon Ads API can pull reports and manage campaigns programmatically when access is approved.

**Explain it to a fresh graduate:** API work turns repeated console clicks into software. It is great for scale, but it needs validation.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use scripts for reporting, classification, alerts, and draft changes. Keep final execution human-approved for high-risk actions.

**Operator view:** Automation should apply rules consistently, but humans must set the strategy and guardrails.

**Practical workflow:**
- Define the exact decision rule.
- Set data thresholds and max change limits.
- Test on a low-risk scope.
- Review logs and exceptions.
- Keep human approval for high-impact actions.

**Worked mini-example:** A rule can lower bids when spend exceeds threshold and orders are zero, but it should not touch launch campaigns that are intentionally gathering data.

**Common beginner mistakes:**
- Automating before the process is understood.
- Letting rules fight each other.
- Changing bids too often without enough data.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management.md`

```markdown
---
title: "16.4 AI-Augmented PPC Management"
page_id: "16-4"
section: "16. Automation, Rules & Scripts"
learner_level: "Applied"
topic_tags: ["automation"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 16.4 AI-Augmented PPC Management

**What this page teaches:** AI can classify search terms, summarize reports, draft recommendations, and detect anomalies.

**Explain it to a fresh graduate:** AI is a helpful analyst, not the account owner. It can suggest. Humans approve.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use human-in-the-loop guardrails, evidence requirements, and rollback plans for AI-assisted changes.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/16-16-automation-rules-and-scripts/index.md`

```markdown
---
title: "16. Automation, Rules & Scripts"
page_type: section_overview
section_id: "16"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 16. Automation, Rules & Scripts

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[16.1 Native Amazon Automation]]
- [[16.2 Bulk Operations]]
- [[16.3 Custom Scripts & API-Based Automation]]
- [[16.4 AI-Augmented PPC Management]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites.md`

```markdown
---
title: "17.1 All-in-One Suites"
page_id: "17-1"
section: "17. Software & Tools Ecosystem"
learner_level: "Applied"
topic_tags: ["tools"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 17.1 All-in-One Suites

**What this page teaches:** Suites like Helium 10, Jungle Scout, SellerApp, Perpetua, Pacvue, and Teikametrics can combine research, automation, and reporting features.

**Explain it to a fresh graduate:** Tools save time, but each has blind spots. Do not outsource your brain to a dashboard with nice gradients.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build a living comparison table: research, bid automation, reporting, API access, cost, support, marketplace coverage.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions.md`

```markdown
---
title: "17.2 Point Solutions"
page_id: "17-2"
section: "17. Software & Tools Ecosystem"
learner_level: "Applied"
topic_tags: ["tools"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 17.2 Point Solutions

**What this page teaches:** Point solutions solve one job well, such as keyword research, bid automation, reporting, review tracking, or market intelligence.

**Explain it to a fresh graduate:** A point tool is like a specialist. Great at one thing, not always the whole workflow.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use when the team has a specific gap and an all-in-one platform would be too expensive or too broad.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy.md`

```markdown
---
title: "17.3 Build vs. Buy"
page_id: "17-3"
section: "17. Software & Tools Ecosystem"
learner_level: "Applied"
topic_tags: ["tools"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 17.3 Build vs. Buy

**What this page teaches:** Build internal tooling when workflows are unique, repeated, and strategically important. Buy when the need is standard and vendor tools already solve it well.

**Explain it to a fresh graduate:** Building is not free. You pay with time, maintenance, bugs, and future headaches wearing a tiny hat.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use a decision matrix: cost, speed, control, data ownership, maintenance, integrations, risk.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework.md`

```markdown
---
title: "17.4 Tool Evaluation Framework"
page_id: "17-4"
section: "17. Software & Tools Ecosystem"
learner_level: "Applied"
topic_tags: ["tools"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 17.4 Tool Evaluation Framework

**What this page teaches:** A tool should be judged by data accuracy, workflow fit, automation safety, reporting quality, user permissions, integrations, and total cost.

**Explain it to a fresh graduate:** The best tool is the one your team will actually use correctly.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Run a pilot with real tasks. Score before buying. Require export access and change logs.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/17-17-software-and-tools-ecosystem/index.md`

```markdown
---
title: "17. Software & Tools Ecosystem"
page_type: section_overview
section_id: "17"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 17. Software & Tools Ecosystem

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[17.1 All-in-One Suites]]
- [[17.2 Point Solutions]]
- [[17.3 Build vs. Buy]]
- [[17.4 Tool Evaluation Framework]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch.md`

```markdown
---
title: "18.1 New Product Launch"
page_id: "18-1"
section: "18. Strategy by Business Lifecycle Stage"
learner_level: "Advanced"
topic_tags: ["launch"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 18.1 New Product Launch

**What this page teaches:** Launch strategy accepts more learning cost to generate data, visibility, and early sales.

**Explain it to a fresh graduate:** A new product has little history. PPC helps test demand, discover terms, and support ranking.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use controlled auto, broad, phrase, exact seed campaigns, product targeting, and careful budget caps.

**Operator view:** Launch strategy balances learning, ranking, reviews, and budget control.

**Practical workflow:**
- Audit listing readiness.
- Define launch goals and acceptable [[ACOS]] range.
- Start discovery and exact control campaigns.
- Watch budget, terms, and [[CVR]] closely.
- Harvest winners and cut waste after thresholds.

**Worked mini-example:** A new product may tolerate higher [[ACOS]] during the first weeks if the goal is data collection and ranking support.

**Common beginner mistakes:**
- Expecting mature efficiency on day one.
- Launching without enough reviews or inventory.
- Changing everything before data stabilizes.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/18-18-strategy-by-business-lifecycle-stage/18-2-18-2-growth-stage.md`

```markdown
---
title: "18.2 Growth Stage"
page_id: "18-2"
section: "18. Strategy by Business Lifecycle Stage"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 18.2 Growth Stage

**What this page teaches:** Growth stage focuses on scaling proven winners and expanding coverage.

**Explain it to a fresh graduate:** Once the account knows what works, spend more where evidence is strong.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Increase budgets, expand exact winners, test SB/SD, add competitor targeting, and monitor [[TACOS]].

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/18-18-strategy-by-business-lifecycle-stage/18-3-18-3-mature-steady-state.md`

```markdown
---
title: "18.3 Mature/Steady-State"
page_id: "18-3"
section: "18. Strategy by Business Lifecycle Stage"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 18.3 Mature/Steady-State

**What this page teaches:** Mature accounts focus on efficiency, defense, incremental growth, and clean operations.

**Explain it to a fresh graduate:** The goal is not constant chaos. It is controlled improvement.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Reduce waste, protect branded terms, refine long-tail coverage, and improve placement and bid efficiency.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/18-18-strategy-by-business-lifecycle-stage/18-4-18-4-decline-sunset.md`

```markdown
---
title: "18.4 Decline/Sunset"
page_id: "18-4"
section: "18. Strategy by Business Lifecycle Stage"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 18.4 Decline/Sunset

**What this page teaches:** Declining products may need budget reduction, inventory liquidation support, or strategic pause.

**Explain it to a fresh graduate:** Not every product deserves more ad spend. Sometimes the smart move is to stop feeding the zombie SKU.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Lower bids, reduce budget, focus on liquidation keywords, or pause if margin and inventory do not support ads.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/18-18-strategy-by-business-lifecycle-stage/index.md`

```markdown
---
title: "18. Strategy by Business Lifecycle Stage"
page_type: section_overview
section_id: "18"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 18. Strategy by Business Lifecycle Stage

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[18.1 New Product Launch]]
- [[18.2 Growth Stage]]
- [[18.3 Mature/Steady-State]]
- [[18.4 Decline/Sunset]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/19-19-strategy-by-product-category/19-1-19-1-high-consideration-high-price-categories.md`

```markdown
---
title: "19.1 High-Consideration / High-Price Categories"
page_id: "19-1"
section: "19. Strategy by Product Category"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 19.1 High-Consideration / High-Price Categories

**What this page teaches:** Expensive or complex products often need more education, longer decision time, and stronger content.

**Explain it to a fresh graduate:** A shopper buying a $400 item behaves differently from someone buying a $9 sponge.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use richer content, SB video, retargeting, comparison pages, and longer attribution thinking.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/19-19-strategy-by-product-category/19-2-19-2-low-price-impulse-categories.md`

```markdown
---
title: "19.2 Low-Price / Impulse Categories"
page_id: "19-2"
section: "19. Strategy by Product Category"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 19.2 Low-Price / Impulse Categories

**What this page teaches:** Low-price products need tight [[CPC]] control because profit per sale is small.

**Explain it to a fresh graduate:** Cheap products cannot afford expensive clicks unless conversion is excellent or repeat purchase value is strong.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use strict bids, bundles, coupons, high-[[CVR]] terms, and careful waste control.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/19-19-strategy-by-product-category/19-3-19-3-seasonal-gift-categories.md`

```markdown
---
title: "19.3 Seasonal/Gift Categories"
page_id: "19-3"
section: "19. Strategy by Product Category"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 19.3 Seasonal/Gift Categories

**What this page teaches:** Seasonal products require early preparation, aggressive event pacing, and fast post-season wind-down.

**Explain it to a fresh graduate:** Timing matters. If you optimize after the season, congratulations, you are now ready for last year.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Plan keywords, budgets, deals, inventory, creative, and reporting before the demand spike.

**Operator view:** Seasonal planning prevents last-minute budget chaos and inventory-aware mistakes.

**Practical workflow:**
- Identify event dates and lead-in period.
- Forecast spend and inventory needs.
- Prepare campaigns and creatives early.
- Scale bids and budgets gradually.
- Wind down after the event and analyze learnings.

**Worked mini-example:** Prime Day planning should include pre-event ranking work, event-day monitoring, and post-event harvesting and budget normalization.

**Common beginner mistakes:**
- Increasing budgets only on event day.
- Ignoring inventory limits.
- Forgetting post-event cleanup.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/19-19-strategy-by-product-category/19-4-19-4-regulated-categories.md`

```markdown
---
title: "19.4 Regulated Categories"
page_id: "19-4"
section: "19. Strategy by Product Category"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 19.4 Regulated Categories

**What this page teaches:** Regulated categories such as supplements or restricted goods face stricter claims, approvals, and policy review.

**Explain it to a fresh graduate:** Ads can be rejected because of wording, claims, images, or category rules.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Review policy before launch. Avoid medical, exaggerated, or unsupported claims.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/19-19-strategy-by-product-category/index.md`

```markdown
---
title: "19. Strategy by Product Category"
page_type: section_overview
section_id: "19"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 19. Strategy by Product Category

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[19.1 High-Consideration / High-Price Categories]]
- [[19.2 Low-Price / Impulse Categories]]
- [[19.3 Seasonal/Gift Categories]]
- [[19.4 Regulated Categories]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/20-20-seasonal-and-event-planning/20-1-20-1-prime-day-playbook.md`

```markdown
---
title: "20.1 Prime Day Playbook"
page_id: "20-1"
section: "20. Seasonal & Event Planning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 20.1 Prime Day Playbook

**What this page teaches:** Prime Day planning covers pre-event ramp, event-day spend and bid control, and post-event retargeting or cleanup.

**Explain it to a fresh graduate:** Prime Day is not one day of work. It is a campaign season wearing a sale sticker.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Prepare 3-6 weeks ahead: inventory, deals, budgets, bids, Store pages, SB video, defensive coverage.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/20-20-seasonal-and-event-planning/20-2-20-2-q4-holiday-playbook.md`

```markdown
---
title: "20.2 Q4 / Holiday Playbook"
page_id: "20-2"
section: "20. Seasonal & Event Planning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 20.2 Q4 / Holiday Playbook

**What this page teaches:** Q4 includes Black Friday, Cyber Monday, gifting, shipping cutoffs, and post-holiday behavior.

**Explain it to a fresh graduate:** Q4 rewards prepared accounts and punishes messy ones loudly.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use inventory-aware scaling, daily pacing checks, holiday keyword expansion, and post-event budget normalization.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/20-20-seasonal-and-event-planning/20-3-20-3-other-key-dates.md`

```markdown
---
title: "20.3 Other Key Dates"
page_id: "20-3"
section: "20. Seasonal & Event Planning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 20.3 Other Key Dates

**What this page teaches:** Other events include Back to School, Spring Cleaning, summer, Mother's Day, Father's Day, category launches, and local marketplace events.

**Explain it to a fresh graduate:** Every category has its own weather pattern. Learn yours.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build a seasonal calendar by marketplace, category, promo window, content deadline, and budget plan.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/20-20-seasonal-and-event-planning/index.md`

```markdown
---
title: "20. Seasonal & Event Planning"
page_type: section_overview
section_id: "20"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 20. Seasonal & Event Planning

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[20.1 Prime Day Playbook]]
- [[20.2 Q4 / Holiday Playbook]]
- [[20.3 Other Key Dates]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/21-21-international-and-multi-marketplace-ppc/21-1-21-1-marketplace-differences.md`

```markdown
---
title: "21.1 Marketplace Differences"
page_id: "21-1"
section: "21. International & Multi-Marketplace PPC"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 21.1 Marketplace Differences

**What this page teaches:** Marketplaces differ by language, currency, [[CPC]], competition, shopper behavior, ad features, and policy details.

**Explain it to a fresh graduate:** Copying US campaigns into Germany without localization is not strategy. It is international copy-paste with extra steps.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Research each marketplace separately. Translate intent, not just words.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/21-21-international-and-multi-marketplace-ppc/21-2-21-2-cross-marketplace-account-structure.md`

```markdown
---
title: "21.2 Cross-Marketplace Account Structure"
page_id: "21-2"
section: "21. International & Multi-Marketplace PPC"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 21.2 Cross-Marketplace Account Structure

**What this page teaches:** Brands can manage markets centrally or locally depending on team setup, language needs, and budget ownership.

**Explain it to a fresh graduate:** Centralized control gives consistency. Localized control gives nuance. Most mature teams need both.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use global naming standards with local keyword research and local performance targets.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/21-21-international-and-multi-marketplace-ppc/21-3-21-3-localization-considerations.md`

```markdown
---
title: "21.3 Localization Considerations"
page_id: "21-3"
section: "21. International & Multi-Marketplace PPC"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 21.3 Localization Considerations

**What this page teaches:** Localization means adapting keywords, copy, content, seasonality, and shopper assumptions to the market.

**Explain it to a fresh graduate:** A direct translation may miss how real shoppers search.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use native speakers, local autocomplete, local competitor listings, marketplace reports, and language-specific negatives.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/21-21-international-and-multi-marketplace-ppc/index.md`

```markdown
---
title: "21. International & Multi-Marketplace PPC"
page_type: section_overview
section_id: "21"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 21. International & Multi-Marketplace PPC

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[21.1 Marketplace Differences]]
- [[21.2 Cross-Marketplace Account Structure]]
- [[21.3 Localization Considerations]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/22-22-agency-and-team-operations/22-1-22-1-team-roles-and-raci.md`

```markdown
---
title: "22.1 Team Roles & RACI"
page_id: "22-1"
section: "22. Agency & Team Operations"
learner_level: "Foundational"
topic_tags: ["operations"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 22.1 Team Roles & RACI

**What this page teaches:** RACI defines who is responsible, accountable, consulted, and informed for PPC work.

**Explain it to a fresh graduate:** Clear roles stop the classic team sport of 'I thought someone else did it.'

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Define Strategist, Analyst, VA/Executor, Account Manager, QA reviewer, and escalation owner.

**Operator view:** Team operations protect quality, accountability, and repeatability.

**Practical workflow:**
- Define owner, reviewer, and approver.
- Document inputs and outputs.
- Use checklists for recurring work.
- Log changes and decisions.
- Review mistakes in a blameless post-mortem.

**Worked mini-example:** A VA mines search terms, a strategist reviews the recommendations, and a QA reviewer checks the bulk file before upload.

**Common beginner mistakes:**
- Relying on memory instead of SOPs.
- Letting juniors make high-risk changes without review.
- Not documenting client-specific rules.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/22-22-agency-and-team-operations/22-2-22-2-sops-and-workflow-documentation.md`

```markdown
---
title: "22.2 SOPs & Workflow Documentation"
page_id: "22-2"
section: "22. Agency & Team Operations"
learner_level: "Foundational"
topic_tags: ["operations"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 22.2 SOPs & Workflow Documentation

**What this page teaches:** SOPs standardize repeated tasks like weekly optimization, search term mining, budget checks, and reporting.

**Explain it to a fresh graduate:** A good SOP lets a new hire do the task without guessing or asking five people in Slack.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Write SOPs with purpose, inputs, steps, decision rules, QA checks, output, owner, and change log.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/22-22-agency-and-team-operations/22-3-22-3-va-training-and-enablement.md`

```markdown
---
title: "22.3 VA Training & Enablement"
page_id: "22-3"
section: "22. Agency & Team Operations"
learner_level: "Foundational"
topic_tags: ["operations"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 22.3 VA Training & Enablement

**What this page teaches:** VA training should teach concepts, console navigation, daily tasks, QA discipline, and escalation rules.

**Explain it to a fresh graduate:** A VA should not only click buttons. They should understand why the click matters.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build a 5-day bootcamp: foundations, campaign types, targeting, search terms, negatives, metrics, reporting, capstone.

**Operator view:** Training assets turn the wiki into repeatable onboarding. Each page should teach, test, and support real work.

**Practical workflow:**
- Create a learning aid.
- Create a quiz with explanations.
- Create a teaching guide for instructors.
- Create a handout for live work.
- Tag by level, role, time, and prerequisites.

**Worked mini-example:** A targeting page can include a flowchart, a 10-question quiz, and a practice exercise using a fake Search Term Report.

**Common beginner mistakes:**
- Writing only prose with no practice.
- Testing memory instead of judgment.
- Skipping answer explanations.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/22-22-agency-and-team-operations/22-4-22-4-qa-and-review-process.md`

```markdown
---
title: "22.4 QA & Review Process"
page_id: "22-4"
section: "22. Agency & Team Operations"
learner_level: "Foundational"
topic_tags: ["operations"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 22.4 QA & Review Process

**What this page teaches:** QA prevents harmful changes by reviewing bids, budgets, negatives, bulk files, and reports before execution.

**Explain it to a fresh graduate:** In PPC, small mistakes can spend real money. QA is not bureaucracy; it is a seatbelt.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use peer review for high-impact changes, bulk upload previews, before/after logs, and rollback plans.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

### Change-log template

| Field | Example |
|---|---|
| Date | 2026-07-05 |
| Changed by | Operator name |
| Campaign | Running Shoes - Exact |
| Change type | Bid adjustment |
| Old value | $0.75 |
| New value | $0.85 |
| Reason | ACOS below target with strong orders |
| Follow-up result | Review after 7 days |

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/22-22-agency-and-team-operations/index.md`

```markdown
---
title: "22. Agency & Team Operations"
page_type: section_overview
section_id: "22"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 22. Agency & Team Operations

This cluster contains 4 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[22.1 Team Roles & RACI]]
- [[22.2 SOPs & Workflow Documentation]]
- [[22.3 VA Training & Enablement]]
- [[22.4 QA & Review Process]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/23-23-client-and-stakeholder-communication/23-1-23-1-reporting-cadence.md`

```markdown
---
title: "23.1 Reporting Cadence"
page_id: "23-1"
section: "23. Client & Stakeholder Communication"
learner_level: "Foundational"
topic_tags: ["communication", "reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 23.1 Reporting Cadence

**What this page teaches:** Reporting cadence defines weekly, monthly, and quarterly communication rhythms.

**Explain it to a fresh graduate:** Clients should not wonder what is happening. Silence creates anxiety faster than a campaign with 80% [[ACOS]].

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use weekly action summaries, monthly performance narratives, and quarterly strategy reviews.

**Operator view:** Reports turn raw PPC activity into decisions. The best report explains what happened, why it happened, and what happens next.

**Practical workflow:**
- Choose the right report for the question.
- Clean and label the data.
- Compare against target and previous period.
- Find the root cause, not only the metric movement.
- Write the action plan with owner and deadline.

**Worked mini-example:** Instead of saying [[ACOS]] rose from 25% to 32%, explain that [[CPC]] rose on two non-branded exact campaigns while conversion dropped after price increased.

**Common beginner mistakes:**
- Sending tables without interpretation.
- Mixing attribution windows or date ranges.
- Reporting only ad metrics when stakeholders need business impact.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/23-23-client-and-stakeholder-communication/23-2-23-2-setting-expectations.md`

```markdown
---
title: "23.2 Setting Expectations"
page_id: "23-2"
section: "23. Client & Stakeholder Communication"
learner_level: "Foundational"
topic_tags: ["communication"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 23.2 Setting Expectations

**What this page teaches:** Expectation-setting explains volatility, launch learning periods, budget limits, and what PPC can or cannot fix.

**Explain it to a fresh graduate:** A launch campaign may run inefficiently while collecting data. That does not always mean failure.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Explain target [[ACOS]], break-even [[ACOS]], testing budget, timeline, and leading indicators before campaigns go live.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/23-23-client-and-stakeholder-communication/23-3-23-3-handling-difficult-conversations.md`

```markdown
---
title: "23.3 Handling Difficult Conversations"
page_id: "23-3"
section: "23. Client & Stakeholder Communication"
learner_level: "Foundational"
topic_tags: ["communication"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 23.3 Handling Difficult Conversations

**What this page teaches:** Difficult conversations cover underperformance, inventory issues, listing problems, margin constraints, and goal changes.

**Explain it to a fresh graduate:** Trust grows when you explain problems clearly and bring a plan, not excuses.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use: what happened, evidence, root cause, action plan, owner, deadline, expected trade-off.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

### Underperformance script

Performance is below target this month. The main cause is specific and measurable: higher CPC, lower CVR, inventory gaps, listing issues, or stronger competitor promotions. The action plan is to protect proven terms, reduce waste, and review the account again after enough new data has collected.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/23-23-client-and-stakeholder-communication/index.md`

```markdown
---
title: "23. Client & Stakeholder Communication"
page_type: section_overview
section_id: "23"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 23. Client & Stakeholder Communication

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[23.1 Reporting Cadence]]
- [[23.2 Setting Expectations]]
- [[23.3 Handling Difficult Conversations]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/24-24-compliance-policy-and-account-health/24-1-24-1-advertising-policy-basics.md`

```markdown
---
title: "24.1 Advertising Policy Basics"
page_id: "24-1"
section: "24. Compliance, Policy & Account Health"
learner_level: "Advanced"
topic_tags: ["policy"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 24.1 Advertising Policy Basics

**What this page teaches:** Ad policy controls claims, prohibited content, trademarks, restricted products, creative rules, and landing page compliance.

**Explain it to a fresh graduate:** A strong ad that violates policy is still a rejected ad.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Check claims, images, category rules, prohibited words, trademark use, and landing page accuracy.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/24-24-compliance-policy-and-account-health/24-2-24-2-account-health-interplay.md`

```markdown
---
title: "24.2 Account Health Interplay"
page_id: "24-2"
section: "24. Compliance, Policy & Account Health"
learner_level: "Advanced"
topic_tags: ["policy"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 24.2 Account Health Interplay

**What this page teaches:** Account health problems can affect advertising eligibility and product visibility.

**Explain it to a fresh graduate:** Sometimes ads stop because the account or listing has a health issue, not because the campaign manager broke something.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Monitor suppressed listings, inventory, policy warnings, Buy Box, shipping, product condition, and category approval.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/24-24-compliance-policy-and-account-health/24-3-24-3-competitor-and-ethical-boundaries.md`

```markdown
---
title: "24.3 Competitor & Ethical Boundaries"
page_id: "24-3"
section: "24. Compliance, Policy & Account Health"
learner_level: "Advanced"
topic_tags: ["policy"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 24.3 Competitor & Ethical Boundaries

**What this page teaches:** Competitor targeting can be legal and useful, but misleading copy, trademark misuse, and false claims create risk.

**Explain it to a fresh graduate:** Aggressive is not the same as reckless. PPC is not a pirate ship, sadly.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use competitor ASIN/category targeting ethically. Avoid using protected brand names in ad copy unless allowed.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/24-24-compliance-policy-and-account-health/index.md`

```markdown
---
title: "24. Compliance, Policy & Account Health"
page_type: section_overview
section_id: "24"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 24. Compliance, Policy & Account Health

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[24.1 Advertising Policy Basics]]
- [[24.2 Account Health Interplay]]
- [[24.3 Competitor & Ethical Boundaries]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/25-25-advanced-and-emerging-topics/25-1-25-1-retail-media-network-trends.md`

```markdown
---
title: "25.1 Retail Media Network Trends"
page_id: "25-1"
section: "25. Advanced & Emerging Topics"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 25.1 Retail Media Network Trends

**What this page teaches:** Retail media includes ad platforms from retailers like Amazon, Walmart, Target, Instacart, and others.

**Explain it to a fresh graduate:** Amazon PPC skills transfer, but each retail network has its own data, rules, and ad products.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Compare inventory, attribution, audience data, reporting, self-service access, and shopper journey.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/25-25-advanced-and-emerging-topics/25-2-25-2-ai-s-growing-role-in-amazon-ads.md`

```markdown
---
title: "25.2 AI's Growing Role in Amazon Ads"
page_id: "25-2"
section: "25. Advanced & Emerging Topics"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 25.2 AI's Growing Role in Amazon Ads

**What this page teaches:** AI is increasingly used for creative generation, campaign suggestions, bidding, reporting, and predictive optimization.

**Explain it to a fresh graduate:** AI can speed up work, but weak prompts and bad data still produce bad decisions faster.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Track Amazon's native AI features, third-party automation, and internal AI workflows with approval guardrails.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/25-25-advanced-and-emerging-topics/25-3-25-3-privacy-and-signal-loss.md`

```markdown
---
title: "25.3 Privacy & Signal Loss"
page_id: "25-3"
section: "25. Advanced & Emerging Topics"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 25.3 Privacy & Signal Loss

**What this page teaches:** Privacy changes reduce some tracking signals and increase the value of first-party data and clean-room measurement.

**Explain it to a fresh graduate:** Marketers are losing some old tracking shortcuts. Better data discipline matters more now.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Invest in first-party audiences, [[Amazon Marketing Cloud]], incrementality thinking, and reporting that does not rely on one fragile metric.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/25-25-advanced-and-emerging-topics/index.md`

```markdown
---
title: "25. Advanced & Emerging Topics"
page_type: section_overview
section_id: "25"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 25. Advanced & Emerging Topics

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[25.1 Retail Media Network Trends]]
- [[25.2 AI's Growing Role in Amazon Ads]]
- [[25.3 Privacy & Signal Loss]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/26-26-career-certification-and-learning/26-1-26-1-certifications.md`

```markdown
---
title: "26.1 Certifications"
page_id: "26-1"
section: "26. Career, Certification & Learning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 26.1 Certifications

**What this page teaches:** Amazon Ads Academy offers learning paths and certifications that validate Amazon Ads knowledge.

**Explain it to a fresh graduate:** Certifications help prove basic knowledge, but real skill comes from managing accounts and explaining decisions.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Start with beginner certifications, then Sponsored Ads, measurement, retail, DSP, and [[Amazon Marketing Cloud]] tracks as role requires.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/26-26-career-certification-and-learning/26-2-26-2-career-pathing.md`

```markdown
---
title: "26.2 Career Pathing"
page_id: "26-2"
section: "26. Career, Certification & Learning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 26.2 Career Pathing

**What this page teaches:** Career progression can move from VA or Junior Analyst to PPC Specialist, Strategist, Team Lead, and Agency Owner.

**Explain it to a fresh graduate:** Each level adds judgment, communication, ownership, and risk management.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Create a skills matrix: console navigation, reporting, search terms, bidding, strategy, client communication, leadership.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/26-26-career-certification-and-learning/26-3-26-3-continuing-education.md`

```markdown
---
title: "26.3 Continuing Education"
page_id: "26-3"
section: "26. Career, Certification & Learning"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 26.3 Continuing Education

**What this page teaches:** Continuing education includes Amazon updates, communities, newsletters, conferences, case studies, and internal post-mortems.

**Explain it to a fresh graduate:** PPC is not a one-time course. Amazon changes. Competitors change. Shoppers change. Your brain must update too.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Maintain a monthly learning log and quarterly wiki update review.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/26-26-career-certification-and-learning/index.md`

```markdown
---
title: "26. Career, Certification & Learning"
page_type: section_overview
section_id: "26"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 26. Career, Certification & Learning

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[26.1 Certifications]]
- [[26.2 Career Pathing]]
- [[26.3 Continuing Education]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/27-27-case-studies-and-templates/27-1-27-1-case-study-template.md`

```markdown
---
title: "27.1 Case Study Template"
page_id: "27-1"
section: "27. Case Studies & Templates"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 27.1 Case Study Template

**What this page teaches:** A case study should follow situation, strategy, execution, results, and lessons.

**Explain it to a fresh graduate:** Case studies teach judgment. They show why a decision worked, not just what button was clicked.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Template: context, problem, constraints, analysis, actions, results, what changed, what to repeat.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates.md`

```markdown
---
title: "27.2 Downloadable Templates"
page_id: "27-2"
section: "27. Case Studies & Templates"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 27.2 Downloadable Templates

**What this page teaches:** Templates include campaign structure sheets, optimization checklists, client reports, naming cheat sheets, QA logs, and bulk upload trackers.

**Explain it to a fresh graduate:** Templates turn knowledge into action. They reduce memory load for beginners.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Build templates in Sheets, DOCX, PDF, and app-ready JSON where useful.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/27-27-case-studies-and-templates/27-3-27-3-real-case-studies.md`

```markdown
---
title: "27.3 Real Case Studies"
page_id: "27-3"
section: "27. Case Studies & Templates"
learner_level: "Advanced"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 27.3 Real Case Studies

**What this page teaches:** Real case studies should be tagged by category, lifecycle stage, problem type, and skill level.

**Explain it to a fresh graduate:** A beginner learns faster from realistic examples than abstract rules.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Add cases like [[ACOS]] spike, launch learning period, wasted spend cleanup, branded defense, budget starvation, and listing-[[CVR]] issue.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/27-27-case-studies-and-templates/index.md`

```markdown
---
title: "27. Case Studies & Templates"
page_type: section_overview
section_id: "27"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 27. Case Studies & Templates

This cluster contains 3 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[27.1 Case Study Template]]
- [[27.2 Downloadable Templates]]
- [[27.3 Real Case Studies]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/28-28-glossary-and-acronyms/index.md`

```markdown
---
title: "28. Glossary & Acronyms"
page_type: section_overview
section_id: "28"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 28. Glossary & Acronyms

This cluster contains 1 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

The glossary is the learner safety net. Keep terms short, concrete, and linked to the page where the term becomes operational.

## Pages in this section

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The glossary is the beginner's decoder ring. Every acronym should have a short definition, long definition, related terms, and first appearance.

### Core acronyms

| Term | Meaning |
|---|---|
| ACOS | Advertising Cost of Sales: Spend / Ad Sales |
| TACOS | Total Advertising Cost of Sales: Spend / Total Sales |
| ROAS | Return on Ad Spend: Ad Sales / Spend |
| CTR | Click-Through Rate: Clicks / Impressions |
| CVR | Conversion Rate: Orders / Clicks |
| CPC | Cost Per Click: Spend / Clicks |
| SP | Sponsored Products |
| SB | Sponsored Brands |
| SD | Sponsored Display |
| STV | Sponsored TV |
| DSP | Demand Side Platform |
| AMC | Amazon Marketing Cloud |
| SQP | Search Query Performance |

### Beginner rule

Define every acronym the first time it appears on a page. Do not make a fresh graduate play acronym bingo.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/29-29-appendix-formulas-and-calculators/index.md`

```markdown
---
title: "29. Appendix: Formulas & Calculators"
page_type: section_overview
section_id: "29"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 29. Appendix: Formulas & Calculators

This cluster contains 1 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

Use these formulas as calculators inside the wiki or simulator. Always explain the business meaning beside the math.

## Pages in this section

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

Formulas turn PPC into controllable math. Every calculator should show inputs, formula, example, and interpretation.

### Key formulas

`ACOS = Ad Spend / Ad Sales`

`ROAS = Ad Sales / Ad Spend`

`TACOS = Ad Spend / Total Sales`

`Break-even ACOS = Gross Profit / Price`

`Target Bid = Price x Conversion Rate x Target ACOS`

### Harvesting rule starter

Harvest a search term when it has enough clicks, enough orders, and ACOS at or below target. A starter rule is 50+ clicks, 5+ orders, and ACOS under target, but the threshold should change by price, category, and conversion rate.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/30-30-meta-changelog/30-30-meta-changelog.md`

```markdown
---
title: "30. Meta / Changelog"
page_id: "30"
section: "30. Meta / Changelog"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 30. Meta / Changelog

**What this page teaches:** This section records version history, Amazon updates, stale pages, open questions, and review status.

**Explain it to a fresh graduate:** A changelog tells future readers what changed and why. It is boring until the day it saves you from confusion.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use fields: date, version, page, change summary, source, reviewer, impact, next review date.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The changelog protects trust. Amazon changes features, policies, reports, and console layouts often. Track changes so learners know what is current.

### Version history example

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-07-05 | Merged complete data-filled guide into section pages |
| 2.4 | 2026-07-05 | Added complete sections, examples, and schemas |
| 2.0 | 2026-01-01 | Major rewrite and training layer added |
| 1.0 | 2025-07-01 | Initial version |

### Update policy

Every page that describes a live console workflow should include a verification date. If unsure, tag it `[Stale?]` and assign review.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/30-30-meta-changelog/index.md`

```markdown
---
title: "30. Meta / Changelog"
page_type: section_overview
section_id: "30"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 30. Meta / Changelog

This cluster contains 1 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[30. Meta / Changelog]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The changelog protects trust. Amazon changes features, policies, reports, and console layouts often. Track changes so learners know what is current.

### Version history example

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-07-05 | Merged complete data-filled guide into section pages |
| 2.4 | 2026-07-05 | Added complete sections, examples, and schemas |
| 2.0 | 2026-01-01 | Major rewrite and training layer added |
| 1.0 | 2025-07-01 | Initial version |

### Update policy

Every page that describes a live console workflow should include a verification date. If unsure, tag it `[Stale?]` and assign review.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-1-31-1-learning-aid.md`

```markdown
---
title: "31.1 Learning Aid"
page_id: "31-1"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.1 Learning Aid

**What this page teaches:** Each core page should have a one-page visual summary, key terms, common mistakes, and a worked example.

**Explain it to a fresh graduate:** This turns a wiki page into a training asset.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use diagrams, flowcharts, annotated console screenshots, and mini scenarios with numbers.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-2-31-2-quiz.md`

```markdown
---
title: "31.2 Quiz"
page_id: "31-2"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.2 Quiz

**What this page teaches:** Each topic should include 5-10 questions with answer keys and short explanations.

**Explain it to a fresh graduate:** Quizzes prove whether the learner can apply the idea, not just nod politely.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Mix multiple-choice, scenario judgment, and calculation questions. Tag difficulty.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Sample quiz questions

1. Which match type gives the most impressions? Answer: Broad.
2. Which match type is most precise? Answer: Exact.
3. What is the main risk of Broad match? Answer: irrelevant spend.
4. Why add negatives after harvesting? Answer: to prevent duplicate spend and keep discovery campaigns clean.
5. What does ACOS measure? Answer: ad spend efficiency against ad-attributed sales.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-3-31-3-teaching-guide.md`

```markdown
---
title: "31.3 Teaching Guide"
page_id: "31-3"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.3 Teaching Guide

**What this page teaches:** The teaching guide helps trainers deliver the topic consistently.

**Explain it to a fresh graduate:** A trainer should know what to explain, demo, ask, and assign.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Include timing, talking points, live-demo checklist, discussion prompts, and links to quiz and handout.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-4-31-4-handout.md`

```markdown
---
title: "31.4 Handout"
page_id: "31-4"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.4 Handout

**What this page teaches:** A handout is a printable job aid used while working inside the Ads Console.

**Explain it to a fresh graduate:** The learner should be able to keep it open while doing the task.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Include definition, formula, checklist, common mistakes, and QR/link back to full page.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-5-31-5-tagging-and-assembly-system.md`

```markdown
---
title: "31.5 Tagging & Assembly System"
page_id: "31-5"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.5 Tagging & Assembly System

**What this page teaches:** Tags let you assemble custom curricula by topic, level, format, and estimated time.

**Explain it to a fresh graduate:** This makes the wiki modular. You can build a VA bootcamp without rewriting content.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use tags: Topic, Learner Level, Format, Estimated Time, Prerequisites, Role.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-6-31-6-rollout-priority.md`

```markdown
---
title: "31.6 Rollout Priority"
page_id: "31-6"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.6 Rollout Priority

**What this page teaches:** Not every topic needs full training treatment on day one. Start where new hires need the most help.

**Explain it to a fresh graduate:** Build the airport runway before the luxury lounge.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Prioritize Sections 1-4, then 5-9, then 10-11, then 22, then advanced tracks.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/31-7-31-7-assessment-and-certification-tie-in.md`

```markdown
---
title: "31.7 Assessment & Certification Tie-In"
page_id: "31-7"
section: "31. Training Layer Template"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 31.7 Assessment & Certification Tie-In

**What this page teaches:** Assessments should combine topic quizzes, capstone scenarios, role checklists, and retake rules.

**Explain it to a fresh graduate:** Certification should prove readiness to touch real accounts safely.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Define pass threshold, retake policy, practical task review, and role-level competency checklist.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/31-31-training-layer-template/index.md`

```markdown
---
title: "31. Training Layer Template"
page_type: section_overview
section_id: "31"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 31. Training Layer Template

This cluster contains 7 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[31.1 Learning Aid]]
- [[31.2 Quiz]]
- [[31.3 Teaching Guide]]
- [[31.4 Handout]]
- [[31.5 Tagging & Assembly System]]
- [[31.6 Rollout Priority]]
- [[31.7 Assessment & Certification Tie-In]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-1-32-1-content-as-data-separation.md`

```markdown
---
title: "32.1 Content-as-Data Separation"
page_id: "32-1"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.1 Content-as-Data Separation

**What this page teaches:** Wiki content should be human-readable and app-readable.

**Explain it to a fresh graduate:** If the Console Simulator or quiz app needs it, store it as structured data, not only paragraphs.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use markdown plus JSON/YAML frontmatter or database rows for quizzes, glossary, scenarios, and progress.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-2-32-2-standardized-schemas.md`

```markdown
---
title: "32.2 Standardized Schemas"
page_id: "32-2"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.2 Standardized Schemas

**What this page teaches:** Schemas define how each content object should be stored.

**Explain it to a fresh graduate:** A schema is a container shape. Without it, apps cannot reliably use the content.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Define quiz, glossary, scenario, learner progress, page metadata, asset manifest, and prerequisite schemas.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Required schemas

Store quiz questions, glossary terms, simulator scenarios, learner progress, formulas, and asset manifests as structured JSON or YAML. Any content the simulator, LMS, interview lab, or reporting engine might render later needs a schema now.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-3-32-3-simulator-scenario-bank.md`

```markdown
---
title: "32.3 Simulator Scenario Bank"
page_id: "32-3"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.3 Simulator Scenario Bank

**What this page teaches:** Scenario banks store fake but realistic campaign states for training apps.

**Explain it to a fresh graduate:** A trainee should practice decisions without risking real ad spend. Beautiful concept. Wallet-safe too.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Each scenario needs before state, correct actions, common mistakes, scoring rubric, and linked wiki topics.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-4-32-4-asset-library-with-naming-convention.md`

```markdown
---
title: "32.4 Asset Library with Naming Convention"
page_id: "32-4"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.4 Asset Library with Naming Convention

**What this page teaches:** Assets include screenshots, diagrams, flowcharts, and annotated console captures.

**Explain it to a fresh graduate:** If files are named randomly, future updates become archaeology.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Use names like section-topic-assettype-version.png and maintain an asset manifest.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-5-32-5-content-versioning-and-sync-contract.md`

```markdown
---
title: "32.5 Content Versioning & Sync Contract"
page_id: "32-5"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.5 Content Versioning & Sync Contract

**What this page teaches:** Define whether the wiki updates first or the app updates first, and how changes sync.

**Explain it to a fresh graduate:** Without versioning, the app may teach old information while the wiki says something new.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Add last_verified_against_live_console, source_url, schema_version, and review_owner fields.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-6-32-6-api-export-layer.md`

```markdown
---
title: "32.6 API/Export Layer"
page_id: "32-6"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.6 API/Export Layer

**What this page teaches:** The wiki should export structured content to apps through API, database, or scheduled JSON files.

**Explain it to a fresh graduate:** Do not scrape pages later if you can design clean exports now.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Create export endpoints or scheduled jobs for quizzes, glossary, scenarios, assets, and prerequisite graph.

**Operator view:** API work is for scaling reporting and campaign management programmatically. It requires permissions, documentation, and validation.

**Practical workflow:**
- Define the use case and endpoint.
- Confirm account authorization.
- Request reports or campaign objects.
- Validate results against the Ads Console.
- Log every automated write action.

**Worked mini-example:** An internal tool can pull daily targeting reports and flag wasted spend, while a human approves the final negative keyword upload.

**Common beginner mistakes:**
- Writing changes through the API without backup.
- Assuming API fields always match UI labels.
- Skipping rate limits and error handling.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-7-32-7-difficulty-and-progression-graph.md`

```markdown
---
title: "32.7 Difficulty & Progression Graph"
page_id: "32-7"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.7 Difficulty & Progression Graph

**What this page teaches:** A progression graph stores prerequisites between topics.

**Explain it to a fresh graduate:** Some lessons depend on earlier lessons. You should not teach placement modifiers before the learner knows bids.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Store as topic_id plus prerequisite_ids. Use it to unlock lessons and build curricula.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/32-8-32-8-multi-consumer-design.md`

```markdown
---
title: "32.8 Multi-Consumer Design"
page_id: "32-8"
section: "32. App-Building Layer"
learner_level: "Foundational"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---
# 32.8 Multi-Consumer Design

**What this page teaches:** The same content should support the wiki, simulator, quiz UI, reports, and future tools.

**Explain it to a fresh graduate:** Write once, reuse many times. That is the whole trick.

**Why this matters in real accounts:** This topic affects money, visibility, campaign control, reporting clarity, or team execution. A beginner should understand the business reason before learning the console clicks.

**What to build into the wiki:** Design schemas for at least three consumers from day one: wiki, simulator, quiz engine.

**Operator view:** Use this page to understand the decision the topic supports, the data needed before acting, and the safest first move for a beginner.

**Practical workflow:**
- Read the definition and linked glossary terms.
- Identify what decision this topic affects.
- Find the report, console screen, or input data required.
- Make a small reversible change first when working in a live account.
- Write down what changed and why.

**Worked mini-example:** A junior operator reviews the page, opens the correct report, checks the required metric, makes one controlled change, and records it in the change log.

**Common beginner mistakes:**
- Skipping the context and copying tactics blindly.
- Changing a live account without checking eligibility, budget, or data window.
- Forgetting to log the reason behind the change.

**Definition of done:**
- The learner can explain the topic without jargon.
- The learner can name the report, console area, or data input used for this topic.
- The learner can describe one safe action, one risky action, and one escalation trigger.

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/32-32-app-building-layer/index.md`

```markdown
---
title: "32. App-Building Layer"
page_type: section_overview
section_id: "32"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---
# 32. App-Building Layer

This cluster contains 8 wiki page entries. Read it as a mini-module: learn the concept, see the operator workflow, then practice with a report, campaign draft, or simulator scenario.

## Pages in this section

- [[32.1 Content-as-Data Separation]]
- [[32.2 Standardized Schemas]]
- [[32.3 Simulator Scenario Bank]]
- [[32.4 Asset Library with Naming Convention]]
- [[32.5 Content Versioning & Sync Contract]]
- [[32.6 API/Export Layer]]
- [[32.7 Difficulty & Progression Graph]]
- [[32.8 Multi-Consumer Design]]

---

## Merged from Complete Data-Filled Guide
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.

### Operator checklist

- Explain the topic in plain English.
- Identify the report, console area, or input data needed.
- Make the smallest safe change first.
- Log the action, reason, and expected review date.
- Escalate if the issue touches policy, inventory, account health, or large budget changes.
```

---

## File: `docs/sections/zz-capstone-practice-scenarios/index.md`

```markdown
---
title: "Capstone Practice Scenarios"
page_type: section_overview
section_id: "capstone-practice-scenarios"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# Capstone Practice Scenarios

- Broad match wasted spend: A broad campaign spends $80 with 42 clicks, zero orders, and three irrelevant search terms. Learner must classify terms, choose negatives, and decide whether to lower bid.
- Budget-starved winner: An exact campaign has 18% [[ACOS]], runs out of budget by noon, and advertises an in-stock product with healthy margin. Learner must recommend a budget increase and explain why.
- Listing problem disguised as PPC problem: [[CTR]] is strong, [[CPC]] is reasonable, but [[CVR]] drops after price increases and coupon ends. Learner must diagnose listing and offer issues before cutting all bids.
- Branded defense cleanup: Branded and non-branded terms are mixed in one campaign. Learner must separate branded defense, protect exact terms, and clarify reporting.
- Launch learning period: A new product has high [[ACOS]] but search terms show relevant demand. Learner must decide what to keep testing, what to harvest, and what to pause.

## Pages in this section
```

---

## File: `docs/sections/zz-deep-operational-playbooks/index.md`

```markdown
---
title: "Deep Operational Playbooks"
page_type: section_overview
section_id: "deep-operational-playbooks"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# Deep Operational Playbooks

This appendix turns the wiki into real operator guidance. Use it when a learner asks, "Okay, but what do I actually do on Monday morning?"

## Pages in this section

- [[A. PPC Diagnostic Framework]]
- [[B. Search Term Mining SOP]]
- [[C. Bid and Budget Decision Matrix]]
- [[D. New Product Launch Blueprint]]
- [[E. Client Reporting Narrative Builder]]
- [[F. Bulk Upload and Change QA Checklist]]
- [[G. Wiki-to-App Data Schemas]]
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-a-a-ppc-diagnostic-framework.md`

```markdown
---
title: "A. PPC Diagnostic Framework"
page_id: "playbook-a"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# A. PPC Diagnostic Framework

Before changing bids, diagnose the problem. Amazon PPC issues usually come from one of four places: traffic, cost, conversion, or structure.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop.md`

```markdown
---
title: "B. Search Term Mining SOP"
page_id: "playbook-b"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# B. Search Term Mining SOP

Search term mining is the weekly process of turning messy shopper language into clean account decisions.
- Input reports: Search Term Report, Targeting Report, Campaign report, SKU/order data, margin or target [[ACOS]].
- Minimum review window: Use 7 days for high-volume accounts, 14 to 30 days for slower accounts, and longer windows for expensive or low-volume products.
- Classification labels: Promote, keep testing, negate exact, negate phrase, reduce bid, listing issue, irrelevant but not enough data, brand defense.
- Output files: Promoted exact keyword list, negative keyword list, bid-change list, QA notes, client-facing summary if needed.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-c-c-bid-and-budget-decision-matrix.md`

```markdown
---
title: "C. Bid and Budget Decision Matrix"
page_id: "playbook-c"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["bidding", "budget"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# C. Bid and Budget Decision Matrix

Bids should change because the data tells a story. Budgets should change because the campaign has earned or lost the right to spend.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint.md`

```markdown
---
title: "D. New Product Launch Blueprint"
page_id: "playbook-d"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["launch"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# D. New Product Launch Blueprint

Launch PPC is not the same as mature PPC. A launch account pays for learning, demand discovery, and ranking support. That does not mean unlimited waste.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-e-e-client-reporting-narrative-builder.md`

```markdown
---
title: "E. Client Reporting Narrative Builder"
page_id: "playbook-e"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["communication", "reporting"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# E. Client Reporting Narrative Builder

A report should not read like a data dump. Use this structure to turn numbers into a clear business update.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist.md`

```markdown
---
title: "F. Bulk Upload and Change QA Checklist"
page_id: "playbook-f"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# F. Bulk Upload and Change QA Checklist

- Before export: Confirm date range, account, marketplace, campaign names, ad type, and goal.
- Before upload: Check match type, negative match type, bid values, budgets, campaign state, ad group state, SKU/ASIN, and duplicates.
- High-risk fields: Budget, bid, state, negative phrase, portfolio, campaign name, targeting expression, placement modifier.
- Rollback plan: Save the original file, upload file, timestamp, owner, reviewer, and a short reason for every material change.
- Approval rule: Require strategist or lead approval for large budget increases, bulk negatives, account-wide rule changes, and automation changes.
```

---

## File: `docs/sections/zz-deep-operational-playbooks/playbook-g-g-wiki-to-app-data-schemas.md`

```markdown
---
title: "G. Wiki-to-App Data Schemas"
page_id: "playbook-g"
section: "Deep Operational Playbooks"
learner_level: "Applied"
topic_tags: ["amazon-ppc"]
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
status: "draft-ready"
---

# G. Wiki-to-App Data Schemas

Use these as starting schemas when this wiki feeds a Console Simulator, quiz app, LMS, or reporting assistant.
```

---

## File: `docs/sections/zz-how-this-expanded-version-is-different/index.md`

```markdown
---
title: "How this expanded version is different"
page_type: section_overview
section_id: "how-this-expanded-version-is-different"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# How this expanded version is different

- Beginner-first language: Each page explains the topic like the reader has never seen Amazon Seller Central or Ads Console.
- Operator-ready detail: Each page says what to check, what action to take, what mistake to avoid, and when to escalate.
- Data-ready structure: Each page includes page_id, tags, learner level, owner, and review cycle so this can become a wiki database.
- Training-ready format: The content supports lessons, quizzes, handouts, simulator scenarios, and SOPs.

## Pages in this section
```

---

## File: `docs/sections/zz-official-source-checklist-for-maintenance/index.md`

```markdown
---
title: "Official Source Checklist for Maintenance"
page_type: section_overview
section_id: "official-source-checklist-for-maintenanc"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# Official Source Checklist for Maintenance

Use official Amazon sources when verifying platform facts. Keep a verification date inside each wiki page metadata. Amazon changes UI, eligibility, and feature names, so do not treat any guide as permanent scripture. Very official-looking wrong docs are still wrong docs.

## Pages in this section
```

---

## File: `docs/sections/zz-reusable-training-assets/index.md`

```markdown
---
title: "Reusable Training Assets"
page_type: section_overview
section_id: "reusable-training-assets"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# Reusable Training Assets

Use these patterns to turn each wiki page into a training unit.
- Learning aid: One-page visual summary with key terms, common mistakes, one flowchart, and one worked example.
- Quiz: 5-10 questions with answer key. Include multiple choice, scenario judgment, and calculation questions where useful.
- Teaching guide: Trainer notes with delivery time, talking points, live demo steps, discussion prompts, and practice activity.
- Handout: Printable job aid with definition, formula if applicable, checklist, warning signs, and link back to the wiki.
- Simulator scenario: Fake but realistic campaign state with starting data, correct actions, common mistakes, scoring rubric, and ideal after-state.

## Pages in this section
```

---

## File: `docs/sections/zz-start-here-paths/index.md`

```markdown
---
title: "Start Here Paths"
page_type: section_overview
section_id: "start-here-paths"
source_doc: "Amazon_PPC_Wiki_Fresh_Graduate_Guide_EXPANDED.docx"
last_verified_against_live_console: null
owner: "PPC Training Team"
review_cycle: "Quarterly"
---

# Start Here Paths

- Beginner VA: Read Sections 1-4, then 5-11, then 22. Practice with checklists before touching live accounts.
- Junior Strategist: Read Sections 1-11, 14-15, 18, 22-23. Focus on diagnosis and business interpretation.
- Senior Strategist: Read all core sections, then 12-13, 17, 21, 25, and 32. Build systems and review strategy.
- Brand Owner: Read Sections 1, 3, 10, 14-15, 18, 20, and 23. Focus on decisions, targets, and expectations.
- Agency Owner: Read Sections 2, 10-11, 16-17, 22-23, 26-27, and 32. Focus on repeatability and scalable delivery.

## Pages in this section
```

---

## File: `docs/training/index.md`

```markdown
---
title: "Training Layer"
page_type: hub
---

# Training Layer

Use this folder for learning aids, quizzes, teaching guides, and handouts tied to each topic page.

## Recommended first rollout

1. Sections 1-4: Foundations, Architecture, Campaign Types, Targeting.
2. Sections 5-9: Keyword Research, Bidding, Budget, Placements, Negatives.
3. Sections 10-11: Metrics and Reporting.
4. Section 22: Team Ops and SOPs.
```

---

## File: `mkdocs.yml`

```yaml
site_name: Amazon PPC Wiki
site_description: Beginner-friendly Amazon PPC knowledge base and training repo
theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
markdown_extensions:
  - admonition
  - toc:
      permalink: true
  - tables
  - attr_list
plugins:
  - search
nav:
  - Home: index.md
  - Complete Data-Filled Guide: complete-data-filled-guide.md
  - Glossary: glossary/index.md
  - Formula Appendix: appendix/formulas-calculators.md
  - Training Layer: training/index.md
  - App Layer: app-layer/index.md
  - Start Here Paths:
      - "Overview": sections/zz-start-here-paths/index.md
  - How this expanded version is different:
      - "Overview": sections/zz-how-this-expanded-version-is-different/index.md
  - 0. Front Matter:
      - "Overview": sections/00-0-front-matter/index.md
      - "0.1 Home / Landing Page": sections/00-0-front-matter/0-1-0-1-home-landing-page.md
      - "0.2 How to Use This Wiki": sections/00-0-front-matter/0-2-0-2-how-to-use-this-wiki.md
      - "0.3 Contributor / Maintenance Guide": sections/00-0-front-matter/0-3-0-3-contributor-maintenance-guide.md
  - 1. Foundations & Fundamentals:
      - "Overview": sections/01-1-foundations-and-fundamentals/index.md
      - "1.1 What is Amazon PPC": sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md
      - "1.2 The Amazon Advertising Ecosystem": sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.md
      - "1.3 Core Terminology Primer": sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md
      - "1.4 Eligibility & Prerequisites": sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.md
  - 2. Account & Campaign Architecture:
      - "Overview": sections/02-2-account-and-campaign-architecture/index.md
      - "2.1 Account Structure Philosophy": sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.md
      - "2.2 Campaign Structuring Models": sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md
      - "2.3 Ad Group Best Practices": sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.md
      - "2.4 Portfolio & Budget Grouping": sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.md
  - 3. Campaign Types:
      - "Overview": sections/03-3-campaign-types/index.md
      - "3.1 Sponsored Products (SP)": sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md
      - "3.2 Sponsored Brands (SB)": sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md
      - "3.3 Sponsored Display (SD)": sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md
      - "3.4 Sponsored TV / Streaming TV Ads": sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.md
      - "3.5 Amazon DSP": sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md
      - "3.6 Cross-Campaign-Type Strategy": sections/03-3-campaign-types/3-6-3-6-cross-campaign-type-strategy.md
  - 4. Targeting & Match Types:
      - "Overview": sections/04-4-targeting-and-match-types/index.md
      - "4.1 Keyword Match Types": sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md
      - "4.2 Product Targeting": sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md
      - "4.3 Audience Targeting": sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md
      - "4.4 Auto-Targeting Categories": sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.md
  - 5. Keyword Research & Search Term Mining:
      - "Overview": sections/05-5-keyword-research-and-search-term-mining/index.md
      - "5.1 Research Methodology": sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.md
      - "5.2 Keyword Research Tools": sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.md
      - "5.3 Search Term Harvesting Workflow": sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.md
      - "5.4 Long-Tail vs. Head Term Strategy": sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.md
  - 6. Bidding Strategies & Bid Management:
      - "Overview": sections/06-6-bidding-strategies-and-bid-management/index.md
      - "6.1 Manual Bidding Fundamentals": sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md
      - "6.2 Dynamic & Rule-Based Bidding": sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md
      - "6.3 Bid Adjustment Cadence": sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md
      - "6.4 Placement Bid Modifiers": sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md
  - 7. Budget Management & Pacing:
      - "Overview": sections/07-7-budget-management-and-pacing/index.md
      - "7.1 Budget Allocation Frameworks": sections/07-7-budget-management-and-pacing/7-1-7-1-budget-allocation-frameworks.md
      - "7.2 Pacing and Ran Out of Budget Diagnostics": sections/07-7-budget-management-and-pacing/7-2-7-2-pacing-and-ran-out-of-budget-diagnostics.md
      - "7.3 Seasonal Budget Planning": sections/07-7-budget-management-and-pacing/7-3-7-3-seasonal-budget-planning.md
  - 8. Placements & Placement Optimization:
      - "Overview": sections/08-8-placements-and-placement-optimization/index.md
      - "8.1 Placement Types Explained": sections/08-8-placements-and-placement-optimization/8-1-8-1-placement-types-explained.md
      - "8.2 Placement Reporting & Diagnosis": sections/08-8-placements-and-placement-optimization/8-2-8-2-placement-reporting-and-diagnosis.md
  - 9. Negative Keywords & Negation Strategy:
      - "Overview": sections/09-9-negative-keywords-and-negation-strategy/index.md
      - "9.1 Negative Match Types": sections/09-9-negative-keywords-and-negation-strategy/9-1-9-1-negative-match-types.md
      - "9.2 Negation Strategy by Campaign Structure": sections/09-9-negative-keywords-and-negation-strategy/9-2-9-2-negation-strategy-by-campaign-structure.md
      - "9.3 Common Negation Mistakes": sections/09-9-negative-keywords-and-negation-strategy/9-3-9-3-common-negation-mistakes.md
  - 10. Metrics, KPIs & Analytics:
      - "Overview": sections/10-10-metrics-kpis-and-analytics/index.md
      - "10.1 Core Metrics Deep Dive": sections/10-10-metrics-kpis-and-analytics/10-1-10-1-core-metrics-deep-dive.md
      - "10.2 Advanced Metrics": sections/10-10-metrics-kpis-and-analytics/10-2-10-2-advanced-metrics.md
      - "10.3 Health Check Frameworks": sections/10-10-metrics-kpis-and-analytics/10-3-10-3-health-check-frameworks.md
      - "10.4 Benchmarking": sections/10-10-metrics-kpis-and-analytics/10-4-10-4-benchmarking.md
  - 11. Reporting & Data Analysis:
      - "Overview": sections/11-11-reporting-and-data-analysis/index.md
      - "11.1 Native Amazon Reports": sections/11-11-reporting-and-data-analysis/11-1-11-1-native-amazon-reports.md
      - "11.2 Brand Analytics": sections/11-11-reporting-and-data-analysis/11-2-11-2-brand-analytics.md
      - "11.3 Custom Reporting & Dashboards": sections/11-11-reporting-and-data-analysis/11-3-11-3-custom-reporting-and-dashboards.md
      - "11.4 Data Storytelling": sections/11-11-reporting-and-data-analysis/11-4-11-4-data-storytelling.md
  - 12. Amazon Marketing Cloud:
      - "Overview": sections/12-12-amazon-marketing-cloud/index.md
      - "12.1 What AMC Is and Who Needs It": sections/12-12-amazon-marketing-cloud/12-1-12-1-what-amc-is-and-who-needs-it.md
      - "12.2 AMC Use Cases": sections/12-12-amazon-marketing-cloud/12-2-12-2-amc-use-cases.md
      - "12.3 AMC SQL Basics": sections/12-12-amazon-marketing-cloud/12-3-12-3-amc-sql-basics.md
  - 13. Amazon DSP:
      - "Overview": sections/13-13-amazon-dsp/index.md
      - "13.1 DSP Fundamentals": sections/13-13-amazon-dsp/13-1-13-1-dsp-fundamentals.md
      - "13.2 DSP Campaign Types": sections/13-13-amazon-dsp/13-2-13-2-dsp-campaign-types.md
      - "13.3 DSP Audience Building": sections/13-13-amazon-dsp/13-3-13-3-dsp-audience-building.md
      - "13.4 DSP + Sponsored Ads Synergy": sections/13-13-amazon-dsp/13-4-13-4-dsp-plus-sponsored-ads-synergy.md
  - 14. Brand Presence & Content Tie-Ins:
      - "Overview": sections/14-14-brand-presence-and-content-tie-ins/index.md
      - "14.1 Brand Registry": sections/14-14-brand-presence-and-content-tie-ins/14-1-14-1-brand-registry.md
      - "14.2 Brand Store": sections/14-14-brand-presence-and-content-tie-ins/14-2-14-2-brand-store.md
      - "14.3 A+ Content / Premium A+": sections/14-14-brand-presence-and-content-tie-ins/14-3-14-3-aplus-content-premium-aplus.md
  - 15. Listing Optimization:
      - "Overview": sections/15-15-listing-optimization/index.md
      - "15.1 Why Listing Quality Gates PPC Performance": sections/15-15-listing-optimization/15-1-15-1-why-listing-quality-gates-ppc-performance.md
      - "15.2 Title, Bullet, Backend Keyword Optimization": sections/15-15-listing-optimization/15-2-15-2-title-bullet-backend-keyword-optimization.md
      - "15.3 Image & Video Impact on CTR/CVR": sections/15-15-listing-optimization/15-3-15-3-image-and-video-impact-on-ctr-cvr.md
      - "15.4 Pricing & Promotions Interplay with PPC": sections/15-15-listing-optimization/15-4-15-4-pricing-and-promotions-interplay-with-ppc.md
  - 16. Automation, Rules & Scripts:
      - "Overview": sections/16-16-automation-rules-and-scripts/index.md
      - "16.1 Native Amazon Automation": sections/16-16-automation-rules-and-scripts/16-1-16-1-native-amazon-automation.md
      - "16.2 Bulk Operations": sections/16-16-automation-rules-and-scripts/16-2-16-2-bulk-operations.md
      - "16.3 Custom Scripts & API-Based Automation": sections/16-16-automation-rules-and-scripts/16-3-16-3-custom-scripts-and-api-based-automation.md
      - "16.4 AI-Augmented PPC Management": sections/16-16-automation-rules-and-scripts/16-4-16-4-ai-augmented-ppc-management.md
  - 17. Software & Tools Ecosystem:
      - "Overview": sections/17-17-software-and-tools-ecosystem/index.md
      - "17.1 All-in-One Suites": sections/17-17-software-and-tools-ecosystem/17-1-17-1-all-in-one-suites.md
      - "17.2 Point Solutions": sections/17-17-software-and-tools-ecosystem/17-2-17-2-point-solutions.md
      - "17.3 Build vs. Buy": sections/17-17-software-and-tools-ecosystem/17-3-17-3-build-vs-buy.md
      - "17.4 Tool Evaluation Framework": sections/17-17-software-and-tools-ecosystem/17-4-17-4-tool-evaluation-framework.md
  - 18. Strategy by Business Lifecycle Stage:
      - "Overview": sections/18-18-strategy-by-business-lifecycle-stage/index.md
      - "18.1 New Product Launch": sections/18-18-strategy-by-business-lifecycle-stage/18-1-18-1-new-product-launch.md
      - "18.2 Growth Stage": sections/18-18-strategy-by-business-lifecycle-stage/18-2-18-2-growth-stage.md
      - "18.3 Mature/Steady-State": sections/18-18-strategy-by-business-lifecycle-stage/18-3-18-3-mature-steady-state.md
      - "18.4 Decline/Sunset": sections/18-18-strategy-by-business-lifecycle-stage/18-4-18-4-decline-sunset.md
  - 19. Strategy by Product Category:
      - "Overview": sections/19-19-strategy-by-product-category/index.md
      - "19.1 High-Consideration / High-Price Categories": sections/19-19-strategy-by-product-category/19-1-19-1-high-consideration-high-price-categories.md
      - "19.2 Low-Price / Impulse Categories": sections/19-19-strategy-by-product-category/19-2-19-2-low-price-impulse-categories.md
      - "19.3 Seasonal/Gift Categories": sections/19-19-strategy-by-product-category/19-3-19-3-seasonal-gift-categories.md
      - "19.4 Regulated Categories": sections/19-19-strategy-by-product-category/19-4-19-4-regulated-categories.md
  - 20. Seasonal & Event Planning:
      - "Overview": sections/20-20-seasonal-and-event-planning/index.md
      - "20.1 Prime Day Playbook": sections/20-20-seasonal-and-event-planning/20-1-20-1-prime-day-playbook.md
      - "20.2 Q4 / Holiday Playbook": sections/20-20-seasonal-and-event-planning/20-2-20-2-q4-holiday-playbook.md
      - "20.3 Other Key Dates": sections/20-20-seasonal-and-event-planning/20-3-20-3-other-key-dates.md
  - 21. International & Multi-Marketplace PPC:
      - "Overview": sections/21-21-international-and-multi-marketplace-ppc/index.md
      - "21.1 Marketplace Differences": sections/21-21-international-and-multi-marketplace-ppc/21-1-21-1-marketplace-differences.md
      - "21.2 Cross-Marketplace Account Structure": sections/21-21-international-and-multi-marketplace-ppc/21-2-21-2-cross-marketplace-account-structure.md
      - "21.3 Localization Considerations": sections/21-21-international-and-multi-marketplace-ppc/21-3-21-3-localization-considerations.md
  - 22. Agency & Team Operations:
      - "Overview": sections/22-22-agency-and-team-operations/index.md
      - "22.1 Team Roles & RACI": sections/22-22-agency-and-team-operations/22-1-22-1-team-roles-and-raci.md
      - "22.2 SOPs & Workflow Documentation": sections/22-22-agency-and-team-operations/22-2-22-2-sops-and-workflow-documentation.md
      - "22.3 VA Training & Enablement": sections/22-22-agency-and-team-operations/22-3-22-3-va-training-and-enablement.md
      - "22.4 QA & Review Process": sections/22-22-agency-and-team-operations/22-4-22-4-qa-and-review-process.md
  - 23. Client & Stakeholder Communication:
      - "Overview": sections/23-23-client-and-stakeholder-communication/index.md
      - "23.1 Reporting Cadence": sections/23-23-client-and-stakeholder-communication/23-1-23-1-reporting-cadence.md
      - "23.2 Setting Expectations": sections/23-23-client-and-stakeholder-communication/23-2-23-2-setting-expectations.md
      - "23.3 Handling Difficult Conversations": sections/23-23-client-and-stakeholder-communication/23-3-23-3-handling-difficult-conversations.md
  - 24. Compliance, Policy & Account Health:
      - "Overview": sections/24-24-compliance-policy-and-account-health/index.md
      - "24.1 Advertising Policy Basics": sections/24-24-compliance-policy-and-account-health/24-1-24-1-advertising-policy-basics.md
      - "24.2 Account Health Interplay": sections/24-24-compliance-policy-and-account-health/24-2-24-2-account-health-interplay.md
      - "24.3 Competitor & Ethical Boundaries": sections/24-24-compliance-policy-and-account-health/24-3-24-3-competitor-and-ethical-boundaries.md
  - 25. Advanced & Emerging Topics:
      - "Overview": sections/25-25-advanced-and-emerging-topics/index.md
      - "25.1 Retail Media Network Trends": sections/25-25-advanced-and-emerging-topics/25-1-25-1-retail-media-network-trends.md
      - "25.2 AI's Growing Role in Amazon Ads": sections/25-25-advanced-and-emerging-topics/25-2-25-2-ai-s-growing-role-in-amazon-ads.md
      - "25.3 Privacy & Signal Loss": sections/25-25-advanced-and-emerging-topics/25-3-25-3-privacy-and-signal-loss.md
  - 26. Career, Certification & Learning:
      - "Overview": sections/26-26-career-certification-and-learning/index.md
      - "26.1 Certifications": sections/26-26-career-certification-and-learning/26-1-26-1-certifications.md
      - "26.2 Career Pathing": sections/26-26-career-certification-and-learning/26-2-26-2-career-pathing.md
      - "26.3 Continuing Education": sections/26-26-career-certification-and-learning/26-3-26-3-continuing-education.md
  - 27. Case Studies & Templates:
      - "Overview": sections/27-27-case-studies-and-templates/index.md
      - "27.1 Case Study Template": sections/27-27-case-studies-and-templates/27-1-27-1-case-study-template.md
      - "27.2 Downloadable Templates": sections/27-27-case-studies-and-templates/27-2-27-2-downloadable-templates.md
      - "27.3 Real Case Studies": sections/27-27-case-studies-and-templates/27-3-27-3-real-case-studies.md
  - 28. Glossary & Acronyms:
      - "Overview": sections/28-28-glossary-and-acronyms/index.md
  - 29. Appendix: Formulas & Calculators:
      - "Overview": sections/29-29-appendix-formulas-and-calculators/index.md
  - 30. Meta / Changelog:
      - "Overview": sections/30-30-meta-changelog/index.md
      - "30. Meta / Changelog": sections/30-30-meta-changelog/30-30-meta-changelog.md
  - 31. Training Layer Template:
      - "Overview": sections/31-31-training-layer-template/index.md
      - "31.1 Learning Aid": sections/31-31-training-layer-template/31-1-31-1-learning-aid.md
      - "31.2 Quiz": sections/31-31-training-layer-template/31-2-31-2-quiz.md
      - "31.3 Teaching Guide": sections/31-31-training-layer-template/31-3-31-3-teaching-guide.md
      - "31.4 Handout": sections/31-31-training-layer-template/31-4-31-4-handout.md
      - "31.5 Tagging & Assembly System": sections/31-31-training-layer-template/31-5-31-5-tagging-and-assembly-system.md
      - "31.6 Rollout Priority": sections/31-31-training-layer-template/31-6-31-6-rollout-priority.md
      - "31.7 Assessment & Certification Tie-In": sections/31-31-training-layer-template/31-7-31-7-assessment-and-certification-tie-in.md
  - 32. App-Building Layer:
      - "Overview": sections/32-32-app-building-layer/index.md
      - "32.1 Content-as-Data Separation": sections/32-32-app-building-layer/32-1-32-1-content-as-data-separation.md
      - "32.2 Standardized Schemas": sections/32-32-app-building-layer/32-2-32-2-standardized-schemas.md
      - "32.3 Simulator Scenario Bank": sections/32-32-app-building-layer/32-3-32-3-simulator-scenario-bank.md
      - "32.4 Asset Library with Naming Convention": sections/32-32-app-building-layer/32-4-32-4-asset-library-with-naming-convention.md
      - "32.5 Content Versioning & Sync Contract": sections/32-32-app-building-layer/32-5-32-5-content-versioning-and-sync-contract.md
      - "32.6 API/Export Layer": sections/32-32-app-building-layer/32-6-32-6-api-export-layer.md
      - "32.7 Difficulty & Progression Graph": sections/32-32-app-building-layer/32-7-32-7-difficulty-and-progression-graph.md
      - "32.8 Multi-Consumer Design": sections/32-32-app-building-layer/32-8-32-8-multi-consumer-design.md
  - Reusable Training Assets:
      - "Overview": sections/zz-reusable-training-assets/index.md
  - Capstone Practice Scenarios:
      - "Overview": sections/zz-capstone-practice-scenarios/index.md
  - Official Source Checklist for Maintenance:
      - "Overview": sections/zz-official-source-checklist-for-maintenance/index.md
  - Deep Operational Playbooks:
      - "Overview": sections/zz-deep-operational-playbooks/index.md
      - "A. PPC Diagnostic Framework": sections/zz-deep-operational-playbooks/playbook-a-a-ppc-diagnostic-framework.md
      - "B. Search Term Mining SOP": sections/zz-deep-operational-playbooks/playbook-b-b-search-term-mining-sop.md
      - "C. Bid and Budget Decision Matrix": sections/zz-deep-operational-playbooks/playbook-c-c-bid-and-budget-decision-matrix.md
      - "D. New Product Launch Blueprint": sections/zz-deep-operational-playbooks/playbook-d-d-new-product-launch-blueprint.md
      - "E. Client Reporting Narrative Builder": sections/zz-deep-operational-playbooks/playbook-e-e-client-reporting-narrative-builder.md
      - "F. Bulk Upload and Change QA Checklist": sections/zz-deep-operational-playbooks/playbook-f-f-bulk-upload-and-change-qa-checklist.md
      - "G. Wiki-to-App Data Schemas": sections/zz-deep-operational-playbooks/playbook-g-g-wiki-to-app-data-schemas.md
```

---

## File: `requirements.txt`

```text
mkdocs>=1.6.0
mkdocs-material>=9.5.0
jsonschema>=4.0.0
```

---

## File: `schemas/glossary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "term",
    "short_def"
  ],
  "properties": {
    "term": {
      "type": "string"
    },
    "short_def": {
      "type": "string"
    },
    "long_def": {
      "type": "string"
    },
    "related_terms": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "first_appears_in_section": {
      "type": "string"
    }
  }
}
```

---

## File: `schemas/learner-progress.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "learner_id",
    "topic_id",
    "status"
  ],
  "properties": {
    "learner_id": {
      "type": "string"
    },
    "topic_id": {
      "type": "string"
    },
    "status": {
      "enum": [
        "not-started",
        "in-progress",
        "completed",
        "needs-review"
      ]
    },
    "quiz_scores": {
      "type": "array"
    },
    "last_activity": {
      "type": "string"
    }
  }
}
```

---

## File: `schemas/quiz.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "id",
    "topic_tag",
    "difficulty",
    "question",
    "options",
    "correct_answer",
    "explanation"
  ],
  "properties": {
    "id": {
      "type": "string"
    },
    "topic_tag": {
      "type": "string"
    },
    "difficulty": {
      "enum": [
        "Foundational",
        "Applied",
        "Advanced"
      ]
    },
    "question": {
      "type": "string"
    },
    "options": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "correct_answer": {
      "type": "string"
    },
    "explanation": {
      "type": "string"
    }
  }
}
```

---

## File: `schemas/scenario.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "scenario_id",
    "campaign_type",
    "starting_state",
    "correct_actions",
    "common_mistakes",
    "scoring_rubric"
  ],
  "properties": {
    "scenario_id": {
      "type": "string"
    },
    "campaign_type": {
      "type": "string"
    },
    "starting_state": {
      "type": "string"
    },
    "correct_actions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "common_mistakes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "scoring_rubric": {
      "type": "object"
    }
  }
}
```

---

## File: `scripts/build_page_index.py`

```python
#!/usr/bin/env python3
from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]
records=[]
for md in sorted((root/'docs').rglob('*.md')):
    rel=md.relative_to(root/'docs').as_posix()
    text=md.read_text(encoding='utf-8')
    title=md.stem
    if text.startswith('---'):
        fm=text.split('---',2)[1]
        m=re.search(r'^title:\s*"?([^"\n]+)"?',fm,re.M)
        if m: title=m.group(1)
    records.append({'title':title,'path':rel})
(root/'data/page_index.generated.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(f'Indexed {len(records)} docs pages.')
```

---

## File: `scripts/validate_content.py`

```python
#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
for md in (root/'docs').rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    if text.startswith('---'):
        fm=text.split('---',2)[1]
        for field in ['title']:
            if f'{field}:' not in fm: errors.append(f'{md}: missing {field}')
    else:
        if md.name!='index.md': errors.append(f'{md}: missing frontmatter')
try:
    pages=json.loads((root/'data/pages.json').read_text(encoding='utf-8'))
    for p in pages:
        if not (root/'docs'/p['path']).exists(): errors.append(f"Missing page path: {p['path']}")
except Exception as e:
    errors.append(f'pages.json invalid: {e}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Content validation passed.')
```

---

## File: `templates/changelog-template.md`

```markdown
# Changelog Entry

## Date

## Change summary

## Amazon console/report affected

## Pages updated

## Owner

## Verification notes
```

---

## File: `templates/quiz-template.json`

```json
{
  "id": "q-topic-001",
  "topic_tag": "",
  "difficulty": "Foundational",
  "question": "",
  "options": [
    "",
    "",
    "",
    ""
  ],
  "correct_answer": "",
  "explanation": ""
}
```

---

## File: `templates/scenario-template.json`

```json
{
  "scenario_id": "",
  "campaign_type": "",
  "starting_state": "",
  "correct_actions": [],
  "common_mistakes": [],
  "scoring_rubric": {}
}
```

---

## File: `templates/wiki-page-template.md`

```markdown
---
title: ""
page_id: ""
section: ""
learner_level: "Foundational"
topic_tags: []
delivery_format: ["self-paced", "instructor-led"]
estimated_time_minutes: 15
owner: "PPC Training Team"
review_cycle: "Quarterly"
last_verified_against_live_console: null
status: "draft"
---

# Page Title

## What this page teaches

## Explain it to a fresh graduate

## Why this matters in real accounts

## Operator workflow

## Worked example

## Common beginner mistakes

## Definition of done
```
