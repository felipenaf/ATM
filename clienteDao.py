from cliente import Cliente
from connection import Connection

class ClienteDao():

    def getByLoginSenha(login, senha):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM cliente WHERE cpf = %s and senha = %s;", (login, senha))
        except:
            print('\nAlgo deu errado.')
        else:
            return cursor.fetchone()
        finally:
            con.close()
            

    def cadastrar(self, cliente):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (cliente.getCpf(), cliente.getNome(), cliente.getIdade(), cliente.getSenha())
            cursor.execute("INSERT INTO cliente (cpf, nome, idade, senha) VALUES (%s, %s, %s, %s);", dados)
            con.commit()
        except:
            print('Não foi possível realizar o cadastro!\n')
        else:
            print('Cliente cadastrado com sucesso!\n')
        finally:
            con.close()

    def listar(self):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM cliente;")
        except:
            print('\nAlgo deu errado.')
        else:
            result = cursor.fetchall()
            return result
        finally:
            con.close()

    def excluir(self, id):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("DELETE FROM atm.cliente WHERE id = %s;", id)
            con.commit()
        except:
            print('Não foi possível realizar a exclusão!\n')
        else:
            print('Cliente excluído com sucesso!\n')
        finally:
            con.close()
