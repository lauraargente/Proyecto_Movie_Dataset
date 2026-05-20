# 🎬 Análisis de Películas TMDB 5000

Proyecto de análisis de datos y visualización construido en Python a partir de los datasets **TMDB 5000 Movies** y **TMDB 5000 Credits**.

El objetivo principal del notebook es explorar tendencias de la industria cinematográfica, limpiar y transformar datos, responder preguntas de negocio mediante análisis exploratorio (EDA) y preparar un dashboard interactivo con Streamlit.

---

# 📌 Objetivos del proyecto

Este análisis busca responder preguntas como:

* ¿Qué géneros son más rentables?
* ¿Cómo ha evolucionado el presupuesto medio por década?
* ¿Hay directores que “garanticen” taquilla?
* ¿Las películas con mejor puntuación ganan más dinero?
* ¿La duración de la película influye en el éxito?
* ¿Qué géneros reciben mayores presupuestos?
---

# 🧰 Tecnologías utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* MySQL / TiDB
* Streamlit
* Jupyter Notebook

---

# 📂 Estructura del notebook

## Fase 01 — Configuración de la base de datos

* Instalación de dependencias.
* Conexión a MySQL/TiDB.
* Verificación de conexión.

## Fase 02 — Importación de datasets

Se cargan los archivos:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Además:

* Exploración inicial.
* Revisión de tipos de datos.
* Detección de valores nulos.

## Fase 03 — Carga de datos en TiDB

* Inserción de datasets en la base de datos.
* Persistencia de información para análisis posteriores.

## Fase 04 — Dataset analítico

* Unión de tablas.
* Construcción del dataset principal.
* Preparación para limpieza y EDA.

## Fase 05 — Limpieza y preprocesamiento

Transformaciones realizadas:

* Conversión de fechas (`release_date`).
* Extracción de año y década.
* Tratamiento de nulos.
* Eliminación de registros inconsistentes.
* Creación de métricas derivadas:

  * ROI
  * Beneficio
* Parsing de géneros.

## Fase 06 — EDA (Exploratory Data Analysis)

Análisis visual y estadístico para responder preguntas de negocio.

### Análisis realizados

* Géneros más rentables.
* Evolución del presupuesto medio por década.
* Relación entre puntuación y recaudación.
* Distribución de ROI.
* Correlaciones.
* Géneros con mayor presupuesto.

### Visualizaciones utilizadas

* Heatmaps
* Barplots
* Histogramas
* Gráficos de líneas
* Scatter plots

## Fase 07 — Dashboard con Streamlit

Preparación de un dashboard interactivo para visualizar resultados del análisis.

---

# 🗃️ Dataset

Fuente:

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

Contiene información sobre:

* Películas
* Géneros
* Presupuesto
* Recaudación
* Valoraciones
* Popularidad
* Reparto y directores

---

# 📊 Principales métricas analizadas

| Métrica      | Descripción                |
| ------------ | -------------------------- |
| Budget       | Presupuesto de la película |
| Revenue      | Recaudación                |
| Profit       | Beneficio generado         |
| ROI          | Retorno sobre inversión    |
| Vote Average | Valoración media           |

---

# ▶️ Cómo ejecutar el proyecto

## 1. Clonar repositorio

```bash
git clone <repo-url>
cd <repo>
```

## 2. Instalar dependencias

```bash
pip install pandas matplotlib seaborn mysql-connector-python streamlit
```

## 3. Ejecutar notebook

```bash
jupyter notebook
```

Abrir:

```bash
analisis.ipynb
```

---

# ⚙️ Requisitos

* Python 3.10+
* Jupyter Notebook
* Base de datos MySQL/TiDB

---

# 📈 Resultados esperados

El proyecto permite:

* Entender patrones de rentabilidad en cine.
* Detectar géneros más exitosos.
* Analizar evolución histórica del presupuesto.
* Construir dashboards interactivos.
* Practicar workflows completos de análisis de datos.

---

# 🚀 Posibles mejoras futuras

* Modelos predictivos de éxito comercial.
* Recomendador de películas.
* Da
