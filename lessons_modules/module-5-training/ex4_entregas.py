# Crie uma classe Temporizador que funcione como context manager para medir o tempo de execução de um bloco de código.

# Em seguida, crie uma classe PedidoEntrega com os atributos id, distancia_km e peso_kg. Essa classe deve calcular o custo 
# estimado de entrega a partir de uma taxa base, de um valor por quilômetro e de um valor por quilo.

# Implemente também uma função planejar_lotes que receba uma lista de pedidos e um tamanho de lote, dividindo os pedidos em 
# grupos de tamanho fixo (o último lote pode ser menor).

# Por fim, teste o programa criando alguns pedidos, calculando o custo total usando o temporizador e exibindo os lotes planejados.

from __future__ import annotations
import time
from dataclasses import dataclass
from typing import Iterable, Iterator, List
from ex3_decorators import valida_positivo

class Temporizador:
    """Context manager simples para medir tempo de execução."""
    def __enter__(self):
        self._ini = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._ini

@dataclass
class PedidoEntrega:
    id: int
    distancia_km: float
    peso_kg: float

    def __post_init__(self):
        if self.id < 0:
            raise ValueError("id deve ser não-negativo")
        if self.distancia_km < 0 or self.peso_kg < 0:
            raise ValueError("distancia_km e peso_kg devem ser não-negativos")

    @valida_positivo
    def custo_estimado(self, taxa_base: float, por_km: float, por_kg: float) -> float:
        return taxa_base + self.distancia_km * por_km + self.peso_kg * por_kg

@valida_positivo
def planejar_lotes(pedidos: Iterable[PedidoEntrega], tamanho_lote: int) -> Iterator[list[PedidoEntrega]]:
    """Gera lotes de pedidos com tamanho fixo (último pode ser menor)."""
    lote: List[PedidoEntrega] = []
    for p in pedidos:
        lote.append(p)
        if len(lote) == tamanho_lote:
            yield lote
            lote = []
    if lote:
        yield lote

if __name__ == "__main__":
    pedidos = [
        PedidoEntrega(1, 10.0, 2.0),
        PedidoEntrega(2, 5.0, 1.2),
        PedidoEntrega(3, 20.0, 8.0),
        PedidoEntrega(4, 7.0, 0.5),
    ]
    with Temporizador() as t:
        total = sum(p.custo_estimado(5.0, 1.2, 0.8) for p in pedidos)
    print(f"Custo total: {total:.2f} (calculado em {t.elapsed:.6f}s)")

    for i, lote in enumerate(planejar_lotes(pedidos, 2), start=1):
        print(f"Lote {i}: {[p.id for p in lote]}")
