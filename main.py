from models.Relatorios import Relatorios
from models.Routes import Financas 


nome = input("Digite seu nome: ")


financas = Financas()
relatorios = Relatorios(transacao=financas.transacao)


while True:

    print("\n")
    print(f"Bem vindo {nome} ao MOOBY")
    print("\n")
    print("1 - Mostrar Saldo")
    print("2 - Adicionar Entradas")
    print("3 - Adicionar Saídas")
    print("4 - Mostrar Histórico de Transações")
    print("5 - Gerar Relatório")
    print("0 - Sair")
    print("\n")

    try:
        opcao = int(input("O que deseja fazer agora? "))
    except ValueError:
        print("Digite uma opção válida!")
        continue

    print("\n")

    if opcao == 1:
        financas.extrato()
    elif opcao == 2:
        financas.adicionar_receita()
    elif opcao == 3:
        financas.adicionar_despesa()
    elif opcao == 4:
        if not financas.transacao:
            print("Nenhuma transação registrada.")
        else:
            print("Histórico de Transações:")
            for t in financas.transacao:
                print(f" dia: {t['data']} | tipo: {t['tipo']} | valor: R$ {t['valor']} | categoria: {t['categoria']} | descrição: {t['descricao']}")
                print("------------------------------------------")
    elif opcao == 5:
        print("\n")
        print("1- Categoria")
        print("\n")
        print("2- Mês")
        print("\n")
        print("3- Tipo")
        gerar_relatorio = input(("Qual relatório quer gerar?"))
        if gerar_relatorio == "1":
            relatorios.filtrar_por_categoria()
        elif gerar_relatorio == "2":
            relatorios.filtrar_por_mes()
        elif gerar_relatorio == "3":
            relatorios.filtar_por_tipo()
        else:
            print("Opção inválida. Tente novamente.")

    elif opcao == 0:
        print("\nFechando MOOBY!\n")
        break
    else:
        print("Opção inválida. Tente novamente.")




