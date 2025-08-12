---
title: "Usage Guide"
description: "This is a short summary of all the flags and options + how to use them."
summary: "This is a short summary of all the flags and options + how to use them."
date: 2025-08-09T23:17:24+02:00
lastmod: 2025-08-09T23:17:24+02:00
draft: false
weight: 999
toc: true
seo:
  title: "ToDo CLI Usage Guide" # custom title (optional)
  description: "This is a short summary of all the flags and options + how to use them." # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

| Command / Option    | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `todo --help`       | Show all available commands and their expected arguments  |
| `todo add "task"`   | Add a new task to the current project's `.todo.json` file |
| `todo ls`           | List all completed and uncompleted tasks                  |
| `todo check [id]`   | Mark a task as completed                                  |
| `todo uncheck [id]` | Uncheck a task that was marked as complete                |
| `todo rm [id]`      | Remove a task permanently                                 |

There are five commands and one flag to the todo command.

```bash
todo --help
```

Via this flag you can view all the different commands and their expected arguments.

This makes this CLI even more intuitive and that way you do not have to keep visiting the documentation.

```bash
todo add "if the task is longer than one word put it in double quotes"
```

This command adds a task to the `.todo.json` file which is a file that gets created in the repository you are currently working in.

That way you can keep all your projects separated while still being in the terminal and not leaving your programming/development environment.

```bash
todo ls
```

This command shows all your completed and uncompleted tasks.

I recommend keeping the completed tasks until you finish your work for the day and then afterwards delete the tasks using the rm command.

```markdown
- [ ] Task1 id: {id}
- [ ] Task2 id: {id}
- [x] Completed Task id:{id}
- [ ] Another Task id:{id}
```

The ids get displayed for future use of commands that need an id.

```bash
todo check [id]
```

This command marks the task with the corresponding id as completed.

```bash
todo uncheck [id]
```

This command marks the task with the corresponding id as open.

Lastly the rm command

```bash
todo rm [id]
```

Deleted the command with the corresponding id and removes it from the list of tasks forever.

Please practice caution when using the rm command as the removed tasks can not be recovered.
