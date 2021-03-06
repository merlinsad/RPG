from os import sep
from time import sleep
from typing import List
from db.conectar import inserir_conta
from db.conectar import logar

from models.players.jogador import Jogador
from models.classes.history_classes.history_arquer import Arquer
from models.classes.history_classes.history_mage import Mage
from models.classes.history_classes.history_tank import Tank
from models.classes.history_classes.history_warrior import Warrior


jogadores: List[Jogador] = []
arquers: List[Arquer] = []
mages: List[Mage] = []
warriors: List[Warrior] = []
tanks: List[Tank] = []

archers_name: List = []
mages_name: List = []
warriors_name: List = []
tanks_name: List = []


def main() -> None:
    menu()


def menu() -> None:
    print("-- Welcome to the world of Parades --")

    print('1 - Logar')
    print('2 - Cadastrar')
    print('3 - Rank')
    print('4 - Rank por classe')
    print('5 - Sair do jogo')

    opcao: int = int(input("Escolha a opção: "))

    if opcao == 1:
        logar2()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        rank()
    elif opcao == 4:
        rank2()
    elif opcao == 5:
        sair()
    else:
        print("Choose a option existent.")
        sleep(2)
        menu()


def logar2() -> None:
    user: str = input("What's your username? ")
    logar(user)


def cadastrar():
    print(' -- Register -- ')

    nome: str = input("What's your name? ")
    print('-------------------')    
    sleep(1)
    classe: str = input(f'{nome}, e qual seria sua classe?\n- Mago\n- Guerreiro\n- Arqueiro\n- Tanker\n'
                        f'Qual sua escolha? ')
    print('-------------------')
    sleep(1)
    categoria: str = input("Qual seu level?\n- Novato\n- Pleno\n- Profissional\n---> ")

    jogador: Jogador = Jogador(nome, classe, categoria)
    arquer: Arquer = Arquer(nome, classe)
    mage: Mage = Mage(nome, classe, categoria)
    tank: Tank = Tank(nome, classe, categoria)
    warrior: Warrior = Warrior(nome, classe, categoria)

    if classe == 'Mago':
        jogadores.append(jogador)
        mages.append(mage)
        mages_name.append(nome)
        inserir_conta(nome, classe, categoria)
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Guerreiro':
        jogadores.append(jogador)
        warriors.append(warrior)
        warriors_name.append(nome)
        inserir_conta(nome, classe, categoria)
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Arqueiro':
        jogadores.append(jogador)
        arquers.append(arquer)
        archers_name.append(nome)
        inserir_conta(nome, classe, categoria)
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Tanker':
        jogadores.append(jogador)
        tanks.append(tank)
        tanks_name.append(nome)
        inserir_conta(nome, classe, categoria)
        print('-------------------')
        print('-------------------')
        sleep(2)
        menu()
    else:
        print('-----------> Wrong Class. <-------------')
        sleep(3)
        menu()


def rank() -> None:
    if len(jogadores) > 0:
        print("All players")
    
        for jogador in jogadores:
            print('-----------------')
            print(jogador)
            print('-----------------')
            sleep(1)
    else:
        print('Do not have any accounts in system.')
    retorno: str = input('If you wanna come back to the menu, just press "Enter", if you do now want, just not press ')
    if retorno == '':
        sleep(2)
        menu()


def rank2() -> None:
    if len(jogadores) > 0:
        wich_class: str = input("Wich class do you want to see the rank?\n- Mage\n- Warrior\n- Tank\n- Arquer\n--> ")
        if wich_class == 'Mage':
            print("Listagem de contas")
            for mage in mages:
                print('-----------------')
                print(f"Archers that we have knowledge:")
                print(*mages_name, sep=', ')
                print("----------------")
                print(mage)
                print('-----------------')
                sleep(1)
                retorno: str = input(
                    'If you wanna come back to the menu, just press "Enter", if you do now want, just not press ')
                print('----------------------------------/-----------------------------')
                if retorno == '':
                    sleep(2)
                    menu()
        elif wich_class == 'Warrior':
            for warrior in warriors:
                print('-----------------')
                print(f"Archers that we have knowledge:")
                print(*warriors_name, sep=', ')
                print("----------------")
                print(warrior)
                print('-----------------')
                sleep(1)
                retorno: str = input(
                    'If you wanna come back to the menu, just press "Enter", if you do now want, just not press ')
                print('----------------------------------/-----------------------------')
                if retorno == '':
                    sleep(2)
                    menu()
        elif wich_class == 'Arquer':
            for arquer in arquers:
                print('-----------------')
                print(f"Archers that we have knowledge:")
                print(*archers_name, sep=', ')
                print("----------------")
                print(arquer)
                print('-----------------')
                sleep(1)
                retorno: str = input(
                    'If you wanna come back to the menu, just press "Enter", if you do now want, just not press ')
                print('----------------------------------/-----------------------------')
                if retorno == '':
                    sleep(2)
                    menu()
        elif wich_class == 'Tank':
            for tank in tanks:
                print('-----------------')
                print(f"Archers that we have knowledge:")
                print(*tanks_name, sep=', ')
                print("----------------")
                print(tank)
                print('-----------------')
                sleep(1)
                retorno: str = input(
                    'If you wanna come back to the menu, just press "Enter", if you do now want, just not press ')
                print('----------------------------------/-----------------------------')
                if retorno == '':
                    sleep(2)
                    menu()
        else:
            print('Não existem contas cadastradas.')


def sair() -> None:
    exit()


if __name__ == '__main__':
    main()
