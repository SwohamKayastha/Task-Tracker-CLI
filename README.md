# Task Tracker CLI

Task Tracker is a simple command-line interface (CLI) application that allows you to manage your tasks. You can add, update, delete, and view tasks, as well as track their progress. This project is designed to help you practice programming skills such as working with files, handling user inputs, and building a CLI application.

## Features

- **Add Tasks**: Add a new task with a name, to-do item, and progress status.
- **Update Tasks**: Update any field of an existing task by specifying its ID.
- **Delete Tasks**: Remove a task by its ID.
- **List All Tasks**: View all tasks, regardless of their status.
- **List In-Progress Tasks**: View tasks that are currently in progress.
- **List Completed Tasks**: View tasks that have been completed.

## Installation

1. **Clone the Repository:**
   ```bash
   https://github.com/SwohamKayastha/Task-Tracker-CLI.git
   cd "Task-Tracker-CLI"
   
2. **Install Dependencies:**
   ```bash
   pip install click
   
## Usage

1. **Add Task:**
   ```bash
   python main.py item
2. **Update a Task:**
   ```bash
   python main.py update_item
3. **Delete a Task:**
   ```bash
   python main.py delete_item
4. **List All Tasks:**
   ```bash
   python main.py display
4. **List In-Progress Tasks:**
   ```bash
   python main.py display_progress
4. **List Completed Tasks**
   ```bash
   python main.py display_completed