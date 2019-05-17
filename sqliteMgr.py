import sqlite3

def create_db(database):
    connection = sqlite3.connect(database)


def create_table(dataBase, tabla):
    cadena = "CREATE TABLE " + tabla + "( t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, device TEXT NOT NULL, timestamp TEXT NOT NULL, value INTEGER NULL )"
    print(cadena)
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cursor.execute(cadena)
    connection.commit()


def delete_table(dataBase, tabla):
    cadena = "DROP TABLE " + tabla
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cursor.execute(cadena)
    print(cadena)
    connection.commit()


def query_db(dataBase, tabla, campo, valor):
    cursor = ""
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cadena = "SELECT * FROM " + tabla + " WHERE " + campo + " = '" + valor + "'"
    cursor.execute(cadena)
    rows = cursor.fetchall()
    return(rows)

def insert_db(dataBase, tabla, device, tiempo, valor):
    cursor = ""
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    par1 = "INSERT INTO temp ( device, timestamp, value ) VALUES"
    par2 = " ( '" + str(device) + "', '" + str(tiempo) + "', " + str(valor) + " )"
    cadena = par1 + par2
    cursor.execute(cadena)
    connection.commit()
