#!/usr/bin/env python3
import os
import typer
from utils import coloredText, TaskList

app = typer.Typer()

VERSION = 1.2
COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}

def get_task_list():
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    return TaskList(todo_file)

@app.command()
def add(task: str):
    """Add a new task"""
    tasks = get_task_list()
    tasks.add(task)
    coloredText(f'"{task}" was added successfully!', COLORS["SUCCESS"])

@app.command()
def rm(task_id: str):
    """Remove a task by ID"""
    tasks = get_task_list()
    if tasks.rm(task_id):
        coloredText("Remove was successful.", COLORS["SUCCESS"])
    else:
        raise typer.Exit(code=1)

@app.command()
def ls():
    """List all tasks"""
    tasks = get_task_list()
    if tasks.is_empty():
        coloredText("No tasks created yet!", COLORS["ERROR"])
        raise typer.Exit(code=1)

    for id, task in tasks:
        if task.checked():
            coloredText(f"- [X] {task.name} id: {id}", COLORS["SUCCESS"])
        else:
            typer.echo(f"- [ ] {task.name} id: {id}")

@app.command()
def check(task_id: str):
    """Mark a task as completed"""
    tasks = get_task_list()
    if tasks.check(task_id):
        coloredText("Checked task successfully.", COLORS["SUCCESS"])
    else:
        raise typer.Exit(code=1)

@app.command()
def uncheck(task_id: str):
    """Mark a task as open"""
    tasks = get_task_list()
    if tasks.uncheck(task_id):
        coloredText("Unchecked task successfully.", COLORS["SUCCESS"])
    else:
        raise typer.Exit(code=1)

@app.command()
def version():
    """Show version"""
    typer.echo(f"todo {VERSION}")

@app.command()
def help():
    """Show this help message"""
    typer.echo("Usage:")
    typer.echo('  todo add "task"      Add a new task')
    typer.echo("  todo rm <id>         Remove a task by ID")
    typer.echo("  todo ls              List all tasks")
    typer.echo("  todo check <id>      Mark a task as completed")
    typer.echo("  todo uncheck <id>    Mark a task as open")
    typer.echo("  todo --version, -v   Show version")
    typer.echo("  todo --help          Show this help message")

if __name__ == "__main__":
    app()
