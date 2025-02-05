import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n--- To-Do list ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task List")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()
    print(f"task '{task}' added!")

def remove_task():
    if not tasks:
        print("No tasks to remove!")
    else:
        task_num = int(input("Enter the number of the task you want to remove: ")) - 1
        if 0 <= task_num <= len(tasks):
            removed = tasks.pop(task_num)
            save_tasks()
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")

def show_tasks():
    if not tasks:
        print("There's no tasks added yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def quit():
    print("Goodbye!")

tasks = load_tasks()

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
        quit()
        break

    else:
        print("\nInvalid choice, please try a valid number.")
