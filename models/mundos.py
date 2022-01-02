class Mundos:
    def __init__(self: object, nome: str, classe: str) -> None:
        self.__nome: str = nome
        self.__classe: str = classe

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def classe(self: object) -> str:
        return self.__classe
        
    @property
    def historia(self: object) -> str:
        return self.__historia

    def __str__(self) -> str:
        return f'Mapa: {self.nome}\nClasse: {self.classe}\nHistória: {self.história}'