from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula

    @property
    def curso(self):
        return self.__curso

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @curso.setter
    def curso(self, curso):
        self.__curso = curso
