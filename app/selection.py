import tkinter as tk
from tkinter import ttk
from csp.implementation import SchedulingProblem
from models.course_model import CourseModel
from models.instructor_model import InstructorModel
from models.laboratory_model import LaboratoryModel
from models.section_model import SectionModel


class SelectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Selection")
        root.geometry("1250x850")

        # Program Dropdown
        self.label_program = tk.Label(self.root, text="Select Program:")
        self.label_program.pack()
        self.program_options = ["BSCS", "BSIT", "BLIS", "BSIS"]
        self.program_var = tk.StringVar()
        self.dropdown_program = ttk.Combobox(
            self.root, textvariable=self.program_var, values=self.program_options
        )
        self.dropdown_program.pack()

        # Year Dropdown
        self.label_year = tk.Label(self.root, text="Select Year:")
        self.label_year.pack()
        self.year_options = ["1", "2", "3", "4"]
        self.year_var = tk.StringVar()
        self.dropdown_year = ttk.Combobox(
            self.root, textvariable=self.year_var, values=self.year_options
        )
        self.dropdown_year.pack()

        # Course Dropdown
        self.label_course = tk.Label(self.root, text="Select Course:")
        self.label_course.pack()
        self.course_options = [
            "Introduction to Computing",
            "Data Structures and Algorithms",
            "Advanced Database Systems",
            "Multimedia Systems",
        ]
        self.course_var = tk.StringVar()
        self.dropdown_course = ttk.Combobox(
            self.root, textvariable=self.course_var, values=self.course_options
        )
        self.dropdown_course.pack()

        self.label_section = tk.Label(self.root, text="Select section:")
        self.label_section.pack()
        self.section_options = [section for section in SectionModel().all()]
        self.section_var = tk.StringVar()
        self.dropdown_section = ttk.Combobox(
            self.root, textvariable=self.section_var, values=self.section_options
        )
        self.dropdown_section.pack()

        # Instructor Dropdown
        self.label_instructor = tk.Label(
            self.root, text="Select Instructor (Optional):"
        )
        self.label_instructor.pack()
        self.instructor_var = tk.StringVar()
        self.dropdown_instructor = ttk.Combobox(
            self.root, textvariable=self.instructor_var
        )
        self.dropdown_instructor.pack()

        # Lab Dropdown
        self.label_lab = tk.Label(self.root, text="Select Lab (Optional):")
        self.label_lab.pack()
        self.lab_options = [lab[1] for lab in LaboratoryModel().all()]
        self.lab_var = tk.StringVar()
        self.dropdown_lab = ttk.Combobox(
            self.root, textvariable=self.lab_var, values=self.lab_options
        )
        self.dropdown_lab.pack()

        # Lab Dropdown
        self.label_time = tk.Label(self.root, text="Select Time (Optional):")
        self.label_time.pack()
        self.time_options = [
            "Monday 7:00 am",
            "Monday 8:00 am",
            "Monday 9:00 am",
            "Monday 10:00 am",
            "Monday 11:00 am",
            "Monday 12:00 pm",
            "Monday 1:00 pm",
            "Monday 2:00 pm",
            "Monday 3:00 pm",
            "Monday 4:00 pm",
            "Monday 5:00 pm",
            "Monday 6:00 pm",
            "Monday 7:00 pm",
            "Tuesday 7:00 am",
            "Tuesday 8:00 am",
            "Tuesday 9:00 am",
            "Tuesday 10:00 am",
            "Tuesday 11:00 am",
            "Tuesday 12:00 pm",
            "Tuesday 1:00 pm",
            "Tuesday 2:00 pm",
            "Tuesday 3:00 pm",
            "Tuesday 4:00 pm",
            "Tuesday 5:00 pm",
            "Tuesday 6:00 pm",
            "Tuesday 7:00 pm",
            "Wednesday 7:00 am",
            "Wednesday 8:00 am",
            "Wednesday 9:00 am",
            "Wednesday 10:00 am",
            "Wednesday 11:00 am",
            "Wednesday 12:00 pm",
            "Wednesday 1:00 pm",
            "Wednesday 2:00 pm",
            "Wednesday 3:00 pm",
            "Wednesday 4:00 pm",
            "Wednesday 5:00 pm",
            "Wednesday 6:00 pm",
            "Wednesday 7:00 pm",
            "Thursday 7:00 am",
            "Thursday 8:00 am",
            "Thursday 9:00 am",
            "Thursday 10:00 am",
            "Thursday 11:00 am",
            "Thursday 12:00 pm",
            "Thursday 1:00 pm",
            "Thursday 2:00 pm",
            "Thursday 3:00 pm",
            "Thursday 4:00 pm",
            "Thursday 5:00 pm",
            "Thursday 6:00 pm",
            "Thursday 7:00 pm",
            "Friday 7:00 am",
            "Friday 8:00 am",
            "Friday 9:00 am",
            "Friday 10:00 am",
            "Friday 11:00 am",
            "Friday 12:00 pm",
            "Friday 1:00 pm",
            "Friday 2:00 pm",
            "Friday 3:00 pm",
            "Friday 4:00 pm",
            "Friday 5:00 pm",
            "Friday 6:00 pm",
            "Friday 7:00 pm",
            "Saturday 7:00 am",
            "Saturday 8:00 am",
            "Saturday 9:00 am",
            "Saturday 10:00 am",
            "Saturday 11:00 am",
            "Saturday 12:00 pm",
            "Saturday 1:00 pm",
            "Saturday 2:00 pm",
            "Saturday 3:00 pm",
            "Saturday 4:00 pm",
            "Saturday 5:00 pm",
            "Saturday 6:00 pm",
            "Saturday 7:00 pm",
        ]
        self.time_var = tk.StringVar()
        self.dropdown_time = ttk.Combobox(
            self.root, textvariable=self.time_var, values=self.time_options
        )
        self.dropdown_time.pack()

        # Button to Print Selections
        self.btn_submit = tk.Button(
            self.root, text="Schedule Course", command=self.add_schedule
        )
        self.btn_submit.pack()

        # Set up trace on year and program variables to update course options
        self.year_var.trace("w", self.update_course_options)
        self.program_var.trace("w", self.update_course_options)
        self.course_var.trace("w", self.update_instructor_options)

    def update_course_options(self, *args):
        selected_year = self.year_var.get()
        selected_program = self.program_var.get()
        if not selected_year or not selected_program:
            return
        course_model = CourseModel()

        courses = course_model.select_data(
            course_model.table,
            condition=f"year_id = {selected_year} AND program_id = '{selected_program.lower()}'",
        )

        data = list(map(lambda course: course[3], courses))

        # Update course dropdown options
        self.dropdown_course["values"] = data

    def update_instructor_options(self, *args):
        selected_course = self.course_var.get()
        if not selected_course:
            return

        instructor_model = InstructorModel()

        instructors = instructor_model.select_data(
            instructor_model.table,
            condition=f"expertise = '{selected_course}'",
        )

        # Extract instructor names from the result
        data = list(map(lambda instructor: instructor[2], instructors))

        # Update instructor dropdown options
        self.dropdown_instructor["values"] = data

    def add_schedule(self):
        selected_year = self.year_var.get()
        selected_program = self.program_var.get()
        selected_course = self.course_var.get()
        selected_section = self.section_var.get()
        selected_instructor = self.instructor_var.get()
        selected_laboratory = self.lab_var.get()
        selected_time = self.time_var.get()
        solutions = SchedulingProblem(
            selected_year,
            selected_program,
            selected_course,
            selected_section,
            selected_instructor,
            selected_laboratory,
            selected_time,
        ).solve()

        for i in solutions:
            print(i)
