# Librerias
import numpy as np

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
    	"""
    	Método para calcular la velocidad de rotación kepleriana del planeta.
    
    	Devuelve la velocidad de rotación kepleriana del planeta basada en la masa del planeta y su distancia alrededor de su estrella.
    
    	Returns:
        	float: La velocidad de rotación kepleriana del planeta.
    	"""
    return float(2 * np.pi * np.sqrt((self._alpha ** 3) / (G.value * self._masa)))

    def calcular_velocidad_orbital(self):
    	"""
    	Método para calcular la velocidad orbital del planeta.
    
    	Imprime un mensaje indicando que se está calculando la velocidad orbital del planeta.
    
    	Returns:
        	float: La velocidad orbital del planeta.
    	"""
    print("Calculando la velocidad orbital del planeta...")
    return np.sqrt(G.value * self._estrella.masa * self._alpha * (1 - self._e ** 2)) / self._alpha

