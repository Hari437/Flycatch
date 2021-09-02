#! /usr/bin/env python
import pyodbc, sqlite3
from contextlib import contextmanager
from pandas import read_csv, DataFrame

CSV_FILE = "myFile0.csv"
DB_NAME = "db.sqlite3"
TABLE_NAME = "peoples_people"

@contextmanager
def get_sqlite_conn(db):
    # conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=sqlite.db")
    conn = sqlite3.connect(db)
    try:
        yield conn
    finally:
        conn.close()

def create_table(db, table_name):
    with get_sqlite_conn(db) as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS %s (
                id integer PRIMARY KEY,
                firstname TEXT,
                lastname TEXT,
                email TEXT,
                profession TEXT
            );""" % table_name)

def convert_csv_to_df(csv_file, coloumns):
    data = read_csv(csv_file)
    df = DataFrame(data, columns=coloumns)
    print(df)
    return df

def main():
    create_table(DB_NAME, TABLE_NAME)
    df = convert_csv_to_df(CSV_FILE, ['id', 'firstname', 'lastname', 'email', 'profession'])
    insert_query = "INSERT INTO %s (id,first_name,last_name,email,profession) VALUES (?,?,?,?,?)" %TABLE_NAME
    with get_sqlite_conn(DB_NAME) as conn:
        cur = conn.cursor()
        cur.executemany(insert_query, df.itertuples(index=False))
        conn.commit()


if __name__ == "__main__":
    main()

