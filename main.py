# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de los parámetros fijos
precio_venta = 70000  # Precio de venta por unidad
costos_fijos = 240000000  # Costos fijos (administrativos y publicidad)

# Distribuciones de las variables de entrada
# Cada función simula una variable con las especificaciones dadas en el trabajo
# Simulación del costo de mano de obra (distribución discreta)
def generar_costo_mano_obra():
    return np.random.choice([10000, 13000, 16000, 19000, 22000], p=[0.1, 0.3, 0.3, 0.2, 0.1])

# Simulación del costo de componentes (distribución uniforme continua)
def generar_costo_componentes():
    return 25000 + np.random.uniform(0, 1) * (35000 - 25000)

# Simulación de la demanda anual (distribución normal)
def generar_demanda():
    return np.clip(np.random.normal(14500, 4000), 9000, 28500)

# Generamos muestras de cada variable para visualización de sus distribuciones
muestras_costo_mano_obra = [generar_costo_mano_obra() for _ in range(10000)]
muestras_costo_componentes = [generar_costo_componentes() for _ in range(10000)]
muestras_demanda = [max(0, generar_demanda()) for _ in range(10000)]  # Evitar valores negativos en demanda

# Visualización de las distribuciones de las variables de entrada
# Ajuste en la visualización de distribuciones de las variables de entrada
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Distribución de Costo de Mano de Obra
sns.histplot(muestras_costo_mano_obra, kde=False, color='skyblue', edgecolor='black', ax=axs[0])
axs[0].set_title("Distribución del Costo de Mano de Obra", fontsize=14)
axs[0].set_xlabel("Costo de Mano de Obra por Unidad (pesos)", fontsize=12)
axs[0].set_ylabel("Frecuencia", fontsize=12)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Distribución de Costo de Componentes
sns.histplot(muestras_costo_componentes, kde=True, color='lightcoral', edgecolor='black', ax=axs[1])
axs[1].set_title("Distribución del Costo de Componentes", fontsize=14)
axs[1].set_xlabel("Costo de Componentes por Unidad (pesos)", fontsize=12)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Distribución de la Demanda
sns.histplot(muestras_demanda, kde=True, color='lightgreen', edgecolor='black', ax=axs[2])
axs[2].axvline(np.mean(muestras_demanda), color='darkgreen', linestyle='--', label="Media de Demanda")
axs[2].set_title("Distribución de la Demanda Anual", fontsize=14)
axs[2].set_xlabel("Demanda Anual (Unidades)", fontsize=12)
axs[2].legend()
axs[2].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Iniciamos el proceso de simulación de Montecarlo
n_simulaciones = 10000  # Número de iteraciones para la simulación
utilidades = []  # Lista para almacenar el resultado de cada simulación

# Ejecución de las iteraciones
for _ in range(n_simulaciones):
    # Generación de valores aleatorios para cada variable en una iteración
    costo_mano_obra = generar_costo_mano_obra()
    costo_componentes = generar_costo_componentes()
    demanda = max(0, generar_demanda())  # Evitar valores negativos en demanda

    # Cálculo de la utilidad para esta combinación de variables
    utilidad = (precio_venta - costo_mano_obra - costo_componentes) * demanda - costos_fijos
    utilidades.append(utilidad)

# Convertimos la lista de utilidades a un array de numpy para el análisis
utilidades = np.array(utilidades)

# Cálculo de estadísticas clave
utilidad_promedio = np.mean(utilidades)
utilidad_mediana = np.median(utilidades)
probabilidad_perdida = np.sum(utilidades < 0) / n_simulaciones

# Visualización de la distribución de la utilidad con área de pérdidas resaltada y porcentaje de pérdidas

plt.figure(figsize=(12, 6))
# Visualización de la distribución de la utilidad con métricas clave y casos extremos

# Calcular el caso pesimista (mínima utilidad) y el caso optimista (máxima utilidad)
utilidad_minima = np.min(utilidades)  # Caso pesimista
utilidad_maxima = np.max(utilidades)  # Caso optimista

plt.figure(figsize=(12, 6))

# Graficamos la distribución de la utilidad
sns.histplot(utilidades, kde=True, color='blue', bins=50, label="Distribución de Utilidad")

# Resaltar el área de pérdidas (utilidad negativa)
plt.fill_betweenx(y=[0, plt.gca().get_ylim()[1]], x1=-1e8, x2=0, color='red', alpha=0.3, label="Pérdidas")

# Líneas de referencia para la media y mediana
plt.axvline(utilidad_promedio, color='red', linestyle='--', label=f'Promedio: {utilidad_promedio:,.2f}')
plt.axvline(utilidad_mediana, color='green', linestyle='--', label=f'Mediana: {utilidad_mediana:,.2f}')

# Agregar líneas y anotaciones para el caso pesimista y optimista
plt.axvline(utilidad_minima, color='purple', linestyle='--', label=f'Caso Pesimista: {utilidad_minima:,.2f}')
plt.axvline(utilidad_maxima, color='orange', linestyle='--', label=f'Caso Optimista: {utilidad_maxima:,.2f}')

# Cuadro de texto con las métricas clave
plt.text(0.65e8, plt.gca().get_ylim()[1] * 0.8,
         f"Promedio: {utilidad_promedio:,.2f}\nMediana: {utilidad_mediana:,.2f}\n"
         f"Prob. de Pérdida: {probabilidad_perdida*100:.2f}%\n"
         f"Optimista: {utilidad_maxima:,.2f}\nPesimista: {utilidad_minima:,.2f}",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Etiquetas y leyenda
plt.title("Distribución de la Utilidad Simulada con Casos Pesimista y Optimista")
plt.xlabel("Utilidad en pesos")
plt.ylabel("Frecuencia")
plt.legend()

# Mostrar gráfico
plt.show()

# Mostramos las métricas clave en pantalla
utilidad_promedio, utilidad_mediana, probabilidad_perdida, plt.show()
