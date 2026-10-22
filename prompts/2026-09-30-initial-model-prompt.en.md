# Initial prompt, 2026-09-30 (English translation)

This is a translation of `2026-09-30-initial-model-prompt.sv.md`, the prompt that produced the
first model. It was given to Claude Code (model Claude Fable 5.1) at 07:29 local time on
2026-09-30, with the research group's source material available in a `docs/` folder. The
translation follows the original closely; headings and lists are as in the original.

---

You are to build a first technical prototype of an agent-based model (ABM) of organised
waste crime in Sweden.

**Background**

The project is research-oriented. The research group has gathered knowledge about organised
waste crime, Swedish actors, authority processes, economic incentives, crime schemes and the
relevant ABM literature. The same literature and material used in the project is in the
folder:

docs/

Use this material as the primary source. Read the documents before you design the model. If
something is not supported by the source material, do not invent it. Instead, mark clearly
that it is an assumption, a simplification or an open question.

**Goal**

The goal is not to build a finished, scientifically validated model. The goal is to create a
first runnable prototype that makes the research group's ideas concrete and helps us identify:

1. which agents need to exist,
2. which properties the agents need,
3. which relations need to be modelled,
4. which decisions the agents make,
5. which crime pathways need to exist,
6. which authority interventions can be simulated,
7. which data are needed for calibration,
8. which parts still lack sufficient empirical support,
9. which outputs are meaningful to measure.

**Way of working**

Work iteratively and build a minimal but runnable model first.

Important:
- do not start with a large or complex system,
- use Python unless something in the material strongly argues for something else,
- choose an established and simple ABM structure or a suitable library if it simplifies the work,
- prioritise comprehensibility and traceability over technical elegance,
- every major modelling decision must be traceable to the source material or marked as an
  explicit assumption.

**Documentation**

From the start, create a document, for example:

ABM_MODEL_NOTES.md

That document is to be updated continuously throughout the work.

The document is to be written in Swedish and intended for a non-technical reader, for
example researchers, domain experts or clients who cannot program.

It must explain:
- what an ABM is in this particular project,
- which parts the model consists of,
- which agents exist,
- what each agent represents,
- which properties the agents have,
- how the agents make decisions,
- how they interact,
- what the model's "environment" or landscape consists of,
- which assumptions the model makes,
- why these assumptions are made,
- which choices are based on source material,
- which choices are provisional,
- which parts are uncertain,
- how the simulation proceeds step by step,
- which scenarios or interventions can be tested,
- which results the model produces,
- how the results are to be interpreted,
- what the model cannot say,
- which data are needed later for better calibration and validation.

Avoid technical language when it is not needed. If technical terms are used, explain them
immediately.

**Sources**

When you build the model, first take stock of the documents in docs/ and identify which are
used for what.

Preferably create a section in ABM_MODEL_NOTES.md:

"Sources and how they are used"

There you can for example describe:
- methodological literature on ABM,
- research on organised crime,
- research on illegal supply chains,
- Swedish reports on waste crime,
- material on authority processes,
- case studies such as Think Pink, Black Mass and Stena Recycling,
- material on risk, reward, effort and propensity,
- material on different pathways into waste crime.

**The model's first version**

Start from the material in docs/ and try to create a first conceptual model with as few
agent types as possible.

Possible agent types to examine are for example:
- waste producers,
- waste companies,
- transporters,
- receiving or treatment facilities,
- brokers or intermediaries,
- front men or formal representatives,
- actual decision-makers,
- organised criminal actors,
- supervisory authorities,
- police or other law enforcement authorities.

Do not automatically use all of them. Judge from the source material which ones are actually
needed in a first prototype.

The model should be able to represent that:
- waste is generated,
- the waste needs to be taken care of,
- different actors can choose between legal and illegal handling,
- illegal handling can be economically attractive through avoided costs,
- companies and individuals can differ in their propensity to break rules,
- the risk of detection affects decisions,
- authorities have limited resources,
- supervision and inspections can change the risk picture,
- actors can adapt to inspection and supervision.

Examine in particular whether the decision logic can be expressed with the type of utility
function found in the material:

U = reward + propensity - effort - risk

where risk in turn can depend on:
- probability of being detected,
- probability of being sanctioned,
- the size of the sanction.

Do not, however, use the formula mechanically if the material shows that the model needs to
be more nuanced.

**Crime pathways**

The material suggests that waste crime should not be modelled as a single mechanism.

