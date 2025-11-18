class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        ##O valor no parametro limite tira a obrigatoriedade de passar esse parametro
        ##Atributos com __ na frente tornam o atributo privado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod ##cria método estático
    def codigo_banco():
        return "001"

    @staticmethod ##cria método estático
    def codigos_bancos():
        return {"BB":"001","Caixa":"104","Bradesco":"237"}

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

    def extrato(self):
        print("Saldo de R${} do titular {} e limite de R${}".format(self.saldo, self.titular, self.limite))

    def deposita(self, valor):
        if(valor > 0):
            self.__saldo += valor
        else:
            print("Você não pode depositar um valor menor ou igual a zero")

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {}  passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)