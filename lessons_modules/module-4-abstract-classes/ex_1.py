from abc import ABC, abstractmethod

# Classe abstrata: define um contrato
class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass  # Obrigatório implementar nas subclasses


# Subclasses implementam o método abstrato
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"


class Gato(Animal):
    def emitir_som(self):
        return "Miau!"


# Uso
dog = Cachorro()
cat = Gato()

print(dog.emitir_som())  # Au Au!
print(cat.emitir_som())  # Miau!
