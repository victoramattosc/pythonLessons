from abc import ABC, abstractmethod

# Classe abstrata que representa um "Pagamento"
class Pagamento(ABC):

    @abstractmethod
    def processar(self, valor):
        pass

    @staticmethod
    def validar_valor(valor):
        # Método estático: não depende de self nem da classe
        return valor > 0


# Subclasses concretas
class CartaoCredito(Pagamento):
    def processar(self, valor):
        if self.validar_valor(valor):
            return f"Pagamento de R${valor} processado no cartão de crédito."
        return "Valor inválido."


class Boleto(Pagamento):
    def processar(self, valor):
        if self.validar_valor(valor):
            return f"Boleto gerado no valor de R${valor}."
        return "Valor inválido."


# Uso
cc = CartaoCredito()
boleto = Boleto()

print(cc.processar(100))   # Pagamento de R$100 processado no cartão de crédito.
print(boleto.processar(-50))  # Valor inválido.
