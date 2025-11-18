endereco = "rua alzimar vargas batista, 386, parque continental, guarulhos, sp, 07077203"

import re #regular expression - RegEx - módulo para trabalhar com expressões regulares

#padrão do cep no Brasil => 5 dígitos + - (opcional) + 3 dígitos => 99999-999 ou 99999999

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
#método compile recebe uma string com parâmetros para estabelecer um padrão de uma string desejada
#o ? após um parâmetro o estabelece como opcional
#as {número} falam quantas vezes aquele parâmetro se repete em seguida
#é possível quantificar de quantas vezes até quantas vezes um parâmetro se repete {de, até}
#o hífen no parâmetro permite passar um intervalo
busca = padrao.search(endereco) #na string vai encontrar o padrão (match); se não encontrar retorna none
if busca:
    cep = busca.group() #retorna a string encontrada no padrão
    print(cep)