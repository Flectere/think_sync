import tkinter as tk
from tkinter import ttk, filedialog
from core import push_vault, pull_vault, write_config

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, folder)
        add_info()

# Создаем окно
root = tk.Tk()
root.title("Think Sync")
root.geometry("1000x700")
root.minsize(900, 600)

# Стили
style = ttk.Style()
style.configure('Title.TLabel', font=('Helvetica', 24, 'bold'))
style.configure('TLabel', font=('Helvetica', 16))
style.configure('TButton', font=('Helvetica', 16), padding=12)
style.configure('TEntry', font=('Helvetica', 16), padding=10)

# Главный контейнер
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both", pady=20)

# Заголовок (теперь идеально по центру)
title_frame = ttk.Frame(main_frame)
title_frame.pack(fill="x", pady=(0, 30))

title_label = ttk.Label(title_frame, text="Think Sync", style='Title.TLabel')
title_label.pack()

# Центральный блок с полями ввода
center_frame = ttk.Frame(main_frame)
center_frame.pack(expand=True, fill="both", padx=100)

def add_info():
    write_config(url_entry.get(), dir_entry.get()+"/Think Hub")

def create_input_row(parent, label_text, browse_command=None):
    frame = ttk.Frame(parent)
    frame.pack(fill="x", pady=15)
    
    label = ttk.Label(frame, text=label_text, width=16)
    label.pack(side="left", padx=(0, 10))
    
    entry = ttk.Entry(frame)
    entry.pack(side="left", expand=True, fill="x", padx=(0, 10))
    
    if browse_command:
        btn_text = "Обзор" if browse_command != add_info else "Сохранить"
        btn = ttk.Button(frame, text=btn_text, command=browse_command, width=10)
        btn.pack(side="left")

    return entry

# Поля ввода
url_entry = create_input_row(center_frame, "URL репозитория:", add_info)
dir_entry = create_input_row(center_frame, "Папка назначения:", select_directory)

# Кнопки Push и Pull в отдельном фрейме для центрирования
actions_frame = ttk.Frame(center_frame)
actions_frame.pack(pady=20)  # отступ сверху/снизу

pull_button = ttk.Button(actions_frame, text="Pull", width=15, command=pull_vault)
pull_button.pack(side="left", padx=10)

push_button = ttk.Button(actions_frame, text="Push", width=15, command=push_vault)
push_button.pack(side="left", padx=10)




def load_gui(url, folder):
    url_entry.insert(0, url)
    dir_entry.insert(0, folder)
    if not url or not folder:
        push_button.pack_forget()
        pull_button.pack_forget()
    root.mainloop()