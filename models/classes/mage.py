class Mage:
    contador: int = 1
    contador_level: int = 1

    def __init__(self: object, historia: str, ataque: int, vida: int
                 , defesa: int, magia: int) -> None:
        self.__historia: str = historia
        self.__ataque: int = ataque
        self.__vida: int = vida
        self.__defesa: int = defesa
        self.__magia: int = magia

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