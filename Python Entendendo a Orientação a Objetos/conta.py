class Conta:


    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {}".format(self.__saldo))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor passou do limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel
    @staticmethod
    def codigo_banco(self):
        return "001"
    @staticmethod
    def codigos_bancos(self):
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}