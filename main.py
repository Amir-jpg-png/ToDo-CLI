#!/usr/bin/env python3
import os
import click
from utils import TaskList, error, warning, success

VERSION = "1.4.1"


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
    success(f'"{task}" was added successfully!')


@cli.command()
@click.argument('task_id')
def rm(task_id):
    """Remove a task by ID"""
    tasks = get_task_list()
    match tasks.rm(task_id):
        case 0:
            success("Remove was successful.")
        case code:
            error(f"Programm exited with error code {code}!")
            raise SystemExit(code)


@cli.command()
def ls():
    """List all tasks"""
    tasks = get_task_list()
    if tasks.is_empty():
        warning("No tasks created yet!")
        raise SystemExit(1)
    for id, task in tasks:
        if task.checked():
            success(f"- [X] {id}: {task.name}")
        else:
            click.echo(f"- [ ] {id}: {task.name}")


@cli.command()
@click.argument('task_id')
def check(task_id):
    """Mark a task as completed"""
    tasks = get_task_list()
    match tasks.check(task_id):
        case 0:
            success("Checked task successfully.")
        case code:
            error(f"Programm exited with error code {code}!")
            raise SystemExit(code)


@cli.command()
@click.argument('task_id')
def uncheck(task_id):
    """Mark a task as open"""
    tasks = get_task_list()
    match tasks.uncheck(task_id):
        case 0:
            success("Unchecked task successfully.")
        case code:
            error(f"Programm exited with error code {code}!")
            raise SystemExit(code)


@cli.command()
@click.option("--verbose", "-v", help="display all removed tasks", default=False, is_flag=True)
def purge(verbose: bool):
    """Removes all checked tasks"""
    tasks = get_task_list()
    return_code, purged = tasks.purge()
    if verbose:
        for id, task in purged.items():
            print(f"{id}: {task.name}")

    match return_code:
        case 0:
            return
        case 1:
            warning("Nothing to purge.")
        case code:
            error(f"Programm exited with error code {code}!")
            raise SystemExit(code)



@cli.command()
def version():
    """Show version"""
    click.echo(f"todo {VERSION}")


@cli.command(deprecated=True)
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
