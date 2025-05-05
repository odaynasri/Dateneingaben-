import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk

bg_color = '#346366'

#--Mitarbeiter Klasse--
class Mitarbeiter:
    def __init__(self, vorname, nachname, position, einstellungsdatum, nationalitaet):
        self.vorname = vorname
        self.nachname = nachname
        self.position = position
        self.einstellungsdatum = einstellungsdatum
        self.nationalitaet = nationalitaet
        self.gehalt = self.gehalt_berechnen()

    def gehalt_berechnen(self):
        gehaltstabelle = {
            'Verwaltung': 1500,
            'Manager': 2000,
            'Abteilungsleiter': 2500,
            'Production': 5000,
            'Versandabteilung': 3650,
            'Rechnungsabteilung': 2750,
            'Montage': 2200,
            'Putzabteilung': 1900,
            'Kundenservice': 2000,
            'Scadensabteilung': 2100
        }
        return gehaltstabelle.get(self.position, 1000)

    def __str__(self):
        return (f"{self.vorname} {self.nachname} | {self.position} | {self.nationalitaet} |"
                f"Eingestellt am: {self.einstellungsdatum} | Gehalt ist: {self.gehalt}€")

#--Hauptfentster--
window = tk.Tk()
window.title('Dateneingaben')
window.eval('tk::PlaceWindow . center')

x = window.winfo_screenwidth() // 2
y = int(window.winfo_screenheight() * 0.1)
window.geometry('700x800+' + str(x) + '+' + str(y))

frame = tk.Frame(window, width=700, height=800, bg=bg_color)
frame.pack(fill='both', expand=True)
frame.pack_propagate(False)

#--Logo--
logo_img = ImageTk.PhotoImage(file=r'/home/odaynasri/Schreibtisch/IT/Dateneingaben/Images\Logo2.png')
logo_widget = tk.Label(frame, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

#--Benutzereingabe--
benutzer_frame = tk.LabelFrame(
    master=frame,
    text='Dateneingabe',
    bg=bg_color,
    fg='pink',
    font=('TkMenuFont', 14)
)
benutzer_frame.pack()

tk.Label(benutzer_frame, text='Vorname', bg=bg_color, fg='white').grid(row=0, column=0)
tk.Label(benutzer_frame, text='Nachname', bg=bg_color, fg='white').grid(row=0, column=1)

vorname_entry = tk.Entry(benutzer_frame)
vorname_entry.grid(row=1, column=0)

nachname_entry = tk.Entry(benutzer_frame)
nachname_entry.grid(row=1, column=1)

tk.Label(benutzer_frame, text='Arbeitsposition', bg=bg_color, fg='white').grid(row=0, column=2)
titel_combobox = ttk.Combobox(benutzer_frame, values=[
    'Manager', 'Verwaltung', 'Abteilungsleiter', 'Production', 'Versandabteilung', 'Rechnungsabteilung',
    'Montage', 'Putzabteilung', 'Kundenservice', 'Scadensabteilung'
])
titel_combobox.grid(row=1, column=2)

tk.Label(benutzer_frame, text='Einstellungsdatum', bg=bg_color, fg='white').grid(row=2, column=0)
datum_var = tk.StringVar(value='TT.MM.JJJJ')
datum_entry = ttk.Entry(benutzer_frame, textvariable=datum_var)
datum_entry.grid(row=3, column=0)

tk.Label(benutzer_frame, text='Nationalität', bg=bg_color, fg='white').grid(row=2, column=2)
natio_combobox = ttk.Combobox(benutzer_frame, values=[
    'afghanisch', 'ägyptisch', 'albanisch', 'algerisch', 'amerikanisch', 'britisch',
    'bulgarisch', 'deutsch', 'französisch', 'indonesisch', 'irisch', 'iseralisch',
    'italienisch', 'japanisch', 'libanesisch', 'mexikanisch', 'österreichisch',
    'schweizerisch', 'spanisch', 'südafrikanisch', 'syrisch', 'türkisch', 'ukrainisch',
])
natio_combobox.grid(row=3, column=2)

#--Kalender Klasse--
class Openkalender:
    def __init__(self, root):
        self.root = root
        self.datum_button = tk.Button(root, text='Kalender öffnen', bg=bg_color, fg='white', command=self.open_kalender)
        self.datum_button.grid(row=3, column=1, padx=10)

    def open_kalender(self):
        kalender_popup = tk.Toplevel(self.root)
        kalender_popup.title('Datum auswählen')

        kalender = Calendar(kalender_popup, selectmode='day', bg=bg_color, fg='white', date_pattern='dd.mm.yyyy')
        kalender.pack()

        def datum_bestätigen():
            datum_auswählen = kalender.get_date()
            datum_var.set(datum_auswählen)
            kalender_popup.destroy()

        d_bestätigen = tk.Button(kalender_popup, text='Datum bestätigen', command=datum_bestätigen)
        d_bestätigen.pack()

Openkalender(benutzer_frame)

#--Mitarbeiter speichern--
def mitarbeiter_speichern():
    mitarbeiter = Mitarbeiter(
        vorname_entry.get(),
        nachname_entry.get(),
        titel_combobox.get(),
        datum_var.get(),
        natio_combobox.get()
    )
    ausgabe_label.config(text=str(mitarbeiter))
    print('Mitarbeiter gespeichert', mitarbeiter)

speichern_button= tk.Button(benutzer_frame, text='Mitarbeiter speichern', command=mitarbeiter_speichern, bg='green', fg='white')
speichern_button.grid(row=5, column=1, pady=20)

ausgabe_label= tk.Label(benutzer_frame, text='', bg=bg_color, fg='white', justify='left')
ausgabe_label.grid(row=6, column= 0, columnspan=3)

window.mainloop()