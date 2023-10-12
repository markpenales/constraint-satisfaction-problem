from database.database import SQLiteDatabase


class InstructorModel(SQLiteDatabase):
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        super().__init__(db_name)
        self.table = "instructor"

    def insert_instructor(self, title, name, courses):
        # Insert instructor into the instructor table
        for course in courses:
            data = {"title": title, "name": name, "expertise": course}
            instructor_id = self.insert_data(self.table, data)

    def all(self):
        return self.select_data(self.table)

    def truncate(self):
        query = f"DELETE FROM {self.table}"
        self.cursor.execute(query)
