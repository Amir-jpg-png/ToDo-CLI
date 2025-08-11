---
title: "Command Reference"
description: "Complete reference for all available ToDo CLI commands and options."
summary: "A terse, complete guide to every command and flag in the ToDo CLI."
date: 2025-08-09T23:50:00+02:00
lastmod: 2025-08-09T23:50:00+02:00
draft: false
weight: 920
toc: true
seo:
  title: "ToDo CLI Command Reference"
  description: "Complete syntax and description of all ToDo CLI commands and flags."
  canonical: ""
  noindex: false
---

## Overview

The ToDo CLI manages project-specific task lists using a `.todo.json` file in your current working directory.

---

## Global Options

| Option      | Description                              |
| ----------- | ---------------------------------------- |
| `--help`    | Display help text and available commands |
| `--version` | Show current CLI version                 |

---

## Commands

### `todo add <task>`

Add a new task to the current project's `.todo.json`.

**Arguments:**

- `<task>` — The task description (wrap in quotes if it contains spaces).

**Example:**

```bash
todo add "Write unit tests for authentication"
```

---

### `todo ls`

List all tasks, grouped by completion status.

**Example:**

```bash
todo ls
```

---

### `todo check <id>`

Mark the task with the given ID as completed.

**Arguments:**

- `<id>` — Task ID as shown in `todo ls`.

**Example:**

```bash
todo check 3
```

---

### `todo rm <id>`

Remove the task with the given ID permanently.

**Arguments:**

- `<id>` — Task ID as shown in `todo ls`.

**Example:**

```bash
todo rm 2
```

---
