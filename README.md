# Benchmarking Benchmarks

Status: working paper and illustrative benchmark audit.

This repository develops *A Benchmark for Benchmarks*, an argument and research agenda about what machine-learning benchmarks should measure and how they should be built.

The organizing conclusion is that a benchmark is a measurement system, not merely a dataset. It joins an intended use, target population, construct, reference set, coverage specification, data and labels, designed interventions, metric, evaluation protocol, uncertainty analysis, and governance rules. The reference set names the cases, test forms, runs, tasks, or problems that could have been different while still counting as another admissible use of the benchmark. A dataset can be sound while the benchmark built around it is not.

The paper distinguishes sampled observations from designed interventions. Representative samples estimate population performance. Designed interventions test whether model outputs respond correctly to controlled changes, invariances, negative controls, and contradictions. Both require a stated reference set if their results are meant to extend beyond the observed cases. These designs support different claims and should not be collapsed into one score without defensible weights.

The paper also distinguishes direct performance estimands from latent capability claims. Item response theory can help with dimensionality, item information, linking, and efficient testing when a latent response model is justified; it does not replace construct validation, coverage, or representative sampling.

An illustrative audit applies the framework to a stratified random sample of twelve English text-classification benchmark families from the final public Papers with Code snapshot. It reports a profile of documented evidence, not a benchmark ranking or an omnibus quality score.

## Repository map

- manuscript/main.tex: working manuscript
- manuscript/references.bib: source-checked bibliography used by the manuscript
- audit/README.md: sampling protocol and codebook
- audit/frame.csv: candidate frame, eligibility decisions, and random draw
- audit/ratings.csv: criterion-level ratings with evidence locators
- audit/analyze.py: validation and generated manuscript table

## Build

The local checks require Python 3, latexmk, pdflatex, bibtex, chktex, and rg.

    make check

The compiled paper is written to build/main.pdf. Generated files are ignored by Git.

## Audit boundary

The audit asks what can be recovered from primary papers, official data pages, and evaluation documentation. A `not_found` rating is not evidence that an activity never occurred. The current twelve-family audit is single-coded and illustrative; independent recoding is required before using it to estimate population prevalence.
