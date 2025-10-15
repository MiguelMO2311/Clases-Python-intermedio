# 1. Patrón Strategy
# Ejercicio: Implementa una clase Calculadora que pueda cambiar dinámicamente entre estrategias de cálculo
# (suma, resta, multiplicación) usando funciones como parámetros.

class Calculadora:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, a:int, b: int)-> int:
        return self.estrategia(a, b)
    
# Ejemplos de estrategias
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b   

# Uso de la Calculadora con diferentes estrategias
calc = Calculadora(suma)
print("Suma: ", calc.calcular(10, 5))  # Output: 15
calc.estrategia = resta
print("Resta: ", calc.calcular(10, 5))  # Output: 5
calc.estrategia = multiplicacion
print("Multiplicación: ", calc.calcular(10, 5))  # Output : 50
calc.estrategia = division
print("División: ", calc.calcular(10, 5))  # Output: 2.0
print("División por cero: ", calc.calcular(10, 0))  # Output: Error: División por cero

# 2. 🏗️ Patrón Builder
# Ejercicio: Crea una clase ConstructorInforme que permita construir un informe paso a paso con título,
# fecha, autor y contenido. Usa métodos encadenados y un método construir() que devuelva el informe como diccionario.

import datetime

class ConstructorInforme:
    def __init__(self):
        self.informe = {}

    def agregar_titulo(self, titulo:str)-> 'ConstructorInforme':
        self.informe['titulo'] = titulo
        return self

    def agregar_fecha(self, fecha:datetime.date)-> 'ConstructorInforme':
        self.informe['fecha'] = fecha
        return self

    def agregar_autor(self, autor:str)-> 'ConstructorInforme':
        self.informe['autor'] = autor
        return self

    def agregar_contenido(self, contenido:str)-> 'ConstructorInforme':
        self.informe['contenido'] = contenido
        return self

    def construir(self):
        return self.informe
    
# Uso del ConstructorInforme
informe = (ConstructorInforme()
           .agregar_titulo("Informe de Ventas")
           .agregar_fecha(datetime.date.today())
           .agregar_autor("Miguel M.")
           .agregar_contenido("Este es el contenido del informe de ventas.")
           .construir())
print(informe)

# Patrón Adapter
# Ejercicio: Dado dos clases LegacyLogger y ModernLogger con métodos distintos (log() y write_log()), 
# crea un LoggerAdapter que unifique el acceso con un método registrar().

class LegacyLogger:
    def log(self, mensaje: str) -> None:
        print(f"Legacy Logger: {mensaje}")

class ModernLogger:
    def write_log(self, mensaje: str) -> None:
        print(f"Modern Logger: {mensaje}")

class LoggerAdapter:
    def __init__(self, logger: object)  -> None:
        self.logger = logger

    def registrar(self, mensaje: str) -> None:
        if isinstance(self.logger, LegacyLogger):
            self.logger.log(mensaje)
        elif isinstance(self.logger, ModernLogger):
            self.logger.write_log(mensaje)
        else:
            raise ValueError("Logger no soportado")

# Uso del LoggerAdapter
legacy_logger = LegacyLogger() 
modern_logger = ModernLogger()
adapter1 = LoggerAdapter(legacy_logger)
adapter2 = LoggerAdapter(modern_logger)
adapter1.registrar("Mensaje desde Legacy Logger")  # Output: Legacy Logger: Mensaje desde Legacy Logger
adapter2.registrar("Mensaje desde Modern Logger")  # Output: Modern Logger: Mensaje desde Modern Logger 

# Herencia y mixins
# Ejercicio: Crea una clase base Animal y dos mixins: Volador y Nadador.
# Luego crea clases como Pato y Delfín que hereden de Animal y los mixins correspondientes.

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def hacer_sonido(self) -> str:
        return "Sonido genérico de animal"

class Volador:
    def volar(self) -> str:
        return f"{self.nombre} está volando"
class Nadador:
    def nadar(self) -> str:
        return f"{self.nombre} está nadando"
class Pato(Animal, Volador, Nadador):
    def hacer_sonido(self) -> str:
        return "Cua Cua"
class Delfin(Animal, Nadador):
    def hacer_sonido(self) -> str:
        return "Click Click"

# Uso de las clases con mixins
pato = Pato("Pato Donald")
delfin = Delfin("Delfín Flipper")
print(pato.hacer_sonido())  # Output: Cua Cua
print(pato.volar())         # Output: Pato Donald está volando
print(pato.nadar())         # Output: Pato Donald está nadando
print(delfin.hacer_sonido()) # Output: Click Click
print(delfin.nadar())        # Output: Delfín Flipper está nadando
# print(delfin.volar())       # Error: Delfín no puede volar    

# Decorador de validación
# Ejercicio: Implementa un decorador @validar_datos que verifique que los argumentos de una función no sean None. 
# Si alguno lo es, lanza una excepción.

def validar_datos(func):
    def wrapper(*args, **kwargs):
        if any(arg is None for arg in args) or any(value is None for value in kwargs.values()):
            raise ValueError("Los argumentos no pueden ser None")
        return func(*args, **kwargs)
    return wrapper

