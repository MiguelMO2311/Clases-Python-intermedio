import datetime

def medir_tiempo(funcion):
    def wrapper(*arg, **kwargs):
        inicio = datetime.datetime.now()
        resultado =funcion(*arg, **kwargs)
        final = datetime.datetime.now()
        print (final-inicio)
        return resultado
    return wrapper

@medir_tiempo
def elevaadiez(numero:int) -> int:
    return numero ** 10
print(elevaadiez(3))

@medir_tiempo
def suma(n1, n2) -> int:
    return n1 + n2
print(suma(5, n2=7))