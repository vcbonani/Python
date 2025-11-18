print('Python na Escola de Programação da Alura.')

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
print(f'Seu nome é {nome} e sua idade é {idade}')

print('A','L','U','R','A',sep='\n')

pi = 3.14159
#pi_arredondado = round(pi, 2) => poderia usar o round direto no print também ao invés de variável
#print(f'O valor arredondado de PI é {pi_arredondado}')

#outra forma de arredondar usando f string
print(f'O valor arredondado de PI é {pi:.2f}')