# Utilizando o sistema de transporte do Exercício 1, crie testes unitários em Python com pytest:

# Teste se um objeto Carro(5) possui capacidade igual a 5.
# Teste se o método mover() de Carro retorna a string correta.
# Teste se o método mover() de Bicicleta retorna a string correta.
# Crie também um teste de falha proposital para verificar se a criação de um Carro com capacidade negativa (Carro(-3)) 
# gera um erro ou comportamento esperado.

import pytest
from ex1_transporte import Carro, Bicicleta

def test_capacidade_carro():
    c = Carro(5)
    assert c.capacidade == 5

def test_mover_carro():
    c = Carro(5)
    assert c.mover() == "O carro está se movendo com até 5 passageiros"

def test_mover_bicicleta():
    b = Bicicleta(1)
    assert b.mover() == "A bicicleta está se movendo com até 1 pessoas"

def test_carro_capacidade_negativa():
    with pytest.raises(ValueError):
        Carro(-3)
