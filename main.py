#!/usr/bin/env python3
import os
from sys import argv
from utils import coloredText, TaskList

VERSION = 1.2
COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}

def main():
    """Entry point of programm"""
    flags = ["add", "rm", "ls", "check", "--help", "--version", "-v"]
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    tasks = TaskList(todo_file)

    if len(argv) <= 1:
        coloredText(
            "Please enter a flag or enter todo --help to find a list of all options.",
            COLORS["WARNING"]
        )
        return

    flag = argv[1]

    if flag not in flags:
        coloredText(f"{flag} is not a valid flag.", COLORS["WARNING"])
        exit(1)

    if flag == "--help":
        print()
        print("Usage:")
        print('  todo add "task"      Add a new task')
        print("  todo rm <id>         Remove a task by ID")
        print("  todo ls               List all tasks")
        print("  todo check <id>      Mark a task as completed")
        print("  todo --version, -v    Show version")
        print("  todo --help           Show this help message")
    elif flag == "ls":
        print()
        if tasks.is_empty():
            coloredText("No tasks created yet!", COLORS["ERROR"])
            exit(1)
        for id, task in tasks:
            if task.completed:
                coloredText(f"- [X] {task.name} id: {id}", COLORS["SUCCESS"])
            else:
                print(f"- [ ] {task.name} id: {id}")
    if flag in ["--version", "-v"]:
        print(f"todo {VERSION}")
    if flag == "add":
        if len(argv) <= 2:
            coloredText("Please specify a task to add.", COLORS["WARNING"])
            exit(1)
        tasks.add(argv[2])
        coloredText(f'"{argv[2]}" was added successfully!', COLORS["SUCCESS"])
        exit(0)
    if flag == "check":
        if len(argv) <= 2:
            coloredText("Please specify the id of the task to mark as checked.", COLORS["WARNING"])
            exit(1)
        if tasks.check(argv[2]):
            coloredText("Checked task successfully.", COLORS["SUCCESS"])
            exit(0)
        else:
            exit(1)
    if flag == "rm":
        if len(argv) <= 2:
            coloredText("Please specify the id of the task to remove.", COLORS["WARNING"])
            exit(1)
        if tasks.rm(argv[2]):
            coloredText("Remove was successfully.", COLORS["SUCCESS"])
            exit(0)
        else:
            exit(1)


if __name__ == "__main__":
    main()
