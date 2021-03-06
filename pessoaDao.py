from pessoa import Pessoa
from contaCorrente import ContaCorrente
from connection import Connection
import time
from funcoes import voltar

class PessoaDao():

    def getByLoginSenha(login, senha):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * from atm.pessoa "
                            "LEFT JOIN atm.documento "
                                "ON atm.pessoa.id = atm.documento.idPessoa "
                            "LEFT JOIN atm.contaCorrente "
                                "ON atm.pessoa.id = atm.contaCorrente.idPessoa "
                            "WHERE login = %s and senha = %s;", (login, senha))
        except Exception as e:
            print('\nAlgo deu errado.\n', e)
        else:
            return cursor.fetchone()
        finally:
            con.close()

    def getById(self, id):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * from atm.pessoa "
                            "LEFT JOIN atm.documento "
                                "ON atm.pessoa.id = atm.documento.idPessoa "
                            "LEFT JOIN atm.contaCorrente "
                                "ON atm.pessoa.id = atm.contaCorrente.idPessoa "
                            "WHERE pessoa.id = %s;", (id, ))
        except Exception as e:
            print('\nAlgo deu errado.\n', e)
        else:
            return cursor.fetchone()
        finally:
            con.close()


    def cadastrar(self, pessoa, conta):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (pessoa.getLogin(), pessoa.getSenha(), pessoa.getNome())
            cursor.execute("INSERT INTO pessoa (login, senha, nome) VALUES (%s, %s, %s);", dados)
            ultimoId = cursor.lastrowid
            dadosDoc = (pessoa.getTipo().lower(), pessoa.getDocumento(), ultimoId)
            cursor.execute("INSERT INTO documento (tipo, numero, idPessoa) VALUES (%s, %s, %s);", dadosDoc)
            dadosConta = (conta.getNumeroCC(), conta.getAgencia(), conta.getSaldo(), ultimoId)
            cursor.execute("INSERT INTO contaCorrente (numero, agencia, saldo, idPessoa) VALUES (%s, %s, %s, %s);", dadosConta)
            con.commit()
        except Exception as e:
            print('\nNão foi possível realizar o cadastro!\n', e)
        else:
            print('\nCliente cadastrado com sucesso!')
            print('\nNúmero da Agência:', conta.getAgencia())
            print('\nNúmero da Conta:', conta.getNumeroCC())
        finally:
            con.close()
            voltar()

    def listar(self):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("SELECT * from atm.pessoa INNER JOIN atm.documento on atm.documento.idPessoa = atm.pessoa.id INNER JOIN atm.contaCorrente on atm.contaCorrente.idPessoa = atm.pessoa.id;")
        except Exception as e:
            print('\nAlgo deu errado.\n', e)
        else:
            result = cursor.fetchall()
            return result
        finally:
            con.close()

    def excluir(self, pessoa):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            cursor.execute("DELETE FROM atm.documento WHERE idPessoa = %s;", (pessoa.getId(),))
            cursor.execute("DELETE FROM atm.contaCorrente WHERE idPessoa = %s;", (pessoa.getId(),))
            cursor.execute("DELETE FROM atm.pessoa WHERE id = %s;", (pessoa.getId(),))
            con.commit()
        except Exception as e:
            print('\nNão foi possível realizar a exclusão!\n', e)
        else:
            print('\nCliente excluído com sucesso!\n')
        finally:
            con.close()
            voltar()

    def editar(self, pessoa, contaCorrente):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (pessoa.getLogin(), pessoa.getSenha(), pessoa.getId())
            dadosConta = (contaCorrente.getAgencia(), pessoa.getId())
            cursor.execute("UPDATE atm.pessoa SET login = %s, senha = %s where id = %s;", dados)
            cursor.execute("UPDATE atm.contaCorrente SET agencia = %s where idPessoa = %s;", dadosConta)
            con.commit()
        except Exception as e:
            print('\nErro!!\n', e)
        else:
            print('\nAlterações cadastradas com sucesso!\n')
        finally:
            con.close() 
            voltar()

    def atualizaSaldo(self, conta, msg):
        try:
            con = Connection.instance()
            cursor = con.cursor()
            dados = (conta.getSaldo(), conta.getIdPessoa())
            cursor.execute("update atm.contaCorrente set saldo = %s where idPessoa = %s;", dados)
            con.commit()
        except Exception as e:
            print('\nErro!!\n', e)
        else:
            print("\n{} realizado com sucesso!\n".format(msg))
        finally:
            con.close() 
            voltar()
