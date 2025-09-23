"""Exercício 3 (trabalhoso): classe Conta com estado e exceções específicas.

Rode os testes com:
    pytest -q
"""
from dataclasses import dataclass, field

class ValorInvalidoError(ValueError):
    """Erro para valores não positivos em operações financeiras."""

class SaldoInsuficienteError(ValueError):
    """Erro quando o saque excede o saldo disponível."""

class LimiteDiarioExcedidoError(ValueError):
    """Erro quando o valor sacado no dia excede o limite diário."""

@dataclass
class Conta:
    saldo: float = 0.0
    limite_diario: float = 1000.0
    _retirado_hoje: float = field(default=0.0, init=False, repr=False)

    def depositar(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("valor do depósito deve ser numérico")
        if valor <= 0:
            raise ValorInvalidoError("Depósito deve ser maior que zero")
        self.saldo += float(valor)

    def sacar(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("valor do saque deve ser numérico")
        if valor <= 0:
            raise ValorInvalidoError("Saque deve ser maior que zero")
        valor = float(valor)

        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente")

        if self._retirado_hoje + valor > self.limite_diario:
            raise LimiteDiarioExcedidoError("Limite diário excedido")

        self.saldo -= valor
        self._retirado_hoje += valor

    def resetar_limite_diario(self) -> None:
        """Reseta o acumulado diário (simula virada de dia)."""
        self._retirado_hoje = 0.0