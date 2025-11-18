class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property ##isso diz que se trata de uma propriedade e não exige os () após o nome da função, define como um getter
    def nome(self):
        return self.__nome.title() ##title coloca a primeira letra como maiúscula

    @nome.setter ##isso define a função como um setter
    def nome(self, nome):
        self.__nome = nome