# Measurement principles for benchmark design

## Central claim

A benchmark is a measuring instrument. The object being measured is usually not a bare model file but a model-development procedure under stated training, tuning, prompting, and resource conditions. The observed score is meaningful only relative to a claimed interpretation and use.

This changes the design question. The first question is not which datasets are available. It is what inference a score should support, for which object, over which universe of observations, and for what decision.

## What the measurement literature teaches

### 1. Validate an interpretation and use, not a dataset

Cronbach and Meehl treat construct validation as an accumulation of evidence. Messick and the *Standards for Educational and Psychological Testing* make validity unitary: different studies supply evidence for or against a proposed score interpretation. Kane makes the logic operational by asking for an interpretation/use argument.

For a benchmark, that argument has four links:

1. **Scoring:** Does the transformation from model outputs to a score preserve the performance feature of interest?
2. **Generalization:** Does performance generalize across admissible items, datasets, raters, prompts, runs, and occasions?
3. **Extrapolation:** Does the benchmark domain support the claim about the target population or deployment setting?
4. **Decision:** Does using the score to select, reject, or deploy a model improve the decision under the relevant costs and harms?

Evidence for one link does not validate the others. Clean labels do not justify extrapolation. A representative sample does not justify an arbitrary metric. Predictive association does not establish that a deployment rule is acceptable.

### 2. Guard against underrepresentation and irrelevant variance

Measurement theory names two rival explanations that organize many benchmark defects.

- **Construct underrepresentation:** the benchmark omits important parts of the claimed capability. A sentiment benchmark with only simple declarative English cannot support a broad claim about sentiment understanding.
- **Construct-irrelevant variance:** scores depend on features outside the construct. Indoor backgrounds in dog images, source artifacts, annotation style, prompt format, hardware, or memorized test items can alter scores without changing the intended capability.

The benchmark blueprint should list the construct facets and justify their representation. Every proposed item feature should be classified as construct-relevant, construct-irrelevant, or an open question to test.

### 3. Reliability is conditional on a universe of admissible observations

Reliability does not mean only inter-annotator agreement. Generalizability theory asks which facets may vary and decomposes the resulting score variance. For model benchmarks, possible facets include:

- tasks and datasets;
- examples within datasets;
- annotators or label aggregation rules;
- training runs and random seeds;
- prompts, demonstrations, and decoding settings;
- software, hardware, and time; and
- benchmark form or version.

The benchmark must say which facets are fixed and which are sampled. A score on a fixed set of datasets supports a claim about those datasets. A claim about new tasks needs a defensible task universe and between-task uncertainty.

A generalizability study estimates the variance contributed by each facet and its interactions. A decision study then asks whether more items, datasets, annotators, or runs would most improve precision. This is more useful than choosing a large round test-set size without knowing the dominant error source.

The needed precision also depends on the use. Ranking two models is a relative decision. Certifying that a model exceeds a deployment threshold is an absolute decision. The same score design can be adequate for one and inadequate for the other.

### 4. Design a test blueprint before collecting items

The blueprint connects the construct to content. It states:

- the target population and intended use;
- the capability and content facets;
- the sampling or coverage rule for each facet;
- the item formats and expected response processes;
- the scoring rule and metric;
- the precision target near the decision boundary; and
- exclusions and prohibited uses.

Representative sampling estimates population performance. Stratified or purposive items improve coverage of rare but important facets. These should remain distinguishable because they support different inferences.

### 5. Study items, not only aggregate scores

Pilot items should be checked for label reliability, ambiguity, difficulty, discrimination, dependence, and sensitivity to irrelevant features. Negative discrimination can flag a bad key, an ambiguous item, a specialized subskill, or a model-family artifact.

Item-response models can be useful when their dimensionality, local-independence, and invariance assumptions fit. They should not be used merely to turn a multidimensional performance profile into an impressive latent score. If item clusters measure distinct capabilities, the benchmark should report a profile.

### 6. Seek convergent and discriminant evidence

A proposed capability measure should agree with other defensible measures of the same capability and remain distinct from measures of different capabilities. Agreement only among benchmarks that share sources, templates, or labeling artifacts is method variance, not strong convergence.

For example, a cat--dog score should relate to other animal-recognition measures but not be explained mainly by indoor--outdoor accuracy. A name-inference score should change when the target population changes in ways predicted by the population definition.

### 7. Treat fairness as comparability and consequences, not only representation

More demographic diversity can improve coverage, but representation alone does not establish fairness. Benchmark builders should test whether instructions, labels, item content, scoring, and access create construct-irrelevant differences. Matched or counterfactual item pairs can probe whether represented-group attributes change responses when the construct says they should not.

The analogy to differential item functioning needs care. In psychometrics, people are test takers. In model evaluation, models are the test takers and demographic attributes often describe item content. A subgroup accuracy gap and psychometric DIF are therefore not the same object.

### 8. Standardize administration and link versions

Scores are comparable only when the evaluation conditions are controlled or modeled. The benchmark should freeze model inputs, preprocessing, prompts, tuning access, external data, compute, decoding, metric implementation, and treatment of abstentions.

When a benchmark changes, raw scores from old and new forms are not automatically comparable. Use immutable versions and, when longitudinal comparison matters, anchor items or another explicit linking design. Public exposure and repeated leaderboard use create practice and contamination effects, so benchmark security and refresh rules are part of measurement quality.

### 9. Evaluate consequences

Benchmarks alter research behavior. They reward some tasks, metrics, and forms of progress, can encourage selective reporting, and can turn a public test set into training data. These consequences do not tell us whether an item was labeled correctly, but they matter to whether the score should be used to allocate attention, claim general progress, or choose a deployed system.

## Where Ribeiro-style tests enter

CheckList contributes targeted evidence within the validity argument:

| CheckList test | Measurement role | What it can show | What it cannot show alone |
|---|---|---|---|
| Minimum functionality | Content coverage and local construct representation | A named capability succeeds or fails on simple specified cases | Population prevalence or full-domain coverage |
| Invariance | Test of construct-irrelevant sensitivity | A prediction changes when the specification says it should not | Why the model changed internally |
| Directional expectation | Test of construct-relevant sensitivity | A controlled change moves the output in the expected direction | Calibration, utility, or overall generalization |

Because CheckList is black-box testing, calling it response-process evidence requires restraint. It tests observable implications of a claimed process. It does not directly establish the internal process that produced the response.

Behavioral cases should be mapped to the blueprint, validated by people, grouped by template family, and reported separately from representative population performance. A weighted aggregate is defensible only when the weights come from deployment frequency, utility, or a prespecified decision rule.

## Consequences for the original checklist

The original criteria remain useful but move into a measurement sequence:

1. intended interpretation and use;
2. construct and target population;
3. blueprint and content authorization;
4. label and scoring design;
5. representative sample plus planned coverage samples;
6. behavioral and rival-hypothesis tests;
7. reliability and generalizability study;
8. fairness, consequences, and prohibited uses;
9. standardized protocol, security, and version linking; and
10. validation dossier stating what the score does and does not support.

The result is not a universal checklist in which every box has equal weight. It is an argument. The evidence required depends on the claim and the stakes.
