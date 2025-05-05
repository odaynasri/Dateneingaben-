import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
import os

# === Datenbank vorbereiten ===
db_datei = "benutzer_daten.db"

def init_db():
    conn = sqlite3.connect(db_datei)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS benutzer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vorname TEXT NOT NULL,
            nachname TEXT NOT NULL,
            titel TEXT,
            geburtsdatum TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# === GUI ===
window = tk.Tk()
window.title('Dateneingaben')
window.geometry('600x300')
window.configure(background='#A1CDEC')

frame = tk.Frame(master=window)
frame.pack()

benutzer_info_frame = tk.LabelFrame(master=frame, text='Benutzerinformationen')
benutzer_info_frame.grid(row=0, column=0, padx=20, pady=20)

# Labels und Eingabefelder
tk.Label(master=benutzer_info_frame, text='Vorname').grid(row=0, column=0)
tk.Label(master=benutzer_info_frame, text='Nachname').grid(row=0, column=1)

vorname_entry = tk.Entry(master=benutzer_info_frame)
vorname_entry.grid(row=1, column=0)

nachname_entry = tk.Entry(master=benutzer_info_frame)
nachname_entry.grid(row=1, column=1)

tk.Label(master=benutzer_info_frame, text='Titel').grid(row=0, column=2)
titel_combobox = ttk.Combobox(master=benutzer_info_frame, values=['', 'Dr.', 'Mr.', 'Ms.', 'Mrs.'])
titel_combobox.grid(row=1, column=2)

tk.Label(master=benutzer_info_frame, text='Geburtsdatum').grid(row=2, column=0)
geburtsdatum_var = tk.StringVar(value='TT.MM.JJJJ')
geburtsdatum_entry = tk.Entry(master=benutzer_info_frame, textvariable=geburtsdatum_var)
geburtsdatum_entry.grid(row=3, column=0)

# Kalender Popup
def open_calendar():
    calendar_popup = tk.Toplevel(window)
    calendar_popup.title("Geburtsdatum auswählen")

    calendar = Calendar(calendar_popup, selectmode='day', date_pattern='dd.mm.yyyy')
    calendar.pack(padx=10, pady=10)

    def confirm_date():
        selected_date = calendar.get_date()
        geburtsdatum_var.set(selected_date)
        calendar_popup.destroy()

    confirm_btn = tk.Button(calendar_popup, text="Datum bestätigen", command=confirm_date)
    confirm_btn.pack(pady=10)

tk.Button(benutzer_info_frame, text='Geburtstag eingeben', command=open_calendar).grid(row=3, column=1)

# === Daten speichern ===
def speichern():
    vorname = vorname_entry.get()
    nachname = nachname_entry.get()
    titel = titel_combobox.get()
    geburtsdatum = geburtsdatum_var.get()

    if not vorname or not nachname or geburtsdatum == 'TT.MM.JJJJ':
        print("Bitte alle Pflichtfelder ausfüllen.")
        return

    conn = sqlite3.connect(db_datei)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO benutzer (vorname, nachname, titel, geburtsdatum)
        VALUES (?, ?, ?, ?)
    ''', (vorname, nachname, titel, geburtsdatum))
    conn.commit()
    conn.close()

    print("Daten gespeichert!")
    # Optional: Felder leeren
    vorname_entry.delete(0, tk.END)
    nachname_entry.delete(0, tk.END)
    titel_combobox.set('')
    geburtsdatum_var.set('TT.MM.JJJJ')

# Speicher-Button
tk.Button(window, text="Speichern", command=speichern).pack(pady=10)

window.mainloop()
