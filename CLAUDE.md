# CLAUDE.md

Instructions for Claude Code when working in this repository.

## About this project

- This is a learning project for a Python course. The code is written to teach,
  so clear and well-commented code matters more than clever or short code.
- Explain new concepts in plain language and keep examples small.
- Write all code, comments and commit messages in English.

## Project structure

- `Lessons/` - one file per subject, numbered in course order, e.g.
  `Lessons/04-classes.py`. Helper modules used by a lesson go in
  `Lessons/modules/`.
- `Excersise/` - practice exercises.
- `Tools/` - small tools built during the course.
- When a new lesson is added, also add it to the lesson table in `README.md`.

## Lesson file style

Follow the layout of the existing lessons:

1. A header block that names the lesson and sums up the subject.
2. Sections separated by `# ----` divider comments, one per topic.
3. A short comment above each example explaining what it does, and inline
   comments showing the expected output where it helps.

## Running code

- Use the project's virtual environment: `.venv/Scripts/python.exe <file>`
- Run any file you create or change and check that it finishes without errors
  before committing.

## Git workflow (git-flow)

- `develop` is the default branch. Never commit directly to `main` or `develop`.
- Start each change on a feature branch from `develop`, e.g.
  `feature/04-classes`, and open a pull request into `develop`.
- Only commit the files that belong to the change. Never commit `__pycache__/`,
  `.venv/` or `.idea/`.
- Ask before pushing, merging or deleting branches, unless told to do it.
