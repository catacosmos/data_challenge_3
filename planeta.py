# Librerias
import numpy as np
import pandas as pd

# Constantes
from astropy.constants import L_sun, M_sun, G

class Planeta(object):
    def __init__(self, nombre, estrella_anfitriona, masa_planetaria, radio, radio_semi_mayor, inclinacion, excentricidad, periastron):
        # Constructor de la clase Planeta
        # Inicializa los atributos del planeta
        self.nombre = nombre
        self._estrella = estrella_anfitriona
        self._masa = masa_planetaria
        self._radio = radio
        self._alpha = radio_semi_mayor
        self._i = inclinacion
        self._e = excentricidad
        self._omega = periastron

    def rotacion_kepleriana(self):
        # Método para calcular la velocidad de rotación kepleriana del planeta
        return float(2 * np.pi * np.sqrt((self._alpha ** 3) / (G.value * self._masa)))
