import forca
import adivinhacao_for

def escolhe_jogo():
    print("\n*****************")
    print("Escolha seu jogo!")
    print("*****************")

    print("\n(1) Forca (2) Adivinhação")

    jogo = int(input("\nQual jogo? "))

    if(jogo == 1):
        print("\nJogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("\nJogando adivinhação")
        adivinhacao_for.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()