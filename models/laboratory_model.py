from database.database import SQLiteDatabase


class LaboratoryModel(SQLiteDatabase):
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        super().__init__(db_name)
        self.table = "laboratory"

    def insert_laboratory(self, name, courses=None):
        data = {"name": name, "courses": courses if courses is not None else []}
        self.insert_data(self.table, data)

    def all(self):
        return self.select_data(self.table)

    def truncate(self):
        query = f"DELETE FROM {self.table}"
        self.cursor.execute(query)
