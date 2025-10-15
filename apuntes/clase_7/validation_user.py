def validar_usuario(usuario, validaciones):
    for validar in validaciones:
        resultado = validar(usuario)
        if resultado is not True:
            return resultado  # Devuelve el primer error
    return True  # Si todo pasa, devuelve True

# Funciones de validación - callbacks
def es_mayor_de_edad(usuario):
    return True if usuario["edad"] >= 18 else "Error:  El usuario es menor de edad"

def dni_valido(usuario):
    dni = usuario["dni"]
    return True if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha() else "Error: DNI del usuario inválido"


# Ejemplo de uso
usuario = {"nombre": "Miguel", "edad": 17, "dni": "50236789D"}
validaciones = [es_mayor_de_edad, dni_valido]

print(validar_usuario(usuario, validaciones))
