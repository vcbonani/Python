#para usar uma classe com um método abstrato, é necessário importar da biblioteca abc os seguintes:
from abc import ABCMeta, abstractmethod

#permite fazer uma implementação de uma ordenação total sem a necessidade de criar funções extras para isso
#basta colocar o @total_ordering acima da classe e implementar __eq__ e __lt__
from functools import total_ordering

#ao criar a classe, é necessário informar que ela herda do ABCMeta
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita (self, valor):
        self._saldo += valor

    #@abstractmethod #isso força com que todas as classes que herdem a classe mãe implementem este método
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo,self._saldo)


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -=3


class ContaInvestimento(Conta): #esta classe dará erro na hora de instanciar um objeto porque não implementou o método passa_o_mes
    pass

conta20 = ContaInvestimento(30)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta18 = ContaCorrente(18)
conta18.deposita(1000)
conta19 = ContaPoupanca(19)
conta19.deposita(1000)
contas = [conta18, conta19]
for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)


##ARRAY PADRÃO DO PYHTON - EVITAR USAR
import array as arr

arr.array('d', [1, 3.5]) #o array é criado com um parâmetro inicial definindo o tipo dos valores
                         #no dia-a-dia usa-se as listas
                         #as tuplas são usadas quando as posições são fixas, querem dizer alguma coisa

#se for importante um alto desempenho matemático com uma lista, usa-se o numpy e não o array
import numpy as np
numeros = np.array([1, 3.5])
print(numeros)
numeros = numeros + 3
print(numeros)

@total_ordering
class ContaSalario:

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    #implementar o __eq__ permite criar uma comparação baseada no atributo que desejamos
    #desta maneira, não é comparado por exemplo um endereço de memória
    #a comparação pode ser feita com atributos e tipos
    def __eq__(self, other):
        return self._codigo == other._codigo and self._saldo == other._saldo

    ##implementar o lt, permite criar uma maneira de comparar objetos por meio de um atributo
    ##neste caso, o lt é para a operação < (menor que); isso vale para > (maior que) também
    ##usar dessa maneira, permite usar o sorted em uma lista de objetos, por exemplo
    def __lt__(self, other):
        #colocar desta maneira, ordeno primeiro pelo saldo, se for igual, ordeno pelo código
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return("Codigo {} Saldo {}".format(self._codigo,self._saldo))


conta1 = ContaSalario(37)
conta1.deposita(10)
conta2 = ContaSalario(37)
print(type(conta1))
print(conta1==conta2) #estão sendo comparados dois objetos distintos, por mais que tenham o mesmo código

#essa função verifica se o objeto é uma instância de uma classe determinada
print(isinstance(conta1,ContaSalario))

conta_vinicius = ContaSalario(17)
conta_vinicius.deposita(100)
conta_karine = ContaSalario(18)
conta_karine.deposita(100)
conta_leticia = ContaSalario(15)
conta_leticia.deposita(50)
contas = [conta_leticia,conta_karine,conta_vinicius]

from operator import attrgetter

##o attrgetter  permite trazer um atributo de uma classe
##usar o sorted dessa maneira, permite ordenar os objetos por meio do uso de um atributo (no caso aqui, o saldo)
##pode-se usar mais de um atributo como critério para ordenação
for conta in sorted(contas, key=attrgetter("_saldo","_codigo")):
    print(conta)

print(conta_vinicius <= conta_leticia)