SHELL := /bin/sh
TEXBIN := $(dir $(realpath $(shell command -v pdflatex)))
export PATH := $(TEXBIN):$(PATH)

.PHONY: all audit paper lint check clean

all: check

audit:
	python3 audit/analyze.py

paper: audit
	mkdir -p build
	cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build main.tex

lint:
	chktex -q manuscript/main.tex

check: paper lint
	! rg -n "LaTeX Warning: (Citation|Reference).*undefined|There were undefined references|multiply defined|Overfull \\\\[hv]box" build/main.log
	test -s build/main.pdf

clean:
	cd manuscript && latexmk -C -outdir=../build main.tex
