# Exercício 4

# Teste chamando as funções com valores positivos (funciona normalmente) e valores negativos (gera erro).

import pytest
from simulado3 import raiz_quadrada, divisao


def test_raiz_quadrada_good():
    assert raiz_quadrada(9) == 3

def test_raiz_quadrada_bad():
    with pytest.raises(ValueError):
        raiz_quadrada(-3)

def test_divisao_good():
    assert divisao(10, 2) == 5

def test_divisao_bad():
    with pytest.raises(ValueError):
        divisao(-10, 2)