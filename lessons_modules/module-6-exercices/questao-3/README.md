# Questão 3 — Sistema de Biblioteca

## Enunciado

### Exercício Único — Sistema de Biblioteca

Implemente um sistema simples de biblioteca em Python que atenda aos pontos abaixo:

#### Itens de biblioteca

- Deve existir um tipo base que não pode ser instanciado diretamente.
- Cada item tem um título.
- Todo item deve ter uma forma de mostrar sua descrição.
- Deve existir pelo menos dois tipos de item diferentes (ex.: livro e revista) com comportamentos próprios.

#### Validações

- Um título vazio ou inválido deve gerar um erro.
- Um livro não pode ter quantidade de páginas menor ou igual a zero.
- Uma revista não pode ter edição menor que 1.

#### Método estático

- Deve haver um método que verifique se um título é válido (não vazio).

#### Decorator

- Crie um decorator que valide se todos os números recebidos por uma função são positivos.
- Use esse decorator em pelo menos duas funções simples que façam cálculos (por exemplo, tempo de leitura, proporção, etc.).
- Se algum número for inválido, deve ocorrer erro.

#### Testes unitários (pytest)

Deve haver testes que mostrem:

- Criação correta de livro e revista.
- Erros quando dados inválidos forem usados.
- Funcionamento do método estático de validação.
- Funcionamento correto do decorator nas funções com valores válidos e inválidos.

👉 O que esperamos: um sistema funcional, que use classes abstratas, herança, método estático, decorator e testes.
👉 O que importa é que o comportamento acima aconteça — a forma como você organiza ou nomeia não é relevante.
