print("\n**********")
print("Bem-vindo ao jogo de Adivinhação")
print("**********")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):

    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute_str = input("\nDigite o seu número: ")
    print("\nVocê digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("\nFim do jogo!")