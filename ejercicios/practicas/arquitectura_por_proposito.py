# guia_interactiva_patrones.py

def listar_propósitos():
    print(" Propósitos disponibles (elige un número):\n")
    propósitos = {
        1: "Validar datos de usuario",
        2: "Generar informes paso a paso",
        3: "Ejecutar acciones encapsuladas (botones, comandos)",
        4: "Aplicar operaciones sobre objetos sin modificar clases",
        5: "Crear familias de objetos compatibles (UI, exportadores)",
        6: "Unificar interfaces incompatibles",
        7: "Separar abstracción de implementación",
        8: "Añadir funcionalidades sin modificar clases",
        9: "Reaccionar automáticamente a eventos",
        10: "Crear objetos según tipo o contexto",
        11: "Coordinar módulos sin acoplarlos",
        12: "Serializar y exportar datos"
    }
    for numero, descripcion in propósitos.items():
        print(f"{numero}. {descripcion}")
    return propósitos

def arquitectura_por_proposito(opcion: int):
    opciones = {
        1: {
            "proposito": "Validar datos de usuario",
            "patron": "Chain of Responsibility",
            "clase": "@dataclass (Usuario)",
            "interfaz": "Validador(ABC)",
            "mixins": ["LoggerMixin"],
            "generador": "Encadenamiento de validadores",
            "fixture": "usuario_valido",
            "ejemplo": "Validar edad, email y nombre con validadores encadenados"
        },
        2: {
            "proposito": "Generar informes paso a paso",
            "patron": "Builder",
            "clase": "@dataclass (PasoInforme)",
            "interfaz": None,
            "mixins": [],
            "generador": "InformeBuilder con pasos",
            "fixture": "informe_demo",
            "ejemplo": "Informe con secciones como título, resumen, tabla"
        },
        3: {
            "proposito": "Ejecutar acciones encapsuladas",
            "patron": "Command",
            "clase": "@dataclass (ComandoGuardar)",
            "interfaz": "Comando(ABC)",
            "mixins": ["LoggerMixin"],
            "generador": None,
            "fixture": "comando_guardar",
            "ejemplo": "Botón que guarda datos y registra la acción"
        },
        4: {
            "proposito": "Aplicar operaciones sobre objetos",
            "patron": "Visitor",
            "clase": "@dataclass (Empleado)",
            "interfaz": "Visitador(ABC)",
            "mixins": [],
            "generador": None,
            "fixture": "empleado_demo",
            "ejemplo": "Calcular bonus según tipo de empleado"
        },
        5: {
            "proposito": "Crear familias de objetos compatibles",
            "patron": "Abstract Factory",
            "clase": "@dataclass (BotonWindows)",
            "interfaz": "FabricaUI(ABC)",
            "mixins": [],
            "generador": None,
            "fixture": "fabrica_windows",
            "ejemplo": "Crear botones y menús para Windows y Mac"
        },
        6: {
            "proposito": "Unificar interfaces incompatibles",
            "patron": "Adapter",
            "clase": "@dataclass (ClienteLegacy)",
            "interfaz": "Adaptador(ABC)",
            "mixins": ["SerializerMixin"],
            "generador": None,
            "fixture": "cliente_legacy",
            "ejemplo": "Adaptar API antigua a nueva estructura"
        },
        7: {
            "proposito": "Separar abstracción de implementación",
            "patron": "Bridge",
            "clase": "@dataclass (CanalEmail)",
            "interfaz": "Canal(ABC)",
            "mixins": [],
            "generador": None,
            "fixture": "canal_sms",
            "ejemplo": "Enviar mensajes por email, SMS o push sin acoplar lógica"
        },
        8: {
            "proposito": "Añadir funcionalidades sin modificar clases",
            "patron": "Decorator",
            "clase": "Función decoradora",
            "interfaz": None,
            "mixins": ["LoggerMixin", "ValidadorMixin"],
            "generador": None,
            "fixture": "funcion_decorada",
            "ejemplo": "Decorar función con logging y validación"
        },
        9: {
            "proposito": "Reaccionar automáticamente a eventos",
            "patron": "Observer",
            "clase": "@dataclass (SuscriptorEmail)",
            "interfaz": "Suscriptor(ABC)",
            "mixins": ["NotificadorMixin"],
            "generador": None,
            "fixture": "pedido_actualizado",
            "ejemplo": "Notificar por email y SMS cuando cambia el estado de un pedido"
        },
        10: {
            "proposito": "Crear objetos según tipo o contexto",
            "patron": "Factory Method",
            "clase": "@dataclass (UsuarioAdmin)",
            "interfaz": "Usuario(ABC)",
            "mixins": [],
            "generador": None,
            "fixture": "usuario_admin",
            "ejemplo": "Crear usuario según rol: admin, cliente, invitado"
        },
        11: {
            "proposito": "Coordinar módulos sin acoplarlos",
            "patron": "Mediator",
            "clase": "@dataclass (PanelNotificaciones)",
            "interfaz": "Mediador(ABC)",
            "mixins": [],
            "generador": None,
            "fixture": "mediador_ui",
            "ejemplo": "Centralizar comunicación entre chat, historial y notificaciones"
        },
        12: {
            "proposito": "Serializar y exportar datos",
            "patron": "Adapter / Strategy",
            "clase": "@dataclass (ExportadorCSV)",
            "interfaz": "Exportador(ABC)",
            "mixins": ["SerializerMixin"],
            "generador": None,
            "fixture": "datos_exportables",
            "ejemplo": "Exportar datos en CSV, JSON o XML según estrategia"
        }
    }
    return opciones.get(opcion, {"error": "Propósito no reconocido"})

# Ejemplo de uso
if __name__ == "__main__":
    propósitos = listar_propósitos()
    seleccion = int(input("\nSelecciona el número del propósito: "))
    resultado = arquitectura_por_proposito(seleccion)
    print("\n Arquitectura recomendada:\n")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
