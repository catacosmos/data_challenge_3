# Librerias
import numpy as np
import pandas as pd

# Constantes
from astropy.constants import L_sun, M_sun, G

# Heredamos la clase Planeta
class Exoplaneta(Planeta):

    # Método para establecer el método de descubrimiento del planeta
    def set_metodo_de_descubrimiento(self, metodo):
        self.metodo = metodo

    # Método para obtener el método de descubrimiento del planeta
    def get_metodo_de_descubrimiento(self):
        return self.metodo
        
    # Método para calcular la densidad del exoplaneta en función de su masa y radio    
    def calcular_densidad(self):
        densidad = self._masa / ((4 / 3) * np.pi * (self._radio ** 3))
        return densidad
        
    def impact_parameter(self):
        b = (self._alpha * np.cos(np.radians(self._i))) * ((1 - self._e ** 2) / (self._estrella._R * (1 + self._e * np.sin(np.radians(self._omega)))))
        if np.isnan(b):
            return 'Error: No se puede calcular el parametro de impacto'
        else:
            if b <= 0:
                return 0
            elif 0 < b < 1:
                return b
            else:
                return 1
