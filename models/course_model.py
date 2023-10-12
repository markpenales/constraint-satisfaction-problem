from database.database import SQLiteDatabase


class CourseModel(SQLiteDatabase):
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        super().__init__(db_name)
        self.table = "course"

    def insert_course(self, name, units, year, program) -> None:
        data = {"name": name, "units": units, "program_id": program, "year_id": year}
        self.insert_data("course", data)

    def seed_courses(self, course_data):
        for program, years in course_data.items():
            for year, courses in years.items():
                for course_name, units in courses.items():
                    # Insert course into the database
                    self.insert_course(course_name, units, year, program)

        self.commit_and_close()

    def all(self):
        return self.select_data(self.table)

    def truncate(self):
        query = f"DELETE FROM {self.table}"

        self.cursor.execute(query)
