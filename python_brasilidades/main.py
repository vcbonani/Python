# testa a lógica das classes

from Cpf_cnpj import Documento
from Telefones_Br import TelefonesBR

#cpf_um = Cpf("12345678901")
#print(cpf_um)
#cpf_dois = Cpf("39109149856")
#print(cpf_dois)

from validate_docbr import CNPJ

exemplo_cnpj = "50094090000103"
exemplo_cpf = "39109149856"

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
print(type(documento))

documento2 = Documento.cria_documento(exemplo_cpf)
print(documento2)
print(type(documento2))

#expressões regulares

import re

padrao = "[0-9][a-z]{2}[0-9]" # padrão a ser buscado
texto = "1231a21cc3aa1"       # texto a ser localizado
resposta = re.search(padrao,texto) #search busca o padrão no texto
print(resposta.group())

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "dsdasdaa vcbonani@gmail.com.br aiudhaisusa"
resposta = re.search(padrao,texto) #search traz só a primeira ocorrência
print(resposta.group())

padrao_telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto_telefone = "meu nome é vinicius e meu telefone 11987234450 e meu residencial era 1124564868"
resposta = re.findall(padrao_telefone,texto_telefone) #findall traz todas as ocorrências
print(resposta)


telefone_cadastro = "5521926481234"
telefone = TelefonesBR(telefone_cadastro)
print(telefone)

from Datas_Br import DatasBR

cadastro = DatasBR()
print(cadastro.tempo_cadastro())

from Acesso_CEP import BuscaEndereco

cep = "07077203"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.formata_cep())
bairro,cidade,uf = objeto_cep.acessa_via_cep()
print(bairro,cidade,uf)