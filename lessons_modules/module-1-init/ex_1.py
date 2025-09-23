# Exemplo simples de uma classe em Python

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome   # atributo da instância
        self.idade = idade # atributo da instância

    def apresentar(self):
        # método que imprime uma apresentação básica
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto (instância da classe)
p1 = Pessoa("Ana", 20)
p1.apresentar()  # saída: Olá, meu nome é Ana e tenho 20 anos.
