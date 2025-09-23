#  Crie uma classe ContaBancaria que tenha um titular e um saldo (padrão 0).
# A classe deve permitir depositar e sacar valores, atualizando o saldo e mostrando mensagens apropriadas.
# No final, crie uma conta para João com saldo inicial de 100, faça um depósito de 50, depois tente sacar 120 e, em seguida, sacar 50.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo  # saldo inicial (padrão 0)

    def depositar(self, valor):
        self.saldo += valor  # atualiza saldo
        print(f"Depósito de R${valor}. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor}. Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente!")

# Testando
conta1 = ContaBancaria("João", 100)
conta1.depositar(50)
conta1.sacar(120)
conta1.sacar(50)
