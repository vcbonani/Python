class Sistema:

    def __init__(self):
        self.texto = ""

    def le_entrada(self):
        self.texto = input("Digite um texto: ")

    def exibe_saida(self):
        print("O texto digitado foi: {}".format(self.texto))