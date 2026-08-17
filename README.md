# Benchmarking Benchmarks

Status: working paper and research repository.

This repository develops *A Benchmark for Benchmarks*, an argument and research agenda about what machine-learning benchmarks should measure and how they should be built.

The organizing conclusion is that a benchmark is a measurement system, not merely a dataset. It joins an intended use, target population, construct, coverage specification, data and labels, designed interventions, metric, evaluation protocol, uncertainty analysis, and governance rules. A dataset can be sound while the benchmark built around it is not.

The paper distinguishes sampled observations from designed interventions. Representative samples estimate population performance. Designed interventions test whether model outputs respond correctly to controlled changes, invariances, negative controls, and contradictions. These designs support different claims and should not be collapsed into one score without defensible weights.

## Repository map

- manuscript/main.tex: working manuscript
- manuscript/references.bib: source-checked bibliography used by the manuscript

## Build

The local checks require latexmk, pdflatex, bibtex, chktex, and rg.

    make check

The compiled paper is written to build/main.pdf. Generated files are ignored by Git.

## Current boundary

The repository contains no benchmark data, model results, or empirical findings. The research agenda remains a proposal. No outcome analysis should begin until the target task population, candidate procedures, metrics, and comparison protocol are frozen.
