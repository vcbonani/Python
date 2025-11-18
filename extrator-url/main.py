url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

##Sanitização da URL
#url = url.replace(" ","") ##substitui uma string por outro valor
url = url.strip() ##remove espaços em branco a direita, esquerda da string e também caracteres especiais

##Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

##busca os caracteres dentro da cadeia de strings
##0 é a posição inicial
##19 é a posição final, porém mostra o caractere na posição final -1 -> 18

##Separa base e os parâmetros
indice_interrogacao = url.find("?") ##o find localiza a primeira posição de um caractere/string na string
url_base = url[:indice_interrogacao] ##omitir a posição inicial ou a final, assume-se que será pego desde o início ou até o final
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

##Busca o valor de um parâmetro
parametro_busca = "quantidade" ##parâmetro de busca
indice_parametros = url_parametros.find(parametro_busca) ##posição do parâmetro na url
indice_valor = indice_parametros + len(parametro_busca) + 1 ##posição do valor do parâmetro na url
indice_e_comercial = url_parametros.find("&", indice_valor) ##localiza se há um & na url a partir de uma posição
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:] ##caso não tenha mais & - busca o valor até o final da url
else:
    valor = url_parametros[indice_valor:indice_e_comercial] ##caso ainda tenha & - busca o valor até o próximo &
print(valor)

print(url.startswith("https"))
print(url_base)
print(url_base.endswith("/cambio"))