# Resumo rápido — Prova de Python

> **Foco da prova:** sintaxe essencial, POO (classes/objetos), decorators, classes e métodos abstratos, métodos estáticos e noções de testes com `pytest`.

---

## 1) Ambiente e comandos básicos

```bash
# (opcional) criar ambiente virtual
python -m venv .venv
# ativar (Windows)
.venv\Scripts\activate
# ativar (macOS/Linux)
source .venv/bin/activate

# instalar pytest
pip install pytest

# rodar os testes
pytest               # roda tudo
pytest -q            # saída silenciosa
pytest tests/test_x.py::test_func  # roda um teste específico
```

> **Dica:** mantenha o `requirements.txt` ou `pyproject.toml` com as dependências do projeto. Se perder o ambiente é só recriar
> com `pip install -r requirements.txt`.

**Estrutura simples de projeto**

```
meu_projeto/
  app/              # código fonte
    __init__.py
    models.py
    services.py
  tests/            # testes unitários
    test_models.py
    test_services.py
```

*Tudo em testes precisa conseguir importar o código principal.* Se der erro de importação, garanta que a raiz do projeto está no `PYTHONPATH` (por exemplo, rodando `pytest` a partir da raiz).

---

## 2) Sintaxe essencial

### Variáveis e tipos básicos

* Atribuição: `x = 10`, `nome = "Ana"`
* Tipos comuns: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`.
* F-strings para formatar: `f"Olá, {nome}!"`

```python
idade = 20          # int
altura = 1.75       # float
nome = "Ana"        # str
ativo = True        # bool

numeros = [1, 2, 3]               # list (mutável)
coordenada = (10, 20)             # tuple (imutável)
contatos = {"email": "a@b.com"}  # dict (chave -> valor)
unique = {1, 2, 2, 3}             # set (sem duplicados => {1,2,3})

print(f"{nome} tem {idade} anos")  # f-string
```

### Controle de fluxo

```python
# if/elif/else
nota = 7
if nota >= 6:
    status = "aprovado"
elif 4 <= nota < 6:
    status = "recuperação"
else:
    status = "reprovado"

# for
total = 0
for n in [1, 2, 3]:
    total += n

# while
contador = 0
while contador < 3:
    contador += 1
```

### Funções

*Retorne sempre que possível (em vez de só `printar`) para facilitar o teste automatizado.*

```python
def soma(a, b=0):            # b com valor padrão
    return a + b             # sempre retorne o resultado

# dica: nomes claros e parâmetros pequenos
resultado = soma(2, 3)
```

### Imports e módulos

```python
# importar módulo inteiro
import math
print(math.sqrt(9))

# importar algo específico
from math import sqrt
print(sqrt(16))
```

### Erros e exceções (básico)

```python
try:
    x = int("10")
except ValueError:            # capture o erro certo
    x = 0
```

**Boas práticas rápidas**

* Indentação com 4 espaços (sem tabs misturados).
* Nomes de variáveis/métodos em `snake_case`.
* Funções curtas, claras e com responsabilidade única.
* Use comentários curtos para explicar `"porquê"` algo existe (o `"como"` deve ser compreensível só lendo o código).
* Separe código em funções para facilitar testes e reaproveitamento.

---

## 3) Programação Orientada a Objetos (POO)

### Classe e objeto

```python
class Pessoa:
    def __init__(self, nome, idade):  # __init__ inicializa o objeto
        self.nome = nome              # use self para acessar atributos
        self.idade = idade

    def apresentar(self):             # método de instância
        return f"Sou {self.nome} e tenho {self.idade} anos"

p = Pessoa("Ana", 20)                 # cria objeto
print(p.apresentar())
```

**Dicas importantes**

* **Sempre** inclua `self` no primeiro parâmetro de métodos de instância.
* Atributos "privados" por convenção usam `_` (ex.: `_saldo`).
* Se for criar vários objetos com dados semelhantes, considere usar `@dataclass` (facilita criação de `__init__`, `__repr__`, etc.).

### Herança (básico)

```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)   # chama construtor da base
        self.cargo = cargo
