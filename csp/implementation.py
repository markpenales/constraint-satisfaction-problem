from constraint import *
from models.laboratory_model import LaboratoryModel

from models.schedule_model import ScheduleModel

from datetime import datetime


class SchedulingProblem:
    def __init__(
        self,
        year,
        program,
        course,
        section,
        instructor=None,
        laboratory=None,
        time=None,
        day=None,
    ):
        self.problem = Problem(BacktrackingSolver())
        self.year = year
        self.program = program
        self.course = course
        self.section = section

        # These constraints are hard constraints if they are defined
        self.laboratory = laboratory
        self.time = time
        self.day = day
        self.instructor = instructor

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

        labs = [laboratory[1] for laboratory in lab_model.all()]

        self.problem.addVariable("laboratory", labs)
        self.problem.addVariable("timeslot", self.timeslots)

        self.problem.addConstraint(self.laboratory_constraint, ["laboratory"])
        self.problem.addConstraint(self.time_constraint, ["timeslot"])

        solutions = self.problem.getSolutions()

        for solution in solutions:
            print(solution)
        return solutions

    def laboratory_constraint(self, laboratory):
        if self.laboratory is None:
            return True
        return self.laboratory == laboratory

    def time_constraint(self, timeslot):
        schedules = ScheduleModel().all(
            columns=[
                "day_id",
                "time_start",
                "time_end",
            ]
        )
        time = self.get_time(timeslot)

        for schedule in schedules:
            start = self.get_time(schedule[1])
            end = self.get_time(schedule[2])
            if (
                time >= start
                and time < end
                and timeslot.split(" ")[0] == schedule[1].split(" ")[0]
            ):
                return False

        return True

    def get_time(self, time):
        time_format = "%I:%M %p"
        time_arr = time.split(" ")
        time_arr.pop(0)
        time = " ".join(time_arr)
        value = datetime.strptime(time, time_format).time()

        return value
