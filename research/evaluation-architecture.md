# Evaluation architecture

## Decision

Ribeiro-style tests should be part of a benchmark when they encode behavior required by the intended score interpretation or use. They supply targeted validity evidence. They do not replace representative sampling, reliability analysis, or evaluation of a score-based decision.

The benchmark should expose four layers.

| Layer | Question | Case source | Primary output |
|---|---|---|---|
| Population | How well does the procedure perform on the target population? | Probability sample or weighted approximation | Expected loss and interval |
| Slices | How well does it perform for prespecified groups or conditions? | Population sample plus defensible oversamples | Group-specific loss, gaps, and intervals |
| Behavioral | Does it satisfy named capabilities and relations? | Hand-written, templated, or generated cases | Failures by capability and test family |
| Shift | What happens under a named distribution change? | Sample from a defined target shift or controlled intervention | Loss, calibration, coverage, or abstention utility under shift |

## Required record for each behavioral test

Each test family should state:

1. the capability and the inference it supports;
2. the test type and expected output relation;
3. the case generator, source templates, and version;
4. the domain over which the oracle is claimed to be valid;
5. human validation of generated cases and expected outputs;
6. the unit of analysis and dependence among variants from the same template;
7. the failure-rate estimator and interval, clustered by template when appropriate;
8. contamination controls and whether examples are public or hidden; and
9. examples of failures, not only an aggregate count.

## Aggregation rule

Default: do not produce one overall behavioral score.

Report a capability-by-test-family matrix and a compact profile of prespecified critical failures. Aggregate only when weights have a substantive interpretation, such as estimated deployment frequencies, expected harm, or an explicit product requirement. Freeze those weights before evaluating candidate models. A macro-average over arbitrary test families measures the curator's inventory, not deployment quality.

## Learning cycle

A discovered behavioral failure can motivate a prespecified slice in the next benchmark version. Representative sampling can then estimate how often the condition occurs. Frequent population errors can in turn motivate behavioral tests that isolate the failing capability.

Tests added after inspecting current model failures are exploratory for that version. They become confirmatory only after they are frozen for a later version or evaluated against a held-out generator. Immutable versions keep this learning cycle from being mistaken for independent confirmation.

## Main risks

- **Template gaming:** keep a hidden confirmation generator and version test families immutably.
- **Invalid perturbations:** verify that meaning and label relations are preserved.
- **Dependence:** do not treat hundreds of variants from one template as independent observations.
- **Capability cherry-picking:** publish the full prespecified matrix, including failures.
- **Score laundering:** do not let a favorable population average conceal a critical behavioral failure, or a large arbitrary test suite conceal poor population performance.
- **Contamination:** distinguish development examples from locked evaluation cases.
- **Process overclaim:** black-box behavior does not by itself identify the model's internal reasoning.
