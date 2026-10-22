#!/bin/bash
# Runs the NetLogo model headless over every scenario and seed, then compares the
# result with the Python model's runs. Used locally and in GitHub Actions.
#
#   NETLOGO_HOME=/path/to/NetLogo\ 7.0.4 bash tools/run_regression.sh [threads]
#
# Needs Java 17 or later on the PATH (or JAVA_HOME set) and Python 3.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${NETLOGO_HOME:?Set NETLOGO_HOME to the unpacked NetLogo folder (the one with netlogo-headless.sh)}"
THREADS="${1:-4}"
mkdir -p netlogo/results
echo "Running BehaviorSpace experiment 'regression' with $THREADS threads ..."
( cd netlogo && bash "$NETLOGO_HOME/netlogo-headless.sh" \
    --model waste_crime.nlogox --experiment regression \
    --table results/netlogo_runs.csv --threads "$THREADS" 2>&1 | grep -v '^JAVA_HOME' || true )
test -s netlogo/results/netlogo_runs.csv || { echo "No NetLogo output produced."; exit 1; }
# Python is "python3" on Linux and macOS and usually "python" on Windows, where "python3"
# may be a Microsoft Store stub that only prints an error. Take the first that runs.
# PYTHON=/path/to/python overrides.
if [ -z "${PYTHON:-}" ]; then
  for candidate in python3 python py; do
    if "$candidate" -c "import sys" > /dev/null 2>&1; then PYTHON="$candidate"; break; fi
  done
fi
test -n "${PYTHON:-}" || { echo "No working Python found on the PATH. Set PYTHON=/path/to/python."; exit 1; }
echo "Comparing with the Python reference runs ..."
"$PYTHON" tools/compare.py netlogo/results/netlogo_runs.csv reference/python_runs_v0.2.csv \
    --out netlogo/results/comparison.md
echo "Report: netlogo/results/comparison.md"
