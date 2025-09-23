"""Exercício 2 (médio): aplicar desconto com regras de validação.

Rode os testes com:
    pytest -q
"""

def aplicar_desconto(preco, percentual):
    """Aplica um desconto percentual sobre o preço.

    Args:
        preco (float): preço base (deve ser >= 0)
        percentual (float): entre 0 e 100

    Returns:
        float: preço final após desconto

    Levanta:
        TypeError: se tipos forem inválidos.
        ValueError: se preco < 0 ou percentual fora de [0, 100].
    """
    if not isinstance(preco, (int, float)):
        raise TypeError("preco deve ser numérico")
    if not isinstance(percentual, (int, float)):
        raise TypeError("percentual deve ser numérico")

    if preco < 0:
        raise ValueError("Preço não pode ser negativo")
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido (deve estar entre 0 e 100)")

    return preco * (1 - percentual / 100.0)

def aplicar_descontos_em_cascata(preco, percentuais):
    """Aplica uma sequência de descontos (em cascata).

    Ex.: preco=100, percentuais=[10, 20] -> 100 * 0.9 * 0.8 = 72

    Levanta:
        TypeError: se percentuais não for iterável numérico.
        ValueError: se algum percentual for inválido ou preco < 0.
    """
    if preco < 0:
        raise ValueError("Preço não pode ser negativo")
    total = float(preco)
    try:
        for p in percentuais:
            total = aplicar_desconto(total, p)
    except TypeError:
        raise TypeError("percentuais deve ser uma sequência de números")
    return total