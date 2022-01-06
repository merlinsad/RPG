class Tank:
    codigo: int = 1
    level_tank: int = 1
    atack_tank: int = 250
    life_tank: int = 400
    defense_tank: int = 300
    magic_tank: int = 250

    def __init__(self: object, historia: str, nome: str, categoria: str) -> None:
        self.__nome: str = nome
        self.__codigo: int = Tank.codigo
        self.__nome: str = nome
        self.__historia: str = historia
        self.__ataque: int = Tank.atack_tank
        self.__vida: int = Tank.life_tank
        self.__defesa: int = Tank.defense_tank
        self.__magia: int = Tank.magic_tank
        self.__categoria: str = categoria

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
    def categoria(self: object) -> str:
        return self.__categoria

    def __str__(self: object) -> str:
        return f'Historia: {self.historia}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\n' \
               f'Vida: {self.vida}\nMagia: {self.magia}'