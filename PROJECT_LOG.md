# Project log

Everything done in the project, in order, with what was done, why, on what basis and with
what effect. New entries go at the bottom. Dates are Swedish local time. "The author" is the
person who gave the instructions; "the AI" is Claude Code with the model Claude Fable 5.1,
which wrote all code and documentation. The exact instructions are in `prompts/`.

This log was started on 2026-10-22 and backfilled from the Git history, the change log in
the Swedish model notes, the Claude Code session logs and the author's notes. Entries before
that date are reconstructions; where a time is given it comes from the session logs.

## Sources available to the AI

The AI was given a `docs/` folder with the research group's material. None of it is in this
repository. The AI read the five Word documents and the Police report in full and the four
articles up to and including their discussion and limitations sections.

| Material | Used for |
| --- | --- |
| Birks, Groff & Malleson (2025), Agent-Based Modeling in Criminology, Annual Review of Criminology | The workflow (conceptualise, build, verify, calibrate, validate, experiment); start simple and state every assumption; validate against patterns rather than exact counts |
| Gerritsen (2015), Agent-based modelling as a research tool for criminological research, Crime Science | The four steps conceptualisation, formalisation, simulation, evaluation; the fault-finding logic |
| Calderoni et al. (2022), Recruitment into Organized Crime: An Agent-Based Approach, J. Quantitative Criminology | The design: baseline versus interventions, intervention switched on after burn-in, many repeated runs, sensitivity at 0.5 and 1.5, scaled-down population; the group's decision not to use a utility function |
| van der Zwet et al. (2025), Opportunistic Organization of Illicit Supply Chains, J. Quantitative Criminology | Supply chain as a sequence of activities; actors weighing profit against risk; replacement of removed actors |
| Swedish Police (Noa), EcoCrim report on environmental and waste crime 2024 | Justice chain outcomes 2024 (reports, dropped cases, fines); who reports; modus operandi; 71 active gang criminals in 113 waste transport companies; market size |
| The group's literature review of Swedish reports (August 2026) | Numbers of companies, transporters, representatives, company brokers; share with criminal records and organised-crime links; roles in the chain; front men; the contagion effect through price pressure |
| The group's text on how authorities operate, vulnerabilities and the illegal business model | How supervision, reporting and investigation work; the eight vulnerabilities; the business model |
| The group's case descriptions: Think Pink, Black Mass, Stena Recycling | Mechanics of the schemes; real amounts per tonne; how profit was shared |
| The group's memo with the decision formula and meeting notes of 28 August 2026 | U = reward + propensity − effort − risk; the group's conceptual model |

## 2026-09-30, model version 0.0 to 0.2 and the first documentation

**07:29. Initial prompt.** The author gave the AI the initial prompt (`prompts/2026-09-30-initial-model-prompt.en.md`): build a first runnable prototype in Python from the material in `docs/`, invent nothing without labelling it, document everything in Swedish for non-technical readers in `ABM_MODEL_NOTES.md`, work in a stated order with documentation before code, and treat the prototype as a tool for making the group's assumptions explicit.

**Version 0.0: documentation before code.** The AI inventoried the sources, wrote the source overview, the group's conceptual model, candidate agents and relations, what is empirically established and what is missing, alternatives for the model's landscape, and a proposal for a minimal first model. Basis: the initial prompt's order of work. No code yet.

**Version 0.1: first runnable model.** Five agent types (waste producers, waste firms, decision-makers, supervisory authorities, one justice chain), two illegal options (dumping, reclassification), inspection, the justice chain, learning of perceived risk, firm switching, and eight scenarios (baseline plus seven interventions). Monthly steps over ten years, 30 runs per scenario with shared seeds, interventions switched on in month 37. Baseline gave 4.0 % of waste handled illegally; the interventions gave 4 to 19 % reductions. Results archived in the private repository under `resultat/arkiv_v0.1/`.

Three deviations from the proposal, made during the first test runs and recorded in the change log:

1. The decision is made per arrangement (customer relation) and revisited about once a year, not per consignment every month. Reason: with monthly decisions more than half of all ordinary firms handled at least one consignment illegally each year, 22 % of inspections produced a finding and a fifth of all firms were banned within ten years, unlike the sources' picture of long-running schemes by a smaller number of actors. Labelled as an assumption supported by the case descriptions (Stena, Black Mass). New placeholder parameter: revisit once a year. Effect: illegal handling concentrates in fewer firms; findings per inspection fell to 8 %; the level is unchanged.
2. The placeholder propensity values were changed from −5.5 / −3.5 / −1.0 to −6.0 / −4.0 / −1.0 for the three decision-maker types, as a consequence of the change above. Still placeholders.
3. New placeholder parameter: half of the customers follow a decision-maker to a new firm. Without it a new firm starts from zero and switching is unreasonably costly; Think Pink ran several firms under one brand.

