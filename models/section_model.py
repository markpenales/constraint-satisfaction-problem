from database.database import SQLiteDatabase


class SectionModel(SQLiteDatabase):
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        super().__init__(db_name)
        self.table = "section"

    def insert_section(self, program, year, section):
        data = {"program_id": program, "year_id": year, "section_name_id": section}
        self.insert_data(self.table, data)

    def all(self):
        query = f"SELECT DISTINCT section_name_id FROM {self.table}"

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.commit_and_close()

        return result

    def sections(self):
        query = f"SELECT program_id, year_id, section_name_id FROM {self.table}"

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def truncate(self):
        query = f"DELETE FROM {self.table}"
        self.cursor.execute(query)
