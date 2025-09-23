import pytest
from exerc_3 import Conta, ValorInvalidoError, SaldoInsuficienteError, LimiteDiarioExcedidoError

def test_deposito_valido_aumenta_saldo():
    c = Conta()
    c.depositar(100)
    assert c.saldo == 100

def test_deposito_negativo_erro():
    c = Conta()
    with pytest.raises(ValorInvalidoError):
        c.depositar(-10)

def test_deposito_tipo_invalido_erro():
    c = Conta()
    with pytest.raises(TypeError):
        c.depositar("100")

def test_saque_valido_diminui_saldo():
    c = Conta(200)
    c.sacar(50)
    assert c.saldo == 150

def test_saque_acima_do_saldo_erro():
    c = Conta(30)
    with pytest.raises(SaldoInsuficienteError):
        c.sacar(100)

def test_limite_diario_excedido_erro():
    c = Conta(saldo=1000, limite_diario=500)
    c.sacar(300)
    with pytest.raises(LimiteDiarioExcedidoError):
        c.sacar(250)  # 300 + 250 > 500

def test_resetar_limite_diario():
    c = Conta(saldo=1000, limite_diario=500)
    c.sacar(400)
    c.resetar_limite_diario()
    c.sacar(200)  # deve passar após reset
    assert c.saldo == 400

def test_saque_negativo_erro():
    c = Conta(100)
    with pytest.raises(ValorInvalidoError):
        c.sacar(-1)

def test_saque_tipo_invalido_erro():
    c = Conta(100)
    with pytest.raises(TypeError):
        c.sacar(object())