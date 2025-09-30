"""Implementação integrada do sistema de biblioteca da questão 3."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable

Numero = int | float


class ItemBiblioteca(ABC):
    """Item base da biblioteca."""

    def __init__(self, titulo: str) -> None:
        if not self.titulo_valido(titulo):
            raise ValueError("O título deve ser uma string não vazia.")
        self.titulo = titulo

    @staticmethod
    def titulo_valido(titulo: str | None) -> bool:
        """Verifica se um título é válido (não vazio)."""
        return isinstance(titulo, str) and titulo.strip() != ""

    @abstractmethod
    def descricao(self) -> str:
        """Retorna a descrição do item da biblioteca."""


class Livro(ItemBiblioteca):
    """Livro disponível para empréstimo."""

    def __init__(self, titulo: str, paginas: int) -> None:
        super().__init__(titulo)
        if paginas <= 0:
            raise ValueError("Um livro deve ter pelo menos uma página.")
        self.paginas = paginas

    def descricao(self) -> str:
        return f"Livro: '{self.titulo}' com {self.paginas} páginas."


class Revista(ItemBiblioteca):
    """Revista periódica."""

    def __init__(self, titulo: str, edicao: int) -> None:
        super().__init__(titulo)
        if edicao < 1:
            raise ValueError("A edição da revista deve ser maior ou igual a 1.")
        self.edicao = edicao

    def descricao(self) -> str:
        return f"Revista: '{self.titulo}' edição {self.edicao}."


def somente_positivos(func: Callable[..., Numero]) -> Callable[..., Numero]:
    """Decorator que garante que todos os números recebidos sejam positivos."""

    def wrapper(*args: Any, **kwargs: Any) -> Numero:
        for valor in list(args) + list(kwargs.values()):
            if isinstance(valor, (int, float)) and not isinstance(valor, bool):
                if valor <= 0:
                    raise ValueError("Todos os números devem ser positivos.")
        return func(*args, **kwargs)

    return wrapper


@somente_positivos
def tempo_de_leitura(paginas: int, paginas_por_hora: int) -> float:
    """Calcula o tempo necessário para ler um livro em horas."""
    return paginas / paginas_por_hora


@somente_positivos
def proporcao_emprestimos(emprestados: int, total: int) -> float:
    """Calcula a proporção de itens emprestados."""
    return emprestados / total


def executar_exemplos() -> list[str]:
    """Retorna mensagens ilustrando o uso do sistema da biblioteca."""
    mensagens: list[str] = []

    itens: list[ItemBiblioteca] = [Livro("Python Básico", 180), Revista("Ciência Hoje", 42)]
    for item in itens:
        mensagens.append(item.descricao())

    mensagens.append(f"Tempo de leitura (h): {tempo_de_leitura(180, 60)}")
    mensagens.append(
        f"Proporção de empréstimos: {proporcao_emprestimos(30, 50)}"
    )

    for descricao, chamada in (
        ("tempo_de_leitura", lambda: tempo_de_leitura(0, 60)),
        ("proporcao_emprestimos", lambda: proporcao_emprestimos(30, 0)),
    ):
        try:
            chamada()
        except ValueError as erro:
            mensagens.append(f"Erro esperado em {descricao}: {erro}")

    return mensagens


if __name__ == "__main__":
    for mensagem in executar_exemplos():
        print(mensagem)
