import tkinter as tk
from tkinter import ttk

process_data = [
    {"PID": 101, "Nombre": "Proceso1", "%CPU": 15, "Memoria": "150MB", "Estado": "Activo"},
    {"PID": 102, "Nombre": "Proceso2", "%CPU": 25, "Memoria": "250MB", "Estado": "Suspendido"},
    {"PID": 103, "Nombre": "Proceso3", "%CPU": 35, "Memoria": "350MB", "Estado": "Activo"},
    {"PID": 104, "Nombre": "Proceso4", "%CPU": 45, "Memoria": "450MB", "Estado": "Activo"},
    {"PID": 105, "Nombre": "Proceso5", "%CPU": 55, "Memoria": "550MB", "Estado": "Suspendido"}
]

def create_main_window():
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
    root.mainloop()

create_main_window()