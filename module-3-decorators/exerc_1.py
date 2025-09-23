# Decorator simples que imprime antes e depois de uma função
def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()  # executa a função original
        print("Depois da função")
    return wrapper

@meu_decorator
def diga_ola():
    print("Olá, mundo!")

diga_ola()
