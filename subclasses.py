from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        Pessoa.__init__(self, nome, cpf)
        self.matricula = matricula
        self.curso = curso

    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_curso(self, curso):
        self.curso = curso

    def get_matricula(self):
        return self.matricula

    def get_curso(self):
        return self.curso


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idf):
        Pessoa.__init__(self, nome, cpf)
        self.idf = idf

    def set_idf(self, idf):
        self.idf = idf

    def get_idf(self):
        return self.idf
