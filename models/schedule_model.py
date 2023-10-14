from database.database import SQLiteDatabase


class ScheduleModel(SQLiteDatabase):
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        super().__init__(db_name)
        self.table = "schedule"

    def insert_schedule(
        self,
        section_id,
        course_id,
        day_id,
        instructor_id,
        laboratory_id,
        time_start,
        time_end,
    ):
        data = {
            "section_id": section_id,
            "course_id": course_id,
            "day_id": day_id,
            "instructor_id": instructor_id,
            "laboratory_id": laboratory_id,
            "time_start": time_start,
            "time_end": time_end,
        }
        self.insert_data(self.table, data)

    def all(self, columns=None):
        return self.select_data(self.table, columns=columns)

    def get_schedule_by_section(self, section, columns=None):
        return self.select_data(
            self.table, condition=f"section_id='{section}'", columns=columns
        )

    def get_schedule_by_laboratory(self, laboratory, columns=None):
        return self.select_data(
            self.table, condition=f"laboratory_id='{laboratory}'", columns=columns
        )

    def truncate(self):
        query = f"DELETE FROM {self.table}"
        self.cursor.execute(query)
