# Questão 2 — Animais, Testes e Decorator Positivo

## Enunciado

### Exercício 1

Implemente um sistema de animais em Python utilizando classes abstratas:

- Crie uma classe abstrata `Animal` com um atributo `velocidade`, um método abstrato `mover()` e um método concreto `info()` que exibe a velocidade.
- Crie duas subclasses:
  - `Guepardo`, que imprime "O guepardo corre a até X km/h.".
  - `Tartaruga`, que imprime "A tartaruga anda a até X km/h.".
- No programa principal, crie objetos das duas subclasses, adicione-os em uma lista e invoque `mover()` e `info()` para cada um.

### Exercício 2

Utilizando o sistema de animais do Exercício 1, crie testes unitários em Python com pytest:

- Teste se um objeto `Guepardo(100)` possui `velocidade` igual a 100.
- Teste se o método `mover()` de `Guepardo(90)` retorna a string correta.
- Teste se o método `mover()` de `Tartaruga(2)` retorna a string correta.
- Crie também um teste de falha proposital para verificar se a criação de um `Guepardo` com velocidade negativa (`Guepardo(-10)`) gera um erro ou comportamento esperado.

### Exercício 3

Crie um decorator em Python chamado `valida_positivo` que verifica se todos os argumentos numéricos de uma função são positivos:

- Se todos os argumentos forem válidos, a função deve ser executada normalmente.
- Se algum argumento for negativo ou zero, deve ser levantado um `ValueError`.

Use esse decorator em pelo menos duas funções:

- `logaritmo_natural(x)`, que retorna `math.log(x)`.
- `proporcao(a, b)`, que retorna o resultado de `a / b`.

Teste chamando as funções com valores positivos (funcionam normalmente) e negativos/zero (gera erro).
