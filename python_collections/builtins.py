idades = [15,87,32,65,56,32,49,37]
## posição na sequência começa do 0 até n

#imprime o elemento mas não a posição
for idade in idades:
    print(idade)

#argumento range imprime a primeira posição e a quantidade de elementos
print(range(len(idades)))

#assim eu imprimo a posição e o elemento que está na posição
for i in range(len(idades)):
    print(i, idades[i])

#força a geração dos valores das posições
print(list(range(len(idades))))

#enumerate cria a tupla posição (índice) e elemento
#assim gera de uma maneira única para o usuário
print(list(enumerate(idades)))

#assim gera elemento a elemento
for indice,idade in enumerate(idades): #isso desempacota a tupla
    print(indice, "x",idade)

usuarios = [("Vini",30),("Karine",29)]

for nome,_ in usuarios: #usar o _ me permite ignorar as posições da tupla que eu não quero
    print(nome)

#geradores de iteraveis:

#o sorted ordena de forma ascendente uma sequência
print(sorted(idades))
#o sorted com reverse=True ordena de forma descendente
print(sorted(idades,reverse=True))
#o sorted já devolve uma lista
#idades é uma lista que pode ser reordenada, mudada a qualquer momento
#o comando list.sort() ordena a lista, muda a ordem original dos elementos