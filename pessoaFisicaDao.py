from pessoaFisica import PessoaFisica
from connection import Connection

class PessoaDao():

    def getByLoginSenha(login, senha):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM atm.pessoaFisica INNER JOIN atm.pessoa ON atm.pessoaFisica.idPessoa = atm.pessoa.id WHERE cpf = %s AND senha = %s;", (login, senha))
        except:
            print('\nAlgo deu errado.')
        else:
            return cursor.fetchone()
        finally:
            con.close()
            

    def cadastrar(self, pessoaFisica):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (pessoaFisica.getLogin(), pessoaFisica.getSenha())
            dados = (pessoaFisica.getCpf(), pessoaFisica.getNome())
            cursor.execute("INSERT INTO pessoa (login, senha) VALUES (%s, %s);", dados)
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
