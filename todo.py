#!/usr/bin/env python3
import json
import os
from sys import argv

VERSION = 1.2

"""
Version: 1.2 
- added --version and -v flag 
- improved --help flag
"""


class colors:
    ERROR = "\033[0;31m"
    END = "\33[0m"
    SUCCESS = "\33[0;32m"
    WARNING = "\33[0;33m"


def colorPrinter(message, color):
    print(color + message + colors.END)


def main():
    """Entry point of programm"""
    flags = ["add", "rm", "ls", "check", "--help", "--version", "-v"]
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    tasks = load_tasks(todo_file)

    if len(argv) <= 1:
        colorPrinter(
            "Please enter a flag or enter todo --help to find a list of all options.",
            colors.WARNING,
        )
        return

    flag = argv[1]

    if flag not in flags:
        colorPrinter(f"{flag} is not a valid flag.", colors.WARNING)
        return

    if flag == "--help":
        print()
        print("Usage:")
        print('  todo add "task"      Add a new task')
        print("  todo rm <id>         Remove a task by ID")
        print("  todo ls               List all tasks")
        print("  todo check <id>      Mark a task as completed")
        print("  todo --version, -v    Show version")
        print("  todo --help           Show this help message")
        return

    if flag in ["--version", "-v"]:
        print(f"todo {VERSION}")

    if flag == "ls":
        print()
        if len(tasks) == 0:
            colorPrinter("No tasks created yet!", colors.ERROR)
        for i, task in enumerate(tasks):
            if task["completed"] is True:
                marker = "- [X]"
                color = colors.SUCCESS
            else:
                marker = "- [ ]"
                color = ""
            print(color + f'{marker} {task["name"]} id: {i}' + colors.END)
        return
    if flag == "add":
        if len(argv) <= 2:
            colorPrinter("Please specify a task to add.", colors.WARNING)
            return
        task = {}
        task["name"] = argv[2]
        task["completed"] = False
        tasks.append(task)
        save_tasks(todo_file, tasks)
        colorPrinter(f'{task["name"]} was added to tasks successfully!', colors.SUCCESS)
        return
    if flag == "check":
        if len(argv) <= 2:
            colorPrinter(
                "Please specify the id of the task to mark as checked.", colors.WARNING
            )
            return
        check_task(argv[2], tasks, todo_file)
        return
    if flag == "rm":
        if len(argv) <= 2:
            colorPrinter("Please specify the id of the task to remove.", colors.WARNING)
            return
        remove_task(argv[2], tasks, todo_file)

        return


def load_tasks(filepath):
    try:
        with open(filepath, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(filepath, tasks):
    with open(filepath, "w") as f:
        json.dump(tasks, f, indent=4)


def check_task(id, tasks, filepath):
    try:
        id = int(id)
    except ValueError:
        colorPrinter("Please enter a valid nummeric id!", colors.WARNING)
        return
    if id < 0 or id >= len(tasks):
        colorPrinter("No task with that id found!", colors.ERROR)
        return
    task = tasks[id]
    task["completed"] = True
    save_tasks(filepath, tasks)
    print(colors.SUCCESS + f'Task "{task["name"]}" was marked as checked!' + colors.END)


def remove_task(id, tasks, filepath):
    try:
        id = int(id)
    except ValueError:
        colorPrinter("Please enter a valid nummeric id!", colors.WARNING)
        return
    if id < 0 or id >= len(tasks):
        colorPrinter("No task with that id found!", colors.ERROR)
        return
    name = tasks[id]["name"]
    tasks.pop(id)
    save_tasks(filepath, tasks)
    colorPrinter(f'Task "{name}" was removed!', colors.SUCCESS)


if __name__ == "__main__":
    main()
