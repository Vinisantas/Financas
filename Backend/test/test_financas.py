from models.Financas import Financas


def test_adicionar_receita():
    f = Financas()
    resultado = f.adicionar_receita(150, "gasolina", "carro")
    assert resultado == 150


def test_adicionar_despesa():
    f = Financas()
    resultado = f.adicionar_despesa(150, "Restaurante", "Comida")
    assert resultado == 150


def test_atualizar_saldo():
    f = Financas()
    f.adicionar_receita(200, "salário", "pagamento")
    f.adicionar_despesa(50, "alimentação", "almoço")
    f.atualizar_saldo()
    assert f.saldo == 150


def test_extrato():
    f = Financas()
    f.adicionar_receita(200, "salário", "pagamento")
    f.adicionar_despesa(150, "alimentação", "almoço")
    f.atualizar_saldo()
    f.extrato()
    assert f.saldo == 50


def test_transacao_salva():
    f = Financas()
    f.adicionar_receita(9999, "investimento", "lucro inesperado")
    f.adicionar_receita(500, "gasolina", "carro")
    f.adicionar_receita(1000, "comida", "almoço")

    ultima = f.transacao[-3]

    assert ultima["tipo"] == "receita"
    assert ultima["valor"] == 9999
    assert ultima["categoria"] == "investimento"
    assert ultima["descricao"] == "lucro inesperado"
