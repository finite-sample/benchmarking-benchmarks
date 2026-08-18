# Illustrative benchmark audit

This directory contains the empirical audit reported in *A Benchmark for
Benchmarks*. It is deliberately small. Its purpose is to show what a
measurement-centered audit reveals, not to rank benchmarks or estimate a
precise failure rate for all machine-learning benchmarks.

## Population and sample

The frame begins with every dataset listed directly under **Text
Classification** in the final public Papers with Code evaluation-table
snapshot, retrieved July 28, 2025. The frozen source is
`pwc-archive/evaluation-tables@7dd607a42427a2c27fcedc689a7415df58788c50`.
The linked dataset metadata comes from
`pwc-archive/datasets@994583626a421babe1288db5d8ea6e34c00bd9fa`.

An entry is eligible when:

1. the frozen leaderboard contains at least one reported result;
2. the linked archive record identifies English as an input language;
3. the evaluated output is a discrete label for one or more text inputs;
4. a canonical dataset and evaluation protocol can be identified; and
5. the entry is not a duplicate alias of another benchmark family.

The unit is a benchmark family, not a repository mirror or an individual
model-result row. `frame.csv` records all 101 candidates and every exclusion.
The screen left 25 eligible families.

Eligible families were divided by the number of result rows in the frozen
leaderboard: low activity (one row), middle activity (two to four rows), and
high activity (five or more rows). Within each stratum, the order was randomly
permuted with seed `20260817`. The first four eligible families in each order
were selected. One provisionally eligible entry, Twitter Sentiment Analysis,
was removed before outcome coding because its linked paper evaluated IMDB and
SRAA and did not identify a Twitter dataset or protocol. The next low-activity
family in the frozen draw order, RTE, replaced it.

The resulting sample has twelve benchmark families. Inclusion probabilities
and inverse-probability weights are recorded in `frame.csv`. Because the sample
is small and coding is currently by one reviewer, the manuscript reports an
evidence profile and case studies rather than weighted population estimates.
Independent recoding should precede population-prevalence claims.

## Coding rule

The audit asks what the benchmark's primary paper, official data page, and
evaluation documentation establish. It does not infer undocumented practices.
The target-population, source-frame, content-blueprint, and dependability
criteria jointly show whether a reader can recover the benchmark's reference
sets: the cases, forms, runs, tasks, or settings for which the score is meant to
supply evidence.
The ratings are:

- `yes`: the available evidence satisfies the criterion;
- `partial`: some evidence is present, but a material part is missing;
- `no`: the source explicitly says the criterion was not satisfied;
- `not_found`: the criterion was not found in the reviewed sources; and
- `not_applicable`: the criterion does not apply to the benchmark.

`not_found` is not evidence that an activity never occurred. It means that a
reader could not recover it from the reviewed record.

## Criteria

| ID | Question |
|---|---|
| `claim_population` | Is the target population for the score stated? |
| `claim_construct` | Is the outcome or construct, including its categories, defined? |
| `claim_use` | Is the intended interpretation or use of the score stated? |
| `claim_metric` | Is the metric justified by the intended use, class distribution, or error costs? |
| `coverage_frame` | Are the source frame, selection rule, and evaluation split documented? |
| `coverage_blueprint` | Is content coverage organized by named facets or requirements? |
| `labels_process` | Are label sources, instructions, or construction rules documented? |
| `labels_reliability` | Is label repeatability or inter-rater agreement assessed? |
| `labels_validity` | Is there evidence that labels represent the intended construct? |
| `designed_cases` | Are cases deliberately designed or stratified to test named requirements? |
| `designed_pairs` | Are controlled pairs linked to an expected invariant or directional response? |
| `dependability` | Is score variation examined across relevant samples, items, tasks, raters, runs, or settings? |
| `governance` | Are provenance and relevant license, privacy, consent, or ethics conditions documented? |
| `duplicates` | Are duplicates, related entities, or train--test dependence examined or controlled? |

The criteria are reported separately. They are not added into a quality score.

## Files

- `frame.csv`: complete candidate frame, screening decisions, and random draw.
- `ratings.csv`: one row per sampled family and criterion, with the source and
  evidence locator used for the rating.
- `analyze.py`: validates both files and generates the LaTeX evidence profile
  used by the manuscript.

Run `python3 audit/analyze.py`. Generated files are written under `build/` and
are not committed.
