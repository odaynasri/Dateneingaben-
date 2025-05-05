import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import sqlite3
import os


window = tk.Tk()
window.title('Dateneingaben')
window.eval('tk::PlaceWindow . center')


window.geometry('600x500')
window.configure(background='#A1CDEC')

frame = tk.Frame(window)
frame.pack()

benuzter_info_frame = tk.LabelFrame(master= frame, text= 'Benuterinformationen')
benuzter_info_frame.grid(row= 0, column= 0, padx= 20, pady= 20)

tk.Label(master= benuzter_info_frame, text= 'Vorname').grid(row= 0, column= 0)
tk.Label(master= benuzter_info_frame, text= 'Nachname').grid(row= 0, column= 1)

vorname_entry = tk.Entry(master= benuzter_info_frame)
vorname_entry.grid(row = 1, column = 0)

nachname_entry = tk.Entry(master= benuzter_info_frame)
nachname_entry.grid(row = 1, column = 1)

tk.Label(master= benuzter_info_frame, text= 'Titel').grid(row= 0, column= 2)
titel_combobox = ttk.Combobox(master= benuzter_info_frame, values=['', 'Dr.', 'Ms.', 'Mr.', 'Mrs.'])
titel_combobox.grid(row = 1, column= 2)

tk.Label(master= benuzter_info_frame, text= 'Geburtsdatum').grid(row= 2, column= 0)
geburtsdatum_var = tk.StringVar(value= 'TT.MM.JJJJ')
geburtsdatum_entry = ttk.Entry(master= benuzter_info_frame, textvariable= geburtsdatum_var)
geburtsdatum_entry.grid(row= 3, column= 0)

tk.Label(master= benuzter_info_frame, text= 'Nationalität').grid(row= 2, column = 1)
nationalität_combobox = ttk.Combobox(master= benuzter_info_frame,
             values= ['afghanisch', 'ägyptisch', 'albanisch', 'algerisch', 'amerikanisch', 'britisch',
                      'bulgarisch', 'deutsch', 'französisch','indonesisch', 'irisch', 'iseralisch',
                      'italienisch', 'japanisch', 'libanesisch', 'mexikanisch', 'österreichisch',
                      'schweizerisch', 'spanisch', 'südafrikanisch', 'syrisch', 'türkisch',
                      'ukrainisch',
                      ]
             )
nationalität_combobox.grid(row= 3, column= 1)

tk.Label(master= benuzter_info_frame, text= 'Geburtsort').grid(row= 2, column= 2)
geburtsort_entry = ttk.Entry(master= benuzter_info_frame)
geburtsort_entry.grid(row= 3, column= 2)

tk.Label(master= benuzter_info_frame, text= 'E-mail')
email_var = tk.StringVar(value= "'e-mail-adresse@gxx.cxm'")
email_entry = ttk.Entry(master=benuzter_info_frame, textvariable= email_var, font= 0)
email_entry.grid(row= 4, column= 0)




window.mainloop()