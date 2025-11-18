lista = [2,3,2,8,5]
palavra = "banana"
print(len(lista))
print(len(palavra))
print(min(lista))
print(min(palavra))
print(max(lista))
print(max(palavra))
serie = range(0,10)
print(serie[0])

dias=["S","T","Q","Q","S","S","D"]
dias.append("D2")
print(dias)

#declaracao de tupla - tupla é imutável
dias_novo=("S","T","Q","Q","S","S","D")
print(type(dias_novo))

#tuplas e listas juntas
p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
linha = [p1,p2,p3]
print(linha)

p1 = ("Vini",29)
p2 = ("Nico", 39)
instrutores = [p1,p2]
print(len(instrutores))

palavras = []
palavras.append("banana")
palavras.append("abacaxi")
nova = tuple(palavras) #transforma uma lista em tuple
print(type(palavras))
print(type(nova))
nova2 = list(nova) #transforma uma tuple em lista

#colecao de dados tipo set
nomes = {"vini","ka"}
nomes.add("vini") #nao permite adicionar membros duplicados
print(nomes)

#colecao dictionary
instrutores = {"vini":29, "nico":39}
print(instrutores["vini"]) #imprime o dado associado a chave

#list comprehension
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]
print(lista)

inteiros = [1,3,4,5,7,8]
quadrados = [n*n for n in inteiros]
print(quadrados)

#list comprehensino com condicao
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
print(pares)