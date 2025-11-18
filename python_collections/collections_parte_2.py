# lista do python é entre [] colchetes
usuarios_data_science = [15, 24, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# para copiar os elementos de uma lista para outra -> copy
assistiram = usuarios_data_science.copy()
# para adicionar mais elementos a uma lista -> extend
assistiram.extend(usuarios_machine_learning)
print(assistiram)

# o set transforma a lista em um conjunto, ou seja, não haverão mais elementos repetidos
# o conjunto ordena os membros de forma ascendente
# não é possível acessar uma posição dentro de um conjunto igual uma lista
# o comando set cria um conjunto, ele é representado entre {} chaves
print(set(assistiram))

# é possível acessar os elementos de um conjunto por meio de iterações
for assistiu in set(assistiram):
    print(assistiu)

# criando um conjunto representado entre {} chaves
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# usar o | pipe permite visualizar os membros de qualquer conjunto
# isso é semelhante a operação de extend das listas
# o | é uma operação de "ou"
print(usuarios_machine_learning | usuarios_data_science)

# usar o & traz os elementos que são comuns a ambos os conjuntos, intersecção
print(usuarios_machine_learning & usuarios_data_science)

# usar o - retira do conjunto a esquerda os elementos da direita que seriam comuns
print(usuarios_machine_learning - usuarios_data_science)
fez_machine_learning_mas_nao_data_science = usuarios_machine_learning - usuarios_data_science
print(15 in fez_machine_learning_mas_nao_data_science)

# o ^ é o "ou exclusivo" traz os elementos que são exclusivos entre os conjuntos, desconsiderando o que está na intersecção
print(usuarios_machine_learning ^ usuarios_data_science)

# os conjuntos não possuem uma ordem interna igual a uma lista, por exemplo
usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

# o comando add adiciona um novo elemento ao conjunto
# este elemento precisa ser exclusivo, se já houver um igual este novo não é adicionado
usuarios.add(50)
print(len(usuarios))

# este comando congela um conjunto e não permite a adição de novos elementos
usuarios_congelado = frozenset(usuarios)
print(type(usuarios_congelado))

# o comando split separa todas as palavras de uma string
# transformar o resultado do split em um conjunto elimina as palavras duplicadas da string
meu_texto = "Olá meu nome é Vinícius e gosto de ler HQs com o herói de nome Homem-Aranha"
print(set(meu_texto.split()))

# Dicionário
# criando um objeto de tipo dicionário
aparicoes = {"Vinicius": 1, "HQs": 2, "nome": 3}
# para imprimir o valor a que o elemento nos colchetes se refere
print(aparicoes["Vinicius"])
# se o elemento buscado não existir no dicionário, imprimir um valor alternativo
print(aparicoes.get("xpto","não existe"))

# outra forma de instanciar um dicionário, a forma de trazer um valor é o mesmo
aparicoes = dict(Vinicius = 1, nome = 3)
print(aparicoes['Vinicius'])

#adicionando um elemento
aparicoes["Carlos"] = 7
print(aparicoes)
#apagando um elemento
del aparicoes["nome"]
print(aparicoes)
#verificando se um elemento (chave) existe no dicionário
print("Vinicius" in aparicoes)

#imprimindo na tela os elementos (chaves) do dicionário
for elemento in aparicoes:
    print(elemento)

#imprimindo na tela os elementos (chaves) do dicionário
for elemento in aparicoes.keys():
    print(elemento)

#imprimindo na tela os valores dos elementos do dicionário
for elemento in aparicoes.values():
    print(elemento)

#imprimindo na tela as tuplas com os elementos e valores do dicionário
for chave,valor in aparicoes.items():
    print(chave, "=", valor)

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

meu_texto = "Olá meu nome é Vinícius e gosto de ler HQs com o herói de nome Homem-Aranha"
meu_texto_preparado = meu_texto.lower() #deixar todas as letras da string em minúsculo
aparicoes = {} #cria um dicionário em branco que conterá a palavra e a quantidade de vezes em que aparece na string
for palavra in meu_texto_preparado.split():
    ate_agora = aparicoes.get(palavra, 0) #o 0 é para iniciar a contagem das novas palavras
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict #o defaultdict elimina a necessidade de passar um inicializador em 0 igual o acima

aparicoes = defaultdict(int)
for palavra in meu_texto_preparado.split():
    aparicoes[palavra] += 1

print(aparicoes)

#é possível criar um dicionário de objetos, no exemplo abaixo a partir da classe de Conta
class Conta:
    def __init__(self):
        print("Criando uma conta nova")

contas = defaultdict(Conta)
contas[15]
contas[17]
contas[20]
print(contas)

from collections import Counter

#usar o Counter ajuda a contar a quantidade de vezes que uma palavra aparece em uma string
aparicoes = Counter(meu_texto_preparado.split())
print(aparicoes)