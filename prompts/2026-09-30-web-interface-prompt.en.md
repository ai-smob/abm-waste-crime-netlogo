# Web interface prompt, 2026-09-30 (English translation)

This is a translation of `2026-09-30-web-interface-prompt.sv.md`, the prompt that produced the
web interface. It was given to Claude Code (model Claude Fable 5.1) at 15:06 local time on
2026-09-30, after the model (version 0.2) and its documentation existed. The Swedish original
was pasted as one line; the section structure below is restored from its headings.

---

You are to further develop the existing system for agent-based simulation of organised waste
crime. Build a Swedish-language web interface where researchers can change parameters, run
experiments and compare the results.

## Starting point

Read first:
- `README.md`
- `ABM_MODEL_NOTES.md`
- existing configuration files, run scripts and model code
- any project instructions.

Start from what actually exists in the project. Reuse the simulation and its decision logic.
The interface must call the same model as the command-line tools, without a separate
implementation.

The model is a technical prototype that is not calibrated or validated. The interface is to
help the researchers examine assumptions and prioritise data collection. Results are to be
presented as outcomes under chosen assumptions.

Choose a simple technical solution that fits the existing Python project. Streamlit is a
possible option if the project lacks a web interface. Document the technology choice and carry
out the work.

## 1. Create and configure experiments

The researcher must be able to:
- give the experiment a name and description,
- choose which existing intervention scenarios to compare,
- change model parameters,
- set the number of repetitions, 30 by default,
- reset to the model's default values,
- see a summary of the changes before starting.

Start with a clear selection of important parameters:
- propensity to offend for each type of decision-maker,
- price advantage for companies that handle waste illegally,
- customers' price sensitivity,
- contagion effect,
- legal treatment cost,
- inspection frequency,
- share of on-site inspections,
- detection probabilities,
- corporate fine and sanction probability,
- company switches.

Verify the parameters' actual names and meaning in the code. Group them comprehensibly. Put
the other settings in an advanced view.

Each parameter must show:
- Swedish name and explanation,
- unit and default value,
- source or reference to the model notes,
- label: SOURCE, DERIVED, PLACEHOLDER or ASSUMPTION.

Distinguish technically permitted values from empirically established ranges. Do not invent
scientifically plausible bounds. Use numeric fields where sliders would give misleading
limits, for example for propensity.

Changes in the interface must create a separate experiment configuration and not overwrite
the project's default files.

## 2. Compare with a baseline

Distinguish between:
- changed assumptions about the market, the actors and the starting state,
- interventions that change how the authorities work.

When assumptions are changed, a new baseline must be run with those assumptions. The
interventions are to be compared with this baseline, under the same shared assumptions.

Reuse the model's design with a burn-in period and the same set of random seeds for
comparable scenarios. Keep the existing logic for when interventions are activated. Report
which assumptions and interventions each comparison is based on.

## 3. Sweep a parameter range

Implement a function where the researcher chooses a parameter and specifies:
- lowest value,
- highest value,
- number of values to try.

For each value the system must run the baseline and the chosen interventions several times.
Show how both the level of illegal handling and the interventions' effect change.

The first version only needs to vary one parameter at a time. Describe this as a limited
sensitivity analysis, not as a complete analysis of all uncertainty.

Show the number of planned runs before starting and set a configurable limit against
unintentionally very large experiments.

## 4. Running and status

Runs are to be handled so that the interface remains usable.

Show:
- status: waiting, running, done, cancelled or failed,
- number of completed and remaining runs,
- current parameter combination and scenario,
- comprehensible error information.

Prevent accidental double starts. Let the researcher cancel the remaining runs. Keep completed
partial results but mark a cancelled experiment as incomplete.

## 5. Results

Present results in Swedish with clear tables and charts:
- share of illegally handled waste,
- detected and undetected illegal waste,
- illegal profit,
- findings, bans and company switches,
- number of supervisory and roadside inspections,
- distribution between actor types.

Show mean and spread between runs. In scenario comparisons, differences are to be computed
between runs with the corresponding random seed.

Distinguish clearly between:
- percent and percentage points,
- relative and absolute change,
- variation from randomness and uncertainty in the assumptions.

Statistical intervals describe variation in the simulation under the chosen assumptions. They
must not be presented as covering the uncertainty about reality.

Use the existing definitions of measures, especially the dark figure and detection. Explain
what is counted: tonnes, consignments, findings or cases.

Show a short, visible notice that the model is not calibrated or validated. The number of
inspections must not be presented as the measure's economic cost.

## 6. Save and reuse experiments

Save experiments locally and persistently in a separate results folder with:
- unique ID, name, description and date,
- the researcher's reason for the experiment,
- the complete configuration used,
- changes compared with default values,
- scenarios and random seeds,
- model version and Git revision if available,
- results per run and summaries,
- status and any errors.

The researcher must be able to open earlier experiments, duplicate the settings and export
results as CSV and configuration and metadata in a machine-readable format.

## 7. Documentation and verification

Update `README.md` with how the interface is started and used.

Update `ABM_MODEL_NOTES.md` with:
- the interface's functions,
- how comparisons and parameter ranges work,
- how uncertainty is shown,
- remaining limitations.

Verify in particular that:
- the interface and the command line give the same results with the same configuration and
  random seeds,
- default files are not changed by experiments,
- interventions are compared with the right baseline,
- saved experiments can be reopened and reproduced,
- errors and cancelled runs are handled correctly.

Run the existing tests and add relevant tests for the experiment handling. Start the
interface and check the whole flow with a small experiment.

The work is done when a researcher can change parameters, run repeated simulations, sweep a
parameter range, compare scenarios and save the results without editing files or using the
terminal.
