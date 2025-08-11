#!/usr/bin/env python3
import json
import os
from sys import argv
from jsonpickle import encode, decode
from termcolor import colored

VERSION = 1.2

"""
Version: 1.2
- added --version and -v flag
- improved --help flag
"""


COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}


def coloredText(text: str, color: str) -> None:
    print(colored(text, color))


def load_tasks(filepath: str) -> tuple[int, dict[str, "Task"]]:
    try:
        with open(filepath, "r") as f:
            t = f.read()
            if not t.strip() or t == '"{}"':
                return (0, {})
            data: dict = decode(json.loads(t))
            slot = 0 if not data else int(max(data.keys())) + 1
            return (slot, data)
    except FileNotFoundError:
        return (0, dict())


class Task:
    def __init__(self, name: str, completed: bool = False):
        self.name = name
        self.completed = completed

    def __repr__(self):
        return f"Task(name={self.name}, completed={self.completed})"

    def complete(self):
        self.completed = True


class TaskList:
    def __init__(self, todo_file: str):
        self.file = todo_file
        self.lowestSlot, self.tasks = load_tasks(self.file)

    def __iter__(self):
        return iter(self.tasks.items())

    def __del__(self):
        with open(self.file, "w") as f:
            json.dump(encode(self.tasks), f, indent=4)

    def add(self, taskname: str) -> int:
        """Adds a new task to the list and returns the id"""
        self.tasks[str(self.lowestSlot)] = Task(taskname)
        self.lowestSlot += 1
        return self.lowestSlot - 1

    def rm(self, id: str) -> bool:
        """Removes the task with id `id`, if not possible, return false"""
        try:
            del self.tasks[id]
            return True
        except KeyError:
            return False

    def check(self, id: str) -> bool:
        """Checks the task with id `id`, if not possible, return false"""
        try:
            self.tasks[id].complete()
            return True
        except KeyError:
            return False

    def is_empty(self) -> bool:
        """Checks if the TaskList has any tasks, completed or not"""
        return not bool(self.tasks)


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
