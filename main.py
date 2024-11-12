import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de los parámetros
precio_venta = 70000  # Precio de venta por unidad
costos_fijos = 240000000  # Costos fijos en pesos

# Distribuciones de las variables
def generar_costo_mano_obra():
    return np.random.choice([10000, 13000, 16000, 19000, 22000], p=[0.1, 0.3, 0.3, 0.2, 0.1])

def generar_costo_componentes():
    return 25000 + np.random.uniform(0, 1) * (35000 - 25000)

def generar_demanda():
    return np.random.normal(14500, 4000)

# Simulación de Montecarlo
n_simulaciones = 10000
utilidades = []

for _ in range(n_simulaciones):
    # Generación de valores aleatorios para cada variable
    costo_mano_obra = generar_costo_mano_obra()
    costo_componentes = generar_costo_componentes()
    demanda = max(0, generar_demanda())  # Evitar valores negativos en demanda

    # Cálculo de la utilidad para esta iteración
    utilidad = (precio_venta - costo_mano_obra - costo_componentes) * demanda - costos_fijos
    utilidades.append(utilidad)

# Convertimos la lista a un array de numpy para análisis
utilidades = np.array(utilidades)

# Cálculo de estadísticas
utilidad_promedio = np.mean(utilidades)
utilidad_mediana = np.median(utilidades)
probabilidad_perdida = np.sum(utilidades < 0) / n_simulaciones

# Visualización de los resultados
plt.figure(figsize=(12, 6))
sns.histplot(utilidades, kde=True, color='blue', bins=50)
plt.axvline(utilidad_promedio, color='red', linestyle='--', label=f'Promedio: {utilidad_promedio:,.2f}')
plt.axvline(utilidad_mediana, color='green', linestyle='--', label=f'Mediana: {utilidad_mediana:,.2f}')
plt.title("Distribución de la Utilidad Simulada")
plt.xlabel("Utilidad en pesos")
plt.ylabel("Frecuencia")
plt.legend()

# Mostrar las métricas clave en pantalla
utilidad_promedio, utilidad_mediana, probabilidad_perdida, plt.show()
