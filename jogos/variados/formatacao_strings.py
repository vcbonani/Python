print("Tentativa {} de {}".format("primeira","segunda"))

print("Tentativa {1} de {0}".format("primeira","segunda"))

print("R$ {:.2f}".format(1.59))

print("R$ {:.2f}".format(1234.5))

print("R$ {:7.2f}".format(34.5))

print("R$ {:07.2f}".format(34.5))

print("R$ {:07d}".format(5))

print("R$ {:7d}".format(5))

print("Data {:2d}/{:2d}".format(9,4))
print("Data {:02d}/{:02d}".format(19,4))

##Documentação de strings https://docs.python.org/3/library/string.html#formatexamples

print("R$ {:6.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))

nome = "Vinicius"
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')
print(f'Meu nome é {nome.upper()}')