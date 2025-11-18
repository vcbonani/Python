numero_escolhido = int(input('Insira um número: '))
if numero_escolhido % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')

idade_usuario = int(input('Qual é a sua idade? '))
if 0 <= idade_usuario <= 12:
    print('Você é uma criança!')
elif 13 <= idade_usuario <= 18:
    print('Você é um adolescente!')
elif idade_usuario > 18:
    print('Você é um adulto!')

usuario_banco = 'admin'
senha_banco = 'admin'
usuario_parametro = input('Digite seu usuário: ')
senha_parametro = input('Digite sua senha: ')
if usuario_parametro == usuario_banco:
    if senha_parametro == senha_banco:
        print('Acesso garantido!')
    else:
        print('Senha errada!')
else:
    print('Usuário inexistente!')

print('Informe as coordenadas x e y de seu ponto: ')
x = int(input('Informe a coordenada X: '))
y = int(input('Informe a coordenada Y: '))
if x > 0 and y > 0:
    print('O ponto está no primeiro quadrante')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante')
elif x < 0 and y < 0:
    print('AO ponto está no terceiro quadrante')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem')