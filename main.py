import tkinter as tk
from app.selection import SelectionGUI
from app.calendar import CalendarGUI
from csp.implementation import SchedulingProblem

from database import create_database_tables as db
from database.course_seeder import seed
from database.database import SQLiteDatabase
from database.instructor_seeder import seed as instructor_seeder
from database.laboratory_seeder import seed as lab_seeder
from database.section_seeder import seed as section_seeder
from models.schedule_model import ScheduleModel

if __name__ == "__main__":
    root = tk.Tk()
    db.create_table()
    # selection = SelectionGUI(root)
    root.geometry("1500x850")

    selection = CalendarGUI(root)
    seed()
    instructor_seeder()
    lab_seeder()
    section_seeder()

    root.mainloop()
