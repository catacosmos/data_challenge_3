# Librerias
import numpy as np
import pandas as pd

# Constantes
from astropy.constants import L_sun, M_sun, G

class SistemaPlanetario(object):
    def __init__(self, estrella, planetas=[]):
        # Constructor de la clase SistemaPlanetario
        # Inicializa la estrella central y una lista de planetas (opcional)
        self.estrella = estrella
        self.planetas = planetas

    def agregar_planeta(self, planeta):
        # Método para agregar un planeta al sistema planetario
        self.planetas.append(planeta)

    def numero_de_planetas(self):
        # Método para obtener el número de planetas en el sistema
        return len(self.planetas)

    def planetas_ordenados_por_radio(self):
        # Método para ordenar los planetas por su radio semi-mayor
        planetas_ordenados = sorted(self.planetas, key=lambda planeta: planeta._alpha)
        for planeta in planetas_ordenados:
            print(f" - Planeta {planeta.nombre} - Radio semi-mayor: {planeta._alpha}")
        return planetas_ordenados