@validar_datos
def procesar_datos(nombre: str, edad: int) -> str:
    return f"Procesando datos de {nombre}, edad {edad}"

# Uso del decorador de validación
try:
    print(procesar_datos("Ana", 30))  # Output: Procesando datos de Ana, edad 30
    print(procesar_datos(None, 25))   # Lanza ValueError
except ValueError as e:
    print(e)  # Output: Los argumentos no pueden ser None

# Pandas y DataFrame
# Ejercicio: Crea un DataFrame con datos de usuarios (nombre, edad, email) y filtra los mayores de edad.
# Exporta el resultado a CSV.

import pandas as pd

# Crear un DataFrame con datos de usuarios
data = {
    'nombre': ['Ana', 'Luis', 'Marta', 'Carlos'],
    'edad': [22, 17, 35, 15],
    'email': ['ana@example.com', 'luis@example.com', 'marta@example.com', 'carlos@example.com']
              }
df = pd.DataFrame(data)
# Filtrar los usuarios mayores de edad 
mayores_de_edad = df[df['edad'] >= 18]
print(mayores_de_edad)
# Exportar el resultado a CSV
mayores_de_edad.to_csv('mayores_de_edad.csv', index=False)

# Iteradores y generadores
# Ejercicio: Implementa un generador generar_pares(n) que devuelva los primeros n números pares. 
# Luego úsalo en un bucle for.

def generar_pares(n: int):
    for i in range(n):
        yield i * 2

# Uso del generador generar_pares
for numero in generar_pares(5):
    print(numero)  # Output: 0, 2, 4, 6, 8

# Testing con pytest
# Ejercicio: Escribe un test para verificar que la función es_mayor_de_edad(usuario) devuelve 
# True si el usuario tiene 18 años o más, y un mensaje de error si no.

import pytest

def es_mayor_de_edad(usuario: dict) -> bool:
    if 'edad' not in usuario:
        raise ValueError("El usuario debe tener una clave 'edad'")
    return usuario['edad'] >= 18

# Test con pytest
def test_es_mayor_de_edad():
    assert es_mayor_de_edad({'nombre': 'Ana', 'edad': 20}) == True
    assert es_mayor_de_edad({'nombre': 'Luis', 'edad': 17}) == False
    try:
        es_mayor_de_edad({'nombre': 'Marta'})
    except ValueError as e:
        assert str(e) == "El usuario debe tener una clave 'edad'"


# Validación con callbacks
# Ejercicio: Implementa una función validar_usuario(usuario, validaciones) que reciba un diccionario 
# y una lista de funciones de validación. Devuelve True si todas pasan, o el primer error.

def validar_usuario(usuario: dict, validaciones: list) -> bool:
    for validacion in validaciones:
        resultado = validacion(usuario)
        if resultado is not True:
            return resultado
    return True

# Ejemplos de funciones de validación
def validar_nombre(usuario: dict):
    if 'nombre' not in usuario or not usuario['nombre']:
        return "El nombre es obligatorio"
    return True

def validar_edad(usuario: dict):
    if 'edad' not in usuario or not isinstance(usuario['edad'], int) or usuario['edad'] < 0:
        return "La edad debe ser un número entero no negativo"
    return True

def validar_email(usuario: dict):
    if 'email' not in usuario or '@' not in usuario['email']:
        return "El email no es válido"
    return True

# Uso de la función validar_usuario
usuario = {'nombre': 'Ana', 'edad': 25, 'email': 'ana@example.com'}
validaciones = [validar_nombre, validar_edad, validar_email]
resultado = validar_usuario(usuario, validaciones)
print(resultado)  # Output: True

usuario_invalido = {'nombre': '', 'edad': -5, 'email': 'anaexample.com'}
resultado_invalido = validar_usuario(usuario_invalido, validaciones)
print(resultado_invalido)  # Output: El nombre es obligatorio



# -----------------------------------------------
# 🛠️ CREACIÓN DE PROYECTO CON POETRY PASO A PASO
# -----------------------------------------------

# 1. Crear un nuevo proyecto llamado "validacion_usuario"
# poetry new validacion_usuario

# Esto genera la siguiente estructura:
# validacion_usuario/
# ├── pyproject.toml
# ├── README.md
# ├── validacion_usuario/
# │   └── __init__.py
# └── tests/
#     └── __init__.py

# 2. Entrar al directorio del proyecto
# cd validacion_usuario

# 3. Activar el entorno virtual del proyecto
# poetry shell

# 4. Instalar pandas como dependencia principal
# poetry add pandas

# 5. Instalar pytest como dependencia de desarrollo
# poetry add pytest --dev

# 6. Verificar que pandas está correctamente instalado
# python -c "import pandas as pd; print(pd.__version__)"

# 7. Verificar que pytest está disponible
# pytest --version

# 8. Crear un archivo de test (opcional)
# Por ejemplo: tests/test_validacion.py
# con una función como esta:

# def test_suma():
#     assert 2 + 3 == 5

# 9. Ejecutar todos los tests del proyecto
# pytest

# 10. Ejecutar un test específico
# pytest tests/test_validacion.py

# -----------------------------------------------
# ✅ ¡Proyecto listo para trabajar con pandas y pytest!
# -----------------------------------------------



