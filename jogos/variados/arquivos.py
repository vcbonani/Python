#manipulacao de arquivos texto
arquivo = open("../palavras.txt", "w") #w de escrita, r de leitura, a de adicionar (append)
arquivo.write("banana") #escrita no arquivo
arquivo.write("melancia")
arquivo.close() #sempre importante fechar o arquivo após o uso


arquivo = open("../palavras.txt", "a")
arquivo.write("maca\n")
arquivo.write("pera\n")
arquivo.close()

arquivo = open("../palavras.txt")
for linha in arquivo: #percorrer um arquivo
    print(linha)
linha = arquivo.readline() #ler cada linha
linha = arquivo.read() #lê o arquivo inteiro de uma vez