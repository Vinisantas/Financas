import os


def pausar_menu():
    input("Pressione ENTER para continuar")




def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
