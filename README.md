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
| `netlogo/` | The NetLogo port of the model. Not started yet. |

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

## Plan

1. Port the model (agents, decision, monthly steps, inspection, justice chain, learning, firm
   switching, scenarios, metrics) to NetLogo so that the group's ABM expert can read the code.
2. Share the parameters and scenarios between the Python and NetLogo implementations, so
   that no value is typed twice by hand.
3. Regression-test the two against each other: statistical agreement of every metric over
   repeated runs, deterministic checks where randomness can be removed, and an AI review of
   divergences against the written specification.
4. Translate the Python solution to English and, in the longer run, generalise the
   infrastructure so that other ABMs can be built on it.

## Licence

Not yet decided; to be agreed with the research group before any code is added.
