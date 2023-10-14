import calendar
import tkinter as tk
from tkinter import ttk


import tkinter as tk
from tkinter import ttk

from app.selection import SelectionGUI
from models.schedule_model import ScheduleModel
from models.section_model import SectionModel


class CalendarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weekly Schedule")

        # Days of the week
        self.days_of_week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        # Time slots
        self.time_slots = [
            "7:00 AM",
            "8:00 AM",
            "9:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "1:00 PM",
            "2:00 PM",
            "3:00 PM",
            "4:00 PM",
            "5:00 PM",
            "6:00 PM",
        ]

        # Section Dropdown
        self.label_section_top = tk.Label(self.root, text="Select Section:")
        self.label_section_top.grid(row=0, column=len(self.days_of_week) + 2)
        self.section_options_top = [
            section for section in SectionModel().sections()
        ]  # Replace with your section options
        self.section_var_top = tk.StringVar()
        self.dropdown_section_top = ttk.Combobox(
            self.root,
            textvariable=self.section_var_top,
            values=self.section_options_top,
        )
        self.dropdown_section_top.grid(row=0, column=len(self.days_of_week) + 3)
        self.dropdown_section_top.set(
            self.section_options_top[12]
        )  # Set default selection

        # Row heights for time slots
        self.row_heights = [40] * len(self.time_slots)

        # Create labels for days of the week
        for day in self.days_of_week:
            label = tk.Label(
                root,
                text=day,
                padx=10,
                pady=5,
                borderwidth=2,
                relief="ridge",
                width=20,
                font=("Helvetica", 10, "bold"),
            )
            label.grid(row=0, column=self.days_of_week.index(day) + 1)

        # Create labels for time slots
        for i, time_slot in enumerate(self.time_slots):
            label = tk.Label(
                root,
                text=time_slot,
                padx=10,
                pady=5,
                borderwidth=2,
                relief="ridge",
                width=20,
                font=("Helvetica", 10, "bold"),
            )
            label.grid(row=i + 1, column=0, rowspan=1, sticky="nsew")

        # Create entry widgets for each cell
        self.entries = [
            [None for _ in range(len(self.days_of_week))]
            for _ in range(len(self.time_slots))
        ]
        # for i in range(len(self.time_slots)):
        #     for j in range(len(self.days_of_week)):

        # 7 Monday
        entry_7 = ttk.Entry(root, justify="center", font=("Helvetica", 10))
        entry_7.grid(row=1, column=1, ipadx=10, ipady=20, sticky="nsew")
        self.entries[1][1] = entry_7.insert(0, "7:00")

        # Adjust row heights
        for i, height in enumerate(self.row_heights):
            root.grid_rowconfigure(i + 1, minsize=height)

        # Button to go to SelectionGUI
        self.btn_goto_selection = tk.Button(
            root, text="Go to Course Selection", command=self.show_selection_gui
        )
        self.btn_goto_selection.grid(
            row=len(self.time_slots) + 2,
            column=0,
            columnspan=len(self.days_of_week) + 1,
        )

        # Event handler for section dropdown
        self.dropdown_section_top.bind("<<ComboboxSelected>>", self.on_section_select)

        # Store the selected section
        self.selected_section = None

    def on_section_select(self, event):
        self.selected_section = self.dropdown_section_top.get()
        sectionArr = self.selected_section.split(" ")
        section = sectionArr[0] + " " + sectionArr[1] + sectionArr[2]
        self.schedules = ScheduleModel().get_schedule_by_section(section)

    def show_selection_gui(self):
        selection_root = tk.Toplevel(self.root)
        selection_gui = SelectionGUI(selection_root)
