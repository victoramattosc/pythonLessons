# Simulado Python (5 exercícios)

## Estrutura
- `ex1_transporte.py` — ABC `Transporte`, subclasses `Carro` e `Bicicleta` com `mover()` e `info()`.
- `test_ex2_transporte.py` — testes `pytest` para o Exercício 1.
- `ex3_decorators.py` — decorator `valida_positivo`, `raiz_quadrada` e `divisao`.
- `ex4_entregas.py` — `PedidoEntrega` (dataclass), `Temporizador` (context manager), `planejar_lotes` (generator).
- `ex5_integracao.py` — integração: escolhe transporte e simula rota, salvando um JSON.

## Como rodar
```bash
# (opcional) criar venv e ativar...
pip install -r requirements.txt

# Exercício 1 (demonstração)
python ex1_transporte.py

# Exercício 2 (testes)
pytest -q

# Exercício 3 (demonstração)
python ex3_decorators.py

# Exercício 4 (demonstração)
python ex4_entregas.py

# Exercício 5 (demonstração)
python ex5_integracao.py
```
