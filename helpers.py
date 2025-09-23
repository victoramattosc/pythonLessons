"""
helpers.py

Este arquivo serve como um "cheat sheet" com exemplos de construções básicas e avançadas da linguagem Python.
Os exemplos incluídos aqui podem ser copiados e colados em outros projetos para referência rápida.

1. Variáveis e tipos básicos
2. Definição de funções
3. Classes e métodos (incluindo métodos estáticos e de classe)
4. Classes abstratas e interfaces usando abc.ABC
5. Polimorfismo e herança
6. Decoradores de funções e de métodos
7. Propriedades com @property
"""

# 1. Variáveis e tipos básicos
# Atribuição simples de diferentes tipos de dados
my_int: int = 42
my_float: float = 3.14
my_string: str = "Hello, Python!"
my_list: list[int] = [1, 2, 3]
my_dict: dict[str, str] = {"chave": "valor"}
my_tuple: tuple[int, ...] = (4, 5, 6)

# 2. Definição de funções
def add(a: int, b: int) -> int:
    """Retorna a soma de dois números."""
    return a + b

def greet(name: str, greeting: str = "Olá") -> None:
    """Saúda uma pessoa com uma saudação opcional."""
    print(f"{greeting}, {name}!")

# Função com *args e **kwargs
def print_args_kwargs(*args, **kwargs) -> None:
    """Exibe valores posicionais e nomeados."""
    print("Args:", args)
    print("Kwargs:", kwargs)

# 3. Classes e métodos
class ExampleClass:
    """Exemplo de classe com variáveis de instância, classe e métodos diversos."""
    class_var: str = "Sou uma variável de classe"

    def __init__(self, instance_var: str) -> None:
        self.instance_var = instance_var

    def instance_method(self) -> str:
        """Método que usa a variável de instância."""
        return f"Variável de instância: {self.instance_var}"

    @classmethod
    def class_method(cls) -> str:
        """Método de classe que acessa a variável de classe."""
        return f"Variável de classe: {cls.class_var}"

    @staticmethod
    def static_method() -> str:
        """Método estático que não acessa dados da instância ou da classe."""
        return "Sou um método estático"

# 4. Classes abstratas
from abc import ABC, abstractmethod

class AbstractWorker(ABC):
    """Interface de exemplo usando classe abstrata."""

    @abstractmethod
    def work(self) -> None:
        """Método que deve ser implementado pelas subclasses."""
        pass

class Developer(AbstractWorker):
    """Implementação concreta de AbstractWorker."""

    def work(self) -> None:
        print("Escrevendo código...")

class Designer(AbstractWorker):
    """Outra implementação concreta de AbstractWorker."""

    def work(self) -> None:
        print("Desenhando interfaces...")

# 5. Polimorfismo e herança
class Animal:
    """Classe base para demonstrar polimorfismo."""

    def speak(self) -> str:
        """Método que será sobrescrito pelas subclasses."""
        raise NotImplementedError("Subclasses devem implementar este método.")

class Dog(Animal):
    def speak(self) -> str:
        return "Au Au!"

class Cat(Animal):
    def speak(self) -> str:
        return "Miau!"

def make_animal_speak(animal: Animal) -> None:
    """Função que aceita qualquer Animal e executa seu método speak."""
    print(animal.speak())

# 6. Decoradores de funções
def simple_decorator(func):
    """Exemplo de decorador simples que envolve a execução de uma função."""
    def wrapper(*args, **kwargs):
        print("Antes da chamada da função")
        result = func(*args, **kwargs)
        print("Depois da chamada da função")
        return result
    return wrapper

@simple_decorator
def say_hello(name: str) -> None:
    """Função decorada que simplesmente imprime uma saudação."""
    print(f"Olá, {name}!")

# Decorador com parâmetros
def repeat(n: int):
    """Decorador que repete a execução de uma função n vezes."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet_three_times() -> None:
    print("Olá!")

# 7. Propriedades com @property
class Person:
    """Exemplo de uso do @property para encapsular acesso a atributos."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Obtém o nome da pessoa."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Define o nome da pessoa com validação."""
        if not value:
            raise ValueError("O nome não pode ser vazio.")
        self._name = value

    def __str__(self) -> str:
        """Representação amigável da instância."""
        return f"Person(name={self._name})"

# Uso das classes abstratas e polimorfismo (exemplo de execução, se desejado)
if __name__ == "__main__":
    # Demonstrar o decorador simples
    say_hello("Mundo")

    # Demonstrar o decorador com repetição
    greet_three_times()

    # Demonstrar polimorfismo
    animals: list[Animal] = [Dog(), Cat()]
    for animal in animals:
        make_animal_speak(animal)

    # Demonstrar o uso de propriedade
    pessoa = Person("Alice")
    print(pessoa)
    pessoa.name = "Bob"
    print(pessoa)