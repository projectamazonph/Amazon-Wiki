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
