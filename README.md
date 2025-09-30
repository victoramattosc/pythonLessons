# Visão Geral do Projeto

Este repositório reúne conteúdos para estudar Python voltado à prova: exemplos rápidos, módulos de aula, simulados e exercícios com testes automatizados. A ideia é ter um mapa completo para você saber **onde** praticar cada assunto e **como** validar seu código.

## Início rápido

1. Clone ou baixe o projeto e entre na pasta `pythonLessons/`.
2. (Opcional) Crie e ative um ambiente virtual: `python -m venv .venv` e `source .venv/bin/activate` (Linux/macOS) ou `.venv\Scripts\activate` (Windows).
3. Instale o `pytest` (e outras dependências quando o módulo tiver `requirements.txt`).
4. Rode os testes na raiz com `pytest` ou execute módulos isolados conforme descrito abaixo.

## Mapa das pastas principais

```text
pythonLessons/
├── helping.md          # Guia de estudos rápido (sintaxe, POO, decorators, testes)
├── helpers.py          # "Cheat sheet" com exemplos de código prontos
├── resume.md           # (este arquivo) Sumário global
├── lessons_modules/    # Conteúdo organizado por módulos temáticos
└── simulado/           # Scripts de simulados completos para praticar provas
```

## lessons_modules/

Cada módulo foca em um tema e, quando necessário, traz testes prontos.

### module-1-init
- `ex_1.py`, `ex_2.py`, `ex_3.py`: exemplos básicos de classes, métodos, propriedades e encapsulamento.
- Ótimo ponto de partida para revisar POO essencial antes de avançar.

### module-2-tests
- `ex_1.py` a `ex_3.py`: funções simples com exercícios de teste.
- Pasta `tests/` contendo `test_ex1.py`, `test_ex2.py`, `test_ex3.py` para praticar `pytest`.
- Use `pytest lessons_modules/module-2-tests` para focar apenas nesse módulo.

### module-3-decorators
- Três arquivos (`ex_1.py`, `ex_2.py`, `ex_3.py`) mostrando diferentes estilos de decorators.
- Inclui exemplos com funções internas, argumentos variáveis e reuso com `functools.wraps`.

### module-4-abstract-classes
- Exercícios sobre `abc.ABC`, métodos abstratos e hierarquias de classes.
- Ideal para fixar contratos obrigatórios e uso de `super()`.

### module-5-training
- Mini simulado com README explicando cada exercício.
- Arquivos chave:
  - `ex1_transporte.py`: exemplo completo de classes abstratas e subclasses.
  - `ex3_decorators.py`, `ex4_entregas.py`, `ex5_integracao.py`: integra decorators, generators, dataclasses e contexto (`with`).
- `requirements.txt`: dependências específicas (instale antes de rodar os scripts).
- Pasta `tests/` com `test_ex2_transporte.py` para validar o exercício de transporte.
- Rode `pytest -q` dentro da pasta para conferir apenas esse conjunto.

### module-6-exercices
Conjunto de questões maiores, cada uma com estrutura própria (`README.md`, `exercicio.py`, `tests/`).

- **questao-1**: sistema de instrumentos musicais com classes abstratas, decorator de validação e testes obrigatórios.
- **questao-2**: animais com validação de velocidade e decorator `valida_positivo`.
- **questao-3**: sistema de biblioteca completo usando método estático, decorator e suíte de testes.

> Cada questão sugere onde criar módulos (`instrumentos.py`, `decorators.py`, etc.) e os testes ficam em `tests/test_*.py`. Abra o README correspondente para detalhes do enunciado.

## simulado/

Scripts para revisar todos os tópicos de uma vez.

- `simulado.py`: transporte com classes abstratas e validações.
- `simulado3.py`, `simuladoTeste.py`, `simuladoTeste3.py`: variações do simulado para reforçar POO, decorators e testes.
- Use estes arquivos para treinar fluxo completo — implemente, depois crie seus próprios testes seguindo as dicas do `helping.md`.

## Outros arquivos úteis

- `helping.md`: manual prático com comandos de ambiente, revisão de sintaxe, POO, decorators, classes abstratas e guia de testes (incluindo quando rodar `pytest`).
- `helpers.py`: coleções de exemplos prontos (funções, classes, decorators, propriedades). Copie trechos para experimentos rápidos.

## Como escolher onde praticar

- **Preciso revisar teoria rapidamente:** leia `helping.md` e experimente os snippets do `helpers.py`.
- **Quero treinar um assunto específico:** abra o módulo correspondente em `lessons_modules/` e execute os arquivos `ex_*.py`.
- **Quero praticar testes:** use `module-2-tests` ou as pastas `tests/` de `module-5-training` e `module-6-exercices`.
- **Quero simular a prova inteira:** resolva um dos arquivos de `simulado/` ou siga uma questão completa de `module-6-exercices`.

## Dúvidas comuns

- **Onde criar novos testes?** Veja a seção 6.1 do `helping.md` para decidir em qual pasta salvar e quando rodar o `pytest`.
- **Erros de importação?** Rode `pytest` a partir da raiz do repositório para que os módulos sejam encontrados corretamente.
- **Sem tempo para tudo?** Foque primeiro em `module-5-training` (mistura vários temas) e depois valide com um dos simulados.

Boa prática e bons estudos! Simplifique os passos, experimente em blocos pequenos e rode os testes com frequência.
