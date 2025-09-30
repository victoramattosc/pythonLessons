"""Implementação integrada dos exercícios da questão 1."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Iterable

Numero = int | float


class Instrumento(ABC):
    """Representa um instrumento musical com volume controlado."""

    def __init__(self, volume: int) -> None:
        if not 0 <= volume <= 100:
            raise ValueError("O volume deve estar entre 0 e 100.")
        self.volume = volume

    @abstractmethod
    def tocar(self) -> str:
        """Retorna a descrição do som produzido pelo instrumento."""

    def info(self) -> str:
        """Retorna informações básicas sobre o instrumento."""
        return f"Volume: {self.volume} dB"


class Guitarra(Instrumento):
    """Guitarra elétrica simples."""

    def tocar(self) -> str:
        return f"A guitarra está tocando em {self.volume} dB com distorção moderada."


class Bateria(Instrumento):
    """Bateria acústica com batida marcante."""

    def tocar(self) -> str:
        return f"A bateria está tocando em {self.volume} dB com batida marcante."


def _argumentos_numericos(args: tuple[Any, ...], kwargs: dict[str, Any]) -> Iterable[Numero]:
    """Itera sobre todos os valores numéricos presentes em args e kwargs."""
    for valor in args:
        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            yield valor
    for valor in kwargs.values():
        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            yield valor


def limita_intervalo(minimo: Numero, maximo: Numero) -> Callable[[Callable[..., Numero]], Callable[..., Numero]]:
    """Decorator que garante que os valores numéricos estejam em um intervalo."""

    def decorator(func: Callable[..., Numero]) -> Callable[..., Numero]:
        def wrapper(*args: Any, **kwargs: Any) -> Numero:
            for valor in _argumentos_numericos(args, kwargs):
                if not minimo <= valor <= maximo:
                    raise ValueError(
                        f"Valor {valor} fora do intervalo permitido [{minimo}, {maximo}]."
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def _media(nums: Iterable[Numero]) -> float:
    """Calcula a média aritmética de uma sequência numérica."""
    total = 0.0
    quantidade = 0
    for numero in nums:
        total += float(numero)
        quantidade += 1
    if quantidade == 0:
        raise ValueError("É necessário informar ao menos um número para a média.")
    return total / quantidade


@limita_intervalo(0, 100)
def media_aritmetica(*nums: Numero) -> float:
    """Retorna a média aritmética simples de valores entre 0 e 100."""
    return _media(nums)


@limita_intervalo(0, 10_000)
def porcentagem(parte: Numero, total: Numero) -> float:
    """Calcula a porcentagem de um valor em relação ao total informado."""
    if total == 0:
        raise ValueError("O total não pode ser zero para calcular porcentagem.")
    return (float(parte) / float(total)) * 100


def executar_exemplos() -> list[str]:
    """Retorna mensagens ilustrando o uso das classes e funções."""
    mensagens: list[str] = []

    instrumentos: list[Instrumento] = [Guitarra(70), Bateria(85)]
    for instrumento in instrumentos:
        mensagens.append(instrumento.tocar())
        mensagens.append(instrumento.info())

    mensagens.append(f"Média aritmética: {media_aritmetica(10, 20, 30)}")
    mensagens.append(f"Porcentagem: {porcentagem(25, 50)}")

    for descricao, chamada in (
        ("media_aritmetica", lambda: media_aritmetica(-1, 50)),
        ("porcentagem", lambda: porcentagem(12_000, 100)),
    ):
        try:
            chamada()
        except ValueError as erro:
            mensagens.append(f"Erro esperado em {descricao}: {erro}")

    return mensagens


if __name__ == "__main__":
    for mensagem in executar_exemplos():
        print(mensagem)
