livros_vini = [['Banco MySQL'],['Certificação PHP', 'TDD PHP'],['HTML5 e CS3']]
print(livros_vini)

livros_pedro = livros_vini
print(livros_pedro)

livros_vini.append(['Jogos iOS'])
print(livros_vini)

print(livros_pedro)

print(livros_vini is livros_pedro)