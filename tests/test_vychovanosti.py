import pytest

from dobre_vychovana_hra.babicka_dozorce import BabickaDozorce
from dobre_vychovana_hra.exceptions import FunkceJeNezdvorila

SLUSNA_ODPOVED = "rádo se stalo"


@pytest.fixture
def babicka_na_testovani():
    poproseni = "prosim pekne"
    darebactvi = ["ty kravo"]
    babicka = BabickaDozorce(poproseni=poproseni, darebactvi=darebactvi)
    babicka.pridat_darebactvi("trhni si")
    return babicka


@pytest.fixture
def tovarna_na_nevychovane_funkce(babicka_na_testovani):
    def nevychovana_funkce():
        return {"slusna_odpoved": SLUSNA_ODPOVED+" "+babicka_na_testovani.darebactvi}
    return nevychovana_funkce


@pytest.fixture
def tovarna_na_vychovane_funkce():
    def vychovana_funkce(zadost=None):
        return {"ta vec kterou chces": [], "slusna_odpoved": SLUSNA_ODPOVED}
    return vychovana_funkce


def test_funkce_je_vychovana(tovarna_na_vychovane_funkce, babicka_na_testovani):
    vychovana_funkce = tovarna_na_vychovane_funkce
    assert babicka_na_testovani.je_funkce_vychovana(vychovana_funkce) is True


def test_funkce_je_nevychovana(tovarna_na_nevychovane_funkce, babicka_na_testovani):
    nevychovana_funkce = tovarna_na_nevychovane_funkce
    with pytest.raises(FunkceJeNezdvorila):
        babicka_na_testovani.je_funkce_vychovana(nevychovana_funkce)
