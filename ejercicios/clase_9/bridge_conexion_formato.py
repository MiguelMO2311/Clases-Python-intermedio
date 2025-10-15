from abc import ABC, abstractmethod

# FORMATO DEL DATO (parte 1 del puente)
class FormatoDato(ABC):
    @abstractmethod
    def serializar(self, datos: dict) -> str:
        pass

class JSON(FormatoDato):
    def serializar(self, datos: dict) -> str:
        import json
        return json.dumps(datos)

class Bin(FormatoDato):
    def serializar(self, datos: dict) -> str:
        return str(datos).encode("utf-8").hex()

class HTTP(FormatoDato):
    def serializar(self, datos: dict) -> str:
        lineas = []
        for clave, valor in datos.items():
            linea = f"{clave}: {valor}"
            lineas.append(linea)
        return "\n".join(lineas)


# TIPO DE CONEXIÓN (parte 2 del puente)
class Conexion(ABC):
    def __init__(self, formato: FormatoDato):
        self.formato = formato

    @abstractmethod
    def enviar(self, datos: dict):
        pass

class GoogleDrive(Conexion):
    def enviar(self, datos: dict):
        contenido = self.formato.serializar(datos)
        print(f"[GoogleDrive] Subiendo archivo con contenido:\n{contenido}")

class HttpTransport(Conexion):
    def enviar(self, datos: dict):
        contenido = self.formato.serializar(datos)
        print(f"[HTTP] Realizando solicitud POST con datos:\n{contenido}")

class WebSocket(Conexion):
    def enviar(self, datos: dict):
        contenido = self.formato.serializar(datos)
        print(f"[WebSocket] Transmitiendo mensaje:\n{contenido}")
        
# Ejemplo de uso del patrón Bridge

datos = {"usuario": "miguel", "accion": "login", "estado": "ok"}

# Enviar por WebSocket en formato JSON
conexion1 = WebSocket(JSON())
conexion1.enviar(datos)

# Enviar por GoogleDrive en formato Binario
conexion2 = GoogleDrive(Bin())
conexion2.enviar(datos)

# Enviar por HTTP en formato HTTP 
conexion3 = HttpTransport(HTTP())
conexion3.enviar(datos)
