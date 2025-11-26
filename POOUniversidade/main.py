from Classes import Universidade, Curso, Campus

def exibir_menu_principal():
    print("\n### Sistema de Gerenciamento Acadêmico ###")
    print("1. Gerenciar Campi")
    print("2. Gerenciar Cursos")
    print("3. Sair")
    return input("Escolha uma opção: ")

def exibir_menu_crud(entidade):
    print(f"\n--- Gerenciar {entidade} ---")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Remover")
    print("5. Voltar ao menu principal")
    return input("Escolha uma opção: ")

def gerenciar_campi(universidade):
    while True:
        opcao = exibir_menu_crud("Campi")
        if opcao == '1':
            nome = input("Digite o nome do novo campus: ")
            cidade = input(f"Digite a cidade do campus {nome}: ")
            novo_campus = Campus(nome, cidade)
            universidade.adicionar_campus(novo_campus)
        elif opcao == '2':
            universidade.listar_campi()
        elif opcao == '3':
            nome_antigo = input("Digite o nome do campus que deseja atualizar: ")
            campus = universidade.buscar_campus(nome_antigo)
            if campus:
                novo_nome = input(f"Digite o novo nome para o campus '{campus.nome}' (ou deixe em branco para não alterar): ")
                nova_cidade = input(f"Digite a nova cidade para o campus '{campus.nome}' (ou deixe em branco para não alterar): ")
                if novo_nome:
                    campus.nome = novo_nome
                if nova_cidade:
                    campus.cidade = nova_cidade
                print("Campus atualizado com sucesso")
            else:
                print(f"Campus '{nome_antigo}' não encontrado")
        elif opcao == '4':
            nome_campus = input("Digite o nome do campus que deseja remover: ")
            universidade.remover_campus(nome_campus)
        elif opcao == '5':
            break
        else:
            print("Opção inválida")

def gerenciar_cursos(universidade):
    universidade.listar_campi()
    nome_campus = input("\nDigite o nome do campus para gerenciar os cursos: ")
    campus_selecionado = universidade.buscar_campus(nome_campus)

    if not campus_selecionado:
        print(f"Campus '{nome_campus}' não encontrado.")
        return

    while True:
        print(f"\n### Gerenciando Cursos do Campus: {campus_selecionado.nome} ###")
        opcao = exibir_menu_crud("Cursos")
        if opcao == '1':
            nome_curso = input("Digite o nome do novo curso: ")
            id_curso = input(f"Digite o código/id do curso {nome_curso} (ex: 'ADS' para o curso Análise e desenvolvimento de sistemas): ")
            if campus_selecionado.buscar_curso(id_curso):
                print("Erro: já existe um curso com esse id nesse campus")
            else:
                novo_curso = Curso(nome_curso, id_curso)
                campus_selecionado.adicionar_curso(novo_curso)
        elif opcao == '2':
            campus_selecionado.listar_cursos()
        elif opcao == '3':
            id_curso = input("Digite o id do curso que deseja atualizar: ")
            curso = campus_selecionado.buscar_curso(id_curso)
            if curso:
                novo_nome = input(f"Digite o novo nome para o curso '{curso.nome}' (deixe em branco para não alterar): ")
                novo_id = input(f"Digite o novo id para o curso '{curso.id_curso}' (deixe em branco para não alterar): ")
                if novo_nome:
                    curso.nome = novo_nome
                if novo_id:
                    curso.id_curso = novo_id
                print("curso atualizado com sucesso.")
            else:
                print(f"Curso com código '{id_curso}' não encontrado")
        elif opcao == '4':
            id_curso = input("Digite o id do curso que deseja remover: ")
            campus_selecionado.remover_curso(id_curso)
        elif opcao == '5':
            break
        else:
            print("opção inválida")

def main():
    ufc = Universidade("Universidade Federal do Ceará")

    pici = Campus("Pici", "Fortaleza")
    jardins_de_anita = Campus("Jardins de Anita", "Itapajé")
    ufc.adicionar_campus(pici)
    ufc.adicionar_campus(jardins_de_anita)
    pici.adicionar_curso(Curso("Ciência da Computação", "CC"))
    pici.adicionar_curso(Curso("Engenharia de Software", "ES"))
    jardins_de_anita.adicionar_curso(Curso("Análise e Desenvolvimento de Sistemas", "ADS"))
    print("\nDados de exemplo carregados.")

    while True:
        opcao_principal = exibir_menu_principal()
        if opcao_principal == '1':
            gerenciar_campi(ufc)
        elif opcao_principal == '2':
            gerenciar_cursos(ufc)
        elif opcao_principal == '3':
            print("Saindo do sistema... até mais! :D")
            break
        else:
            print("opção invalida")

if __name__ == "__main__":
    main()
