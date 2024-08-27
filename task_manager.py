import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import random

# Définition des couleurs pastel de violet
violet_clair = '#B19CD9'
violet_moyen = '#9370DB'
violet_fonce = '#7D3C98'

# Dictionnaire pour associer chaque projet à une couleur de surbrillance unique
couleurs_projets = {}

# Fonction pour attribuer une couleur unique à un projet
def couleur_unique():
    while True:
        couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if couleur not in couleurs_projets.values():
            return couleur

# Fonction de validation pour l'échéance (accepte uniquement les chiffres et '/')
def validate_date_input(char):
    return char.isdigit() or char == '/'

# Fonction pour ajouter une tâche à la liste
def add_task():
    task = description_entry.get()
    priority = priority_combobox.get()
    deadline = deadline_entry.get()
    project = project_entry.get()
    
    if task and priority and deadline and project:
        couleur = couleurs_projets.get(project)
        if not couleur:
            couleur = couleur_unique()
            couleurs_projets[project] = couleur
            
        task_info = f"Tâche: {task} - Priorité: {priority} - Échéance: {deadline} - Projet: {project}"
        tasks_listbox.insert(tk.END, task_info)
        tasks_listbox.itemconfig(tk.END, {'bg': couleur})  # Configure la couleur de surbrillance pour cette tâche
        description_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        project_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")

# Fonction pour marquer une tâche comme complétée
def mark_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        task_info = tasks_listbox.get(selected_task)
        tasks_listbox.itemconfig(selected_task, {'fg': 'gray', 'font': ('Helvetica', 10, 'italic')})
        tasks_listbox.insert(tk.END, f"{task_info} - Complétée le {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        tasks_listbox.delete(selected_task)
    except IndexError:
        pass

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Gestionnaire de tâches avancé")
root.geometry("600x400")  # Taille initiale de la fenêtre

# Créer des widgets Tkinter avec des styles personnalisés
style = ttk.Style()

style.configure('TButton', background=violet_moyen, foreground=violet_fonce, padding=5, borderwidth=0, font=('Helvetica', 10, 'bold'))
style.configure('TEntry', background='#ecf0f1', foreground=violet_fonce, borderwidth=0, font=('Helvetica', 10))
style.configure('TLabel', background='#ecf0f1', foreground=violet_fonce, font=('Helvetica', 10))
style.configure('TListbox', background='#ecf0f1', foreground=violet_fonce, highlightthickness=0, borderwidth=0, font=('Helvetica', 10))

description_label = ttk.Label(root, text="Description de la tâche:")
description_entry = ttk.Entry(root)
priority_label = ttk.Label(root, text="Priorité:")
priority_combobox = ttk.Combobox(root, values=["Haute", "Moyenne", "Basse"])
deadline_label = ttk.Label(root, text="Échéance (format: JJ/MM/AAAA HH:MM):")
deadline_entry = ttk.Entry(root)
deadline_entry.config(validate="key", validatecommand=(root.register(validate_date_input), '%S'))
project_label = ttk.Label(root, text="Projet:")
project_entry = ttk.Entry(root)
add_button = ttk.Button(root, text="Ajouter", command=add_task)
tasks_listbox = tk.Listbox(root)
mark_button = ttk.Button(root, text="Marquer comme complétée", command=mark_task)

# Disposer les widgets dans la fenêtre
description_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
description_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
priority_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
deadline_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
deadline_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
project_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
project_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
tasks_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
mark_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Configurer le gestionnaire de grille pour que les lignes et les colonnes soient redimensionnées de manière égale
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

# Lancer la boucle principale Tkinter
root.mainloop()
