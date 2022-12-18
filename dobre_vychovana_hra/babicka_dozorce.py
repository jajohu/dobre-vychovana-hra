from inspect import signature

from dobre_vychovana_hra.exceptions import FunkceJeNezdvorila


# Axiom: Je neslusne byt snob

class BabickaDozorce:
    zadost_sentinel = "zadost"

    def __init__(self, poproseni=None, darebactvi=None, napomenuti=None):
        self.poproseni = "prosim" if not poproseni else poproseni
        self.darebactvi = [] if not darebactvi else darebactvi
        self.napomenuti = "tak takhle teda ne, to by neslo" if not napomenuti else napomenuti
        self.odpoved = None

    def hlidka(self, func):
        def wrapper(*args, **kwargs):
            try:
                self.odpoved = func(*args, **kwargs)
                self.je_funkce_vychovana(func)
                return self.odpoved
            except FunkceJeNezdvorila:
                raise
        return wrapper

    def pridat_darebactvi(self, darebactvi):
        self.darebactvi.append(darebactvi)

    def je_funkce_vychovana(self, func):
        if self._je_funkce_poprositelna(func) and self._je_funkce_opravdu_taktni(func):
            return True
        raise FunkceJeNezdvorila(self.napomenuti)

    def _je_funkce_poprositelna(self, func):
        func_signature = signature(func)
        if func_signature.parameters.get(self.zadost_sentinel):
            return True
        return False

    def _je_funkce_opravdu_taktni(self, func):
        if not self.mam_odpoved:
            self.odpoved = func()
        slusna_odpoved = self.odpoved.get("slusna_odpoved")
        if slusna_odpoved and not self.odpoved.get("neslusna_odpoved"):
            if self._zamumlal_darebactvi(slusna_odpoved):
                return False
            return True
        return False

    @property
    def mam_odpoved(self):
        return self.odpoved

    def _zamumlal_darebactvi(self, odpoved):
        return any(nadavka in odpoved for nadavka in self.darebactvi)
