from database.database import SQLiteDatabase

tables = {
    "program_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
        "code": "TEXT",
    },
    "year_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "year": "INTEGER",
    },
    "section_name_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
    },
    "laboratory_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
    },
    "instructor_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT",
        "name": "TEXT",
        "expertise": "INTEGER",
    },
    "section_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "program_id": "INTEGER",
        "year_id": "INTEGER",
        "section_name_id": "INTEGER",
    },
    "course_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "program_id": "INTEGER",
        "year_id": "INTEGER",
        "name": "TEXT",
        "units": "INTEGER",
    },
    "day_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
    },
    "schedule_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "section_id": "INTEGER",
        "course_id": "INTEGER",
        "day_id": "INTEGER",
        "instructor_id": "INTEGER",
        "laboratory_id": "INTEGER",
        "time_start": "TEXT",
        "time_end": "TEXT",
    },
    "user_table": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "username": "TEXT",
        "password": "TEXT",
    },
}

foreign_keys = {
    "section_foreign_key": [
        ("program_id", "program", "id"),
        ("year_id", "year", "id"),
        ("section_name_id", "section_name", "id"),
    ],
    "course_foreign_key": [
        ("program_id", "program", "id"),
        ("year_id", "year", "id"),
    ],
    "schedule_foreign_key": [
        ("section_id", "section", "id"),
        ("course_id", "course", "id"),
        ("day_id", "day", "id"),
        ("instructor_id", "instructor", "id"),
        ("laboratory_id", "laboratory", "id"),
    ],
}


def create_table():
    db = SQLiteDatabase()

    print("Creating Tables...")

    for key in tables:
        table = key.split("_")
        table.pop()

        table_name = "_".join(table)
        db.create_table(
            table_name,
            tables[key],
            foreign_keys=foreign_keys.get(f"{table_name}_foreign_key"),
        )

    db.commit_and_close()
    print("Tables Created")
