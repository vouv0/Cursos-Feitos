class Caractere:
    def __init__(self, caractere):
        self.__caractere = ''
        self.caractere = caractere

    @property
    def caractere(self):
        return self.__caractere

    @caractere.setter
    def caractere(self, outro):
        if len(outro) > 1:
            raise Exception('Caractere deve ter no máximo tamanho 1.')
        self.__caractere = outro


letra = Caractere('b')
print(letra.caractere)
