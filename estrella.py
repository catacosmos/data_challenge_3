# Librerias
import numpy as np
import pandas as pd

# Constantes
from astropy.constants import L_sun, M_sun, G

class Estrella(object):
    def __init__(self, nombre, masa, radio, temperatura, distancia, movimiento_propio):
        self.nombre = nombre
        self._M = masa
        self._R = radio
        self._Teff = temperatura
        self._d = distancia
        self._delta = movimiento_propio

    def luminosidad(self):
        return float(4 * np.pi * (self._R ** 2) * self._Teff)

    def l_secuencia_principal(self):
        return float(L_sun.value * (self._M / M_sun.value) ** 3.5)
