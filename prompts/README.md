# Prompts

Every instruction given to the AI during the project, so that the way the prototype was built
can be examined.

| File | Content |
| --- | --- |
| `2026-09-30-initial-model-prompt.sv.md` | The prompt that produced the model, Swedish original, verbatim |
| `2026-09-30-initial-model-prompt.en.md` | The same in English |
| `2026-09-30-web-interface-prompt.sv.md` | The prompt that produced the web interface, Swedish original, verbatim |
| `2026-09-30-web-interface-prompt.en.md` | The same in English |
| `follow-up-prompts.md` | Every later instruction, in order, Swedish and English |

## How the prompts were produced and used

The two long prompts were not written in one go. The author reasoned about the task in a chat
with an AI assistant, iterating on what the group needed and what the prototype should and
should not claim. When the reasoning settled, the assistant was asked to write the prompt.
That prompt was then given to Claude Code, an agentic coding tool from Anthropic, running in
the project folder with the source material available to it. Claude Code read the material,
wrote the documentation and the code, ran the model and reported back. The result was then
iterated through the shorter follow-up prompts.

All sessions used the model Claude Fable 5.1. The author has stated that he had no prior
knowledge of agent-based modelling or of waste crime research; the model design and every
parameter value were produced by the AI from the material it was given, under the constraint
in the initial prompt that nothing may be invented without being labelled as such.

The chat sessions in which the prompts were drafted are not logged here. Claude Code's own
session logs, from which the prompts above were extracted, are kept on the author's computer.
