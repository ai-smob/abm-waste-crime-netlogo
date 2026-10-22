"""Compares the NetLogo port with the Python model, run by run and scenario by scenario.

The two implementations use different random number generators, so the same seed
gives different runs. The comparison is therefore statistical: for every scenario
and metric, the mean over the seeds in NetLogo is compared with the mean over the
seeds in Python, and the difference is judged against its standard error. The
intervention effects (scenario minus baseline, pairwise by seed within each
implementation) are compared in the same way.

    python tools/compare.py netlogo/results/netlogo_runs.csv reference/python_runs_v0.2.csv

Writes a Markdown report (default results/comparison.md) and exits with status 1 if
any metric disagrees. Only the Python standard library is used.

Verdict per scenario and metric:
    agree      |difference of means| <= Z * standard error of the difference
    DIFFERS    otherwise
with Z = 3 (about one false alarm in 400 comparisons when the models are identical).
Metrics whose spread is zero in both implementations must be exactly equal.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

# NetLogo metric reporter -> Python metric name (outputs.py)
METRICS = {
    "illegal-share": "illegal_share",
    "illegal-batches-per-year": "illegal_batches_per_year",
    "avoided-cost-per-year-msek": "avoided_cost_per_year_msek",
    "fines-per-year-msek": "fines_per_year_msek",
    "fines-to-gain": "fines_to_gain",
    "fines-uncollectable-share": "fines_uncollectable_share",
    "inspections-per-year": "inspections_per_year",
    "road-checks-per-year": "road_checks_per_year",
    "hit-rate": "hit_rate",
    "detections-per-year": "detections_per_year",
    "reports-private-per-year": "reports_private_per_year",
    "sanctions-per-year": "sanctions_per_year",
    "prohibitions-per-year": "prohibitions_per_year",
    "company-switches-per-year": "company_switches_per_year",
    "detected-share": "detected_share",
    "top5pct-share-of-illegal": "top5pct_share_of_illegal",
    "max-companies-per-controller": "max_companies_per_controller",
    'pathway-share-of-illegal "dumping"': "dumping_share_of_illegal",
    'pathway-share-of-illegal "misclassification"': "misclassification_share_of_illegal",
    'perceived-detection-end "dumping"': "perceived_detection_dumping_end",
    'perceived-detection-end "misclassification"': "perceived_detection_misclassification_end",
    'share-of-illegal-ctype "ordinary"': "share_of_illegal_ctype_ordinary",
    'share-of-illegal-ctype "prior_record"': "share_of_illegal_ctype_prior_record",
    'share-of-illegal-ctype "oc_linked"': "share_of_illegal_ctype_oc_linked",
    'share-of-detections-ctype "ordinary"': "share_of_detections_ctype_ordinary",
    'share-of-detections-ctype "prior_record"': "share_of_detections_ctype_prior_record",
    'share-of-detections-ctype "oc_linked"': "share_of_detections_ctype_oc_linked",
}
Z = 3.0


def to_float(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        return float("nan")


def read_netlogo(path: Path) -> dict[tuple[str, int], dict[str, float]]:
    """BehaviorSpace table: six header lines, then a header row and one row per run."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    rows = list(csv.reader(lines[6:]))
    header, body = rows[0], rows[1:]
    out = {}
    for row in body:
        record = dict(zip(header, row))
        key = (record["scenario-name"], int(float(record["run-seed"])))
        out[key] = {py: to_float(record[nl]) for nl, py in METRICS.items() if nl in record}
    return out


def read_python(path: Path) -> dict[tuple[str, int], dict[str, float]]:
    out = {}
    with open(path, encoding="utf-8") as f:
        for record in csv.DictReader(f):
            key = (record["scenario"], int(record["seed"]))
            out[key] = {py: to_float(record[py]) for py in METRICS.values() if py in record}
    return out


def by_scenario(runs: dict) -> dict[str, dict[int, dict[str, float]]]:
    result: dict = defaultdict(dict)
    for (scenario, seed), metrics in runs.items():
        result[scenario][seed] = metrics
    return result


def stats(values: list[float]) -> tuple[float, float, int]:
    values = [v for v in values if not math.isnan(v)]
    if not values:
        return float("nan"), float("nan"), 0
    return mean(values), (stdev(values) if len(values) > 1 else 0.0), len(values)


