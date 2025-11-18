from abc import ABC # abstract base classes
from collections.abc import MutableSequence
from numbers import Complex
from collections.abc import Sized

class Numero(Complex):
    def __getitem__(self, item):
        super().___getitem__()


class Minha_Listagem(Sized):
    def __init__(self,descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = Minha_Listagem()
print(lista)