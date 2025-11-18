class Programa:  ## a classe Programa é a superclasse

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

    def __str__(self):  ##o __str__ é uma forma Pythonico de representar textualmente um objeto ao invés de usar print()
        return f'{self.__nome} - {self.ano} - {self.__likes} Likes'


class Filme(Programa):  ##a classe "mãe" entre parenteses representa a herança

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao  ##isso "extende" a classe mãe

    def __str__(self):  ##o __str__ é uma forma Pythonico de representar textualmente um objeto ao invés de usar print()
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'


class Serie(Programa):

    ##python data modelo - tdo método que inicia e termina com __
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  ##o __str__ é uma forma Pythonico de representar textualmente um objeto ao invés de usar print()
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'


##class Playlist(list): fazer isso ajuda a classe a herdar as propridades de uma list, por exemplo len()
class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        ##super().__init__(programas) passa para o inicializador da list a list dos programas

    ##o método com __ é um "dunder method"
    ##este comportamento como uma lista se chama "ducktyping"
    def __getitem__(self, item):  ##torna o objeto iterável sem a necessidade de herdar isso da list
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f'Nome da Playlist: {playlist_fim_de_semana.nome} - Tamanho: {len(playlist_fim_de_semana)} programas')
for programa in playlist_fim_de_semana:
    ## if "ternário" -> detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    ##o hasattr verifica se um determinado atributo existe na classe
    print(programa)
print(atlanta in playlist_fim_de_semana) ##verificar se um item existe na lista
