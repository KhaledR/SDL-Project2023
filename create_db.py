import sqlite3
def create_db():
    conn = sqlite3.connect(database = r"billsystem.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Gender text, Contact text, DoB text, DoJ text, Pass text, UserType text, Address text, Salary text)")
    conn.commit
create_db()