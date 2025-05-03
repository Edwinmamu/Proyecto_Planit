import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("SITIOS_TURISTICOS_20250502.csv")

# Título de la app
st.title("Sitios Turísticos")

# Mostrar el DataFrame completo
st.dataframe(df)

# Agregar filtros opcionales
st.sidebar.header("Filtrar por:")
tipo = st.sidebar.selectbox("Tipo de Atractivo", ["Todos"] + df["Tipo de Atractivo"].unique().tolist())
ubicacion = st.sidebar.selectbox("Ubicación", ["Todos"] + df["Ubicación"].unique().tolist())

# Aplicar filtros si se seleccionan
if tipo != "Todos":
    df = df[df["Tipo de Atractivo"] == tipo]

if ubicacion != "Todos":
    df = df[df["Ubicación"] == ubicacion]

# Mostrar resultados filtrados
st.subheader("Resultados filtrados")
st.dataframe(df)
