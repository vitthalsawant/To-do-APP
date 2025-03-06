import tkinter as tk
from tkinter import messagebox
import pickle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.listbox = tk.Listbox(self.frame, height=15, width=50, bg="light yellow", activestyle='dotbox')
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def load_tasks(self):
        try:
            with open("tasks.dat", "rb") as file:
                self.tasks = pickle.load(file)
                self.update_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.dat", "wb") as file:
            pickle.dump(self.tasks, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.save_tasks)
    root.mainloop()
