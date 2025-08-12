#!/usr/bin/env python3
import os
import click
from utils import coloredText, TaskList

VERSION = "1.3"
COLORS = {
    "ERROR": "red",
    "WARNING": "yellow",
    "SUCCESS": "green",
}


def get_task_list():
    current_dir = os.getcwd()
    todo_file = os.path.join(current_dir, ".todo.json")
    return TaskList(todo_file)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task"""
    tasks = get_task_list()
    tasks.add(task)
    coloredText(f'"{task}" was added successfully!', COLORS["SUCCESS"])


@cli.command()
@click.argument('task_id')
def rm(task_id):
    """Remove a task by ID"""
    tasks = get_task_list()
    if tasks.rm(task_id):
        coloredText("Remove was successful.", COLORS["SUCCESS"])
    else:
        raise SystemExit(1)


@cli.command()
def ls():
    """List all tasks"""
    tasks = get_task_list()
    if tasks.is_empty():
        coloredText("No tasks created yet!", COLORS["ERROR"])
        raise SystemExit(1)
    for id, task in tasks:
        if task.checked():
            coloredText(f"- [X] {task.name} id: {id}", COLORS["SUCCESS"])
        else:
            click.echo(f"- [ ] {task.name} id: {id}")


@cli.command()
@click.argument('task_id')
def check(task_id):
    """Mark a task as completed"""
    tasks = get_task_list()
    if tasks.check(task_id):
        coloredText("Checked task successfully.", COLORS["SUCCESS"])
    else:
        raise SystemExit(1)


@cli.command()
@click.argument('task_id')
def uncheck(task_id):
    """Mark a task as open"""
    tasks = get_task_list()
    if tasks.uncheck(task_id):
        coloredText("Unchecked task successfully.", COLORS["SUCCESS"])
    else:
        raise SystemExit(1)


@cli.command()
def version():
    """Show version"""
    click.echo(f"todo {VERSION}")


@cli.command()
def help():
    """Show this help message"""
    click.echo("Usage:")
    click.echo('  todo add "task"      Add a new task')
    click.echo("  todo rm <id>         Remove a task by ID")
    click.echo("  todo ls              List all tasks")
    click.echo("  todo check <id>      Mark a task as completed")
    click.echo("  todo uncheck <id>    Mark a task as open")
    click.echo("  todo --version, -v   Show version")
    click.echo("  todo --help          Show this help message")


if __name__ == "__main__":
    cli()
