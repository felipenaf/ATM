from connection import Connection

CON = Connection().instance()

CURSOR = CON.cursor()

# cursor.execute("DROP TABLE employees;")
# cursor.execute("CREATE TABLE employees(nome varchar(50));")

CON.close()
