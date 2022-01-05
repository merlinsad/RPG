class Warrior:
    codigo: int = 1
    level_warrior: int = 1
    atack_warrior: int = 250
    life_warrior: int = 400
    defense_warrior: int = 300
    magic_warrior: int = 250

    def __init__(self: object, historia: str, name: str, categoria: str) -> None:
        self.__codigo: int = Warrior.codigo
        self.__name: str = name
        self.__historia: str = historia
        self.__ataque: int = Warrior.atack_warrior
        self.__vida: int = Warrior.life_warrior
        self.__defesa: int = Warrior.defense_warrior
        self.__magia: int = Warrior.magic_warrior
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
        return f'Historia: {self.historia}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\n'\
               f'Vida: {self.vida}\nMagia: {self.magia}'