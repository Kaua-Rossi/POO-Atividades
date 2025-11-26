class Campus:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Curso '{curso.nome}' adicionado ao Campus {self.nome}.")

    def buscar_curso(self, id_curso):
        for curso in self.cursos:
            if curso.id_curso == id_curso:
                return curso
        return None

    def remover_curso(self, id_curso):
        curso_remover = self.buscar_curso(id_curso)
        if curso_remover:
            self.cursos.remove(curso_remover)
            print(f"curso '{curso_remover.nome}' removido do Campus {self.nome}.")
            return True
        print(f"erro: curso com id '{id_curso}' não encontrado")
        return False

    def listar_cursos(self):
        print(f"\n--- Cursos do Campus {self.nome} ---")
        if not self.cursos:
            print("Nenhum curso cadastrado.")
        else:
            for curso in self.cursos:
                print(f"- {curso}")

    def __str__(self):
        return f"Campus: {self.nome} - Cidade: {self.cidade}"
