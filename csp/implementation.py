from constraint import *
from models.laboratory_model import LaboratoryModel

from models.schedule_model import ScheduleModel


class SchedulingProblem:
    def __init__(
        self,
        year,
        program,
        course,
        section,
        instructor,
        laboratory,
        time,
    ):
        self.problem = Problem()
        self.year = year
        self.program = program
        self.course = course
        self.section = section
        self.instructor = instructor
        self.laboratory = laboratory
        self.time = time
        self.timeslots = [
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

    def solve(self):
        schedule_model = ScheduleModel()
        lab_model = LaboratoryModel()
        section_schedules = schedule_model.get_schedule_by_section(self.section)
        for schedule in section_schedules:
            if self.course == schedule[2]:
                return "Schedule was already set for this section. Please find another course"
        labs = [laboratory[1] for laboratory in lab_model.all()]
        self.problem.addVariable("laboratory", labs)
        self.problem.addVariable("time", self.timeslots)

        # Add constraints
        self.problem.addConstraint(
            self.laboratory_and_time_constraint, ("laboratory", "time")
        )
        # self.problem.addConstraint(self.section_time_constraint, "time")

        # Solve the problem
        solutions = self.problem.getSolutions()
        print("Solutions: ")
        # Print solutions
        return solutions

    def laboratory_and_time_constraint(self, laboratory, time):
        schedule_model = ScheduleModel()
        existing_schedules = schedule_model.get_schedule_by_laboratory(laboratory)

        slots = self.timeslots.copy()
        for schedule in existing_schedules:
            try:
                end_index = slots.index(schedule[7])
                start_index = slots.index(schedule[6])
                slots = slots[end_index:]
            except ValueError:
                continue

        existing_schedules_section = schedule_model.get_schedule_by_section(
            self.section
        )

        for schedule in existing_schedules_section:
            try:
                end_index = slots.index(schedule[7])
                start_index = slots.index(schedule[6])
                slots = slots[end_index:]
            except ValueError:
                continue
        if self.laboratory == "" and time in slots:
            return True
        if time in slots and laboratory == self.laboratory:
            return True

        return False
