import sqlite3

# SQLite 파일에 QUERY 동작
def SQLite_UPDATE(PATH, QUERY):
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.execute(QUERY)
    connection.commit()