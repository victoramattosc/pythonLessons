# Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos numéricos de uma função são positivos:

# Se todos os argumentos forem válidos, a função deve ser executada normalmente.
# Se algum argumento for negativo, deve ser levantado um ValueError.
# Use esse decorator em pelo menos duas funções:
# raiz_quadrada(x), que retorna a raiz quadrada de x.
# divisao(a, b), que retorna o resultado de a / b.
# Teste chamando as funções com valores positivos (funciona normalmente) e valores negativos (gera erro).

from __future__ import annotations
import math
from functools import wraps

def _is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def valida_positivo(func):
    """Decorator que garante que todos os argumentos numéricos sejam positivos."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if _is_number(arg) and arg < 0:
                raise ValueError(f"Argumento negativo não permitido: {arg}")
        for _, val in kwargs.items():
            if _is_number(val) and val < 0:
                raise ValueError(f"Argumento negativo não permitido: {val}")
        return func(*args, **kwargs)
    return wrapper

@valida_positivo
def raiz_quadrada(x: float) -> float:
    return math.sqrt(x)

@valida_positivo
def divisao(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    # Exemplos
    print("raiz_quadrada(9) =", raiz_quadrada(9))
    print("divisao(10, 2) =", divisao(10, 2))

    # Descomente para ver erros:
    # raiz_quadrada(-4)
    # divisao(10, -1)
