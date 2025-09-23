# Exercício 3

# Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos numéricos de 
# uma função são positivos:

# Se todos os argumentos forem válidos, a função deve ser executada normalmente.
# Se algum argumento for negativo, deve ser levantado um ValueError.
# Use esse decorator em pelo menos duas funções:
# raiz_quadrada(x), que retorna a raiz quadrada de x.
# divisao(a, b), que retorna o resultado de a / b.

import math

def valida_positivo(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Valor negativo detectado: {arg}")
        
        for arg in kwargs.values():
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Valor negativo detectado: {arg}")
        
        return func(*args, **kwargs)
    return wrapper

@valida_positivo
def raiz_quadrada(x):
    return math.sqrt(x)

@valida_positivo
def divisao(a, b):
    return a / b

print(raiz_quadrada(9)) 
print(divisao(10, 2))
