import os
import json
import tkinter as tk
from tkinter import simpledialog

# Criar a janela principal
root = tk.Tk()
root.title("Minha GUI Tkinter")

# Def path to json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

# Function to load the task list from the json file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Creating the task list
tasks = load_tasks()

# Function to save the changes on the json file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Update the tasks display
def update_task_display():
    task_display.config(state="normal")
    task_display.delete("1.0", tk.END)
    for task in tasks:
        task_display.insert(tk.END, f"- {task['name']} ({task['status']})\n")
    task_display.config(state="disabled")

# Function that sets the pattern for a new task
def create_task(name):
    task = {"name": name, "status": "Pending"}
    return task

# Function to add a new task
def add_task_prompt():
    task_name = simpledialog.askstring("New Task", "Type the new task: ")
    if task_name and task_name.strip():
        task = create_task(task_name.strip())
        tasks.append(task)
        save_tasks()
        update_task_display()

# Quit function
def quit():
    root.destroy()

# Seting text box
task_display = tk.Text(root, height=10, width=40, state="disabled")  
task_display.pack(expand=True, fill="both", padx=10, pady=10)

# Seting add task button
add_task_btn = tk.Button(root, text="Add Task", command= add_task_prompt)
add_task_btn.pack()

# Seting remove task button
remove_task_btn = tk.Button(root, text="Remove Task")
remove_task_btn.pack()

# Seting quit button
quit_btn = tk.Button(root, text="Quit", command=quit)
quit_btn.pack()

# Update task display
update_task_display()

# Rodar o loop principal
root.mainloop()