import sqlite3
from sqlite3 import Error


# creating connection
def sql_connection():
    try:
        db = sqlite3.connect('mytest.db')
        return db
    except Error:
        print(Error)


# create table employees
def create_table(con):
    try:
        cur = con.cursor()
        cur.execute('''CREATE TABLE employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        department TEXT,
        position TEXT,
        salary REAL,
        date TEXT);''')
        con.commit()
        print('The table is created successfully')
    except Error:
        print(Error)


# insert data to table
def insert_data(con, entities):
    query = """INSERT INTO employees (id, name, surname, department, position,
            salary, date) VALUES(?,?,?,?,?,?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Error:
        print(Error)


def add_data(con):
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO employees VALUES(2, 'David', 'Anderson', 'IT', 'Dev', 3000, '2020-06-01')")
        cur.execute("INSERT INTO employees VALUES(3, 'Tom', 'Roger', 'IT', 'Manager', 3000, '2018-03-02')")
        cur.execute("INSERT INTO employees VALUES(4, 'Alan', 'Meyer', 'IT', 'Dev', 5000, '2019-04-15')")
        con.commit()
        print("The records added successfully")
    except Error:
        print(Error)


# read data
def fetch(con):
    cur = con.cursor()
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    for row in rows:
        print(row)


# update a record
def update(con, salary, id):
    try:
        cur = con.cursor()
        cur.execute("UPDATE employees SET salary = ?  WHERE id = ?", (salary, id))
        con.commit()
        print("The record updated successfully")
    except Error:
        print(Error)


# delate a record
def delate(con, surname):
    query = "DELETE FROM employees WHERE surname = ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (surname,))
        con.commit()
        print("The record delated successfully")
    except Error:
        print(Error)


def main():
    con = sql_connection()
    create_table(con)
    entities = (1, 'Anna', 'Smith', 'IT', 'Dev', 2000, '2020-02-09')
    insert_data(con, entities)
    add_data(con)
    fetch(con)
    update(con, 3000, 1)
    delate(con, "Roger")
    con.close()


if __name__ == "__main__":
    main()
