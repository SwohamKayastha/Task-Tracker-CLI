"""
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
"""

import click
import json


@click.group
def commands():
    pass


# Function that adds a list to do
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
@click.option("--name", prompt="Name", help="input the name object")
@click.option("--to_do", prompt="To Do", help="input the to_do object")
def item(name, to_do, filepath):
    filepath = "store.json"
    with open(filepath, 'r') as fb:
        data = json.load(fb)

    new_json = {
        "name": name,
        "to_do": to_do
    }

    data["list"].append(new_json)

    with open(filepath, 'w') as fb:
        json.dump(data, fb, indent=4, sort_keys=True)


@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
def display(filepath):
    filepath = "store.json"

    with open(filepath, 'r') as fb:
        data = json.load(fb)

        print("\nDisplaying The whole list of To Do :")
        for i in data["list"]:
            print(f"Name:{i["name"]}")
            print(f"To Do: {i["to_do"]}\n")


# Command Function
commands.add_command(item)
commands.add_command(display)

if __name__ == "__main__":
    commands()