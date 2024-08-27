import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Mots de Passe Sécurisés")
        self.root.configure(bg="#e8d8fa")  # Violet pastel
        self.center_window()

        self.password_length_label = tk.Label(root, text="Longueur du Mot de Passe:", bg="#e8d8fa")
        self.password_length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.password_length_entry = tk.Entry(root)
        self.password_length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.password_length_entry.insert(0, "12")

        self.generate_button = tk.Button(root, text="Générer Mot de Passe", command=self.generate_password, bg="#a68fd5", fg="white")  # Violet foncé
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.generated_password_label = tk.Label(root, text="Mot de Passe Généré:", bg="#e8d8fa")
        self.generated_password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.generated_password_listbox = tk.Listbox(root, bg="#d8c2f7", height=3)  # Violet plus clair
        self.generated_password_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.copy_button = tk.Button(root, text="Copier Mot de Passe", command=self.copy_password, bg="#a68fd5", fg="white", state="disabled")  # Violet foncé
        self.copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def center_window(self):
        window_width = 400
        window_height = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def generate_password(self):
        try:
            password_length = int(self.password_length_entry.get())
            if password_length <= 0:
                raise ValueError
        except ValueError:
            self.generated_password_listbox.delete(0, tk.END)
            self.generated_password_listbox.insert(tk.END, "Veuillez saisir une longueur de mot de passe valide.")
            return

        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))

        # Effacer le contenu précédent de la listbox
        self.generated_password_listbox.delete(0, tk.END)

        # Afficher le mot de passe généré dans la listbox
        self.generated_password_listbox.insert(tk.END, generated_password)

        # Activer le bouton de copie
        self.copy_button.config(state="normal")

        # Sauvegarder le mot de passe généré
        self.generated_password = generated_password

    def copy_password(self):
        pyperclip.copy(self.generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
