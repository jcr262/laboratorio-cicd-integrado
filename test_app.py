from app import sumar, es_par


def test_sumar():
    assert sumar(3, 5) == 8


def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False
