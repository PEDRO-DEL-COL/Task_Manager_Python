import os
import json
import tkinter as tk

root = tk.Tk()
root.title("Task Manager")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n--- To-Do list ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task List")
    print("4. Edit task")
    print("5. Change Status")
    print("6. Exit")

def create_task(name):
    task = {"name": name, "status": "Pending"}
    return task

def add_task():
    task_name = input("Enter a task: ")
    task = create_task(task_name)
    tasks.append(task)
    save_tasks()
    print(f"task '{task_name}' added!")

def remove_task():
    if not tasks:
        print("No tasks to remove!")
    else:
        print("\nYour tasks:\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']}\n   Status: {task['status']}\n")
        task_num = int(input("Enter the number of the task you want to remove: ")) - 1
        if 0 <= task_num <= len(tasks):
            removed = tasks.pop(task_num)
            save_tasks()
            print(f"Removed task: {removed["name"]}")
        else:
            print("Invalid task number!")

def show_tasks():
    if not tasks:
        print("There's no tasks added yet!")
    else:
        print("\nYour tasks:\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']}\n   Status: {task['status']}\n")

def edit_task():
    if not tasks:
        print("No tasks available to edit.")
        return

    print("\nYour tasks:\n")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}\n   Status: {task['status']}\n")

    try:
        edit_index = int(input("Type the number of the task you want to edit: ")) - 1

        if 0 <= edit_index < len(tasks):
            new_task = input("Type the new task: ")
            tasks[edit_index]["name"] = new_task
            print("Possible status:\n")
            status_list = ["Completed", "Pending"]
            for i, status in enumerate(status_list, start=1):
                print(f"{i}. {status}")
            choice = input("Type the number of the status you want for this task: ")
            if choice == "1":
                tasks[edit_index]["status"] = "Completed"
            elif choice == "2":
                tasks[edit_index]["status"] = "Pending"
            else:
                print("Invalid task number.")
            save_tasks()
            print(f"Task edited succesfuly: {task['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Type a valid number.")

def change_status():
    print("\nYour tasks:\n")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}\n   Status: {task['status']}\n")

    try:
        status_index = int(input("Type the number of the task you want to change the status: ")) - 1
        if 0 <= status_index < len(tasks):
            print("Possible status:\n")
            status_list = ["Completed", "Pending"]
            for i, status in enumerate(status_list, start=1):
                print(f"{i}. {status}")
            choice = input("Type the number of the status you want for this task: ")
            if choice == "1":
                tasks[status_index]["status"] = "Completed"
            elif choice == "2":
                tasks[status_index]["status"] = "Pending"
            else:
                print("Invalid task number.")
    except ValueError:
        print("Type a valid number.")
    
def quit():
    print("Goodbye!")

root = tk.Tk()
root.title("Task Manager")

root.mainloop()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    
    elif choice == "2":
        remove_task()
    
    elif choice == "3":
        show_tasks()

    elif choice == "4":
        edit_task()

    elif choice == "5":
        change_status()

    elif choice == "6":
        quit()
        break

    else:
        print("\nInvalid choice, please try a valid number.")
