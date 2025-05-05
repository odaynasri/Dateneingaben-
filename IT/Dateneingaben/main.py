import tkinter
from tkinter import ttk, Label
from tkinter.constants import BROWSE
from tkinter import *
from tkcalendar import *
from tkinter import ttk
import ttkbootstrap

window = tkinter.Tk()
window.title('Dateneingaben')
window.geometry('600x300')
window.configure(background= '#A1CDEC')

frame = tkinter.Frame(master= window)
frame.pack()

# Benutzerinformationen
benutzer_info_frame = tkinter.LabelFrame(master= frame, text= 'Benutzerinformationen')
benutzer_info_frame.grid(row= 0, column= 0, padx= 20, pady= 20)

vorname_label = tkinter.Label(master= benutzer_info_frame, text= 'Vorname')
vorname_label.grid(row= 0, column= 0)

nachname_label = tkinter.Label(master= benutzer_info_frame, text= 'Nachname')
nachname_label.grid(row= 0, column= 1)

vorname_entry = tkinter.Entry(master= benutzer_info_frame)
vorname_entry.grid(row= 1, column= 0)

nachname_entry = tkinter.Entry(master= benutzer_info_frame)
nachname_entry.grid(row=1, column= 1)

titel_lebel = tkinter.Label(master= benutzer_info_frame, text= 'Titel')
titel_lebel.grid(row= 0, column= 2)

titel_combobox = ttk.Combobox(master= benutzer_info_frame, values=['', 'Dr.', 'Mr.', 'Ms.', 'Mrs.'])
titel_combobox.grid(row= 1, column= 2)

alt_label = tkinter.Label(master= benutzer_info_frame, text= 'Geburtsdatum')
alt_label.grid(row= 2, column= 0)

class KalenderApp:
    def __init__(self, window):
        self.window = window

        self.button = tkinter.Button(window, text= 'Geburstag eingeben', command= self.offen_kalender)

    def offen_kalender(self):
        kalender_popup = tkinter.Toplevel(self.window)
        kalender_popup.title('Datum auswählen')

        kalender = Calendar(kalender_popup, selectmode= 'day', date_pattern= 'TT.MM.JJJJ')
        kalender.grid(row= 3, column= 0)

    def einstellen_des_Datums(self):
        neue_Datum = kalender.get_date()
        kalender_popup.destroy()



alt_entey_var = tkinter.StringVar(value= 'TT.MM.JJJJ')
alt_entry = tkinter.Entry(master= benutzer_info_frame, textvariable= alt_entey_var)
alt_entry.grid(row= 3, column= 0)


window.mainloop()