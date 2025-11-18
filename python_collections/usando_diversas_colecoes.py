from collections import Counter

texto1 = """
Você já se perguntou como funciona o processo de encantamento de clientes feito pelas empresas que se tornam referência para eles? Ou ainda como você pode implantar esse processo na sua empresa?

Saiba que é possível e é o que veremos neste guia!

Muitas empresas utilizam algumas táticas para encantar seus clientes, como atendimento personalizado, reconhecimento, senso de comunidade, entre outras. Vamos conhecer cada uma delas e entender como funcionam na prática. Também veremos neste artigo:

O que é encantamento e quais os diferenciais que estão atrelados a ele;
Como saber se as pessoas usuárias e clientes foram encantadas.
Vamos para a leitura!
"""

texto2 = """
A descoberta sobre uma vulnerabilidade crítica na biblioteca Log4j tem movimentado a vida de quem trabalha com desenvolvimento de software. A descoberta dessa falha de segurança também tem causado preocupação a diversas empresas e órgãos públicos.

O que exatamente significa Log4j?
O Log4j é uma biblioteca open source que faz parte do Apache Logging Services Project, mantida pela Apache Software Foundation. Essa biblioteca é amplamente utilizada em aplicações Java para fazer o processo de logging, que consiste em registrar dados dos envios de informações, processamentos, interações, resultados de operações ou outros dados da aplicação. Esses logs armazenados são usados geralmente para análises e monitoramento de alterações, inclusões, exclusões, erros e outras ações.

A falha de segurança ocorre pois permite que aplicativos registrem internamente uma string específica. Quando os logs são processados, essa string pode forçar o sistema a executar um script malicioso, permitindo que atacantes obtenham controle total, roubando dados, instalando malwares e realizando todo tipo de dano possível.
"""

#uma string se comporta como uma lista iterável de caracteres

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower()) #dicionário com a quantidade de aparições de cada letra
    total_de_caracteres = sum(aparicoes.values())

    aparicoes_proporcoes = [(letra, frequencia / total_de_caracteres) for letra,frequencia in aparicoes.items()]
    aparicoes_proporcoes = Counter(dict(aparicoes_proporcoes))
    mais_comuns = aparicoes_proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))


analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
