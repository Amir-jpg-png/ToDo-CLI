#!/usr/bin/env python3
import json
import os
from sys import argv
from termcolor import colored


COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}


def coloredText(text: str, color: str) -> None:
    print(colored(text, color))


def main():
    flags = ["add", "rm", "ls", "check", "--help"]
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    tasks = load_tasks(todo_file)

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
        for i in flags:
            if i == "ls":
                print(f"todo {i}")
            elif i in ["rm", "check"]:
                print(f'todo {i} "id"')
            else:
                print(f'todo {i} "task"')
    if flag == "ls":
        print()
        if len(tasks) == 0:
            colorPrinter("No tasks created yet!", colors.ERROR)
        for i in range(len(tasks)):
            task = tasks[i]
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
            coloredText("Please specify a task to add.", COLORS["WARNING"])
            return
        task = {}
        task["name"] = argv[2]
        task["completed"] = False
        tasks.append(task)
        save_tasks(todo_file, tasks)
        coloredText(f'"{argv[2]}" was added to tasks successfully!', COLORS["SUCCESS"])
        return
    if flag == "check":
        if len(argv) <= 2:
            coloredText("Please specify the id of the task to mark as checked.", COLORS["WARNING"])
            return
        check_task(argv[2], tasks, todo_file)
        return
    if flag == "rm":
        if len(argv) <= 2:
            coloredText("Please specify the id of the task to remove.", COLORS["WARNING"])
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
        coloredText("Please enter a valid nummeric id!", COLORS["WARNING"])
        return
    if id < 0 or id >= len(tasks):
        coloredText("No task with that id found!", COLORS["ERROR"])
        return
    task = tasks[id]
    task["completed"] = True
    save_tasks(filepath, tasks)
    coloredText(f'Task "{task["name"]}" was marked as checked!', COLORS["SUCCESS"])


def remove_task(id, tasks, filepath):
    try:
        id = int(id)
    except ValueError:
        coloredText("Please enter a valid nummeric id!", COLORS["WARNING"])
        return
    if id < 0 or id >= len(tasks):
        coloredText("No task with that id found!", COLORS["ERROR"])
        return
    name = tasks[id]["name"]
    tasks.pop(id)
    save_tasks(filepath, tasks)
    coloredText(f'Task "{name}" was removed!', COLORS["SUCCESS"])


if __name__ == "__main__":
    main()
