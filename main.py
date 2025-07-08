
class financas:
    def __init__(self):
        self.saldo = 0
        self.ganhos = []
        self.despesas = []


    def saldo(self):
        if not self.despesas and not self.ganhos: # lista vazia
            print(f"Saldo igual a {self.saldo}") 
            return self.saldo
        else:
            self.atualizaSaldo()
            print(f"Saldo igual a {self.saldo}")


    def ganhos(self):
        adicionarGanho = float(input("Quanto quer adicionar?"))
        self.ganhos.append(adicionarGanho)
        print(f" Adicionado  R$ {adicionarGanho} com sucesso!")
        return adicionarGanho
    
    def despesas(self):
        adicionarDespesa = float(input("Quanto quer adicionar?"))
        self.despesas.append(adicionarDespesa)
        print(f" Adicionado  R$ {adicionarDespesa} com sucesso!")
        return self.despesas

    def atualizaSaldo(self):
        self.saldo = sum(self.ganhos) - sum(self.despesas)
        return self.saldo


financas = financas()

nome = input("Qual seu nome? ")
while True:
            print("Bem vindo " + nome + " ao MOOBY")
            print("------------------------------------")
            print("1 - quanto tenho de dinheiro?")
            print("------------------------------------")
            print("2 - Adicionar Ganhos")
            print("------------------------------------")
            print("3 -  Adicionar Despesas")
            print("------------------------------------")
            print("0 - sair")   

            opcao = int(input("O que deseja fazer agora?"))

            if opcao == 1:
                    Financas.saldo()

            elif opcao == 2:
                    Financas.ganhos()

            elif opcao == 3:
                    Financas.despesas()

            else:
                    print("Fechando MOOBY!")
                    break




