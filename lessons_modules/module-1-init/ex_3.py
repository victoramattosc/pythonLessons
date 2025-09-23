# Crie uma classe Animal com um método falar que exibe um som genérico.
# Em seguida, crie duas classes que herdam de Animal: Cachorro e Gato, cada uma sobrescrevendo o método falar para mostrar sons específicos.
# Por fim, crie objetos de Animal, Cachorro e Gato e chame o método falar em cada um para observar o polimorfismo.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som indefinido...")  # método genérico

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome} diz: Miau!")

# Criando objetos de classes diferentes
a = Animal("Bicho")
c = Cachorro("Rex")
g = Gato("Luna")

# Chamando métodos (polimorfismo)
a.falar()  # saída: Som indefinido...
c.falar()  # saída: Rex diz: Au au!
g.falar()  # saída: Luna diz: Miau!
