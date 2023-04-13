import random
import string
import tkinter as tk

def genera_password(num_caratteri, includi_punti, includi_speciali):
    caratteri = string.ascii_letters + string.digits
    if includi_punti:
        caratteri += "."
    if includi_speciali:
        caratteri += string.punctuation
    password = ''.join(random.choice(caratteri) for i in range(num_caratteri))
    return password

def genera_nuova_password():
    num_max_caratteri = int(num_max_caratteri_entry.get())
    includi_punti = punti_checkbox.get()
    includi_speciali = speciali_checkbox.get()
    password_generata = genera_password(num_max_caratteri, includi_punti, includi_speciali)
    password_generata_label.configure(text=password_generata)

# Creazione della finestra principale
finestra = tk.Tk()
finestra.title("Generatore di password casuale")
finestra.geometry("400x200")
finestra.resizable(width=False, height=False)

# Etichetta per il numero massimo di caratteri
num_max_caratteri_label = tk.Label(finestra, text="Numero massimo di caratteri:")
num_max_caratteri_label.pack(anchor="w", padx=10, pady=5)

# Casella di testo per il numero massimo di caratteri
num_max_caratteri_entry = tk.Entry(finestra)
num_max_caratteri_entry.pack(anchor="w", padx=10, pady=5)

# Frame per i checkbox
checkbox_frame = tk.Frame(finestra)
checkbox_frame.pack(side=tk.LEFT, padx=10)

# Checkbox per includere i punti
punti_checkbox = tk.BooleanVar()
punti_checkbox.set(False)
punti_checkbox_label = tk.Checkbutton(checkbox_frame, text="Includi i punti", variable=punti_checkbox)
punti_checkbox_label.pack(anchor="w", pady=5)

# Checkbox per includere i caratteri speciali
speciali_checkbox = tk.BooleanVar()
speciali_checkbox.set(False)
speciali_checkbox_label = tk.Checkbutton(checkbox_frame, text="Includi i caratteri speciali", variable=speciali_checkbox)
speciali_checkbox_label.pack(anchor="w", pady=5)

# Bottone per generare una nuova password
nuova_password_button = tk.Button(finestra, text="Genera nuova password", command=genera_nuova_password)
nuova_password_button.pack(pady=20)

# Etichetta per la password generata
password_generata_label = tk.Label(finestra, text="", fg="black")
password_generata_label.pack(pady=5)

# Posiziona il bottone e la label sotto ad esso
finestra.update_idletasks()
pw_label_x = finestra.winfo_width() // 2
pw_label_y = finestra.winfo_height() - 50
nuova_password_button.place(x=pw_label_x, y=pw_label_y, anchor=tk.CENTER)
password_generata_label.place(x=pw_label_x, y=pw_label_y + 30, anchor=tk.CENTER)

# Loop della finestra principale
finestra.mainloop()
