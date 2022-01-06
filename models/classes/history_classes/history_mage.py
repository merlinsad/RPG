class Mage:
    codigo: int = 1
    level_mage: int = 1
    atack_mage: int = 150
    life_mage: int = 400
    defense_mage: int = 250
    magic_mage: int = 400

    def __init__(self: object, historia: str, nome: str, categoria: str) -> None:
        self.__nome: str = nome
        self.__codigo: int = Mage.codigo
        self.__historia: str = historia
        self.__ataque: int = Mage.atack_mage
        self.__vida: int = Mage.life_mage
        self.__defesa: int = Mage.defense_mage
        self.__magia: int = Mage.magic_mage
        self.__categoria: str = categoria

    def __str__(self: object) -> str:
        return f'Historia: {self.historia}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\n' \
               f'Vida: {self.vida}\nMagia: {self.magia}'

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
