from cliente import Cliente
from connection import Connection

class ClienteDao():

    def getByLoginSenha(login, senha):
        con = Connection.instance()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM cliente WHERE cpf = %s and senha = %s;", (login, senha))
        return cursor.fetchone()
        con.close()

    def cadastrar(self, cliente):
        con = Connection.instance()
        cursor = con.cursor()
        dados = (cliente.getCpf(), cliente.getNome(), cliente.getIdade(), cliente.getSenha())
        cursor.execute("INSERT INTO cliente (cpf, nome, idade, senha) VALUES (%s, %s, %s, %s);", dados)