**Version 0.2: price pressure and fairer roadside checks.**

1. Price pressure switched on: firms that handle waste illegally charge less, and customers are drawn to lower prices. Version 0.1 lacked the mechanism the sources describe as the core of the business model. Source for the mechanism; placeholders for its strength (30 % price advantage, price sensitivity 5). Effect: illegal share from 4.0 to 5.9 %; the organised-crime-linked actors' share of illegal waste from 38 to 51 %; spread between runs doubled.
2. Roadside checks redefined as a share of all transports, with the number of checks counted. In 0.1 the roadside scenario had the largest effect (−19 %) but corresponded to 720 checks a year against 120 inspections, unseen. The scenario was changed from 5 % of illegal transports to 1 % of all. Effect fell to −9 % with 115 more checks a year. Scenarios are now reported with their number of inspections.
3. The contagion effect (legal firms dragged along when the market deteriorates) was built in but switched off (weight 0): the sources mention the mechanism but give no size, and it is not in the group's formula. Tested in the sensitivity analysis, where it nearly triples the illegal share.
4. Fix: a firm already closed during the month gets no further findings (an edge case where two roadside checks in one month could give a fourth finding). Negligible effect.

**Results of version 0.2** (30 runs per scenario, measured from month 37 to 120): baseline 5.9 % illegal, 15.9 % of illegal waste detected, fines 0.5 % of illegal profit (real figure derived from EcoCrim: 0.1 to 0.3 %), a third of fines uncollectable because the firm is gone. Six of seven interventions reduce illegal waste by 4 to 10 %; risk-based targeting alone is indistinguishable from the baseline. The one-at-a-time sensitivity analysis showed the level is governed by propensity, reward weight, price advantage and the contagion effect, all placeholders, while inspection and sanction parameters matter little to the level.

**Tests.** 14 automated tests of the model (parameters match the catalogue, reproducibility with seeds, invariants of the monthly step).

**08:22.** The author asked the AI to save its working notes (project rules: Swedish documentation, no invented values, label everything, update the change log).

**12:34 to 14:42. Printable and HTML versions of the notes.** First a printable version was requested; the AI service returned overload errors (code 529) for part of the day. Then a static HTML page of the notes was built (`build_html.py`) with hover explanations of terms for readers unfamiliar with ABM or the research, from a term list in `config/begrepp.yaml`. The author listed example terms (model, actual decision-makers, municipal supervisory authorities, dumping, reclassification, propensity, baseline scenario, intervention, risk-based supervision, information sharing).

**14:56.** `.gitignore` created. **14:57.** First Git commit, "init", containing the model, the notes, the HTML page, the result files and the tests.

**15:06. Web interface prompt** (`prompts/2026-09-30-web-interface-prompt.en.md`). The author asked for a Swedish web interface in which researchers can change parameters, run experiments, sweep a parameter, compare interventions with a baseline under the same assumptions and seeds, see results with spread and intervals, and save and export experiments, without a separate model implementation. The AI chose Streamlit. The work was carried out the same afternoon:

- A parameter catalogue (`config/parameterkatalog.yaml`) with Swedish name, explanation, unit, default, label (source / derived / placeholder / assumption), reference to the notes, technical bounds, and the empirical basis where one exists. A test fails if a parameter exists without a catalogue entry.
- Four pages: new experiment, run and status, results, saved experiments. Changed assumptions apply from the start in all scenarios including the baseline; interventions switch on after the burn-in; differences are computed pairwise by seed and shown in percentage points with 95 % intervals.
- Runs in a separate process, several in parallel, with a configurable limit on the number of runs and a cancel button.
- Experiments saved under `experiment/` with full configuration, seeds, model version, Git revision, per-run results and status.
- Verification: a standard run in the interface reproduces all 9 840 values of the command-line run exactly. 32 new tests.
- The notes gained a section 22 on the interface, including its limitations (one parameter swept at a time, one experiment at a time, fixed interventions, no cost accounting).

**16:07.** The interface was started locally and the first experiment, "Lokalt test 1", ran 450 runs in 38 seconds.

## 2026-10-01, login, animation, staging and the AI summary

**07:21 to 07:55. Explanations only.** The author read the HTML notes and asked the AI to explain, without changing anything, the difference between baseline scenario, baseline (grundscenario), intervention and experiment, and whether "invented demonstration values" means the AI invented them or took them from the documents, and how calibration is done. The answers led to no code change.

