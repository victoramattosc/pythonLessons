"""Implementação integrada dos exercícios da questão 2."""

from __future__ import annotations

from abc import ABC, abstractmethod
import math
from typing import Any, Callable

Numero = int | float


class Animal(ABC):
    """Representa um animal com velocidade máxima."""

    def __init__(self, velocidade: Numero) -> None:
        if velocidade <= 0:
            raise ValueError("A velocidade deve ser positiva.")
        self.velocidade = float(velocidade)

    @abstractmethod
    def mover(self) -> str:
        """Retorna a descrição do movimento do animal."""

    def info(self) -> str:
        """Retorna informações gerais do animal."""
        return f"Velocidade máxima: {self.velocidade:g} km/h"


class Guepardo(Animal):
    """Guepardo veloz."""

    def mover(self) -> str:
        return f"O guepardo corre a até {self.velocidade:g} km/h."


class Tartaruga(Animal):
    """Tartaruga tranquila."""

    def mover(self) -> str:
        return f"A tartaruga anda a até {self.velocidade:g} km/h."


def valida_positivo(func: Callable[..., Numero]) -> Callable[..., Numero]:
    """Decorator que garante que todos os argumentos numéricos sejam positivos."""

    def wrapper(*args: Any, **kwargs: Any) -> Numero:
        for valor in list(args) + list(kwargs.values()):
            if isinstance(valor, (int, float)) and not isinstance(valor, bool):
                if valor <= 0:
                    raise ValueError("Todos os valores devem ser positivos.")
        return func(*args, **kwargs)

    return wrapper


@valida_positivo
def logaritmo_natural(x: Numero) -> float:
    """Calcula o logaritmo natural de um número positivo."""
    return math.log(float(x))


@valida_positivo
def proporcao(a: Numero, b: Numero) -> float:
    """Retorna a proporção entre dois valores positivos."""
    return float(a) / float(b)


def executar_exemplos() -> list[str]:
    """Retorna mensagens demonstrando os exercícios da questão."""
    mensagens: list[str] = []

    animais: list[Animal] = [Guepardo(100), Tartaruga(2)]
    for animal in animais:
        mensagens.append(animal.mover())
        mensagens.append(animal.info())

    mensagens.append(f"Logaritmo natural: {logaritmo_natural(2.71828):.2f}")
    mensagens.append(f"Proporção: {proporcao(4, 2)}")

    for descricao, chamada in (
        ("logaritmo_natural", lambda: logaritmo_natural(-1)),
        ("proporcao", lambda: proporcao(4, 0)),
    ):
        try:
            chamada()
        except ValueError as erro:
            mensagens.append(f"Erro esperado em {descricao}: {erro}")

    return mensagens


if __name__ == "__main__":
    for mensagem in executar_exemplos():
        print(mensagem)