```

*Use herança somente quando a relação "é um" fizer sentido (por exemplo, `Funcionario` **é um** `Pessoa`).*

---

## 4) Decorators (visão geral)

* **O que são?** Funções que recebem outra função e retornam uma nova função (com comportamento extra).
* **Sintaxe:** usar `@nome_do_decorator` acima da função que será decorada.

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}")
        return func(*args, **kwargs)  # mantenha comportamento original
    return wrapper

@log_calls
def somar(a, b):
    return a + b

somar(2, 3)  # imprime "Chamando somar"
```

> Dica: mantenha o wrapper simples e preserve assinatura/comportamento originais. Se precisar copiar metadata, use `functools.wraps`.

---

## 5) Classes Abstratas e Métodos Abstratos

* Use para **definir contrato** que as subclasses **devem** implementar.
* Módulo: `abc` (`ABC`, `@abstractmethod`).

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):           # contrato: toda Forma tem area()
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# f = Forma()            # ERRO: não pode instanciar classe abstrata
r = Retangulo(2, 3)
print(r.area())
```

### Métodos estáticos (`@staticmethod`)

* Pertencem à classe, **não** ao objeto. Não recebem `self`.
* Úteis para utilitários relacionados à classe, mas que **não** dependem do estado do objeto.

```python
class Validador:
    @staticmethod
    def eh_positivo(n):
        return n > 0

Validador.eh_positivo(10)  # True (sem instanciar)
```

> Observação: `@classmethod` existe, mas foque aqui em `@staticmethod` como pedido.

**Quando usar classe abstrata?**

* Quando você tem várias subclasses que precisam compartilhar a mesma interface (mesmos métodos obrigatórios).
* Para proibir instanciar uma classe `"genérica"` sem implementação concreta.

---

## 6) Testes Unitários com `pytest` (básico)

**Regras simples do pytest**

* Arquivos de teste: `test_*.py`.
* Funções de teste: `def test_alguma_coisa(): ...`
* Use `assert` simples.

```python
# app/calculadora.py

def soma(a, b):
    return a + b

# tests/test_calculadora.py
from app.calculadora import soma

def test_soma_basico():
    assert soma(2, 3) == 5       # assert claro e direto
```

**Dicas de teste**

* AAA (Arrange, Act, Assert): prepare dados, execute a função, faça asserções.
* Um cenário por teste; nomes de teste descritivos.
* Cobrir casos felizes e casos inválidos simples.

### 6.1) Quando criar e rodar testes com `pytest`

* **Criar um teste** sempre que implementar uma função/classe nova ou corrigir um bug — o teste impede que o erro volte.
* **Onde salvar:**
  * Testes rápidos unitários → `tests/` ao lado do código (`tests/test_nome_modulo.py`).
  * Exemplos de uso ou tutoriais → dentro da pasta do módulo (ex.: `module-2-tests/tests/`).
  * Scripts grandes ou simulados → podem ter uma subpasta `tests/` própria para manter isolamento.
* **Rodar os testes**:
  * Antes de commitar: `pytest` na raiz garante que nada quebrou.
  * Ao estudar uma lição: rode apenas o arquivo referente (ex.: `pytest lessons_modules/module-2-tests/tests/test_ex2.py`).
  * Ao explorar um bug difícil: use `-k` para filtrar (`pytest -k nome_do_teste`).
* **Se o teste quebrar:** leia a mensagem inteira, corrija o código **ou** ajuste o teste se o comportamento esperado mudou.
* **Tempo curto?** Execute primeiro os testes do módulo que você alterou; depois rode o conjunto completo quando tiver tempo.

---

## 7) Padrões e dicas rápidas para a prova

* Leia a mensagem de erro: ela geralmente diz **onde** e **o que** quebrou.
* Evite funções/métodos muito longos; quebre em partes.
* Em POO, pense: **quem** é responsável por **qual** ação.
* Decorator: mantenha foco — adicionar **comportamento extra** sem alterar a função original.
* Abstração: só use quando você **precisa** de um contrato comum entre várias subclasses.
* Testes: comece pelo caso mais simples; avance para variações.

---

## 8) Mini‑checklist antes de entregar

* [ ] Código com indentação consistente (4 espaços)
* [ ] Nomes em `snake_case`
* [ ] Métodos de instância com `self` corretamente
* [ ] Decorators simples e comentados
* [ ] Classes abstratas sem instanciar diretamente
* [ ] Testes passando com `pytest`

```
pytest -q
```