**11:01. Login with a one-time code.** Modelled on another SMOB project: the user enters an e-mail address, receives a six-digit code, and is logged in for 180 days. Experiments are saved with the e-mail address as owner and each user sees only their own. Local use on `localhost` skips the login and saves under a default address (asked for at 11:50, since sending e-mail from a local machine is hard). Older experiments without an owner are visible to all. 8 new tests. No model change.

**11:29 to 11:30.** Committed. The branch was renamed from `master` to `main` at the author's request.

**11:32. Animation of a run.** The author's idea: while waiting for an experiment, show the model as moving agents with lines between them (producers to firms, firms to decision-makers). The AI built an animation that replays a real run with annotations of events, with no model logic of its own. At 12:36 to 12:44 the author asked what the animation shows and asked that it keep pace with the experiment and finish when the experiment finishes. Hence "calm pace": an experiment takes at least 60 seconds by default, switchable off. Saved experiments are selected by marking a row. 4 new tests. No model change.

**13:51. Notes as a page, staging deployment.** Committed. The notes became a page inside the application, linked from the side menu (at 14:17 changed to open in a new tab without the side menu). The interface was deployed on a shared staging server as https://stg-abm-avfall.csmob.dev, with login by e-mail code; an unused language model was removed from the server to free memory. The source material is not on the server. The server has two processor cores, so large experiments take time.

**14:14.** Login restricted to addresses ending in `@sh.se` (Södertörn University), since the staging site is reachable from the internet. A server setting, not a model assumption.

**14:23. Developer information removed from the notes.** The notes are now read by researchers in the interface, so everything aimed at developers (how to run the model, files, folders, settings, local use) was moved to the README. Section "21. How to run the model" was removed and later sections renumbered (glossary 21, web interface 22).

**14:58 to 15:03.** `experiment/` added to `.gitignore`. A private GitHub repository was created and the code pushed. A GitHub Actions workflow was added that runs the tests on every push to `main` and, if they pass, deploys to staging; action versions were raised to remove a warning. From here on every push to `main` deploys.

**15:13. AI summary on the results page.** At the top of each result an AI-written summary in prose: what was changed, what the result was, and suggestions for the next experiment. On the server the summary is written by a language model at Berget AI (servers in Sweden); locally by Claude through its command-line tool. The language model receives only numbers already computed for the results page and is instructed to use nothing else, keep percentage points and percent apart, say when a difference cannot be distinguished from chance, remind that the model is not calibrated or validated, and not draw conclusions about reality. When assumptions were changed, a reference run with default values and the same seeds is made so that the effect of the changed assumptions can be stated. The summary is saved with the experiment together with its input and the model that wrote it. Tests never call an AI service. 6 new tests. No model change.

**15:39 to 15:44.** The author asked what to tell the researcher who initiated the project when sending the link, and which sections non-researcher colleagues should read. Advice only.

State at the end of the day: 67 tests passing; everything committed and deployed.

## 2026-10-05, questions to the research group

**11:01.** The author asked for a document listing the assumptions made by the AI that should be converted into facts, or at least informed guesses from an expert. The AI wrote `UNDERLAG_TILL_FORSKARGRUPPEN.md` (Swedish): the five questions that matter most, ordered by the sensitivity analysis (propensity by actor type and whether organised-crime-linked actors offend more; price advantage, customer loyalty and contagion; legal treatment cost and cost shares avoided; inspection frequency, method and detection probabilities; what the real penalty is); all other placeholders and assumptions by theme; derived values that look more reliable than they are; design choices F1 to F13 as yes/no questions; a suggested answer template. It proposes a new label, EXPERT JUDGEMENT with name and date, for informed guesses, which the group has not yet taken a position on.

**11:28.** Converted to HTML and linked from the side menu next to the notes. Committed and pushed, so deployed on staging. No model change.

## 2026-10-06, explanations

The author asked what "random seed" and "limit on the number of runs" mean, and how increasing the seed count helps. Explanations only; no change.

## 2026-10-07, checking assumptions against a research database (uncommitted)

**14:02 to 14:08.** The author asked the AI to search SMOB-MCP, a curated database of research on organised crime run by SMOB (Sweden against Organised Crime), for anything that could replace the model's placeholders, with strict rules: nothing from the AI's own prior knowledge, verify everything against the database, do not change the documentation or the labels, and prefer reporting "nothing found" to inserting an unverified value. A button "Load values from SMOB chat" was to fill the form with whatever was verified.

