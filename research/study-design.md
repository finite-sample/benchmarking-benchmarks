# Proposed empirical studies

No outcome matrix exists. These designs should be frozen before models are run across datasets.

## Study 1: Model-rank portability

### Question

If a researcher selects a model-development procedure because it wins on one text-classification task, how much performance is lost when that procedure is used on a new task from the stated task universe?

### Estimands

For a fixed candidate set, tuning protocol, compute budget, metric policy, and universe of tasks:

- winner-transfer probability: the probability that the procedure selected on task A also minimizes expected loss on independently sampled task B;
- selection regret: expected loss on task B for the procedure selected on task A minus the minimum loss achievable by the candidate set on task B; and
- rank portability: the distribution of pairwise rank correlations across task pairs.

The task is the population-level sampling unit. Test examples estimate performance within a task. They do not turn a convenience collection of tasks into a random sample of a task universe.

### Generalizability design

Treat model-development procedure as the object of measurement. Candidate random facets include task family, task within family, item within task, training run, and evaluation occasion. Prompt format or annotator can be additional facets when relevant.

Estimate variance components before choosing the final allocation. A decision study should compare the precision gained by adding tasks, items per task, or training runs. The primary uncertainty for a claim about new tasks must include between-task variation.

### Choices to freeze

1. Define the task universe by venue, repository, time window, language, label structure, and access rules.
2. State whether datasets for the same construct are distinct tasks or repeated forms within a task family.
3. Freeze candidate procedures rather than bare architecture names.
4. Give every procedure the same tuning information and budget.
5. Choose a primary loss with a cross-task interpretation or standardize regret within task. Do not average raw accuracy and F1.
6. Split shared sources, people, and documents at the deployment dependence level.
7. Repeat stochastic training and propagate within-task test uncertainty and between-run variation.
8. Keep task families held out from design iteration.

### Analysis

- Estimate the model-by-task loss matrix with intervals.
- Use leave-one-task-out selection to compute regret on each held-out task.
- Bootstrap tasks or task families, not individual examples alone, for task-universe uncertainty.
- Show the pairwise win matrix and regret distribution. A single average rank is secondary.
- Treat explanations of heterogeneity as exploratory unless prespecified.

## Study 2: Selective benchmarking

### Question

Are eligible benchmarks more likely to appear in a paper when the proposed method performs relatively well on them?

### Unit and population

The unit is an eligible paper--benchmark pair. The population can be all empirical text-classification papers in specified venues and years crossed with benchmarks that satisfy a frozen eligibility rule based on task, language, license, data availability, and computational feasibility at the paper's submission date.

### Identification problem

Published tables reveal performance on selected benchmarks and hide performance on omitted benchmarks. A regression using only reported cells cannot estimate selection on relative performance. The missing outcomes must be recovered by rerunning the released procedure and comparator set on a sampled set of omitted but eligible benchmarks, or by obtaining complete internal experiment logs.

Even with recovered outcomes, relative advantage can be associated with legitimate eligibility factors such as modality, input length, licensing, compute, or prior convention. Record these before interpreting the association as strategic selection.

### Feasible design

1. Sample papers from a frozen venue-by-year frame.
2. Reconstruct the candidate benchmark set available at each paper's cutoff date without consulting its reported results.
3. Have two coders independently assess eligibility from the paper's task definition and a written codebook.
4. For a random subset of eligible omitted pairs, reproduce the proposed procedure and a frozen comparator under a common protocol.
5. Define relative advantage as the loss difference from the comparator, with uncertainty.
6. Estimate how inclusion changes with relative advantage, conditioning on prespecified eligibility and cost variables.
7. Use benchmark characteristics learned only after the paper's cutoff date as a negative control; they cannot have caused the original selection.
8. Report bounds for unreproduced omitted pairs rather than assuming performance is missing at random.

### Interpretation

The primary outcome is whether an eligible benchmark appears in the main paper or supplement. Evidence that inclusion rises with relative advantage is consistent with selective benchmarking, but unmeasured suitability or cost can produce the same pattern. The paper should name and test these rivals rather than infer intent.

## Order

Study 1 asks whether benchmark choice changes which procedure appears best. Study 2 asks whether reporting choices depend on that advantage. Study 1 should come first because it establishes whether selective reporting could materially change conclusions before investigating whether it occurs.
