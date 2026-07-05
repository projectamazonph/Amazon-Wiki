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
