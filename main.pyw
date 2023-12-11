import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog


def add_task(entry, listbox):
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("An empty task", "Please enter the task!")

def delete_task(listbox):
    try:
        selected_index = listbox.curselection()
        if selected_index:
            listbox.delete(selected_index)
    except:
        pass


def clear_tasks(listbox):
    listbox.delete(0, tk.END)


def change_theme(window, theme, label, label2, listbox, entry, add_button, delete_button, clear_button, open_button, export_button):
    if theme == "Dark":
        window.configure(bg='#222222')
        label.configure(fg='white', bg='#222222')
        label2.configure(fg='white', bg='#222222')
        listbox.configure(bg='#444444', fg='white', selectbackground='#666666', selectforeground='white')
        entry.configure(bg='#444444', fg='white', selectbackground='#666666', selectforeground='white')
        add_button.configure(bg='#555555', fg='white', activebackground='#666666', activeforeground='white')
        delete_button.configure(bg='#555555', fg='white', activebackground='#666666', activeforeground='white')
        clear_button.configure(bg='#555555', fg='white', activebackground='#666666', activeforeground='white')
        open_button.configure(bg='#555555', fg='white', activebackground='#666666', activeforeground='white')
        export_button.configure(bg='#555555', fg='white', activebackground='#666666', activeforeground='white')
    elif theme == "Light":
        window.configure(bg='white')
        label.configure(fg='black', bg='white')
        label2.configure(fg='black', bg='white')
        listbox.configure(bg='white', fg='black', selectbackground='#eeeeee', selectforeground='black')
        entry.configure(bg='white', fg='black', selectbackground='#eeeeee', selectforeground='black')
        add_button.configure(bg='#eeeeee', fg='black', activebackground='#dddddd', activeforeground='black')
        delete_button.configure(bg='#eeeeee', fg='black', activebackground='#dddddd', activeforeground='black')
        clear_button.configure(bg='#eeeeee', fg='black', activebackground='#dddddd', activeforeground='black')
        open_button.configure(bg='#eeeeee', fg='black', activebackground='#dddddd', activeforeground='black')
        export_button.configure(bg='#eeeeee', fg='black', activebackground='#dddddd', activeforeground='black')


def open_file(listbox):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    with open(file_path, 'r') as file:
        tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())


def export_file(listbox):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(file_path, 'w') as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


def main():
    window = tk.Tk()
    window.title("TODO List")
    window.geometry("350x280")
    window.resizable(False, False)
    window.configure(bg='#222222')

    # Создание меню
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    # Создание выпадающего меню "Тема"
    theme_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Theme", menu=theme_menu)
    theme_menu.add_command(label="Black", command=lambda: change_theme(window, "Dark", label, label2, listbox, entry, add_button, delete_button, clear_button, open_button, export_button))
    theme_menu.add_command(label="Light", command=lambda: change_theme(window, "Light", label, label2, listbox, entry, add_button, delete_button, clear_button, open_button, export_button))

    # Создание кнопки "Выход"
    menubar.add_command(label="Exit", command=window.quit)

    # Создание кнопки "Выход"
    menubar.add_command(label="Developer: Tailogs")

    label = tk.Label(window, text="Task list:", fg='white', bg='#222222', font=('Arial', 14, 'bold'))
    label.grid(row=0, column=0, pady=(10, 0))

    listbox = tk.Listbox(window)
    listbox.configure(bg='#444444', fg='white', selectbackground='#666666', selectforeground='white',
                      font=('Arial', 12), bd=0)
    listbox.grid(row=1, column=0, rowspan=5, padx=10, pady=(5, 0))

    label2 = tk.Label(window, text='Add task:', fg='white', bg='#222222', font=('Arial', 12, 'bold'))
    label2.grid(row=0, column=1, pady=(10, 0), padx=(0, 5))

    entry = tk.Entry(window, bg='#444444', fg='white', selectbackground='#666666', selectforeground='white')
    entry.grid(row=1, column=1, ipady=3, padx=(0, 5))


    def bind_enter(event):
        add_task(entry, listbox)
        entry.focus()


    entry.bind("<Return>", bind_enter)
    entry.focus()
    
    add_button = tk.Button(window, text="Add task", command=lambda: add_task(entry, listbox),
                           relief=tk.FLAT, bg='#555555', fg='white', activebackground='#666666',
                           activeforeground='white', font=('Arial', 10))
    add_button.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='w')

    delete_button = tk.Button(window, text="Delete", command=lambda: delete_task(listbox),
                              relief=tk.FLAT, bg='#555555', fg='white', activebackground='#666666',
                              activeforeground='white', font=('Arial', 10))
    delete_button.grid(row=3, column=1, sticky='w', padx=(0, 5))

    clear_button = tk.Button(window, text="Clear", command=lambda: clear_tasks(listbox),
                             relief=tk.FLAT, bg='#555555', fg='white', activebackground='#666666',
                             activeforeground='white', font=('Arial', 10))
    clear_button.grid(row=6, column=0, pady=(5, 0), sticky='w', padx=10)

    open_button = tk.Button(window, text="Open file", command=lambda: open_file(listbox),
                            relief=tk.FLAT, bg='#555555', fg='white', activebackground='#666666',
                            activeforeground='white', font=('Arial', 10))
    open_button.grid(row=4, column=1, sticky='w', padx=(0, 5))

    export_button = tk.Button(window, text="Export file", command=lambda: export_file(listbox),
                              relief=tk.FLAT, bg='#555555', fg='white', activebackground='#666666',
                              activeforeground='white', font=('Arial', 10))
    export_button.grid(row=5, column=1, sticky='w', padx=(0, 5))

    window.mainloop()


if __name__ == "__main__":
    main()
