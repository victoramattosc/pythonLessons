"""Testes do sistema de biblioteca da questão 3."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from exercicio import (  # noqa: E402
    ItemBiblioteca,
    Livro,
    Revista,
    proporcao_emprestimos,
    tempo_de_leitura,
)


def test_criacao_livro() -> None:
    livro = Livro("Python para Todos", 200)
    assert livro.descricao() == "Livro: 'Python para Todos' com 200 páginas."


def test_criacao_revista() -> None:
    revista = Revista("Ciência Hoje", 10)
    assert revista.descricao() == "Revista: 'Ciência Hoje' edição 10."


def test_titulo_invalido() -> None:
    with pytest.raises(ValueError):
        Livro("   ", 120)


def test_paginas_invalidas() -> None:
    with pytest.raises(ValueError):
        Livro("Python", 0)


def test_edicao_invalida() -> None:
    with pytest.raises(ValueError):
        Revista("Ciência Hoje", 0)


def test_metodo_estatico() -> None:
    assert ItemBiblioteca.titulo_valido("Algoritmos")
    assert not ItemBiblioteca.titulo_valido(" ")


def test_tempo_de_leitura_valido() -> None:
    assert tempo_de_leitura(120, 60) == 2


def test_tempo_de_leitura_invalido() -> None:
    with pytest.raises(ValueError):
        tempo_de_leitura(0, 60)


def test_proporcao_emprestimos_valido() -> None:
    assert proporcao_emprestimos(30, 60) == 0.5


def test_proporcao_emprestimos_invalido() -> None:
    with pytest.raises(ValueError):
        proporcao_emprestimos(30, 0)
