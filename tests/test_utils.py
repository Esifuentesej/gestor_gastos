import pytest
from app import validar_monto

@pytest.mark.parametrize("monto_entrada, esperado", [
    ("150.50", True),    # Caso Valido
    ("-10.00", False),   # Caso Invalido (Negativo)
    ("cero", False),     # Caso Invalido (Texto)
    ("0", False),        # Valor Limite
])
def test_casos_de_prueba_monto(monto_entrada, esperado):
    assert validar_monto(monto_entrada) == esperado
