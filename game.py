from time import sleep
from typing import List, Dict


from models.jogador import Jogador
from models.mundos import Mundos

jogadores: List[Jogador] = []

def main() -> None:
    menu()

def menu() -> None:
    print("-- Welcome to the world of Parades --")


    print('1 - Logar')
    print('2 - Cadastrar')
    print('3 - Rank')
    print('4 - Sair do jogo')

    opcao: int = int(input("Escolha a opção: "))

    if opcao == 1:
        logar()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        rank()
    elif opcao == 4:
        sair()
    else:
        print("Nenhuma opção válida selecionada.")
        sleep(2)
        menu()

def logar() -> None:
    pass

def cadastrar() -> None:
    print(' -- Cadastro -- ')

    nome: str = input('Qual seu nome? ')
    print('-------------------')    
    sleep(1)
    classe: str = input(f'{nome}, e qual seria sua classe?\n- Mago\n- Guerreiro\n- Arqueiro\n- Tanker\nQual sua escolha? ')
    print('-------------------')
    sleep(1)
    level: int = input("Qual seu level?\n- Novato\n- Pleno\n- Profissional\n")
    print('-------------------')

    jogador: Jogador = Jogador(nome, classe, level)

    if classe == 'Mago':
        jogadores.append(jogador)
        print(f'O Jogador {jogador.nome} foi cadastrado com sucesso.')
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Guerreiro':
        jogadores.append(jogador)
        print(f'O Jogador {jogador.nome} foi cadastrado com sucesso.')
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Arqueiro':
        jogadores.append(jogador)
        print(f'O Jogador {jogador.nome} foi cadastrado com sucesso.')
        print('-------------------')
        sleep(2)
        menu()        
    elif classe == 'Tanker':
        jogadores.append(jogador)
        print(f'O Jogador {jogador.nome} foi cadastrado com sucesso.')
        print('-------------------')
        sleep(2)
        menu()
    else:
        print('-----------> Classe inválida. <-------------')
        sleep(3)
        menu()

def rank() -> None:
    if len(jogadores) > 0:
        print("Listagem de contas")
    
        for jogador in jogadores:
            print('-----------------')
            print(jogador)
            print('-----------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()

def sair() -> None:
    exit()

if __name__ == '__main__':
    main()
