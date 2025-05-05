from tkinter import *
from tkcalendar import *

from main import benutzer_info_frame

window = Tk()
window.title('Kalender')
window.geometry('600x400')

kal = Calendar(window, selectmode= 'day', year= 2025, month= 4, day= 3)

def geburstag():
    mein_label.config(kal.get_date())

mein_button = Button(master= window, text= 'Geburstag', command= geburstag)
mein_button.pack(pady= 20)

mein_label = Label(master= benutzer_info_frame, text= 'TT.MM.JJJJ')
mein_label.pack(pady= 20)


window.mainloop()