import json
import os
from datetime import datetime

# Define the path for storing the to-do list
TODO_FILE = 'todos.json'

# Function to load the to-do list from a file
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save the to-do list to a file
def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)

# Function to display all tasks
def display_todos(todos):
    if not todos:
        print("No tasks found!")
    else:
        for idx, todo in enumerate(todos, 1):
            status = "Completed" if todo['completed'] else "Pending"
            print(f"{idx}. {todo['task']} | Due: {todo.get('due_date', 'N/A')} | Status: {status}")

# Function to add a new task
def add_task(todos, task, due_date=None):
    new_task = {
        'task': task,
        'completed': False,
        'due_date': due_date,
    }
    todos.append(new_task)
    save_todos(todos)

# Function to update a task
def update_task(todos, index, new_task, due_date=None):
    if 0 <= index < len(todos):
        todos[index]['task'] = new_task
        todos[index]['due_date'] = due_date
        save_todos(todos)
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(todos, index):
    if 0 <= index < len(todos):
        todos.pop(index)
        save_todos(todos)
    else:
        print("Invalid task number.")

def main():
    todos = load_todos()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_todos(todos)
        elif choice == '2':
            task = input("Enter the task description: ")
            due_date = input("Enter the due date (optional, format YYYY-MM-DD): ")
            add_task(todos, task, due_date if due_date else None)
        elif choice == '3':
            display_todos(todos)
            index = int(input("Enter the task number to update: ")) - 1
            task = input("Enter the new task description: ")
            due_date = input("Enter the new due date (optional, format YYYY-MM-DD): ")
            update_task(todos, index, task, due_date if due_date else None)
        elif choice == '4':
            display_todos(todos)
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(todos, index)
        elif choice == '5':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
