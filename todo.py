#!/usr/bin/env python3
import json
import os
from sys import argv


def main():
    flags = ["add", "rm", "ls", "check", "--help"]
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    tasks = load_tasks(todo_file)

    if len(argv) <= 1:
        print("Please enter a flag or enter todo --help to find a list of all options.")
        return

    flag = argv[1]

    if flag not in flags:
        print(f"{flag} is not a valid flag.")
        return

    if flag == "--help":
        print()
        for i in flags:
            if i == "--help":
                continue
            if i == "ls":
                print(f"todo {i}")
                continue
            if i in ["rm", "check"]:
                print(f'todo {i} "id"')
                continue
            print(f'todo {i} "task"')
    if flag == "ls":
        print()
        if len(tasks) == 0:
            print("No tasks created yet!")
        for i in range(len(tasks)):
            task = tasks[i]
            if task["completed"] is True:
                marker = "- [X]"
            else:
                marker = "- [ ]"
            print(f'{marker} {task["name"]} id: {i}')
        return
    if flag == "add":
        if len(argv) <= 2:
            print("Please specify a task to add.")
            return
        task = {}
        task["name"] = argv[2]
        task["completed"] = False
        tasks.append(task)
        save_tasks(todo_file, tasks)
        return
    if flag == "check":
        if len(argv) <= 2:
            print("Please specify the id of the task to mark as checked.")
            return
        check_task(argv[2], tasks, todo_file)
        return
    if flag == "rm":
        if len(argv) <= 2:
            print("Please specify the id of the task to remove.")
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
        print("Please enter a valid nummeric id!")
        return
    if id < 0 or id >= len(tasks):
        print("No task with that id found!")
        return
    task = tasks[id]
    task["completed"] = True
    save_tasks(filepath, tasks)
    print(f'Task "{task["name"]}" was marked as checked!')


def remove_task(id, tasks, filepath):
    try:
        id = int(id)
    except ValueError:
        print("Please enter a valid nummeric id!")
        return
    if id < 0 or id >= len(tasks):
        print("No task with that id found!")
        return
    name = tasks[id]["name"]
    tasks.pop(id)
    save_tasks(filepath, tasks)
    print(f'Task "{name}" was removed!')


if __name__ == "__main__":
    main()
