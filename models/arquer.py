class Arqueiro:
    codigo: int = 1

    def __init__(self: object, historia: str, ataque: int, vida: int
                 , defesa: int, magia: int) -> None:
         pass
    
    def __str__(self: object) -> str:
        return f'Historia: {self.historia}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\nVida: {self.vida}\nMagia: {self.Magia}'