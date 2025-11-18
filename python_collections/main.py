idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39,30,27,18]
print(type(idades))
print(len(idades))
print(idades)
print(idades[1])

idades.append(50) ##adiciona ao final
print(idades)
print(len(idades)) ##imprime o tamanho da list
print(idades[4])

for idade in idades: ##laço que percorre a list
    print(idade)

idades.remove(27) ##remove a primeira ocorrência do elemento passado, caso exista
print(len(idades))

#idades.clear() ##apaga todos os elementos de uma list
print(idades)

print(39 in idades) ##verifica se o elemento está dentro da list (retorna true ou false)

idades.insert(0,20) ##insere um elemento novo na posição desejada
print(idades)

idades.extend([10,15,12,17]) ##adiciona os elementos passados como uma list na list
print(idades)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

idades_2 = [(idade + 1) for idade in idades] ##cria uma lista a partir de uma antiga com uma transformação
print(idades_2)

print([idade for idade in idades if idade >= 30]) ##if ao final aplica um filtro nos dados da list

def faz_processamento_de_visualizacao(lista):
    print(len(lista))

faz_processamento_de_visualizacao(idades)