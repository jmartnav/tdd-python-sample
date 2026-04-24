# Librería pytest para ejecutar tests
import pytest

from ejercicios.operaciones import es_par

def test_numeros_pares():
    assert es_par(2) is True
    assert es_par(0) is True
    assert es_par(100) is True
    assert es_par(-4) is True

def test_numeros_impares():
    assert es_par(3) is False
    assert es_par(7) is False
    assert es_par(-1) is False