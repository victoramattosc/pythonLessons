# arquivo: test_exemplo_facil.py
# Teste simples para validar soma de dois números

def soma(a, b):
    return a + b

def test_soma_basica():
    # Testa se 2 + 3 resulta em 5
    assert soma(2, 3) == 5

def test_soma_negativos():
    # Testa se -1 + (-4) resulta em -5
    assert soma(-1, -4) == -5
