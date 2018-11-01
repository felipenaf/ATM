from pessoa import Pessoa
from connection import Connection
import time

class PessoaDao():

    def getByLoginSenha(login, senha):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM pessoa WHERE login = %s and senha = %s;", (login, senha))
        except:
            print('\nAlgo deu errado.')
        else:
            return cursor.fetchone()
        finally:
            con.close()
            

    def cadastrar(self, pessoa):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (pessoa.getLogin(), pessoa.getSenha(), pessoa.getNome())
            cursor.execute("INSERT INTO pessoa (login, senha, nome) VALUES (%s, %s, %s);", dados)
            con.commit()
            dadosDoc = (pessoa.getTipo(), pessoa.getDocumento(), cursor.lastrowid)
            cursor.execute("INSERT INTO documento (tipo, numero, idPessoa) VALUES (%s, %s, %s);", dadosDoc)
            con.commit()
        except:
            print('\nNão foi possível realizar o cadastro!\n')
        else:
            print('\nCliente cadastrado com sucesso!\n')
        finally:
            time.sleep(3)
            con.close()

    def listar(self):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM pessoa;")
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