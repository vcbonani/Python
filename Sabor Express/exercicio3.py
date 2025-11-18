##CRIAÇÃO DE LISTAS E EXIBIÇÃO
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(f'Número da lista: {numero}')
lista_de_nomes = ['Vini','Ka','LeLe','Mi','Gabi']
for nome in lista_de_nomes:
    print(f'Nome da lista: {nome}')
lista_de_anos = [1991,2025]
for ano in lista_de_anos:
    print(f'Ano da lista: {ano}')

##SOMA DE NÚMEROS IMPARES V1
soma = 0
for numero in lista_de_numeros:
    if numero % 2 != 0:
        soma = soma + numero
        print(f'Soma: {soma}')
##SOMA DE NÚMEROS IMPARES V ALURA
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

##IMPRIMIR NÚMEROS EM ORDEM DECRESCENTE V1
lista_de_numeros.sort(reverse=True)
for numero in lista_de_numeros:
    print(f'Número da lista: {numero}')
##IMPRIMIR NÚMEROS EM ORDEM DECRESCENTE V ALURA
for i in range(10, 0, -1):
    print(i)

##TABUADA
try:
    numero_tabuada = int(input('Digite um número para calcular sua tabuada: '))
    for i in range(10):
        print(numero_tabuada * (i+1))
except:
    print('Numero digitado é inválido!')

##TESTE DOS ELEMENTOS DA LISTA E SOMA E MÉDIA
lista_de_numeros_2 = [10,12,13,'Nome',14]
soma = 0
i = 0
for numero in lista_de_numeros_2:
    try:
        soma = soma + int(numero)
        i = i + 1
    except:
        pass
print(f'Soma: {soma}, Média {soma / i}')

##TESTE COM LISTA VAZIA - ALURA
lista_valores = [10,'cASA']
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}") 