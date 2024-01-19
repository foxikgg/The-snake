import os
import sqlite3
from sqlite3 import Error


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), self.db_name))
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_table(self, table_name):
        try:
            sql = f'''CREATE TABLE {table_name} (
                                attempt_number integer,
                                attempt_date text,
                                attempt_time text,
                                score integer
                            ); '''
            c = self.conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def add_data(self, table_name, attempt_number, attempt_date, attempt_time, score):
        c = self.conn.cursor()
        values = (attempt_number, attempt_date, attempt_time, score)
        c.execute(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?)", values)
        self.conn.commit()

    def print_table(self, table_name):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {table_name}")
        rows = c.fetchall()
        print(f"Содержимое таблицы {table_name}:")
        for row in rows:
            print(row)


def add_data_start():
    db = DatabaseManager('game-snake.db')
    db.create_connection()
    db.create_table("level1")
    db.create_table("level2")
    db.create_table("level3")

    while True:
        table_name = input("Введите уровень (level1, level2, level3) или 'q' для выхода: ")
        if table_name == 'q':
            break
        attempt_number = input("Введите номер попытки: ")
        attempt_date = input("Введите дату попытки (в формате ГГГГ-ММ-ДД): ")
        attempt_time = input("Введите время попытки (в формате ЧЧ:ММ:СС): ")
        score = input("Введите количество очков: ")
        db.add_data(table_name, attempt_number, attempt_date, attempt_time, score)
        db.print_table(table_name)


if __name__ == '__main__':
    add_data_start()
