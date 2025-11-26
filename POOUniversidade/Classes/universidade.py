class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.campi = []

    def adicionar_campus(self, campus):
        self.campi.append(campus)
        print(f"Campus '{campus.nome}' adicionado à universidade.")

    def buscar_campus(self, nome_campus):
        for campus in self.campi:
            if campus.nome.lower() == nome_campus.lower():
                return campus
        return None

    def remover_campus(self, nome_campus):
        campus_a_remover = self.buscar_campus(nome_campus)
        if campus_a_remover:
            self.campi.remove(campus_a_remover)
            print(f"Campus '{campus_a_remover.nome}' removido.")
            return True
        print(f"erro: Campus '{nome_campus}' não encontrado")
        return False

    def listar_campi(self):
        print(f"\n--- Campi da {self.nome} ---")
        if not self.campi:
            print("nenhum campus cadastrado.")
        else:
            for i, campus in enumerate(self.campi):
                print(f"{i + 1}. {campus}")
