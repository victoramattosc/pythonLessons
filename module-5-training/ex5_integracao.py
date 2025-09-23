from __future__ import annotations
import json
from typing import Iterable, List
from ex1_transporte import Transporte, Carro, Bicicleta
from ex3_decorators import valida_positivo

class RegistroSimulacao:
    def __init__(self):
        self.eventos: List[dict] = []

    def add(self, **dados):
        self.eventos.append(dados)

    def salvar(self, caminho: str):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(self.eventos, f, ensure_ascii=False, indent=2)

def escolher_transporte(peso_kg: float) -> Transporte:
    # Heurística simples: cargas acima de 20kg usam Carro, do contrário Bicicleta
    return Carro(4) if peso_kg > 20 else Bicicleta(1)

@valida_positivo
def simular_rota(transporte: Transporte, distancia_km: float, velocidade_kmh: float) -> dict:
    tempo_h = distancia_km / velocidade_kmh
    return {
        "meio": transporte.__class__.__name__,
        "mensagem": transporte.mover(),
        "distancia_km": distancia_km,
        "velocidade_kmh": velocidade_kmh,
        "tempo_h": tempo_h,
    }

def rodar_simulacao(pedidos: Iterable[tuple[float, float]], saida_json: str = "simulacao.json") -> str:
    """Pedidos: Iterable de tuplas (peso_kg, distancia_km)."""
    registro = RegistroSimulacao()
    for i, (peso, distancia) in enumerate(pedidos, start=1):
        t = escolher_transporte(peso)
        res = simular_rota(t, distancia_km=distancia, velocidade_kmh=15 if t.__class__.__name__ == "Bicicleta" else 40)
        res["pedido"] = i
        registro.add(**res)
    registro.salvar(saida_json)
    return saida_json

if __name__ == "__main__":
    pedidos_demo = [(5.0, 3.0), (25.0, 10.0), (18.0, 7.0)]
    path = rodar_simulacao(pedidos_demo, "simulacao_demo.json")
    print(f"Arquivo gerado: {path}")