Therefore examine at least the following pathways:
- illegal dumping / illegal disposal,
- illegal waste handling that emerges gradually,
- misclassification or reclassification of waste,
- illegal transport or export,
- use of legal companies as a front,
- use of front men or company brokers,
- manipulation of documentation,
- changing company when supervision or debts increase.

In the first prototype you may choose one or two pathways if needed to keep the model small.

**Environment / landscape**

A central question from the research group is what the model's "landscape" should look like.

Analyse the sources and document possible alternatives, for example:
- geographical environment,
- network of companies and persons,
- waste flow / supply chain,
- regulatory environment,
- a combination of networks and flows.

Choose the simplest structure that suffices for a first prototype and explain why.

**Simulation**

Build a clear simulation loop.

For example:
1. waste arises,
2. an actor needs to find handling,
3. possible options are identified,
4. the agent makes a decision,
5. the waste is moved or handled,
6. a crime possibly occurs,
7. authorities carry out certain inspections,
8. crimes are possibly detected,
9. sanctions or other consequences occur,
10. the agents' states are updated,
11. the next time step begins.

This is only an example. Adapt to what the source material actually supports.

**Scenarios**

The model should early on be able to compare a baseline scenario with a few simple
interventions.

Examples to examine:
- higher inspection frequency,
- more targeted supervision,
- higher sanctions,
- better information sharing between authorities,
- higher risk of detection,
- inspections targeted at transporters,
- inspections targeted at high-risk companies or brokers.

Implement only scenarios that can be justified from the sources.

**Outputs**

Identify and implement a few clear outputs, for example:
- share of waste handled illegally,
- number of illegal events,
- number of detected crimes,
- number of undetected crimes,
- economic profit from illegal handling,
- which agent types most often take part,
- which actors become central in the network,
- how the result changes between different interventions.

**Technical structure**

Structure the code so that it is easy to:
- add new agent types,
- change parameters,
- add new pathways,
- add new scenarios,
- replace synthetic data with real data later.

Preferably separate:
- agent definitions,
- model / simulation loop,
- parameters,
- scenarios,
- outputs,
- run scripts,
- documentation.

Preferably create a simple config file or equivalent so that parameters do not have to be
hard-coded everywhere.

**Data**

The first version may use synthetic or simplified data if needed.

But:
- document clearly which values are real and which are invented,
- do not use invented values as if they were empirically established,
- identify which parameters should later be calibrated against real Swedish data.

**Validation**

Do not build a complete validation solution now, but create support for later comparing the
model with empirical data.

Document which empirical patterns from the material could be used for validation, for example:
- share of companies with criminal connections,
- structure of company networks,
- number of transporters,
- inspection frequencies,
- typical crime pathways,
- relation between legal and illegal waste handling,
- observed cases such as Think Pink, Black Mass or Stena Recycling.

**Order of work**

Work roughly in the following order:

1. Read and take stock of docs/.
2. Write a short source overview in ABM_MODEL_NOTES.md.
3. Identify the research group's conceptual model.
4. List possible agents, variables, relations and decisions.
5. Identify what is empirically established and what is missing.
6. Propose a minimal first ABM.
7. Document the proposal before coding begins.
8. Implement the model.
9. Run a few simple simulations.
10. Document what the results mean.
11. Identify weaknesses, data gaps and next development steps.
12. Improve the prototype if it can be done without making the model unnecessarily complex.

When you make major changes to the model:
- always update ABM_MODEL_NOTES.md,
- write why the change was made,
- write which source or which assumption lies behind it,
- write what the change is expected to affect.

**Definition of done**

The work is done when there is:

- a runnable minimal ABM prototype,
- clearly defined agents,
- defined decisions and interactions,
- at least one baseline scenario,
- at least one intervention scenario,
- a few simple outputs,
- a reproducible way to run the simulation,
- a thorough but easily understood ABM_MODEL_NOTES.md,
- a list of empirical data gaps,
- a list of open research questions,
- an assessment of what is required to go from prototype to scientifically usable model.

**Important principle**

See the prototype as a tool for making the researchers' assumptions explicit.

When you encounter a question such as:
"how large should the probability be that company X chooses illegal handling?"

do not just invent a value.

Instead do something like:
- create a configurable parameter,
- choose a neutral demonstration value if needed to be able to run the model,
- mark clearly in the documentation that the value is provisional,
- write what kind of empirical information is needed to replace it.

The goal is thus as much to discover which questions the research group must answer as to
write working code.
