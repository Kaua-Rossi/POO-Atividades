class Curso:
    def __init__(self, nome, id_curso):
        self.nome = nome
        self.id_curso = id_curso

    def __str__(self):
        return f"Curso: {self.nome} (ID: {self.id_curso})"
