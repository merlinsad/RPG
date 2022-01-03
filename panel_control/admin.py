from typing import List
from models.worlds.mundos import World

worlds: List[World] = []


def main() -> None:
    menu()


def menu() -> None:
    print("-- Welcome to the world of Parades --")

    print('Seja Bem vindo ADM')
    print('Confira abaixo sua lista de comandos: ')
    print('1 - Deletar conta')
    print('2 - Inserir conta ADM')
    print('3 - Adicionar pontos ao jogador')
    print('4 - Alterar informação do jogador')
    print('5 - Adicionar história')

    def deletar_conta() -> None:
        pass

    def inserir_conta_adm() -> None:
        pass

    def adicionar_pontos() -> None:
        pass

    def alterar_info() -> None:
        pass

    if __name__ == '__main__':
        menu()