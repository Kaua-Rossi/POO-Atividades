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

class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def getTitular(self):
        return self.titular

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        for c in self.contas:
            if c.getNumero() == conta.getNumero():
                print("Conta já cadastrada")
                return

        self.contas.append(conta)

    def procurarConta(self, numero):
        for c in self.contas:
            if c.getNumero() == numero:
                return c
        print("Conta não encontrada")
        return None

    def debitar(self, numero, valor):
        conta = self.procurarConta(numero)
        if conta is not None:
            conta.saldo -= valor
        else:
            print("Conta não encontrada")

    def creditar(self, numero, valor):
        conta = self.procurarConta(numero)
        if conta is not None:
            conta.saldo += valor
        else:
            print("Conta não encontrada")

    def transferir(self, origem, destino, valor):
        contaOrigem = self.procurarConta(origem)
        contaDestino = self.procurarConta(destino)
        if contaOrigem is not None and contaDestino is not None:
            contaOrigem.saldo -= valor
            contaDestino.saldo += valor
        else:
            print("Conta de origem ou destino não encontrada")

    def saldo(self, numero):
        conta = self.procurarConta(numero)
        if conta is not None:
            return f"R${conta.saldo:.2f}"
        return None

gerador_de_numero = lambda cpf: ''.join(filter(str.isdigit, cpf))[-6:] if ''.join(filter(str.isdigit, cpf)) else None

banco = Banco()

pessoas = []

def validar_cpf(cpf):
        cpf_numeros = ""
        for char in cpf:
            if '0' <= char <= '9':
                cpf_numeros += char
        cpf = cpf_numeros

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - (soma % 11)
        if digito1 > 9:
            digito1 = 0

        if int(cpf[9]) != digito1:
            return False

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - (soma % 11)
        if digito2 > 9:
            digito2 = 0

        if int(cpf[10]) != digito2:
            return False

        return True

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar pessoa")
    print("2 - Registrar conta")
    print("3 - Procurar conta")
    print("4 - Realizar débito")
    print("5 - Realizar crédito")
    print("6 - Realizar transferência")
    print("7 - Verificar saldo")
    print("8 - Sair")
    opcao = input()

    match(opcao):
        case "1":
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade da pessoa: ")
            cpf = input("Digite o CPF da pessoa: ")

            if nome == "" or idade == "" or cpf == "":
                print("Preencha todos os campos")
                continue

            if nome.replace(" ", "").isalpha() == False:
                print("Nome precisa conter apenas letras")
                continue

            if len(nome) < 3:
                print("Nome precisa ter 3 ou mais caracteres")
                continue

            try:
                idade = int(idade)
            except ValueError:
                print("Idade inválida")
                continue

            if idade < 0 or idade > 150:
                print("Idade inválida")
                continue

            if idade < 18:
                print("Pessoa menor de idade")
                continue

            if validar_cpf(cpf) == False:
                print("CPF inválido")
                continue

            pessoas.append(Pessoa(nome, idade, cpf))
        case "2":
            print("Digite seu CPF para identificação: ")
            cpf = input()

            pessoa_encontrada = False

            for pessoa in pessoas:
                if pessoa.getCpf() == cpf:
                    numero_da_conta = gerador_de_numero(cpf)
                    banco.cadastrar(Conta(pessoa, numero_da_conta, 0))
                    pessoa_encontrada = True
                    print("Conta cadastrada com sucesso")
                    break
            if pessoa_encontrada == False:
                print("CPF não encontrado")
        case "3":
            print("Digite o CPF ou número da conta: ")
            identificador = input()

            conta = None

            for c in banco.contas:
                if validar_cpf(identificador) == True:
                    if c.getTitular().getCpf() == identificador:
                        conta = banco.procurarConta(c.getNumero())
                        break
            if conta is None:
                conta = banco.procurarConta(identificador)

            if conta is not None:
                print("Titular: ", conta.getTitular().getNome())
                print("Idade: ", conta.getTitular().getIdade())
                print("CPF: ", conta.getTitular().getCpf())
                print("Número da conta: ", conta.getNumero())
                print(f"Saldo: R${conta.getSaldo():.2f}")
        case "4":
            print("Digite o número da sua conta: ")
            numero_da_conta = input()

            print("Digite o valor a ser debitado: ")
            valor = input()

            try:
                valor = float(valor)
            except ValueError:
                print("Valor inválido")
                continue

            banco.debitar(numero_da_conta, valor)
        case "5":
            print("Digite o número da sua conta: ")
            numero_da_conta = input()

            print("Digite o valor a ser creditado: ")
            valor = input()

            try:
                valor = float(valor)
            except ValueError:
                print("Valor inválido")
                continue

            banco.creditar(numero_da_conta, valor)
        case "6":
            print("Digite o número da sua conta: ")
            numero_da_conta = input()

            print("Digite o número da conta de destino: ")
            numero_da_conta_destino = input()

            print("Digite o valor a ser transferido: ")
            valor = input()

            try:
                valor = float(valor)
            except ValueError:
                print("Valor inválido")
                continue

            banco.transferir(numero_da_conta, numero_da_conta_destino, valor)
        case "7":
            print("Digite o número da sua conta: ")
            numero_da_conta = input()

            saldo = banco.saldo(numero_da_conta)

            if saldo is not None:
                print("Saldo: ", saldo)
        case "8":
            print("Saindo do sistema, até mais! :D")
            break
        case _:
            print("Opção inválida")
