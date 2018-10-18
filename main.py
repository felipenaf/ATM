from connection import Connection
from pessoaFisica import PessoaFisica
from contaCorrente import ContaCorrente
from login import Login

l = Login().validaLogin('1','123')

print(l)

if l == True:
    print('Boa garoto')
else:
    print('Taporra fudeu')

# CON = Connection.instance('felipe', '123')
# CURSOR = CON.cursor()

# p = PessoaFisica()
# p.setCpf('123.456.789-10')
# p.setNome('pedro')
# p.setIdade(25)

# print(p.getCpf())
# print(p.getNome())
# print(p.getIdade())

# p.depositar(5)
# p.sacar(2)
# print(p.getSaldo())

# cc = ContaCorrente()
# print (cc.getSaldo())

# query = "INSERT INTO pessoaFisica (cpf, nome, idade) VALUES (%s, %s, %s);"
# info = (P.cpf, P.nome, P.idade)

# CURSOR.execute("DROP TABLE pessoaFisica;")

# CURSOR.execute(
#     "CREATE TABLE pessoaFisica("
#     "cpf VARCHAR(50) NOT NULL PRIMARY KEY,"
#     "nome varchar(50),"
#     "idade INT(5)"
#     ");"
# )

# CURSOR.execute(query, info)

# CON.commit()

# print(CURSOR.rowcount, "record inserted.")

# CON.close()
