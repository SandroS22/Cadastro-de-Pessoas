from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, id_funcionario):
        super().__init__(nome, cpf)
        self.__id_funcionario = id_funcionario

    @property
    def id_funcionario(self):
        return self.__funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario):
        self.__id_funcionario = id_funcionario

