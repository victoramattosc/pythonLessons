"""Testes para o sistema de animais e funções decoradas."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from exercicio import Guepardo, Tartaruga, logaritmo_natural, proporcao  # noqa: E402


def test_velocidade_guepardo() -> None:
    guepardo = Guepardo(100)
    assert guepardo.velocidade == 100


def test_mover_guepardo() -> None:
    guepardo = Guepardo(90)
    esperado = "O guepardo corre a até 90 km/h."
    assert guepardo.mover() == esperado


def test_mover_tartaruga() -> None:
    tartaruga = Tartaruga(2)
    esperado = "A tartaruga anda a até 2 km/h."
    assert tartaruga.mover() == esperado


def test_velocidade_invalida() -> None:
    with pytest.raises(ValueError):
        Guepardo(-10)


def test_logaritmo_natural_valido() -> None:
    assert logaritmo_natural(1) == 0


def test_logaritmo_natural_invalido() -> None:
    with pytest.raises(ValueError):
        logaritmo_natural(-1)


def test_proporcao_valida() -> None:
    assert proporcao(4, 2) == 2


def test_proporcao_invalida() -> None:
    with pytest.raises(ValueError):
        proporcao(4, 0)
