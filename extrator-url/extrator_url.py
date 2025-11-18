import re

class ExtratorURL:

    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url: ##verifica se a url é vazia; isso também se aplica caso seja passado um None
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametros = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametros + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&",indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def realiza_conversao(self):
        valor_dolar = 5.50
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        moeda_destino = self.get_valor_parametro("moedaDestino")
        quantidade = float(self.get_valor_parametro("quantidade"))
        if moeda_origem == "real" and moeda_destino == "dolar" and quantidade > 0:
            conversao = quantidade / valor_dolar
            return print(f"O valor de R${quantidade} em dólares é de: US${conversao:.2f}")
        elif moeda_origem == "dolar" and moeda_destino == "real" and quantidade > 0:
            conversao = quantidade * valor_dolar
            return print(f"O valor de US${quantidade} em reais é de: R${conversao:.2f}")
        else:
            raise ValueError("Os parâmetros passados estão incorretos")

    def __len__(self): ##sobrescrevendo o método especial de retornar o tamanho de uma string
        return len(self.url)

    def __str__(self): ##sobrescrevendo o método especial de retornar um objeto
        return "" + self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other): ##sobrescrevendo o método especial de comparação entre objetos
        return self.url == other.url



url1 = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url2 = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url1)
extrator_url_2 = ExtratorURL(url2)
print("O tamanho da URL é:", len(extrator_url))
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(id(extrator_url)) ##id permite ver o endereço de memória de um objeto instanciado
print(extrator_url == extrator_url_2)

extrator_url.realiza_conversao()
extrator_url_2.realiza_conversao()