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