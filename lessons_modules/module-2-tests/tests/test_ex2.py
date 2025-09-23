import pytest
from ex_2 import aplicar_desconto, aplicar_descontos_em_cascata

def test_desconto_valido():
    assert aplicar_desconto(100, 10) == 90

def test_desconto_zero():
    assert aplicar_desconto(50, 0) == 50

def test_desconto_cem():
    assert aplicar_desconto(80, 100) == 0

def test_desconto_percentual_invalido_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(100, -5)

def test_desconto_percentual_invalido_maior_100():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 101)

def test_desconto_preco_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(-1, 10)

def test_cascata_basico():
    # 100 -> 90 (10%) -> 72 (20%)
    assert aplicar_descontos_em_cascata(100, [10, 20]) == 72

def test_cascata_com_tipo_invalido():
    with pytest.raises(TypeError):
        aplicar_descontos_em_cascata(100, ["10", 20])