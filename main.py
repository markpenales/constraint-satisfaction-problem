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
    # ScheduleModel().insert_schedule(
    #     "BSIT 3D",
    #     "Networking 1",
    #     "1",
    #     "Ray T. Cortez",
    #     "Acad 1 - 103",
    #     "Monday 12:00 pm",
    #     "Monday 2:00 pm",
    # )
    db.create_table()

    seed()
    instructor_seeder()
    lab_seeder()
    section_seeder()
    SchedulingProblem(
        1,
        "BSIT",
        "Networking 1",
        "BSIT 1D",
        # laboratory="Room 1",
        # time="Monday 10:00 am",
    ).solve()

    # root = tk.Tk()
    # # selection = SelectionGUI(root)
    # root.geometry("1500x850")

    # selection = CalendarGUI(root)

    # root.mainloop()
