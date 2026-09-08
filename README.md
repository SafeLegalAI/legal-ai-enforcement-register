---
license: cc-by-4.0
pretty_name: "Consumer legal-AI enforcement, UPL and authorisation register (SafeLegalAI)"
language:
  - en
size_categories:
  - n<1K
tags:
  - enforcement
  - ftc
  - unauthorized-practice
  - regulatory-sandbox
  - consumer-protection
  - legal-services
  - legal
  - safelegalai
configs:
  - config_name: actions
    default: true
    data_files:
      - split: train
        path: data/actions.parquet
---

# Consumer legal-AI enforcement, UPL and authorisation register

> Part of the [SafeLegalAI datasets](https://safelegalai.com/datasets) — CC BY 4.0, mirrored on [Hugging Face](https://huggingface.co/datasets/safelegalaidata/legal-ai-enforcement-register). Every row links to its record page and its primary source. Found an error in a row? [Open an issue](https://github.com/SafeLegalAI/legal-ai-enforcement-register/issues/new?template=row-error.yml) or use [safelegalai.com/report](https://safelegalai.com/report).

**43 official actions about AI-enabled legal services offered to the public — regulator enforcement, unauthorized-practice rulings and opinions, regulatory-sandbox and licensing authorisations that the regulator itself describes as AI or technology based, court and access-to-justice AI deployments for self-represented people — each dated and sourced to the regulator or court.**

Built 2026-09-07 by [SafeLegalAI](https://safelegalai.com) (Cognesio LLP). Canonical pages: [safelegalai.com/regulation/enforcement](https://safelegalai.com/regulation/enforcement) · repository, pipeline and issues: [https://github.com/SafeLegalAI/legal-ai-enforcement-register](https://github.com/SafeLegalAI/legal-ai-enforcement-register) · this mirror: [https://huggingface.co/datasets/safelegalaidata/legal-ai-enforcement-register](https://huggingface.co/datasets/safelegalaidata/legal-ai-enforcement-register).

| table | rows | one row is |
|---|---|---|
| `actions` | 43 | one official action or register entry about an AI legal service for the public |

Every row carries `source_url`, `fetched_at` and, where the Wayback Machine accepted the page, `archive_url`; `url` links the canonical page on safelegalai.com; `notice` carries the terms below. Full schemas: `schema/`.

One official action, one row: `date`, `category` (regulator-enforcement · upl-litigation · upl-opinion · sandbox-authorisation · regulator-register · court-a2j-deployment · policy-statement), `jurisdiction`, `actor`, `entity`, `entity_slug`, `action_type`, `outcome`, `docket`, `regulator_ai_flag` and the regulator's own `regulator_descriptor`, a 40–60-word `summary`, `source_url`, `secondary_url`, `archive_url`, `licence`, `right_of_reply`.

### `actions` by `category`

| value | rows |
|---|---|
| sandbox-authorisation | 25 |
| upl-litigation | 5 |
| regulator-register | 4 |
| court-a2j-deployment | 4 |
| policy-statement | 3 |
| regulator-enforcement | 2 |

### `actions` by `jurisdiction`

| value | rows |
|---|---|
| canada | 21 |
| us-state | 15 |
| uk | 3 |
| us-federal | 3 |
| eu | 1 |

### `actions` by `entity`

| value | rows |
|---|---|
| DoNotPay, Inc. | 5 |
| Arizona Alternative Business Structures Directory | 1 |
| Law Society Innovation Sandbox | 1 |
| Utah legal regulatory sandbox authorized entities | 1 |
| SRA-regulated firms and solicitors | 1 |
| AI system providers | 1 |
| Garfield AI | 1 |
| Lone Star Legal Aid Navi chatbot | 1 |
| Willful | 1 |
| PR Coach | 1 |
| Ownright | 1 |
| Access to Innovation participating providers | 1 |
| LegalWills | 1 |
| Incorporight | 1 |
| eState Planner | 1 |

## Method

Federal Register API and FTC matter pages, federal court opinions, state supreme court orders (Utah Office of Legal Services Innovation register and its authorisation orders), the SRA, Law Society of Ontario and Law Society of BC registers, the Bundesgerichtshof. An entity appears only if it has at least one official action or register entry — this register never reviews, rates or recommends a consumer service. Allegations are stated as the regulator framed them and paired with the outcome.

SafeLegalAI records what courts, regulators, legislatures and vendors' own public pages state; it does not infer, rank or advise. Coding columns are SafeLegalAI's good-faith reading for comparison, not findings about any person or body. Corrections and right of reply: [safelegalai.com/report](https://safelegalai.com/report).

## Licence and notices

US federal works and judicial opinions are public domain; state court orders are edicts; regulator prose is quoted at ≤25 words with attribution (SRA terms permit short extracts). The compilation and coding are **CC BY 4.0** — attribute *SafeLegalAI (safelegalai.com), published by Cognesio LLP*. Code is Apache-2.0.

Provided as is, without warranty. Not legal advice. SafeLegalAI (Cognesio LLP) records what courts, regulators, legislatures and vendors' own public pages state; the linked official documents are the record. Names and marks belong to their owners. Anyone named may reply: https://safelegalai.com/report. Full terms: https://safelegalai.com/disclaimer See `DISCLAIMER.md` and `NOTICE` in this repository.

## Cite

> SafeLegalAI (Cognesio LLP), "Consumer legal-AI enforcement, UPL and authorisation register", v0.1.1, 2026-09-07. https://huggingface.co/datasets/safelegalaidata/legal-ai-enforcement-register — CC BY 4.0. Canonical: https://safelegalai.com/regulation/enforcement
