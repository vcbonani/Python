class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita (self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo,self.saldo)


conta_do_vini = ContaCorrente(15)
print(conta_do_vini)
conta_do_vini.deposita(500)
print(conta_do_vini)

conta_da_dani = ContaCorrente(65465)
conta_da_dani.deposita(1000)
print(conta_da_dani)

#criando lista com objetos
contas = [conta_da_dani, conta_do_vini]
for conta in contas:
    print(conta)

contas = [conta_da_dani, conta_do_vini]

#esta função só funcionará caso os elementos da lista sejam do mesmo tipo
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas)
for conta in contas:
    print(conta)

vinicius = ("Vinicius", 30, 1991) #tupla
karine = ("Karine", 29, 1992) #tupla não possui append, não pode ser alterada, é imutável
#a tupla possui uma sequência definida de campos que a comporão
#no exemplo acima seriam atributos: nome, idade, ano de nascimento
#acessando o valor de uma tupla:
print(vinicius[1])
#a tupla remete mais a uma programação funciona do que orientada a objetos
#tuplas são utilizadas comumente quando usamos vários tipos e quando as posições indicam algo fixo

usuarios = [vinicius,karine] #misturando tupla com lista
print(usuarios)
paulo = ("Paulo",20,2001)
usuarios.append(paulo) #incluindo uma nova tupla na lista
print(usuarios)
#isso não muda o comportamento da tupla, de que ela não pode ter suas informações alteradas em uma posição específica

contas = (conta_do_vini,conta_da_dani) #tupla com objetos
for conta in contas:
    print(conta)
#a tupla não pode ser alterada, porém no exemplo acima os objetos são mutáveis
#tuplas não são comumente usadas com objetos

##HERANÇA E POLIMORFISMO

