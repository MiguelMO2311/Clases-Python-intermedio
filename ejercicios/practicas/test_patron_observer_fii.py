import pytest
from patron_observer_ffi import GestorFondos, SuscriptorEmail, SuscriptorSMS, EventoFinanciero

@pytest.fixture
def entorno_financiero():
    """
    Prepara un entorno con gestor y dos suscriptores.
    """
    gestor = GestorFondos()
    email = SuscriptorEmail("inversor@ejemplo.com")
    sms = SuscriptorSMS("+34 600 123 456")
    return gestor, email, sms

def test_suscripcion(entorno_financiero, capsys):
    """
    Verifica que los suscriptores reciben el evento correctamente.
    """
    gestor, email, sms = entorno_financiero
    gestor.suscriptores = email
    gestor.suscriptores = sms

    evento = EventoFinanciero("Fondo Alpha", "alerta", "Cambio de política de inversión")
    gestor.publicar_evento(evento)

    salida = capsys.readouterr().out
    assert "EMAIL" in salida
    assert "SMS" in salida
    assert "Fondo Alpha" in salida

def test_dessuscripcion(entorno_financiero, capsys):
    """
    Verifica que tras eliminar los suscriptores no se recibe ninguna notificación.
    """
    gestor, email, sms = entorno_financiero
    gestor.suscriptores = email
    gestor.suscriptores = sms
    del gestor.suscriptores

    evento = EventoFinanciero("Fondo Beta", "actualizacion", "Informe disponible")
    gestor.publicar_evento(evento)

    salida = capsys.readouterr().out
    assert "EMAIL" not in salida
    assert "SMS" not in salida
    assert "Fondo Beta" not in salida
