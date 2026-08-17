# Benchmarking Benchmarks

Status: internal working repository. Do not publish or create a remote without an explicit decision from the author.

This repository develops *A Benchmark for Benchmarks*, an argument and research agenda about what machine-learning benchmarks should measure and how they should be built.

The organizing conclusion is that a benchmark is a measurement system, not merely a dataset. It joins an intended use, target population, construct, data and labels, split, metric, evaluation protocol, uncertainty analysis, and governance rules. A dataset can be sound while the benchmark built around it is not.

Ribeiro-style behavioral tests supply targeted validity evidence. They can reveal failures of specified capabilities or invariances that a representative test sample may rarely exercise. Because such cases are deliberately constructed rather than sampled from a target population, their failure rates should not be folded into the main population-performance score unless the benchmark supplies defensible utility weights.

## Repository map

- manuscript/main.tex: working manuscript
- manuscript/references.bib: source-checked bibliography used by the manuscript
- research/measurement-framework.md: translation from measurement theory to benchmark design
- research/evaluation-architecture.md: design for population, slice, behavioral, and shift evidence
- research/study-design.md: designs for model-rank portability and selective benchmarking studies

## Build

The local checks require latexmk, pdflatex, bibtex, chktex, and rg.

    make check

The compiled paper is written to build/main.pdf. Generated files are ignored by Git.

## Current boundary

The repository contains no benchmark data, model results, or empirical claims. The study designs are proposals. No outcome analysis should begin until the target dataset population, candidate model set, metrics, and comparison protocol are frozen.
