import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("todolist.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("todolist.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            task_listbox.delete(0, tk.END)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=20)

task_label = tk.Label(frame, text="Enter Task:")
task_label.grid(row=0, column=0)

task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=0, column=1)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=3)

save_button = tk.Button(frame, text="Save Tasks", command=save_tasks)
save_button.grid(row=1, column=1)

load_button = tk.Button(frame, text="Load Tasks", command=load_tasks)
load_button.grid(row=1, column=2)

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
task_listbox.pack()

load_tasks()

root.mainloop()
