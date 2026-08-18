#!/usr/bin/env python3
"""Validate the benchmark audit and generate the manuscript evidence profile."""

from __future__ import annotations

import csv
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRAME_PATH = ROOT / "audit" / "frame.csv"
RATINGS_PATH = ROOT / "audit" / "ratings.csv"
BUILD_DIR = ROOT / "build"
SUMMARY_CSV = BUILD_DIR / "audit-summary.csv"
SUMMARY_TEX = BUILD_DIR / "audit-summary.tex"
MACROS_TEX = BUILD_DIR / "audit-macros.tex"

CRITERIA = [
    ("claim_population", "Target population"),
    ("claim_construct", "Construct and categories"),
    ("claim_use", "Intended interpretation or use"),
    ("claim_metric", "Metric rationale"),
    ("coverage_frame", "Source frame and selection"),
    ("coverage_blueprint", "Content blueprint"),
    ("labels_process", "Label construction"),
    ("labels_reliability", "Label reliability"),
    ("labels_validity", "Label validity"),
    ("designed_cases", "Designed or stratified cases"),
    ("designed_pairs", "Controlled response pairs"),
    ("dependability", "Score dependability"),
    ("governance", "Provenance and authorization"),
    ("duplicates", "Duplicate or dependence checks"),
]
ALLOWED_RATINGS = {"yes", "partial", "no", "not_found", "not_applicable"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def escape_latex(value: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "_": r"\_",
        "#": r"\#",
    }
    return "".join(replacements.get(character, character) for character in value)


def validate_frame(frame: list[dict[str, str]]) -> list[str]:
    assert len(frame) == 101, f"expected 101 frame rows, found {len(frame)}"
    orders = [row["frame_order"] for row in frame]
    assert len(set(orders)) == len(orders), "frame_order is not unique"
    assert {row["frame_status"] for row in frame} <= {"eligible", "excluded"}
    assert all(row["exclusion_reason"].strip() for row in frame if row["frame_status"] == "excluded")
    assert all(row["selected"] == "no" for row in frame if row["frame_status"] == "excluded")
    assert len({row["source_snapshot"] for row in frame}) == 1, "mixed frame snapshots"
    eligible = [row for row in frame if row["frame_status"] == "eligible"]
    selected = [row for row in eligible if row["selected"] == "yes"]
    assert len(eligible) == 25, f"expected 25 eligible families, found {len(eligible)}"
    assert len(selected) == 12, f"expected 12 selected families, found {len(selected)}"
    eligible_by_stratum = Counter(row["activity_stratum"] for row in eligible)
    assert eligible_by_stratum == {"high": 7, "low": 9, "middle": 9}, eligible_by_stratum
    selected_by_stratum = Counter(row["activity_stratum"] for row in selected)
    assert selected_by_stratum == {"high": 4, "low": 4, "middle": 4}, selected_by_stratum
    for stratum, size in eligible_by_stratum.items():
        stratum_rows = [row for row in eligible if row["activity_stratum"] == stratum]
        draw_orders = sorted(int(row["draw_order"]) for row in stratum_rows)
        assert draw_orders == list(range(1, size + 1)), f"invalid draw order in {stratum}"
        expected_selected = {
            row["canonical_family"] for row in stratum_rows if int(row["draw_order"]) <= 4
        }
        observed_selected = {
            row["canonical_family"] for row in stratum_rows if row["selected"] == "yes"
        }
        assert observed_selected == expected_selected, f"sample does not follow draw order in {stratum}"
        probability = 4 / size
        for row in stratum_rows:
            assert math.isclose(float(row["selection_probability"]), probability, abs_tol=1e-6)
            assert math.isclose(float(row["sample_weight"]), 1 / probability, abs_tol=1e-6)
    return [row["canonical_family"] for row in selected]


def validate_ratings(ratings: list[dict[str, str]], selected: list[str]) -> None:
    criteria = {criterion for criterion, _ in CRITERIA}
    observed: dict[str, set[str]] = defaultdict(set)
    keys: set[tuple[str, str, str]] = set()
    assert {row["coder_id"] for row in ratings} == {"primary"}, "expected the disclosed primary coder"
    assert len(ratings) == len(selected) * len(criteria), "unexpected number of ratings"
    for row in ratings:
        family = row["canonical_family"]
        criterion = row["criterion_id"]
        coder = row["coder_id"]
        key = (family, criterion, coder)
        assert family in selected, f"rating for unsampled family: {family}"
        assert criterion in criteria, f"unknown criterion: {criterion}"
        assert row["rating"] in ALLOWED_RATINGS, f"invalid rating: {row['rating']}"
        assert row["evidence_url"].startswith("http"), f"missing evidence URL for {key}"
        assert row["evidence_locator"].strip(), f"missing evidence locator for {key}"
        assert key not in keys, f"duplicate rating: {key}"
        keys.add(key)
        observed[family].add(criterion)
    assert set(observed) == set(selected), "ratings do not cover every sampled family"
    for family, family_criteria in observed.items():
        assert family_criteria == criteria, f"incomplete criteria for {family}"


def summarize(ratings: list[dict[str, str]]) -> list[dict[str, str | int]]:
    labels = dict(CRITERIA)
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    for row in ratings:
        counts[row["criterion_id"]][row["rating"]] += 1
    summary = []
    for criterion, _ in CRITERIA:
        criterion_counts = counts[criterion]
        summary.append(
            {
                "criterion_id": criterion,
                "criterion": labels[criterion],
                "yes": criterion_counts["yes"],
                "partial": criterion_counts["partial"],
                "no": criterion_counts["no"],
                "not_found": criterion_counts["not_found"],
                "not_applicable": criterion_counts["not_applicable"],
            }
        )
    return summary


def write_outputs(
    summary: list[dict[str, str | int]], frame: list[dict[str, str]], ratings: list[dict[str, str]]
) -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    with SUMMARY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary[0].keys())
        writer.writeheader()
        writer.writerows(summary)

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\small",
        r"\caption{Evidence documented by the twelve sampled benchmark families}\label{tab:audit-profile}",
        r"\begin{tabular}{@{}lrrrr@{}}",
        r"\toprule",
        r"Criterion & Yes & Partial & No & Not found \\",
        r"\midrule",
    ]
    for row in summary:
        no_count = int(row["no"])
        not_found = int(row["not_found"])
        lines.append(
            f"{escape_latex(str(row['criterion']))} & {row['yes']} & {row['partial']} & "
            f"{no_count} & {not_found} \\\\"
        )
    lines.extend(
        [
            r"\bottomrule",
            r"\end{tabular}",
            r"\begin{minipage}{0.96\linewidth}",
            r"\footnotesize\emph{Note:} Each row is a separate evidentiary requirement, not a component of a quality score. ``Not found'' means that the evidence was not recovered from the primary paper, official data page, or evaluation documentation reviewed for this audit; it does not establish that the activity never occurred. The audit is a probability sample from the bounded frame described in the text, but with twelve families and one coder the counts are illustrative rather than population estimates.",
            r"\end{minipage}",
            r"\end{table}",
        ]
    )
    SUMMARY_TEX.write_text("\n".join(lines) + "\n", encoding="utf-8")

    selected = sum(row["selected"] == "yes" for row in frame)
    eligible = sum(row["frame_status"] == "eligible" for row in frame)
    sources = len({row["evidence_url"] for row in ratings})
    MACROS_TEX.write_text(
        "\n".join(
            [
                rf"\newcommand{{\AuditFrameCount}}{{{len(frame)}}}",
                rf"\newcommand{{\AuditEligibleCount}}{{{eligible}}}",
                rf"\newcommand{{\AuditSampleCount}}{{{selected}}}",
                rf"\newcommand{{\AuditSourceCount}}{{{sources}}}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    frame = read_csv(FRAME_PATH)
    ratings = read_csv(RATINGS_PATH)
    selected = validate_frame(frame)
    validate_ratings(ratings, selected)
    summary = summarize(ratings)
    write_outputs(summary, frame, ratings)
    print(
        f"validated {len(frame)} frame rows and {len(ratings)} ratings; "
        f"selected={len(selected)} criteria={len(CRITERIA)}"
    )


if __name__ == "__main__":
    main()
