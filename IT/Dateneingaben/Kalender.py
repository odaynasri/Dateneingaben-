import tkinter as tk
from tkcalendar import Calendar
from tkinter import simpledialog

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Date Picker")

        # Label to display the selected date
        self.label = tk.Label(root, text="Selected Date: Not picked yet", font=("Arial", 14))
        self.label.pack(pady=10)

        # Button to trigger the calendar pop-up
        self.select_button = tk.Button(root, text="Select Date", command=self.open_calendar)
        self.select_button.pack(pady=10)

    def open_calendar(self):
        # Create a pop-up window
        calendar_popup = tk.Toplevel(self.root)
        calendar_popup.title("Select Date")

        # Create a calendar widget
        calendar = Calendar(calendar_popup, selectmode='day', date_pattern='yyyy-mm-dd')
        calendar.pack(pady=20)

        # Function to get the selected date and update the label
        def set_date():
            selected_date = calendar.get_date()  # Get the selected date from the calendar
            self.label.config(text=f"Selected Date: {selected_date}")
            calendar_popup.destroy()  # Close the calendar pop-up

        # Button to confirm the date selection
        confirm_button = tk.Button(calendar_popup, text="Confirm Date", command=set_date)
        confirm_button.pack(pady=10)

# Create the Tkinter main window
root = tk.Tk()
root.geometry('600x400')
app = CalendarApp(root)
root.mainloop()