def judge(a: list[float], b: list[float]) -> tuple[str, float, float, float, float, float]:
    """Returns (verdict, mean_a, sd_a, mean_b, sd_b, z)."""
    ma, sa, na = stats(a)
    mb, sb, nb = stats(b)
    if na == 0 or nb == 0:
        return "no data", ma, sa, mb, sb, float("nan")
    se = math.sqrt(sa ** 2 / na + sb ** 2 / nb)
    if se == 0:
        return ("agree" if abs(ma - mb) < 1e-9 else "DIFFERS"), ma, sa, mb, sb, float("inf")
    z = abs(ma - mb) / se
    return ("agree" if z <= Z else "DIFFERS"), ma, sa, mb, sb, z


def fmt(x: float) -> str:
    if math.isnan(x):
        return "n/a"
    if math.isinf(x):
        return "exact"
    return f"{x:.4g}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("netlogo_csv", type=Path)
    parser.add_argument("python_csv", type=Path)
    parser.add_argument("--out", type=Path, default=Path("results/comparison.md"))
    args = parser.parse_args()

    nl = by_scenario(read_netlogo(args.netlogo_csv))
    py = by_scenario(read_python(args.python_csv))
    scenarios = [s for s in py if s in nl]
    missing = [s for s in py if s not in nl]
    metrics = list(METRICS.values())

    lines = ["# Comparison of the NetLogo port with the Python model", ""]
    lines.append(f"NetLogo runs: `{args.netlogo_csv}`. Python runs: `{args.python_csv}`.")
    lines.append(f"Verdict rule: agree when |difference of means| <= {Z:g} x its standard error. "
                 "Seeds are not comparable between the implementations (different random "
                 "number generators), so only distributions are compared.")
    if missing:
        lines.append(f"\nScenarios missing in the NetLogo results: {', '.join(missing)}")
    n_differs = 0
    n_total = 0

    # 1. Levels per scenario
    for scenario in scenarios:
        lines += ["", f"## {scenario}: levels", "",
                  "| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |",
                  "| --- | --- | --- | --- | --- |"]
        for metric in metrics:
            a = [r[metric] for r in nl[scenario].values() if metric in r]
            b = [r[metric] for r in py[scenario].values() if metric in r]
            verdict, ma, sa, mb, sb, z = judge(a, b)
            n_total += 1
            n_differs += verdict == "DIFFERS"
            lines.append(f"| {metric} | {fmt(ma)} ({fmt(sa)}) | {fmt(mb)} ({fmt(sb)}) | {fmt(z)} | {verdict} |")

    # 2. Intervention effects: scenario minus baseline, pairwise by seed within each implementation
    if "baseline" in scenarios:
        lines += ["", "## Intervention effects (scenario minus baseline, pairwise by seed)", "",
                  "| Scenario | Metric | NetLogo effect (sd) | Python effect (sd) | z | Verdict |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for scenario in scenarios:
            if scenario == "baseline":
                continue
            for metric in ("illegal_share", "detected_share", "detections_per_year",
                           "prohibitions_per_year", "company_switches_per_year",
                           "inspections_per_year", "road_checks_per_year"):
                a = [nl[scenario][s][metric] - nl["baseline"][s][metric]
                     for s in nl[scenario] if s in nl["baseline"]]
                b = [py[scenario][s][metric] - py["baseline"][s][metric]
                     for s in py[scenario] if s in py["baseline"]]
                verdict, ma, sa, mb, sb, z = judge(a, b)
                n_total += 1
                n_differs += verdict == "DIFFERS"
                lines.append(f"| {scenario} | {metric} | {fmt(ma)} ({fmt(sa)}) | {fmt(mb)} ({fmt(sb)}) | {fmt(z)} | {verdict} |")

    summary = (f"**Result: {n_total - n_differs} of {n_total} comparisons agree, "
               f"{n_differs} differ.**")
    lines.insert(4, "")
    lines.insert(5, summary)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(summary)
    print(f"Report: {args.out}")
    return 1 if n_differs else 0


if __name__ == "__main__":
    sys.exit(main())
