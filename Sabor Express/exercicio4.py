##1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoas = [
    {'nome':'vini','idade':34,'cidade':'guarulhos'}, #0
    {'nome':'ka','idade':33,'cidade':'cubatão'},     #1
    {'nome':'le','idade':29,'cidade':'são paulo'}    #2
]

print(pessoas)

##2 - Utilizando o dicionário criado no item 1:

##Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoas[0]['idade'] = 40
print(pessoas)

##Adicione um campo de profissão para essa pessoa;
pessoas[0]['profissão'] = 'arquiteto'
print(pessoas)

##Remova um item do dicionário
del pessoas[0]
print(pessoas)

##3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = []
for i in range(5):
    numero = i+1
    quadrados.append({'número':numero,'quadrado':numero*numero})
print(quadrados)

##ALURA
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

##4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
nome = 'ka'
encontrei = False
for pessoa in pessoas:
    if nome == pessoa['nome']:
        encontrei = True
        break
if encontrei: print(f'Encontrei a pessoa {nome} na lista!') 
else: print(f'Não encontrei a pessoa {nome} na lista')

nome = 'vini'
encontrei = False
for pessoa in pessoas:
    if nome == pessoa['nome']:
        encontrei = True
        break
if encontrei: print(f'Encontrei a pessoa {nome} na lista!') 
else: print(f'Não encontrei a pessoa {nome} na lista')

## ALURA
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

##5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = 'Eu moro numa casa longe da sua casa que é longe da minha casa'
palavras_frase = frase.split()
palavras_nao_duplicadas = set(palavras_frase)
frase_dicionario = []
for palavra in palavras_nao_duplicadas:
    frase_dicionario.append({'palavra':palavra, 'quantas vezes aparece':palavras_frase.count(palavra)})
print(frase_dicionario)

## ALURA
frase = 'Eu moro numa casa longe da sua casa que é longe da minha casa'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
