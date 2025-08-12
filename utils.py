#!/usr/bin/env python3
import json
from jsonpickle import encode, decode
from termcolor import colored

VERSION = "1.3.1"
COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}

def error(msg: str):
    """Prints a styled error message to stdout"""
    print(colored(msg, COLORS["ERROR"]))

def success(msg: str):
    """Prints a styled success message to stdout"""
    print(colored(msg, COLORS["SUCCESS"]))


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
        self._completed = completed

    def __repr__(self):
        return f"Task(name={self.name}, completed={self._completed})"

    def check(self):
        self._completed = True

    def uncheck(self):
        self._completed = False

    def checked(self) -> bool:
        return self._completed


class TaskList:
    """Holds multiple tasks"""
    def __init__(self, todo_file: str):
        self.file = todo_file
        self.lowestSlot, self._tasks = load_tasks(self.file)

    def __iter__(self):
        return iter(self._tasks.items())

    def __del__(self):
        with open(self.file, "w") as f:
            json.dump(encode(self._tasks), f, indent=4)

    def add(self, taskname: str) -> int:
        """Adds a new task to the list and returns the id"""
        self._tasks[str(self.lowestSlot)] = Task(taskname)
        return self.lowestSlot

    def rm(self, id: str) -> bool:
        """Removes the task with id `id`, if not possible, return false"""
        try:
            del self._tasks[id]
            return True
        except KeyError:
            return False

    def check(self, id: str) -> int:
        """Checks the task with id `id`, if not possible, return and error code"""
        try:
            self._tasks[id].check()
            return 0
        except KeyError:
            return 1

    def uncheck(self, id: str) -> int:
        """Unchecks the task with id `id`, if not possible, return the corresponding error code"""
        try:
            self._tasks[id].uncheck()
            return 0
        except KeyError:
            return 1

    def is_empty(self) -> bool:
        """Checks if the TaskList has any tasks, completed or not"""
        return not bool(self._tasks)
