# abm-waste-crime-netlogo

An agent-based model (ABM) of organised waste crime in Sweden, being ported to NetLogo from a
Python prototype, with the complete record of how the prototype was built.

The project is a collaboration between an international research group and SMOB (Sweden
against Organised Crime). The prototype was built in autumn 2026 with Claude Code from the
group's source material, to make the group's assumptions explicit and show where data is
missing. It is not calibrated and not validated. Its results are outcomes under stated
assumptions, not estimates of reality.

## What is here

| Path | Content |
| --- | --- |
| `PROJECT_LOG.md` | Everything done in the project, in order, with reasons, basis and effect. Updated with every change. |
| `prompts/` | Every instruction given to the AI, in Swedish and English, and how the prompts were produced |
| `netlogo/waste_crime.nlogox` | The NetLogo 7 port of the model, one file, with BehaviorSpace experiments. See `netlogo/README.md`. |
| `netlogo/data/` | Parameters and scenarios as CSV, generated from the Python project's configuration |
| `reference/` | The Python model's 240 reference runs (8 scenarios x 30 seeds) and the comparison report |
| `tools/` | `compare.py` (statistical comparison of the two implementations) and `run_regression.sh` |
| `.github/workflows/` | Runs the NetLogo model headless and compares it with Python on every push |

## What is not here

- The research group's source material (reports, articles, case descriptions, memos). The
  log lists what it is and what each piece was used for.
- The Python prototype with its web interface, which is in a private repository. The
  interface runs at https://stg-abm-avfall.csmob.dev with login by e-mail code.
- Any non-public data.

## The model in brief

A small Swedish waste market at one tenth of national scale, simulated month by month over
ten years. Five kinds of agents: waste producers, waste firms, the decision-makers who
actually control the firms, municipal supervisory authorities, and one justice chain. The
decision-makers choose, per customer, between legal handling, dumping and reclassification,
using the group's formula U = reward + propensity − effort − risk, with risk perceived rather
than actual. A baseline and seven interventions are each run 30 times with shared random
seeds. Every parameter value is labelled by origin: source, derived, placeholder, assumption
or open question. Five values rest on Swedish data; the rest are placeholders awaiting the
group's answers.

## Status

1. **Port: done (2026-10-22).** The model (agents, decision, monthly steps, inspection,
   justice chain, learning, firm switching, scenarios, metrics) runs in NetLogo 7.0.4.
2. **Shared data: done.** Parameters and scenarios are exported from the Python project's
   YAML to CSV; a test in the Python project fails if the CSV is stale.
3. **Regression test: done.** `tools/compare.py` compares the distributions of 27 metrics
   per scenario and the intervention effects between the two implementations. The report
   is in `reference/`. Exact equality is impossible (different random number generators),
   so agreement is statistical.
4. Next: review by the research group's ABM expert; translation of the Python solution to
   English; in the longer run a general ABM infrastructure.

## Rule for changes

A change to the model is made in the specification first (the model notes), then in both
implementations, then the regression test must pass. A changed parameter value is made in
the Python project's `config/`, exported, and committed here.

## Licence

Not yet decided; to be agreed with the research group before any code is added.
