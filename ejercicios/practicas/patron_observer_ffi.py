from abc import ABC, abstractmethod

# --- Evento base ---
class EventoFinanciero:
    def __init__(self, fondo: str, tipo: str, mensaje: str) -> None:
        self.fondo = fondo
        self.tipo = tipo    
        self.mensaje = mensaje

# --- Interfaz de suscriptores ---
class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, evento: EventoFinanciero):
        pass

# --- Mixin para notificaciones ---
class NotificadorMixin:
    def enviar_notificacion(self, canal: str, contenido: str):
        print(f"[{canal.upper()}] -> {contenido}")

# --- Suscriptores concretos ---
class SuscriptorEmail(Suscriptor, NotificadorMixin):
    def __init__(self, correo: str):
        self.correo = correo

    def __str__(self):
        return f"SuscriptorEmail({self.correo})"

    def actualizar(self, evento: EventoFinanciero):
        contenido = f"Fondo: {evento.fondo} | Tipo: {evento.tipo} | Mensaje: {evento.mensaje}"
        self.enviar_notificacion("email", f"Para {self.correo}: {contenido}")

class SuscriptorSMS(Suscriptor, NotificadorMixin):
    def __init__(self, telefono: str):
        self.telefono = telefono

    def __str__(self):
        return f"SuscriptorSMS({self.telefono})"

    def actualizar(self, evento: EventoFinanciero):
        contenido = f"{evento.fondo} - {evento.tipo}: {evento.mensaje}"
        self.enviar_notificacion("sms", f"SMS a {self.telefono}: {contenido}")

# --- Interfaz para desacoplar el publicador ---
class PublicadorEventos(ABC):
    @abstractmethod
    def publicar(self, evento: EventoFinanciero):
        pass

    @abstractmethod
    def registrar(self, suscriptor: Suscriptor):
        pass

    @abstractmethod
    def limpiar(self):
        pass

# --- Implementación concreta del canal ---
class CanalEventos(PublicadorEventos):
    def __init__(self):
        self._suscriptores = []

    def registrar(self, suscriptor: Suscriptor):
        if suscriptor not in self._suscriptores:
            self._suscriptores.append(suscriptor)
            print("[CanalEventos] Suscriptor registrado:", suscriptor)
        else:
            print("[CanalEventos] Ya estaba registrado:", suscriptor)

    def publicar(self, evento: EventoFinanciero):
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(evento)

    def limpiar(self):
        print("[CanalEventos] Eliminando todos los suscriptores...")
        self._suscriptores.clear()

# --- Gestor desacoplado ---
class GestorFondos:
    def __init__(self, canal: PublicadorEventos):
        self._canal = canal

    def agregar_suscriptor(self, suscriptor: Suscriptor):
        self._canal.registrar(suscriptor)

    def emitir_evento(self, evento: EventoFinanciero):
        self._canal.publicar(evento)

    def limpiar_suscriptores(self):
        self._canal.limpiar()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    canal = CanalEventos()
    gestor = GestorFondos(canal)

    gestor.agregar_suscriptor(SuscriptorEmail("inversor@ejemplo.com"))
    gestor.agregar_suscriptor(SuscriptorSMS("+34 600 123 456"))

    evento = EventoFinanciero("Fondo Europa 2030", "actualizacion", "Nuevo informe trimestral disponible")
    gestor.emitir_evento(evento)

    gestor.limpiar_suscriptores()
