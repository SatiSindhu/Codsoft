import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔ " if task["done"] else "✘ "
        listbox.insert(tk.END, f"{status}{task['title']}")

# Function to add a new task
def add_task():
    task_title = entry.get()
    if task_title:
        tasks.append({"title": task_title, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as completed
def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["done"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Function to delete a task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# UI Components
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack()

done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Start the GUI event loop
root.mainloop()
