import pytest
from ex_1 import soma, dividir

def test_soma_inteiros():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -4) == -5

def test_soma_float():
    assert soma(2.5, 0.5) == 3.0

def test_soma_tipo_invalido():
    with pytest.raises(TypeError):
        soma("2", 3)

def test_dividir_basico():
    assert dividir(10, 2) == 5

def test_dividir_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_dividir_tipo_invalido():
    import pytest
    with pytest.raises(TypeError):
        dividir(10, "2")