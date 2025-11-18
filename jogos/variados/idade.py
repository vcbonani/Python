idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca = idade < 12
adolescente = idade > 12

print(type(maior_idade))

print(maior_idade,crianca,adolescente)

if(idade > 18):
    print("Voce e maior de idade")
else:
    if(idade < 12):
        print("Voce e uma crianca")
    elif(idade > 12):
        print("Voce e um adolescente")