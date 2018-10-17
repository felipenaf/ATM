from connection import Connection
from pessoaFisica import PessoaFisica

CON = Connection().instance()
CURSOR = CON.cursor()

P = PessoaFisica('402.149.696-55', 'Chelas', 29)
cpf = P.cpf
nome = P.nome
idade = P.idade

query = "INSERT INTO pessoaFisica (cpf, nome, idade) VALUES (%s, %s, %s);"
info = (P.cpf, P.nome, P.idade)

# CURSOR.execute("DROP TABLE pessoaFisica;")
# CURSOR.execute("CREATE TABLE pessoaFisica(cpf VARCHAR(50) NOT NULL PRIMARY KEY, nome varchar(50), idade INT(5));")
CURSOR.execute(query, info)

CON.commit()

print(CURSOR.rowcount, "record inserted.")

CON.close()
