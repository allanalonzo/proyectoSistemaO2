import os
import tkinter as tk
from tkinter import ttk, messagebox
import psutil

process_data = [
    {"PID": 101, "Nombre": "Proceso1", "%CPU": 15, "Memoria": "150MB", "Estado": "Activo"},
    {"PID": 102, "Nombre": "Proceso2", "%CPU": 25, "Memoria": "250MB", "Estado": "Suspendido"},
    {"PID": 103, "Nombre": "Proceso3", "%CPU": 35, "Memoria": "350MB", "Estado": "Activo"},
    {"PID": 104, "Nombre": "Proceso4", "%CPU": 45, "Memoria": "450MB", "Estado": "Activo"},
    {"PID": 105, "Nombre": "Proceso5", "%CPU": 55, "Memoria": "550MB", "Estado": "Suspendido"}
]

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
        pid = proc.info['pid']
        name = proc.info['name']
        cpu_percent = proc.info['cpu_percent']
        memory = f"{proc.info['memory_info'].rss / 1024 ** 2:.2f} MB"
        status = proc.info['status']
        processes.append((pid, name, cpu_percent, memory, status))
    
    return processes

def update_process_list():
    for row in tree.get_children():
        tree.delete(row)
    
    for proc in get_processes():
        tree.insert("", "end", values=proc)
    
    root.after(3000, update_process_list) 
    
root = tk.Tk()
root.title("Administrador de Tareas")
root.attributes('-fullscreen', True)

top_menu_frame = tk.Frame(root)
top_menu_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(top_menu_frame, text="ADMINISTRADOR DE TAREAS", width=100).pack(side=tk.TOP)
    
body_frame = tk.Frame(root)
body_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

columns = ("PID", "Nombre", "%CPU", "Memoria", "Estado")
tree = ttk.Treeview(body_frame, columns=columns, show="headings")
    
for col in columns:
        tree.heading(col, text=col)
    
for process in process_data:
    tree.insert("", tk.END, values=(process["PID"], process["Nombre"], process["%CPU"], process["Memoria"], process["Estado"]))
    
tree.pack(fill=tk.BOTH, expand=True)

bottom_menu_frame = tk.Frame(root)
bottom_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

tk.Button(bottom_menu_frame, text="Finalizar Proceso").pack(side=tk.LEFT)
tk.Button(bottom_menu_frame, text="Suspender Proceso").pack(side=tk.LEFT)
tk.Button(bottom_menu_frame, text="Reaundar Proceso").pack(side=tk.LEFT)

root.protocol("WM_DELETE_WINDOW", root.quit) 
root.bind("<Escape>", lambda e: root.iconify())  
update_process_list()
root.mainloop()

