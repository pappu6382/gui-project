import tkinter as tk
from tkinter import Tk, messagebox,Label,Entry





class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, tasks):
        for task in tasks:
            self.tasks.append(task)
        messagebox.showinfo("Success", "Tasks added successfully!")

    def view_tasks(self):
        if self.tasks:
            task_list = "\n".join([f"{idx}. {task}" for idx, task in enumerate(self.tasks, 1)])
            messagebox.showinfo("Your To-Do List", task_list)
        else:
            messagebox.showinfo("Your To-Do List", "Your To-Do List is empty!")

    def complete_task(self, completed_tasks):
        if completed_tasks:
            self.tasks = [task for idx, task in enumerate(self.tasks, 1) if idx not in completed_tasks]
            messagebox.showinfo("Success", "Selected tasks completed successfully!")
        else:
            messagebox.showerror("Error", "Please select tasks to complete!")

def add_tasks(todo_list, tasks_entry):
    tasks = tasks_entry.get("1.0", tk.END).splitlines()
    if tasks:
        todo_list.add_task(tasks)
        tasks_entry.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", "Please enter tasks!")

def view_tasks(todo_list):
    todo_list.view_tasks()

def complete_task(todo_list, task_number_entry):
    try:
        completed_tasks = [int(task_number) for task_number in task_number_entry.get().split(",")]
        todo_list.complete_task(completed_tasks)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid task numbers!")

def clear_tasks(todo_list):
    todo_list.tasks = []
    messagebox.showinfo("Success", "All tasks cleared!")

todo_list = ToDoList()

root = tk.Tk()
root.title("To-Do List Application")

tasks_label = tk.Label(root, text="Enter tasks (one per line):")
tasks_label.pack()

tasks_entry = tk.Text(root, width=50, height=5)
tasks_entry.pack()

add_button = tk.Button(root, text="Add Tasks", command=lambda: add_tasks(todo_list, tasks_entry))
add_button.pack()

view_button = tk.Button(root, text="View Tasks", command=lambda: view_tasks(todo_list))
view_button.pack()

task_number_label = tk.Label(root, text="Enter task numbers to complete (comma-separated):")
task_number_label.pack()

task_number_entry = tk.Entry(root, width=50)
task_number_entry.pack()

complete_button = tk.Button(root, text="Complete Task", command=lambda: complete_task(todo_list, task_number_entry))
complete_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=lambda: clear_tasks(todo_list))
clear_button.pack()

root.mainloop()
