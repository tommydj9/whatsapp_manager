import tkinter as tk
from AppOpener import open

# Password corretta per accedere
PASSWORD = "cetriolo10"

# Funzione per gestire l'inserimento della password
def submit_pass():
    password = entry.get()
    if password == PASSWORD:
        open("whatsapp")
        print("Accesso a WhatsApp...")
        root.quit()  # Chiude l'applicazione
    else:
        error_label.config(text="Password errata, riprova", fg="red")
        entry.delete(0, tk.END)  # Cancella il testo nella casella di input

# Creazione della finestra principale
root = tk.Tk()
root.title("Accedi a Whatsapp")

# Configura la dimensione della finestra e il colore di sfondo
root.geometry("400x300")
root.configure(bg="black")

# Creazione dell'etichetta per il titolo
title_label = tk.Label(root, text="Accedi a Whatsapp", fg="white", bg="black", font=("Arial", 18, "bold"))
title_label.pack(pady=30)

# Creazione dell'etichetta per l'input
entry_label = tk.Label(root, text="Inserisci la password:", fg="white", bg="black", font=("Arial", 12))
entry_label.pack(pady=10)

# Creazione dell'input box
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

# Creazione dell'etichetta per il messaggio di errore (inizialmente vuota)
error_label = tk.Label(root, text="", fg="red", bg="black", font=("Arial", 10))
error_label.pack(pady=5)

# Creazione del pulsante per inviare la password
submit_button = tk.Button(root, text="Invia", command=submit_pass)
submit_button.pack(pady=20)

# Avvia il loop principale della finestra
root.mainloop()
