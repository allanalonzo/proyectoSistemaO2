import os
import tkinter as tk
from tkinter import ttk, messagebox
import psutil

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
        pid = proc.info['pid']
        name = proc.info['name']
        cpu_percent = proc.info['cpu_percent']
        memory = f"{proc.info['memory_info'].rss / 1024 ** 2:.2f} MB"
        status = proc.info['status']
        processes.append((pid, name, cpu_percent, memory, status))
    
    return sorted(processes, key=lambda x: x[1])  
def update_process_list():
    for row in tree.get_children():
        tree.delete(row)
    
    for proc in get_processes():
        tree.insert("", "end", values=proc)

def search_process():
    query = search_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    
    for proc in get_processes():
        if query in str(proc[0]).lower() or query in proc[1].lower():
            tree.insert("", "end", values=proc)

def end_process():
    selected_item = tree.selection()
    if selected_item:
        pid = tree.item(selected_item)["values"][0]
        try:
            p = psutil.Process(pid)
            p.terminate()
            messagebox.showinfo("Éxito", f"Proceso {pid} finalizado.")
            update_process_list()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo finalizar el proceso {pid}: {e}")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un proceso para finalizar.")

def suspend_process():
    selected_item = tree.selection()
    if selected_item:
        pid = tree.item(selected_item)["values"][0]
        try:
            p = psutil.Process(pid)
            p.suspend()
            messagebox.showinfo("Éxito", f"Proceso {pid} suspendido.")
            update_process_list()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo suspender el proceso {pid}: {e}")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un proceso para suspender.")

def resume_process():
    selected_item = tree.selection()
    if selected_item:
        pid = tree.item(selected_item)["values"][0]
        try:
            p = psutil.Process(pid)
            p.resume()
            messagebox.showinfo("Éxito", f"Proceso {pid} reanudado.")
            update_process_list()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reanudar el proceso {pid}: {e}")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un proceso para reanudar.")

root = tk.Tk()
root.title("Administrador de Tareas")
root.attributes('-fullscreen', True)

top_menu_frame = tk.Frame(root)
top_menu_frame.pack(side=tk.TOP, fill=tk.X)

tk.Label(top_menu_frame, text="ADMINISTRADOR DE TAREAS", width=100).pack(side=tk.TOP)

search_var = tk.StringVar()
search_entry = tk.Entry(top_menu_frame, textvariable=search_var, width=50)
search_entry.pack(side=tk.LEFT, padx=10)
tk.Button(top_menu_frame, text="Buscar", command=search_process).pack(side=tk.LEFT)

body_frame = tk.Frame(root)
body_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

columns = ("PID", "Nombre", "%CPU", "Memoria", "Estado")
tree = ttk.Treeview(body_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)


scrollbar = ttk.Scrollbar(body_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(fill=tk.BOTH, expand=True)

bottom_menu_frame = tk.Frame(root)
bottom_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

tk.Button(bottom_menu_frame, text="Finalizar Proceso", command=end_process).pack(side=tk.LEFT)
tk.Button(bottom_menu_frame, text="Suspender Proceso", command=suspend_process).pack(side=tk.LEFT)
tk.Button(bottom_menu_frame, text="Reanudar Proceso", command=resume_process).pack(side=tk.LEFT)
tk.Button(bottom_menu_frame, text="Actualizar", command=update_process_list).pack(side=tk.LEFT)

root.protocol("WM_DELETE_WINDOW", root.quit) 
root.bind("<Escape>", lambda e: root.iconify())  
update_process_list()
root.mainloop()