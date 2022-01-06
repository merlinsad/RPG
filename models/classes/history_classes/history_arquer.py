class Arquer:
    codigo: int = 1
    level_arquer: int = 1
    atack_arquer: int = 250
    life_arquer: int = 400
    defense_arquer: int = 300
    magic_arquer: int = 250

    historia: str = 'Being of this class, you will have the best view of all, being possible to hit targets from ' \
                    'miles away, as you strengthen and improve your skills,\neach time you will be able to ' \
                    'strengthen your arrows, after all, in the world of Vesquer, all archers came of Elven ' \
                    'bloodlines, and thus, you can imbue your arrows with your powers,\nbeing possible, make ' \
                    'them quick as a bullet, set fire to it on contact, and many other skills still hidden, ' \
                    'so mysterious Elvish people, the Myers.'

    description: str = 'Being of this class, you will have the best view of all, being possible to hit targets from ' \
                       'miles away, as you strengthen and improve your skills,\neach time you will be able to ' \
                       'strengthen your arrows, after all, in the world of Vesquer, all archers came of Elven ' \
                       'bloodlines, and thus, you can imbue your arrows with your powers,\nbeing possible, make ' \
                       'them quick as a bullet, set fire to it on contact, and many other skills still hidden, ' \
                       'so mysterious Elvish people, the Myers.'

    def __init__(self: object, nome: str, categoria: str) -> None:
        self.__nome: str = nome
        self.__historia: str = Arquer.historia
        self.__ataque: int = Arquer.atack_arquer
        self.__vida: int = Arquer.life_arquer
        self.__defesa: int = Arquer.defense_arquer
        self.__magia: int = Arquer.magic_arquer
        self.__categoria: str = categoria
        self.__level: int = Arquer.level_arquer
        self.__description: str = Arquer.description

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
        return f'Archers what knowledge: {self.nome}\nHistoria: {self.historia}\nAtaque: {self.ataque}\n' \
               f'Defesa: {self.defesa}\n' \
               f'Vida: {self.vida}\nMagia: {self.magia}\nDescription: {self.description}'