class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCpf(self):
        return self.cpf
