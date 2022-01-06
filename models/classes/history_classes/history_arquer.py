class Arquer:
    codigo: int = 1
    level_arquer: int = 1
    atack_arquer: int = 250
    life_arquer: int = 400
    defense_arquer: int = 300
    magic_arquer: int = 250

    def __init__(self: object, historia: str, nome: str, categoria: str) -> None:
        self.__nome: str = nome
        self.__historia: str = historia
        self.__ataque: int = Arquer.atack_arquer
        self.__vida: int = Arquer.life_arquer
        self.__defesa: int = Arquer.defense_arquer
        self.__magia: int = Arquer.magic_arquer
        self.__categoria: str = categoria
        self.__level: int = Arquer.level_arquer

    @property
    def historia(self: object) -> str:
        return self.__historia

    @property
    def ataque(self: object) -> int:
        return self.__ataque

    @property
    def vida(self: object) -> int:
        return self.__vida

    @property
    def defesa(self: object) -> int:
        return self.__defesa

    @property
    def magia(self: object) -> int:
        return self.__magia

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def categoria(self: object) -> str:
        return self.__categoria

    @property
    def level(self: object) -> int:
        return self.__level

    def __str__(self: object) -> str:
        return f'Historia: {self.historia}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\n' \
               f'Vida: {self.vida}\nMagia: {self.magia}\n'