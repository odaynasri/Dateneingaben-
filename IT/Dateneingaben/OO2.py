import tkinter as tk
from threading import get_ident
from tkinter import ttk
from tkcalendar import *
import sqlite3
import os
from PIL import ImageTk

bg_color = '#346466'

window = tk.Tk()
window.title('Dateneingaben')
window.eval('tk::PlaceWindow . center')

x = window.winfo_screenwidth() // 2
y = int(window.winfo_screenheight() * 0.1)
window.geometry('700x800+' + str(x) + '+' + str(y))


frame = tk.Frame(window, width=700, height=800, bg=bg_color)
frame.pack(fill='both', expand=True)
frame.pack_propagate(False)
logo_img = ImageTk.PhotoImage(file= r'D:\IT\Dateneingaben\Images\Logo2.png')
#logo_img = ImageTk.PhotoImage(file= r'C:\Users\nasri.ODAYNASRI\OneDrive\Desktop\Dateneingaben\Images\Logo2.png')
logo_widget = tk.Label(frame, image= logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

benutzer_frame = tk.LabelFrame(
                                    master= frame,
                                    text= 'Dateneingabe',
                                    bg=bg_color,
                                    fg='pink',
                                    font=('TkMenuFont', 14)
                                    )
#benutzer_frame.pack_propagate(False)
benutzer_frame.pack()

tk.Label(benutzer_frame, text= 'Vorname', bg=bg_color, fg='white').grid(row=0, column=0)
tk.Label(benutzer_frame, text= 'Nachname', bg=bg_color, fg='white').grid(row=0, column=1)

vorname_entry = tk.Entry(benutzer_frame)
vorname_entry.grid(row=1, column= 0)

nachname_enrty = tk.Entry(benutzer_frame)
nachname_enrty.grid(row=1, column= 1)

tk.Label(benutzer_frame, text= 'Arbeitsposition', bg=bg_color, fg='white').grid(row=0, column=2)
titel_combobox = ttk.Combobox(benutzer_frame, values=['Geschäftsführer', 'Leiter', 'Manager', 'Verwaltung', 'Mitarbeiter', 'Praktikant'])
titel_combobox.grid(row=1, column=2)

tk.Label(benutzer_frame, text= 'Einstellungsdatum', bg=bg_color, fg='white').grid(row=2, column=0)
datum_var = tk.StringVar(value='TT.MM.JJJJ')
datum_entry = ttk.Entry(benutzer_frame, textvariable=datum_var)
datum_entry.grid(row=3, column=0)


tk.Label(benutzer_frame, text='Nationalität', bg=bg_color, fg='white').grid(row=2, column=2)
natio_combobox = ttk.Combobox(benutzer_frame, values= ['afghanisch', 'ägyptisch', 'albanisch', 'algerisch', 'amerikanisch', 'britisch',
                      'bulgarisch', 'deutsch', 'französisch','indonesisch', 'irisch', 'iseralisch',
                      'italienisch', 'japanisch', 'libanesisch', 'mexikanisch', 'österreichisch',
                      'schweizerisch', 'spanisch', 'südafrikanisch', 'syrisch', 'türkisch',
                      'ukrainisch',
                      ]
             )
natio_combobox.grid(row=3, column=2)

class Openkalender:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root)
        self.label.grid(row=4, column=1)

        self.datum_button = tk.Button(root, text='Kalender öffen', bg=bg_color, fg='white', command=self.open_kalender)
        self.datum_button.grid(row=3, column=1)

    def open_kalender(self):
        kalender_popup= tk.Toplevel(self.root, bg=bg_color)
        kalender_popup.title('Datum auswählen')

        kalender= Calendar(kalender_popup, selectmode='day', date_pattern='dd.mm.yyyy')
        kalender.pack()

        def datum_bestätigen():
            datum_auswählen= kalender.get_date()
            datum_var.set(datum_auswählen)
            kalender_popup.destroy()

        d_bestätigen= tk.Button(kalender_popup, text= 'Datum bestätigen', bg=bg_color, fg='white', command=datum_bestätigen)
        d_bestätigen.pack()

Openkalender(benutzer_frame)

window.mainloop()