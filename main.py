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
@click.option("--progress", prompt="Progress", help="input the progress status")
def item(name, to_do, progress, filepath):
    filepath = "store.json"
    with open(filepath, 'r') as fb:
        data = json.load(fb)

    count = 1
    for i in data["list"]:
        count += 1

    new_json = {
        "id": count,
        "name": name,
        "to_do": to_do,
        "progress": progress
    }

    data["list"].append(new_json)

    with open(filepath, 'w') as fb:
        json.dump(data, fb, indent=4, sort_keys=True)


# Function that delete a certain task with given id of it
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
@click.option("--delete_id", prompt="Enter the id of the task you want to delete", help="Delete a item from the task")
def delete_item(delete_id, filepath):
    filepath = "store.json"
    with open(filepath, 'r') as fb:
        data = json.load(fb)

    new_data = {
                    "list": [
                    ]
                }

    for entry in data["list"]:
        if entry["id"] == int(delete_id):
            print(f"Deleting the task {entry["name"]}")
            pass
        else:
            new_data["list"].append(entry)

    with open(filepath, 'w') as fb:
        json.dump(new_data, fb, indent=4, sort_keys=True)


# Function to update the certain field of the task
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
@click.option("--update_id", prompt="Enter the id of the task that you want to update", help="Input id to update the task")
@click.option("--update_field", prompt="Enter the item that you want to update from the task", help="Input the item that you want to update")
@click.option("--update_task", prompt="Enter the task that you want to update:",help="Input the value of task to be updated")
def update_item(update_id, update_field, update_task, filepath):
    filepath = "store.json"
    with open(filepath, 'r') as fb:
        data = json.load(fb)

    for i in data["list"]:
        if i["id"] == int(update_id):
            i[update_field] = update_task
            break

    print(f"{update_field} has been updated in id: {update_id}")

    with open(filepath, 'w') as fb:
        json.dump(data, fb, indent=4, sort_keys=True)


# Function to read whole list
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
def display(filepath):
    filepath = "store.json"

    with open(filepath, 'r') as fb:
        data = json.load(fb)

        print("\nDisplaying The whole list of To Do :")
        for i in data["list"]:
            print(f"ID: {i["id"]}")
            print(f"Name:{i["name"]}")
            print(f"To Do: {i["to_do"]}")
            print(f"Progress: {i["progress"]}\n")


# Function that displays the function that are in progress
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
def display_progress(filepath):
    filepath = "store.json"

    with open(filepath, 'r') as fb:
        data = json.load(fb)

        print("\nDisplaying the list of task in progress only:")
        for i in data["list"]:
            if i["progress"].lower() == "progress":
                print(f"ID: {i["id"]}")
                print(f"Name:{i["name"]}")
                print(f"To Do: {i["to_do"]}")
                print(f"Progress: {i["progress"]}\n")


# Function that displays the task that are completed
@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
def display_completed(filepath):
    filepath = "store.json"

    with open(filepath, 'r') as fb:
        data = json.load(fb)

        print("\nDisplaying the list of task in completed only:")
        for i in data["list"]:
            if i["progress"].lower() == "completed":
                print(f"ID: {i["id"]}")
                print(f"Name:{i["name"]}")
                print(f"To Do: {i["to_do"]}")
                print(f"Progress: {i["progress"]}\n")


# Command Function
commands.add_command(item)
commands.add_command(delete_item)
commands.add_command(update_item)
commands.add_command(display)
commands.add_command(display_progress)
commands.add_command(display_completed)

if __name__ == "__main__":
    commands()
