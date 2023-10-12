import sqlite3


class SQLiteDatabase:
    def __init__(self, db_name: str = "scheduling_system.sqlite"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns, foreign_keys) -> None:
        # Create the table
        columns_str = ", ".join(
            [f"{col} {data_type}" for col, data_type in columns.items()]
        )
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str}"

        # Add foreign key constraints if specified
        if foreign_keys:
            for column_name, referenced_table, referenced_column in foreign_keys:
                create_table_query += (
                    f", FOREIGN KEY ({column_name}) "
                    f"REFERENCES {referenced_table}({referenced_column})"
                )

        create_table_query += ");"

        self.cursor.execute(create_table_query)

    def insert_data(self, table_name, data):
        # data is a dictionary where keys are column names and values are data values
        columns_str = ", ".join(data.keys())
        values_str = ", ".join(
            [
                f'"{value}"' if isinstance(value, str) else str(value)
                for value in data.values()
            ]
        )
        insert_data_query = (
            f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
        )

        print(f"Query: {insert_data_query}")
        self.cursor.execute(insert_data_query)
        self.commit_and_close()

    def select_data(self, table_name, columns=None, condition=None):
        columns_str = "*"
        if columns:
            columns_str = ", ".join(columns)

        select_query = f"SELECT {columns_str} FROM {table_name}"
        if condition:
            select_query += f" WHERE {condition}"

        print(f"Query: {select_query}")

        self.cursor.execute(select_query)
        result = self.cursor.fetchall()
        self.commit_and_close()
        return result

    def commit_and_close(self):
        self.conn.commit()
