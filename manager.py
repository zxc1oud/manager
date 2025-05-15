# Проект 4 из 100

from tkinter import *

def create_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def complete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(END, f"{task} (Выполнено)")

root = Tk()
canvas = Canvas(root, width=800, height=600)
frame = Frame(root, bg='black')

root['bg'] = 'white'
root.title("Task Manager")
root.resizable(width=True, height=True)

title = Label(frame, text="Привет! Это твой личный менеджер задач", bg='black', fg='white')
task_label = None
task_entry = Entry(frame, width=50, bg='black', fg='white', insertbackground='white', selectbackground='gray')
tasks_listbox = Listbox(frame, width=50, height=15, bg='black', fg='white', selectbackground='gray')
button = Button(frame, text="Создать задачу", bg='black', fg='white', command=create_task)
button2 = Button(frame, text="Удалить задачу", bg='black', fg='white', command=delete_task)
button3 = Button(frame, text="Выполнить задачу", bg='black', fg='white', command=complete_task)

canvas.pack()
title.place(x=275, y=20)
task_entry.place(x=250, y=50)
tasks_listbox.place(x=250, y=100)
button.place(x=250, y=400)
button2.place(x=350, y=400)
button3.place(x=450, y=400)
frame.place(relwidth=1, relheight=1)


root.mainloop()