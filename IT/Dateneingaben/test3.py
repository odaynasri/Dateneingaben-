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

#logo_img = ImageTk.PhotoImage(file= r'C:\Users\NasriOday\Desktop\Dateneingaben\Images\Logo2.png')
logo_img = ImageTk.PhotoImage(file= r'D:\IT\Dateneingaben\Images\Logo2.png')
logo_widget = tk.Label(frame, image= logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

benutzer_frame = tk.LabelFrame(
                                    master= frame,
                                    text= 'Benutzerinformationen',
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

tk.Label(benutzer_frame, text= 'Titel', bg=bg_color, fg='white').grid(row=0, column=2)
titel_combobox = ttk.Combobox(benutzer_frame, values=['', 'Dr.', 'Mr.', 'Ms.', 'Mrs.'])
titel_combobox.grid(row=1, column=2)

tk.Label(benutzer_frame, text= 'Geburtsdatum', bg=bg_color, fg='white').grid(row=2, column=0)
geburtsdatum_var = tk.StringVar(value='TT.MM.JJJJ')
geburtsdatum_entry = ttk.Entry(benutzer_frame, textvariable=geburtsdatum_var)
geburtsdatum_entry.grid(row=3, column=0)

tk.Label(benutzer_frame, text='Nationalität', bg=bg_color, fg='white').grid(row=2, column=1)
natio_combobox = ttk.Combobox(benutzer_frame, values= ['afghanisch', 'ägyptisch', 'albanisch', 'algerisch', 'amerikanisch', 'britisch',
                      'bulgarisch', 'deutsch', 'französisch','indonesisch', 'irisch', 'iseralisch',
                      'italienisch', 'japanisch', 'libanesisch', 'mexikanisch', 'österreichisch',
                      'schweizerisch', 'spanisch', 'südafrikanisch', 'syrisch', 'türkisch',
                      'ukrainisch',
                      ]
             )
natio_combobox.grid(row=3, column=1)

tk.Label(benutzer_frame, text='Geburtsort', bg=bg_color, fg='white').grid(row=2, column=2)
ort_label = ttk.Entry(benutzer_frame)
ort_label.grid(row=3, column=2)


window.mainloop()