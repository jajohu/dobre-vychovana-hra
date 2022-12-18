from dobre_vychovana_hra.babicka_dozorce import BabickaDozorce

babicka_dozorce = BabickaDozorce()


@babicka_dozorce.hlidka
def funkce_ktera_neco_dela(zadost=None):
    return {"slusna_odpoved": "tady mate"}


if __name__ == "__main__":
    funkce_ktera_neco_dela("prosim")
