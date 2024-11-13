# Simulación de Montecarlo para Evaluación de Rentabilidad de Impresora Portátil

## Descripción del Proyecto
Este proyecto utiliza una **Simulación de Montecarlo** para evaluar la rentabilidad y el riesgo de lanzamiento de un nuevo producto: una impresora portátil de alta calidad. La empresa PcSA desea estimar el potencial de ganancias del primer año de ventas y evaluar la probabilidad de pérdidas dadas las incertidumbres en costos y demanda.

## Objetivo
El objetivo es proporcionar una estimación robusta de la **utilidad anual esperada** y la **probabilidad de pérdida** considerando las variaciones en los **costos de mano de obra**, **costos de componentes** y la **demanda anual**. Esto ayudará al equipo directivo a tomar decisiones informadas sobre la viabilidad del lanzamiento.

## Estructura del Código

1. **Importación de Librerías**
   - `numpy`: Para generar números aleatorios y cálculos estadísticos.
   - `matplotlib.pyplot` y `seaborn`: Para la visualización de datos y distribuciones.
   
2. **Parámetros Fijos**
   - `precio_venta`: Precio de venta por unidad (70,000 pesos).
   - `costos_fijos`: Costos fijos administrativos y publicitarios (240 millones de pesos).

3. **Funciones para Variables de Entrada**
   - `generar_costo_mano_obra()`: Genera un costo de mano de obra aleatorio entre $10,000 y $22,000 según probabilidades definidas.
   - `generar_costo_componentes()`: Genera un costo de componentes aleatorio entre $25,000 y $35,000 usando una distribución uniforme.
   - `generar_demanda()`: Genera un valor de demanda usando una distribución normal con media de 14,500 y desviación estándar de 4,000, ajustando el rango a 9,000 - 28,500 unidades.

4. **Simulación de Montecarlo**
   - La simulación se ejecuta con 10,000 iteraciones, generando un valor de utilidad para cada combinación aleatoria de costos y demanda. 
   - Para cada iteración, la utilidad se calcula con la fórmula:

     **Utilidad=(Precio de Venta−Costo de Mano de Obra−Costo de Componentes)×Demanda−Costos Fijos**

5. **Visualización de Resultados**
   - Gráficos de la distribución de **Costo de Mano de Obra**, **Costo de Componentes** y **Demanda Anual**.
   - Gráfico de la distribución de la **Utilidad Simulada** que incluye:
     - Líneas de referencia para el promedio y la mediana.
     - Área de pérdidas resaltada y porcentaje de probabilidad de pérdida.
     - Casos **pesimista** (mínima utilidad) y **optimista** (máxima utilidad) destacados.

## Resultados Clave

- **Utilidad Promedio**: Aproximadamente 112,988,652.99 pesos (varia por cada ejecucion del programa)
- **Mediana de la Utilidad**: Aproximadamente 104,136,835.92 pesos (varia por cada ejecucion del programa)
- **Probabilidad de Pérdida**: Entre un 14.5% a 17%, indicando un riesgo moderado. (varia por cada ejecucion del programa)
- **Casos Extremos**:
   - **Caso Optimista** (mayor utilidad): X pesos.
   - **Caso Pesimista** (menor utilidad): X pesos.

Estos resultados permiten a la empresa PcSA evaluar el riesgo y tomar una decisión informada sobre el lanzamiento del producto.

## Instrucciones para Ejecutar el Código

1. **Requisitos**:
   - Python 3.x
   - Librerías necesarias: `numpy`, `matplotlib`, `seaborn`
   
   Puedes instalarlas con:
   ```bash
   pip install numpy matplotlib seaborn
   ```

2. **Ejecución**:
   - Clona el repositorio y navega al directorio del proyecto:
     ```bash
     git clone <URL_DEL_REPOSITORIO>
     cd <NOMBRE_DEL_DIRECTORIO>
     ```
   - Ejecuta el archivo `.py` o el cuaderno de Jupyter que contiene el código:
     ```bash
     python main.py
     ```

## Explicación de los Resultados

Cada gráfico generado permite visualizar los siguientes aspectos del análisis:

- **Distribuciones de las Variables de Entrada**: Muestran la variabilidad esperada en los costos y la demanda.
- **Distribución de la Utilidad Simulada**: Muestra el rango de posibles utilidades, destacando la probabilidad de pérdida y los valores promedio, pesimista y optimista.

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
