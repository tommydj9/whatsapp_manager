import tkinter as tk
import os  # Import per verificare l'esistenza del file
import subprocess

# Definisci correttamente la variabile FILE
FILE = "ps_file.txt"

# Funzione per creare una password e salvarla nel file
def create_password():
    pasw = entry.get()
    with open(FILE, "w") as c:  # Utilizza la variabile FILE correttamente
        c.write(str(pasw))
    print(f"File '{FILE}' created with password.")
    root.quit()

# Funzione per leggere il contenuto del file
def read_file():
    if os.path.exists(FILE):  # Verifica se il file esiste
        with open(FILE, "r") as c:
            return c.read().strip()  # Ritorna il contenuto senza spazi bianchi
    else:
        return ''  # Se il file non esiste, ritorna una stringa vuota

# Funzione per gestire l'inserimento della password
def submit_pass():
    password = entry.get()
    psw = read_file()
    if password == psw:
        subprocess.Popen(["start", "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"], shell=True)
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

# Leggi il contenuto del file per verificare se una password esiste
text_in_file = read_file()

if text_in_file == '':
    # Se il file è vuoto, chiedi di creare una password
    entry_label = tk.Label(root, text="Crea la password:", fg="white", bg="black", font=("Arial", 12))
    entry_label.pack(pady=10)

    # Creazione dell'input box per inserire la nuova password
    entry = tk.Entry(root, show="*", width=30)
    entry.pack(pady=10)

    # Creazione dell'etichetta per il messaggio di errore (inizialmente vuota)
    error_label = tk.Label(root, text="", fg="red", bg="black", font=("Arial", 10))
    error_label.pack(pady=5)

    # Creazione del pulsante per inviare la nuova password
    submit_button = tk.Button(root, text="Crea password", command=create_password)
    submit_button.pack(pady=20)

else:
    # Se il file contiene già una password, chiedi di inserirla per accedere
    entry_label = tk.Label(root, text="Inserisci la password:", fg="white", bg="black", font=("Arial", 12))
    entry_label.pack(pady=10)
    
    # Creazione dell'input box per inserire la password
    entry = tk.Entry(root, show="*", width=30)
    entry.pack(pady=10)

    # Creazione dell'etichetta per il messaggio di errore (inizialmente vuota)
    error_label = tk.Label(root, text="", fg="red", bg="black", font=("Arial", 10))
    error_label.pack(pady=5)

    # Creazione del pulsante per inviare la password e verificare
    submit_button = tk.Button(root, text="Accedi", command=submit_pass)
    submit_button.pack(pady=20)

# Avvia il loop principale della finestra
root.mainloop()

