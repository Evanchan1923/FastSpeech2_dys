# JC Repo Initializer

Use this initializer when preparing a repository for Codex-assisted work.

## Source Image Notes

The reference image describes a Codex project layout with:

- Root project files such as `README.md`, `AGENTS.md`, `.gitignore`, optional `LICENSE`, optional `package.json`, and `CHANGELOG.md`.
- A `.codex/` folder for Codex-specific configuration and working context.
- `.codex/rules/` for useful repository rules, keeping only coding style and general rules for this initializer.
- Task tracking files for pending and completed work.
- Memory files for project context, decisions, and lessons learned.
- Optional scripts for initialization, syncing, and utilities.

This repository uses a compact version of that structure focused on rules, task tracking, memory, and changelog maintenance.

## Target Structure

Create or preserve the following files and folders:

```text
repo-root/
+-- AGENTS.md
+-- .codex/
    +-- rules/
    |   +-- coding-style.md
    |   +-- general-rules.md
    +-- tasks/
    |   +-- todo.md
    |   +-- done.md
    +-- memory/
    |   +-- project-context.md
    |   +-- decisions.md
    |   +-- lessons-learned.md
    +-- changelog.md
```

Do not create `.codex/prompts/`, `.codex/templates/`, or `.codex/snippets/` from this initializer.

## Initialization Steps

1. Create `.codex/rules/`.
2. Create `.codex/tasks/`.
3. Create `.codex/memory/`.
4. Create `.codex/changelog.md`.
5. Create or update `.codex/rules/coding-style.md` and `.codex/rules/general-rules.md`.
6. Create or update `.codex/tasks/todo.md` and `.codex/tasks/done.md`.
7. Create or update `.codex/memory/project-context.md`, `.codex/memory/decisions.md`, and `.codex/memory/lessons-learned.md`.
8. Create or update root-level `AGENTS.md`.

## Required AGENTS.md Rule

Generate root `AGENTS.md` with only the title and this mandatory section:

```markdown
# AGENTS.md

## Codex Task Bookkeeping

- This section is mandatory for every task.
- For each task, update the relevant files inside `.codex/`.
- Follow `.codex/rules/general-rules.md` and `.codex/rules/coding-style.md`.
- Track pending work in `.codex/tasks/todo.md`.
- Move completed work to `.codex/tasks/done.md`.
- Record durable project context in `.codex/memory/project-context.md`.
- Record important decisions in `.codex/memory/decisions.md`.
- Record reusable lessons in `.codex/memory/lessons-learned.md`.
- Add user-visible changes to `.codex/changelog.md`.
```

Do not generate placeholder sections such as `## Working Notes` or `## Project Guidance`.

## File Purpose

- `.codex/rules/coding-style.md`: coding style expectations for this repository.
- `.codex/rules/general-rules.md`: general working rules for Codex in this repository.
- `.codex/tasks/todo.md`: work that has been requested or discovered but not started.
- `.codex/tasks/done.md`: completed tasks with date and short outcome.
- `.codex/memory/project-context.md`: stable facts about the project, environment, and workflow.
- `.codex/memory/decisions.md`: decisions that should influence future work.
- `.codex/memory/lessons-learned.md`: useful findings, pitfalls, and repeated fixes.
- `.codex/changelog.md`: chronological record of meaningful repository changes.

## Starter Content

Create new files as blank templates. Do not add task-specific generated entries.

For `.codex/changelog.md`, keep the date heading and leave the contents under that date empty.

```markdown
# Coding Style

- Follow the style already present in the files being edited.
- Keep changes focused and easy to review.
- Prefer clear names and simple structure over unnecessary abstraction.
- Use concise comments only when they clarify non-obvious behavior.
- Long code lines are acceptable when they improve readability; use 250 characters as the soft maximum before wrapping.
```

```markdown
# General Rules

- Preserve existing user changes.
- Update `.codex/` bookkeeping files for every task.
- Keep `.codex/prompts/`, `.codex/templates/`, and `.codex/snippets/` out of the default initializer unless explicitly requested.
```

```markdown
# Todo
```

```markdown
# Done
```

```markdown
# Project Context
```

```markdown
# Decisions
```

```markdown
# Lessons Learned
```

```markdown
# Changelog

## 2026-06-30
```