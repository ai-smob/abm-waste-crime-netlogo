# Project rules for this repository

This repository is public and is the research group's window into how the model is built.
Everything here is in English.

## Log every change that affects the application

1. **`PROJECT_LOG.md`.** Every change that affects the application gets an entry at the
   bottom, in the same session as the change: date, what was done, why, on what basis
   (source, assumption or the author's decision) and what effect it had on the results.
2. **`prompts/follow-up-prompts.md`.** An instruction from the author that shaped the
   application is added with the Swedish original and an English translation. An
   instruction that mixes application and internal matters is shortened to the application
   part and marked with [...].
3. **Both implementations.** A model change is made in the specification first, then in
   the Python project (`../abm`) and in `netlogo/waste_crime.nlogox`, and
   `tools/run_regression.sh` must pass before the change counts as done. Parameter values
   are changed in the Python project's `config/`, exported with its
   `scripts/export_netlogo_data.py`, and committed here.

**What is logged:** anything that changes the model, parameters, scenarios, metrics, the
interface, login, deployment, the documents the researchers read, the NetLogo port, the
regression test or the shared data files, and anything that changes how the project is
documented.

**What is not logged: administrative prompts.** Instructions that change no decision about
the application go neither into the log nor into the prompt list: explanations, starting
or watching the interface, committing or pushing, saving notes, meeting material, e-mails,
PDF exports, to-do lists, status questions. If such a session nevertheless leads to a
change (a question that reveals a bug, for instance), the change is logged, not the
question.

## Never in this repository

The research group's source material, meeting transcripts, non-public data, server
addresses, secrets, and people's names (refer to people by role). No licence has been
chosen yet; do not add one without the author's say-so.
