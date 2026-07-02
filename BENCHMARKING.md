# Skill Benchmarks

Curated, version-controlled performance records for the skills in this repo. Each skill gets a subfolder; each benchmarked **update** to a skill gets one dated markdown record that quantifies how the new version performed against a baseline (the previous version, or no-skill).

The bulky raw eval outputs — subagent transcripts, the projects they produced, the HTML review viewer — live in the gitignored `skills/<skill>-workspace/` and are **not** committed. Only the distilled numbers and decisions land here, so the history stays readable and diffable.

## Layout

```
skill-benchmarks/
└── <skill-name>/
    ├── README.md       # trajectory index: every iteration, its headline metric, a link
    ├── _template.md    # copy this for each new record
    └── iter-NN-<slug>.md
```

## How a record is produced

Per update (the skill-creator eval loop, in short):

1. Run the eval set with the **new** skill version AND a **baseline** (previous version, or no-skill).
2. Grade objective assertions; aggregate pass-rate, tokens, and duration per config.
3. Distill the result into `iter-NN-<slug>.md`, and add a row to the skill's `README.md`.

The point: make each change to a skill prove it helped (or at least didn't regress), with numbers, before it's accepted.
