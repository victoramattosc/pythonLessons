from __future__ import annotations
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, capacidade: int) -> None:
        if not isinstance(capacidade, int):
            raise TypeError("capacidade deve ser int")
        if capacidade < 0:
            raise ValueError("capacidade não pode ser negativa")
        self.capacidade = capacidade

    @abstractmethod
    def mover(self) -> str:
        """Retorna uma mensagem descrevendo o movimento do transporte."""

    def info(self) -> str:
        return f"Capacidade: {self.capacidade}"

class Carro(Transporte):
    def mover(self) -> str:
        return f"O carro está se movendo com até {self.capacidade} passageiros"

class Bicicleta(Transporte):
    def mover(self) -> str:
        return f"A bicicleta está se movendo com até {self.capacidade} pessoas"

if __name__ == "__main__":
    frota: list[Transporte] = [Carro(5), Bicicleta(1)]
    for t in frota:
        print(t.mover())
        print(t.info())
