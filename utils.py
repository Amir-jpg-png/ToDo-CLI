#!/usr/bin/env python3
import json
from jsonpickle import encode, decode
from termcolor import colored

VERSION = 1.2


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

            tasks = dict()
            for id in data:
                tasks[id] = data[id]
            return (slot, tasks)
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
        return self.lowestSlot

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
