# Exercício 2

# Utilizando o sistema de transporte do Exercício 1, crie testes unitários em Python com pytest:

# Teste se um objeto Carro(5) possui capacidade igual a 5.
# Teste se o método mover() de Carro retorna a string correta.
# Teste se o método mover() de Bicicleta retorna a string correta.
# Crie também um teste de falha proposital para verificar se a criação de um Carro com capacidade 
# negativa (Carro(-3)) gera um erro ou comportamento esperado.

import pytest
from simulado import Carro, Bicicleta

def test_carro_igual_a_cinco():
    carro = Carro(5)
    assert carro.capacidade == 5
    
def test_carro_mover():
    carro = Carro(5)
    assert carro.mover() == "O carro está se movendo com até 5 passageiros"  
    
def test_bicleta_mover():    
    bicicleta = Bicicleta(2)
    assert bicicleta.mover() == "A bicicleta está se movendo com até 2 pessoas"
    
def test_falha_carro():
    with pytest.raises(ValueError):
        Carro(-3)
    
        