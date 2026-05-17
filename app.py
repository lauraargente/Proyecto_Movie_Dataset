# Para lanzar la app:
# streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import ast

st.set_page_config(page_title="Dashboard de Películas", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_pickle("dataset_analitico.pkl")

df_tablajoin = cargar_datos()

# Limpieza básica
df_tablajoin = df_tablajoin[
    (df_tablajoin["budget"] > 0) & 
    (df_tablajoin["revenue"] > 0)
]

# Crear columnas nuevas
df_tablajoin["profit"] = df_tablajoin["revenue"] - df_tablajoin["budget"]
df_tablajoin["roi"] = df_tablajoin["profit"] / df_tablajoin["budget"]

df_tablajoin["genres_parsed"] = df_tablajoin["genres"].apply(
    lambda x: [i["name"] for i in ast.literal_eval(x)]
)

st.title("🎬 Dashboard de Películas")
st.markdown("Análisis de rentabilidad, presupuesto y éxito de películas.")

st.sidebar.header("Filtros")

puntuacion_min = st.sidebar.slider(
    "Puntuación mínima",
    0.0,
    10.0,
    0.0
)

# # Filtro de género
# generos = df_tablajoin.explode("genres_parsed")["genres_parsed"].unique()

# genero_seleccionado = st.sidebar.selectbox(
#     "Selecciona un género",
#     ["Todos"] + sorted(generos.tolist())
# )

# df_f = df_tablajoin[
#     df_tablajoin["vote_average"] >= puntuacion_min
# ].copy()

# # Aplicar filtro de género
# if genero_seleccionado != "Todos":
#     df_f = df_f[
#         df_f["genres_parsed"].apply(
#             lambda x: genero_seleccionado in x
#         )
#     ]

generos = df_tablajoin.explode("genres_parsed")["genres_parsed"].dropna().unique()
generos = [g for g in generos if isinstance(g, str)]

genero_seleccionado = st.sidebar.selectbox(
    "Selecciona un género",
    ["Todos"] + sorted(generos)
)

df_f = df_tablajoin[df_tablajoin["vote_average"] >= puntuacion_min].copy()

if genero_seleccionado != "Todos":
    df_f = df_f[
        df_f["genres_parsed"].apply(lambda x: genero_seleccionado in x)
    ]

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "🎬 Total películas",
    len(df_f)
)

col2.metric(
    "💰 Revenue total",
    f"{df_f['revenue'].sum():,.0f} $"
)

col3.metric(
    "📈 ROI medio",
    f"{df_f['roi'].mean():.2f}"
)

# PREGUNTA 1
st.subheader("🎭 ¿Qué géneros son más rentables?")

df_generos = df_f.explode("genres_parsed")

if genero_seleccionado != "Todos":
    df_generos = df_generos[
        df_generos["genres_parsed"] == genero_seleccionado
    ]

roi_generos = (
    df_generos.groupby("genres_parsed")["roi"]
    .median()
    .sort_values(ascending=False)
)

if len(roi_generos) > 0:
    fig = px.bar(
        roi_generos.head(10),
        title="ROI mediano por género",
        labels={
            "value": "ROI mediano",
            "genres_parsed": "Género"
        }
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write(f"El género más rentable es **{roi_generos.index[0]}**.")
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")

# PREGUNTA 2
st.subheader("💰 ¿Ha cambiado el presupuesto medio por década?")

df_f["year"] = pd.to_datetime(df_f["release_date"]).dt.year
df_f["decade"] = (df_f["year"] // 10) * 10

budget_decade = (
    df_f.groupby("decade")["budget"]
    .mean()
    .sort_index()
)

if len(budget_decade) > 0:
    fig2 = px.line(
        budget_decade,
        markers=True,
        title="Presupuesto medio por década",
        labels={"value": "Presupuesto medio", "decade": "Década"}
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.write(f"La década con mayor presupuesto medio fue **{budget_decade.idxmax()}**.")
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")

# PREGUNTA 3
st.subheader("🎬 ¿Hay directores que garanticen taquilla?")

df_f["director"] = df_f["crew"].apply(
    lambda x: next(
        (persona["name"] for persona in ast.literal_eval(x) if persona["job"] == "Director"),
        None
    )
)

director_revenue = (
    df_f.groupby("director")["revenue"]
    .mean()
    .sort_values(ascending=False)
    .dropna()
)

if len(director_revenue) > 0:
    fig3 = px.bar(
        director_revenue.head(10),
        title="Directores con mayor recaudación media",
        labels={"value": "Recaudación media", "director": "Director"}
    )

    st.plotly_chart(fig3, use_container_width=True)
    st.write(f"El director con mayor recaudación media es **{director_revenue.index[0]}**.")
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")

# PREGUNTA 4
st.subheader("⭐ ¿Las películas con mejor puntuación ganan más dinero?")

df_f["grupo_puntuacion"] = pd.cut(
    df_f["vote_average"],
    bins=[0, 5, 6, 7, 8, 10]
).astype(str)

revenue_score = (
    df_f.groupby("grupo_puntuacion")["revenue"]
    .mean()
)

if len(revenue_score) > 0:
    fig4 = px.bar(
        revenue_score,
        title="Recaudación media según puntuación",
        labels={"value": "Recaudación media", "grupo_puntuacion": "Grupo de puntuación"}
    )

    st.plotly_chart(fig4, use_container_width=True)
    st.write("Las películas con mejor puntuación suelen recaudar más dinero de media.")
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")

# PREGUNTA 5
st.subheader("⏱️ ¿La duración influye en el éxito?")

df_f["grupo_duracion"] = pd.cut(
    df_f["runtime"],
    bins=[0, 90, 120, 150, 300]
).astype(str)

runtime_revenue = (
    df_f.groupby("grupo_duracion")["revenue"]
    .mean()
)

if len(runtime_revenue) > 0:
    fig5 = px.bar(
        runtime_revenue,
        title="Recaudación media según duración",
        labels={"value": "Recaudación media", "grupo_duracion": "Duración"}
    )

    st.plotly_chart(fig5, use_container_width=True)
    st.write("Las películas más largas suelen recaudar más dinero de media.")
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")

# PREGUNTA 6
st.subheader("💸 ¿Qué géneros reciben mayores presupuestos?")

df_generos_budget = df_f.explode("genres_parsed")

budget_generos = (
    df_generos_budget.groupby("genres_parsed")["budget"]
    .mean()
    .sort_values(ascending=False)
)

if len(budget_generos) > 0:
    fig6 = px.bar(
        budget_generos.head(10),
        title="Presupuesto medio por género",
        labels={
            "value": "Presupuesto medio",
            "genres_parsed": "Género"
        }
    )

    st.plotly_chart(fig6, use_container_width=True)

    st.write(
        f"El género con mayor presupuesto medio es **{budget_generos.index[0]}**."
    )
else:
    st.warning("No hay datos suficientes para mostrar este gráfico.")


