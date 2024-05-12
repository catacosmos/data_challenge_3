# Librerias
import numpy as np
import pandas as pd

# Constantes
from astropy.constants import L_sun, M_sun, G

# Lee el archivo CSV
df = pd.read_csv("e1n4AOA4.csv")

# Filtra los planetas por las estrellas específicas
estrellas_interes = ["HR 8799", "HD 202206 A", "TRAPPIST-1", "TOI-1338", "HD 188753", "Kepler-451", "Kepler-16 (AB)"]

# Crea objetos Estrella, Planeta y SistemaPlanetario
estrellas = []
sistemas_planetarios = []

for nombre_estrella in estrellas_interes:

    if nombre_estrella in df['star_name'].values:
        # Extrae los datos de la estrella
        estrella_data = df[df['star_name'] == nombre_estrella].iloc[0]
        estrella = Estrella(nombre_estrella, estrella_data['star_mass'], estrella_data['star_radius'], estrella_data['star_teff'], estrella_data['star_distance'], (estrella_data['ra'], estrella_data['dec']))
        estrellas.append(estrella)

        # Filtra los planetas que orbitan esta estrella
        planetas_estrella = df[df['star_name'] == nombre_estrella]
        planetas = []
        for _, planeta_data in planetas_estrella.iterrows():
            planeta = Exoplaneta(planeta_data['name'], estrella, planeta_data['mass'], planeta_data['radius'], planeta_data['semi_major_axis'], planeta_data['inclination'], planeta_data['eccentricity'], planeta_data['omega'])
            planeta.set_metodo_de_descubrimiento(planeta_data['detection_type'])  # Setting the detection method
            planetas.append(planeta)

        # Crea el sistema planetario y agrega los planetas
        sistema_planetario = SistemaPlanetario(estrella, planetas)
        sistemas_planetarios.append(sistema_planetario)

    elif nombre_estrella in df['star_alternate_names'].values:
        # Extrae los datos de la estrella
        estrella_data = df[df['star_alternate_names'] == nombre_estrella].iloc[0]
        estrella = Estrella(nombre_estrella, estrella_data['star_mass'], estrella_data['star_radius'], estrella_data['star_teff'], estrella_data['star_distance'], (estrella_data['ra'], estrella_data['dec']))
        estrellas.append(estrella)

        # Filtra los planetas que orbitan esta estrella
        planetas_estrella = df[df['star_alternate_names'] == nombre_estrella]
        planetas = []
        for _, planeta_data in planetas_estrella.iterrows():
            planeta = Exoplaneta(planeta_data['name'], estrella, planeta_data['mass'], planeta_data['radius'], planeta_data['semi_major_axis'], planeta_data['inclination'], planeta_data['eccentricity'], planeta_data['omega'])
            planeta.set_metodo_de_descubrimiento(planeta_data['detection_type'])  # Setting the detection method
            planetas.append(planeta)

        # Crea el sistema planetario y agrega los planetas
        sistema_planetario = SistemaPlanetario(estrella, planetas)
        sistemas_planetarios.append(sistema_planetario)

    else:
        print(f"Estrella {nombre_estrella} no encontrada en el archivo CSV\n")

for sistema_planetario in sistemas_planetarios:
    print(f"Sistema Planetario con {sistema_planetario.numero_de_planetas()} planetas:")

    for planeta in sistema_planetario.planetas:
        print(f" - Planeta {planeta.nombre} orbitando la estrella {sistema_planetario.estrella.nombre}")
        print(f"   - Periodo de rotacion kepleriana: {planeta.rotacion_kepleriana()} dias")
        print(f"   - Metodo de descubrimiento: {planeta.get_metodo_de_descubrimiento()}")

        if planeta.get_metodo_de_descubrimiento() == 'Primary Transit':
            print(f"     - Parametro de impacto: {planeta.impact_parameter()}")

        print()

    print(f"Estrella {sistema_planetario.estrella.nombre}:")
    print(f"  - Luminosidad Total: {sistema_planetario.estrella.luminosidad()}")
    print(f"  - Luminosidad de secuencia principal: {sistema_planetario.estrella.l_secuencia_principal()}")
    print()

    # Imprimir los planetas ordenados por radio semi-mayor
    print("Planetas ordenados por radio semi-mayor:")
    sistema_planetario.planetas_ordenados_por_radio()
    print()
