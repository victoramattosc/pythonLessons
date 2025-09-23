from abc import ABC, abstractmethod

# Classe abstrata Funcionário
class Funcionario(ABC):

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

    @staticmethod
    def validar_horas(horas):
        return horas >= 0


# Funcionário Horista
class Horista(Funcionario):
    def __init__(self, nome, horas, valor_hora):
        super().__init__(nome)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        if not self.validar_horas(self.horas):
            return "Horas inválidas."
        return self.horas * self.valor_hora


# Funcionário Assalariado
class Assalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal


# Uso
f1 = Horista("João", 160, 25)
f2 = Assalariado("Maria", 3000)

print(f"{f1.nome} recebe: R${f1.calcular_salario()}")  # João recebe: R$4000
print(f"{f2.nome} recebe: R${f2.calcular_salario()}")  # Maria recebe: R$3000
