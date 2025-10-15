global estoque_comida, estoque_bebida

estoque_comida = {"goiaba" : 3, "sanduiche" : 2, "bolo" : 2, "banana" : 60, "sorvete" : 1, "hamburguer" : 3, "batata frita" : 4, "macarrão" : 2, "camarão" : 9, "peixe" : 3}
estoque_bebida = {"café" : 12, "refrigerante" : 1, "suco de goiaba" : 5, "suco de maçã" : 3, "suco de cajá" : 1, "suco de cajú" : 7, "suco de morango" : 4, "achocolatado" : 2, "suco de melancia" : 3, "suco de melão" : 4}

def mostrar_estoque():
    print("ESTOQUE DE COMIDA:")
    for elemento in estoque_comida:
        print(f"{elemento} : {estoque_comida[elemento]}")
    print("ESTOQUE DE BEBIDA:")
    for elemento in estoque_bebida:
        print(f"{elemento} : {estoque_bebida[elemento]}")

def adicionar_produto(nome, quantidade):
    while True:
        qual_estoque = input(f"Você deseja adicionar {nome} ao estoque de comida ou de bebidas? (c = comida, b = bebidas): ").lower()

        if qual_estoque not in ["c", "b"]:
            print("Erro")
            continue
        else:
            if qual_estoque == "c":
                if nome in estoque_comida:
                    estoque_comida[nome] += quantidade
                else:
                    estoque_comida.update({nome : quantidade})
                break
            else:
                if nome in estoque_bebida:
                    estoque_bebida[nome] += quantidade
                else:
                    estoque_bebida.update({nome : quantidade})
                break

def remover_produto(nome, quantidade):
    while True:
        qual_estoque = input(f"Você deseja remover {nome} do estoque de comida ou de bebidas? (c = comida, b = bebidas): ").lower()

        if qual_estoque not in ["c", "b"]:
            print("Erro")
            continue
        else:
            if qual_estoque == "c":
                if nome in estoque_comida and quantidade >= estoque_comida[nome]:
                     estoque_comida.pop(nome)
                     print(f"Produto {nome} removido completamente.")
                     break
                elif nome in estoque_comida:
                     estoque_comida[nome] -= quantidade
                     print(f"{quantidade} unidades de {nome} foram removidas.")
                     break
                else:
                     print("Produto não encontrado")
                     break
            else:
                if nome in estoque_bebida and quantidade >= estoque_bebida[nome]:
                    estoque_bebida.pop(nome)
                    print(f"Produto {nome} removido completamente.")
                    break
                elif nome in estoque_bebida:
                    estoque_bebida[nome] -= quantidade
                    print(f"{quantidade} unidades de {nome} foram removidas.")
                    break
                else:
                    print("Produto não encontrado")
                    break

def consultar_produto(nome):
    while True:
        if nome in estoque_comida:
            print(f"{nome} : {estoque_comida[nome]}")
        elif nome in estoque_bebida:
            print(f"{nome} : {estoque_bebida[nome]}")
        else:
            print("Produto não encontrado.")
        break

def menu():
    while True:
        print("1 - Mostrar estoque\n"
              "2 - Adicionar produto\n"
              "3 - Remover produto\n"
              "4 - Consultar produto\n"
              "5 - Sair\n"
              "6 - Salvar relatório\n"
              "7 - Repor automático\n")
        opcao = input()

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            nome = input("Digite o nome do produto para adicionar ou atualizar a quantidade: ")
            quantidade = int(input("Digite a quantidade do produto que você deseja adicionar ou atualizar: "))

            adicionar_produto(nome, quantidade)
        elif opcao == "3":
            nome = input("Digite o nome do produto para remover do estoque: ")
            quantidade = int(input("Digite a quantidade do produto que você deseja remover (um valor igual ou acima da quantidade dentro do estoque vai tirar o produto do estoque): "))

            remover_produto(nome, quantidade)
        elif opcao == "4":
            nome = input("Digite o nome do produto que você deseja consultar: ")

            consultar_produto(nome)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        elif opcao == "6":
            print("Salvando o relatório em um arquivo chamado estoque.txt")

            salvar_relatorio()
        elif opcao == "7":
            print("Repondo automaticamente o estoque para produtos com quantidade menor que 3")

            repor_automatico()
        else:
            continue

def salvar_relatorio():
    with open("estoque.txt", "w", encoding='utf-8') as f:
        f.write("ESTOQUE DE COMIDA\n")
        for produto, quantidade in estoque_comida.items():
            f.write(f"{produto}: {quantidade}\n")
            
        f.write("\nESTOQUE DE BEBIDA\n")
        for produto, quantidade in estoque_bebida.items():
            f.write(f"{produto}: {quantidade}\n")

def repor_automatico():
    for elemento in estoque_comida:
        if estoque_comida[elemento] < 3:
            estoque_comida[elemento] += 5
    for elemento in estoque_bebida:
        if estoque_bebida[elemento] < 3:
            estoque_bebida[elemento] += 5
menu()
