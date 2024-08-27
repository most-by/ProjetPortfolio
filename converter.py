import tkinter as tk
from tkinter import ttk

# Dictionnaire des taux de change approximatifs
taux_de_change = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 110.0,
    'CAD': 1.25,
    'AUD': 1.30,
    'CHF': 0.92,
    'CNY': 6.45,
    'INR': 73.0,
    'NZD': 1.40
}

# Fonction pour effectuer la conversion de devises
def convertir_devises():
    try:
        montant = float(entrée_montant.get())
        devise_origine = combo_devise_origine.get()
        devise_destination = combo_devise_destination.get()
        
        taux = taux_de_change[devise_destination] / taux_de_change[devise_origine]
        montant_converti = montant * taux
        résultat.config(text=f'{montant:.2f} {devise_origine} = {montant_converti:.2f} {devise_destination}')
    except ValueError:
        résultat.config(text='Veuillez saisir un montant valide.')

# Création de l'interface utilisateur
racine = tk.Tk()
racine.title('Conversion de Devises')
racine.geometry('400x250')
racine.configure(bg='#f0e6f5')  # Couleur de fond violet pastel

# Cadre principal
cadre_principal = ttk.Frame(racine, padding='20', style='Main.TFrame')
cadre_principal.grid(row=0, column=0, sticky='nsew')

# Style pour le cadre principal
style = ttk.Style()
style.configure('Main.TFrame', background='#f0e6f5')

# Éléments de l'interface
ttk.Label(cadre_principal, text='Montant à convertir:', background='#f0e6f5').grid(row=0, column=0, padx=10, pady=10, sticky='w')
entrée_montant = ttk.Entry(cadre_principal)
entrée_montant.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

ttk.Label(cadre_principal, text='De:', background='#f0e6f5').grid(row=1, column=0, padx=10, pady=10, sticky='w')
combo_devise_origine = ttk.Combobox(cadre_principal, values=list(taux_de_change.keys()))
combo_devise_origine.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
combo_devise_origine.current(0)

ttk.Label(cadre_principal, text='À:', background='#f0e6f5').grid(row=2, column=0, padx=10, pady=10, sticky='w')
combo_devise_destination = ttk.Combobox(cadre_principal, values=list(taux_de_change.keys()))
combo_devise_destination.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
combo_devise_destination.current(0)

bouton_convertir = ttk.Button(cadre_principal, text='Convertir', command=convertir_devises)
bouton_convertir.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

résultat = ttk.Label(cadre_principal, background='#f0e6f5')
résultat.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

racine.mainloop()
