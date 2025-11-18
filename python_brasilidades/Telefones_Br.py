import re

class TelefonesBR:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def valida_telefone(self,telefone):
        padrao_telefone = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao_telefone,telefone)
        if resposta:
            return True
        else:
            return False

    def __str__(self):
        return self.formata_telefone()

    def formata_telefone(self):
        padrao_telefone = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao_telefone,self.numero)
        numero_formatado = "+{} ({}) {}-{}".format(
            resposta.group(1),resposta.group(2),resposta.group(3),resposta.group(4)
        )
        return numero_formatado