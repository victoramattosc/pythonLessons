# Decorator que mede tempo de execução
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo: {fim - inicio:.5f} segundos")
        return resultado
    return wrapper

@medir_tempo
def soma_lenta(a, b):
    time.sleep(1)  # simula função demorada
    return a + b

print(soma_lenta(10, 20))
