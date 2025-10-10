saldo = 1000
historico = []

while True:
  print("\n=== MENU DO CAIXA ELETRÔNICO ===\n"
        "1 - Depositar\n"
        "2 - Sacar\n"
        "3 - Ver saldo\n"
        "4 - Ver histórico de transações\n"
        "5 - Sair\n")
  opcao = input()

  match(opcao):
    case "1":
      valor_deposito = float(input("Digite a quantidade que você deseja depositar: "))
      saldo += valor_deposito
      historico.append(f"Depósito de R${valor_deposito}")
      continue
    case "2":
      valor_saque = float(input("Digite a quantidade que você deseja sacar: "))
      if valor_saque > saldo:
        print("Saldo insuficiente.")
      else:
        saldo -= valor_saque
        historico.append(f"Saque de R${valor_saque}")
      continue
    case "3":
      print(f"O seu saldo atual é de R${saldo}")
      continue
    case "4":
      if len(historico) > 0:
        for _ in historico:
          print(_)
      else:
        print("Nenhuma transação foi registrada.")
      continue
    case "5":
      print("Saindo do programa.")
      break
    case _:
      print("Opção não disponível, digite novamente.")
      continue