**Result.** About 30 queries in Swedish and English. The database holds few waste-crime sources (an Acta Publica 2026 mapping of organised crime among representatives in the waste trade, a 2025 Swedish research overview, Suvantola & Kankaanranta 2018, Environment Agency 2018, UNEP 2015, INTERPOL 2020 and 2022, Comte 2006, Gibbs et al. 2009). No placeholder got a Swedish verified value. Two entries were verifiable: the share of organised-crime-linked firms, 80 of 2 423 (identical to the model's default, now confirmed by a second source, with the figures 55 current, 30 historical and 5 overlapping quoted), and a research range that illegal disposal is three to more than ten times cheaper than legal, loaded as a parameter interval of 10 to 33 % for the cost share avoided by dumping. The overlap of 61 firms and the EcoCrim prosecution figures are not in the database.

**Built.** `config/smob_varden.yaml` with each entry's verbatim quote, source and derivation and a list of what was searched without result; `wastecrime_abm/smob.py`; the button next to "Reset to defaults", which also shows the sources and quotes; 5 new tests (72 passing). As agreed, the notes, the question document, the labels and the README were not touched. As of 2026-10-22 this work is still uncommitted in the private repository.

## 2026-10-20, login opened to all addresses

The author asked that any e-mail address be allowed to log in on staging, so that participants outside Södertörn University can use the interface, and that the change be deployed. Done as a server setting; the restriction can be switched back on. The staging server had also moved to a new address, recorded in the README. Committed and deployed. No model change.

## 2026-10-22, briefing, meeting with the research group, this repository

**08:49 to 09:06. English briefing.** For the meeting with the international research group the author asked for a document in English describing the service. The AI wrote a briefing (purpose; the model with a diagram of the five agent types and their relations; evidence base with the label scheme, the five grounded parameters and the sensitivity table; the web service; status and limitations with the intervention results; open questions; next steps) and exported it as an 11-page PDF, `Waste_Crime_ABM_Prototype_Briefing.pdf`, sent to the group.

**13:25.** The author asked what NetLogo is. Explanation only.

**Meeting with the research group** (a transcript is held privately). Participants: two senior researchers from the group (one in policing and crime at place, one the group's ABM expert, with earlier EU-funded ABM projects on organised crime and recruitment to terrorism), the group's Swedish contact, and from SMOB the innovation lab lead, the AI colleague and the author. Outcomes:

- The group found the prototype a convincing proof of concept. The ABM expert had run it and said the documentation was impressive, with every choice specified, discussed and justified or explicitly marked as invented.
- The decision to hire a full-time programmer was dropped. The group wants SMOB as a research partner. SMOB's time has to be estimated and approved internally.
- Division of work: the group writes a strict and detailed blueprint and answers the questions; SMOB manages the AI and runs the models.
- The group's formula U = reward + propensity − effort − risk was described by the lead researcher as a first thought from a memo, not a settled choice. This confirms open question F13 (keep the formula or replace it with evidenced risk factors) as one for the group.
- The ABM expert prefers NetLogo because he can read that code himself; NetLogo experts he consulted refuse to read machine-written code. He has built a smaller NetLogo model of his own with Claude Code on his own material and wants to compare. The author promised to port the Python model to NetLogo and send it, together with the prompts used.
- The group intends to publish the work. The documentation must have no non-transparent holes.
- A non-public data source is coming: an Italian project producing weights for companies involved in waste crime.
- The lead researcher's longer aim: many such models for different organised crime problems, built quickly and cheaply, to bring ABM into evidence-based policy where no field trials exist.

**14:14 to 14:23. To-do list and this repository.** The author set out the next steps: continuous detailed documentation in English, published openly on GitHub; backfill of the documentation to date; translation of the whole solution to English with a language toggle; a NetLogo port of the model with shared data and regression testing against the Python version, in a public repository; and a general ABM infrastructure that can be filled with any parameters. The AI wrote the to-do list (kept in the private repository for now). The author decided that the public repository holds only what is needed to review the solution, never the source material, and that duplicating data between the two implementations is acceptable if it is simplest.

**This repository** `abm-waste-crime-netlogo` was created, with this log, the prompts in Swedish and English, and a placeholder for the NetLogo port. The log was backfilled from the sources named at the top.

## 2026-10-22, afternoon: the NetLogo port, shared data and the regression test

**Decision (the author).** Keep the public repository simple: it holds only what the group's ABM expert needs to review the solution; data may be duplicated between the Python and NetLogo projects if that is simplest; the source material never goes there. The local folder was renamed `abm-netlogo`, a sister folder of the Python project.

**Shared data.** `scripts/export_netlogo_data.py` in the Python project flattens `config/parametrar.yaml` and `config/scenarier.yaml` into `netlogo/data/parameters.csv` (key, type, value; dotted keys; lists with an index) and `netlogo/data/scenarios.csv`. A new test in the Python project, `tests/test_netlogo_export.py`, fails if the exported files differ from the configuration, so a value cannot exist in two versions. NetLogo cannot read YAML, which is why CSV was chosen; the `csv` and `table` extensions that ship with NetLogo load it into a parameter table at setup.

**NetLogo version.** The NetLogo 6.4 downloads are no longer served; the current release is 7.0.4, which uses a new XML file format (`.nlogox`) and reads the old `.nlogo` as well. The port targets 7.0.4. NetLogo was run headless through its Linux distribution under the system's Java 21, on Windows through Git Bash, which also serves as the GitHub Actions setup.

**The port** (`netlogo/waste_crime.nlogox`, one file, written by the AI from the Python code). Four hidden breeds for producers, firms, decision-makers and authorities; a fifth for illegal consignments; reports and pending firm starts as lists. The monthly loop has the same nine steps in the same order as the Python `step()`. The decision formula, the multinomial-logit extension to two illegal options, the inspection selection (complaints first, then a weighted draw without replacement), vicarious learning once per other active firm, the firm-closure rules and all 27 metrics are written to match the Python definitions line by line. Deliberate correspondences and the places where identical behaviour is impossible are listed in `netlogo/README.md`. The interface is minimal (scenario chooser, seed, buttons, a plot) since the model has no spatial component. Three BehaviorSpace experiments are stored in the file: `smoke`, `regression` (8 scenarios x 30 seeds, final metrics) and `timeseries`.

Compiler errors met and fixed along the way, for the record: `inspect` is a NetLogo primitive (renamed `inspect-company`); a reporter cannot be called as a command; an anonymous reporter cannot hold statements (the utility calculation became a named reporter); turtles cannot `create-` other turtles (`hatch-batches` instead); a global named `C` collided with lambda variables; a stepped value set in the experiment definition made BehaviorSpace run out of memory while enumerating runs, so the seeds are enumerated.

**Regression test.** `tools/compare.py` (standard library only) reads the BehaviorSpace table and the Python model's run table and, for every scenario and metric, compares the mean over the 30 seeds in NetLogo with the mean over the 30 seeds in Python, judged against the standard error of the difference (verdict "agree" when the z-score is at most 3). It does the same for the intervention effects, scenario minus baseline pairwise by seed within each implementation. The Python model's 240 reference runs from 2026-09-30 are committed as `reference/python_runs_v0.2.csv`. `tools/run_regression.sh` runs the experiment headless and the comparison; `.github/workflows/regression.yml` does the same on every push, downloading and caching NetLogo. Exact equality is not possible: NumPy uses PCG64, NetLogo Mersenne Twister, and `ask` processes agents in random order.

**Result of the comparison** (`reference/comparison_2026-10-22_8_scenarios_30_seeds.md`). Of 265 comparisons (27 metrics x 8 scenarios of levels, plus 7 metrics x 7 interventions of effects), 263 agree. The baseline illegal share is 5.6 % in NetLogo against 5.9 % in Python (z = 0.6); the intervention effects on the illegal share agree for all seven interventions with z at most 1.1. The two that fell just over the threshold (roadside checks per year in one scenario, z = 3.07, and the effect of higher sanctions on prohibitions per year, z = 3.22) were rerun with 100 seeds in both implementations (`reference/comparison_2026-10-22_baseline_and_higher_sanctions_100_seeds.md`): all 61 comparisons agree, the two in question at z = 1.9. With 265 comparisons at a threshold of 3, about one false alarm is expected when the models are identical, so the two were chance. The NetLogo port reproduces the Python model within sampling variation. The 240 NetLogo runs are kept as `reference/netlogo_runs_2026-10-22.csv`.

**Not yet done.** Review of the NetLogo code by the group's ABM expert; the deterministic unit checks of the formula with randomness removed; an AI review step that reads both implementations against the specification when the comparison fails.

**First GitHub Actions run.** The workflow ran in 8 minutes on Ubuntu (NetLogo 7.0.4 headless under Java 21) and reproduced the local result exactly: 263 of 265 agree, the same two borderline flags. Since the exit status failed on them, the pass rule in `tools/compare.py` was made family-wise: a run fails only if any comparison has z > 4.5 or more than 2 % of the comparisons have z > 3. Individual flags above 3 are still listed in the report for a person to look at. The reasoning: with 265 comparisons at a threshold of 3, one or two chance flags are expected when the models are identical, while a real divergence shows up as a large z or as many flags at once (every bug met during the port did).
