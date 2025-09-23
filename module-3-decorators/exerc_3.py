# Decorator com argumentos (personalizável)
def repetir(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execução {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)  # vai rodar 3 vezes
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ana")
