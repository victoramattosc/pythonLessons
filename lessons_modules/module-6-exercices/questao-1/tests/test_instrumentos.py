"""Testes para os instrumentos musicais e funções decoradas."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from exercicio import Bateria, Guitarra, media_aritmetica, porcentagem  # noqa: E402


def test_volume_guitarra() -> None:
    guitarra = Guitarra(60)
    assert guitarra.volume == 60


def test_tocar_guitarra() -> None:
    guitarra = Guitarra(50)
    esperado = "A guitarra está tocando em 50 dB com distorção moderada."
    assert guitarra.tocar() == esperado


def test_tocar_bateria() -> None:
    bateria = Bateria(90)
    esperado = "A bateria está tocando em 90 dB com batida marcante."
    assert bateria.tocar() == esperado


def test_volume_invalido() -> None:
    with pytest.raises(ValueError):
        Bateria(-5)


def test_info() -> None:
    guitarra = Guitarra(40)
    assert guitarra.info() == "Volume: 40 dB"


def test_media_aritmetica_valida() -> None:
    assert media_aritmetica(10, 20, 30) == 20


def test_media_aritmetica_invalida() -> None:
    with pytest.raises(ValueError):
        media_aritmetica(-1, 50)


def test_porcentagem_valida() -> None:
    assert porcentagem(25, 50) == 50


def test_porcentagem_invalida() -> None:
    with pytest.raises(ValueError):
        porcentagem(12_000, 100)
