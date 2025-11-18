import os

#usar dicionário para manter o restaurante com nome e atributos
restaurantes = [{'nome':'Pizzaria do Zé', 'categoria':'Pizza', 'ativo':False},
                {'nome':'Sushi Okinawa', 'categoria':'Japonês', 'ativo':True},
                {'nome':'Churrascaria Rio Grande', 'categoria':'Churrasco', 'ativo':False}]

def exibir_subtitulo(texto):
      os.system('cls')
      linha = '*' * len(texto)
      print(linha)
      print(texto)
      print(linha)

def finalizar_app():
    exibir_subtitulo('Encerrando o app...')

def voltar_ao_menu_principal():
      input('\nAperte qualquer tecla para voltar ao menu principal...')
      main()

def opcao_invalida():
      print('Opção inválida!')
      voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Nome do restaurante: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Lista dos restaurantes cadastrados')
      mensagem = (f'{'NOME DO RESTAURANTE'.ljust(30)} | {'CATEGORIA'.ljust(30)} | {'Status'}')
      print(mensagem)
      print('-' * (len(mensagem) + 4))
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'{nome_restaurante.ljust(30)} | {categoria.ljust(30)} | {ativo}')
      voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
      exibir_subtitulo('Alternando o estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  #usando ternário
                  mensagem = f'O restaurante {restaurante['nome']} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante['nome']} foi desativado com sucesso!'
                  print(mensagem)
      if not restaurante_encontrado:
            print(f'O restaurante {nome_restaurante} não foi encontrado!')
      voltar_ao_menu_principal()

def exibir_nome_do_app():

      print('''
                  _                                                    
            | |                                                   
      ___  __ _| |__   ___  _ __    _____  ___ __  _ __ ___  ___ ___ 
      / __|/ _` | '_ \ / _ \| '__|  / _ \ \/ / '_ \| '__/ _ \/ __/ __|
      \__ \ (_| | |_) | (_) | |    |  __/>  <| |_) | | |  __/\__ \__ \/
      |___/\__,_|_.__/ \___/|_|     \___/_/\_\ .__/|_|  \___||___/___/
                                          | |                      
                                          |_|                      
            ''')

def exibir_opcoes():
      print('MENU\n')
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_do_restaurante()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    