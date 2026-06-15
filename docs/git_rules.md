## Purpose

This repository should contain project materials that help the team understand and reproduce results on previous work for the purposes of extending the technical ability of the team.

Obsidian or google docs has been used for working notes, meeting notes, planning, and personal project thinking. Git is used for polished technical documentation, code, notebooks, workflows, and shared project artifacts.

As documents mature and their usefulness for the team increases, they should be promoted to the git repository for team sharing.

---

## What Belongs in Git

Commit files that are useful to the team, including:

- Source code
    
- Jupyter notebooks
    
- Reproducible experiments
    
- Dataset schemas
    
- Annotation rules
    
- Model training instructions
    
- Pipeline documentation
    
- Infrastructure setup guides
    
- Final or team-facing technical reports
    

---

## What Stays in Obsidian

Do not commit personal or draft notes, including:

- Meeting notes
    
- Raw notes
    
- Current priorities
    
- Open questions
    
- Personal planning notes
    
- Brainstorming documents
    
- Unfinished working drafts
    
- Untitled notes
    

These may be promoted to Git later once they become stable team documentation.

---

## Promotion Rule

A document should move from Obsidian to Git when it becomes:

- Stable enough for others to use
    
- Useful for onboarding
    
- Needed to reproduce project work
    
- Part of the technical process
    
- A shared reference for the team
    

---

## File Organization

Use the `docs/` folder for project documentation.

Suggested structure:

```text
docs/
├── onboarding/
├── datasets/
├── pipeline/
├── infrastructure/
├── experiments/
└── architecture/
```

---

## Naming Rules

Use lowercase filenames with underscores or hyphens.

Good:

```text
yolo_onboarding.md
region_definitions.md
mac_setup.md
current_pipeline.md
```

Avoid:

```text
Untitled.md
Final Final Notes.md
My thoughts.md
```

---

## Commit Rule

Before committing, ask:

> Would another team member understand why this file exists?

If yes, commit it.

If no, keep it in Obsidian or Google Docs for now.