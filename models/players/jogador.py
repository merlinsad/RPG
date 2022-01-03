class Jogador:
    contador: int = 1
    contador_level: int = 1

    def __init__(self: object, nome: str, classe: str, categoria: str) -> None:
        self.__codigo: int = Jogador.contador
        self.__nome: str = nome
        self.__classe: str = classe
        self.__level: int = Jogador.contador_level
        self.__categoria: str = categoria
        Jogador.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def classe(self: object) -> str:
        return self.__classe

    @property
    def level(self: object) -> int:
        return self.__level

    @property
    def categoria(self: object) -> str:
        return self.__categoria

    def __str__(self) -> str:
        return f'Codigo: {self.codigo}\nJogador: {self.nome}\nClasse: {self.classe}\nLevel: {self.level}\nCategoria:' \
               f' {self.__categoria}'
