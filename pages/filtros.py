import streamlit as st
import pandas as pd
import datetime

# Función para cargar datos directamente en este archivo
@st.cache_data
def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

# Carga del dataset
df = cargar_datos("data/dataset.csv")  # Asegúrate que el archivo esté en /data/

st.title("🔍 Filtros de Datos")

# Filtro por Región
region_seleccionada = st.selectbox("Selecciona una Región", options=["Todas"] + sorted(df["Region"].unique().tolist()))
if region_seleccionada != "Todas":
    df = df[df["Region"] == region_seleccionada]

# Filtro por Canal de Venta
canal_seleccionado = st.selectbox("Selecciona un Canal de Venta", options=["Todos"] + sorted(df["Sales Channel"].unique().tolist()))
if canal_seleccionado != "Todos":
    df = df[df["Sales Channel"] == canal_seleccionado]

# Filtro por Prioridad de Pedido
prioridad_seleccionada = st.selectbox("Selecciona Prioridad del Pedido", options=["Todas"] + sorted(df["Order Priority"].unique().tolist()))
if prioridad_seleccionada != "Todas":
    df = df[df["Order Priority"] == prioridad_seleccionada]

# Filtro por rango de fechas
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()
fecha_inicio, fecha_fin = st.slider(
    "Selecciona un rango de fechas",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)
df = df[(df["Order Date"].dt.date >= fecha_inicio) & (df["Order Date"].dt.date <= fecha_fin)]

# Mostrar resultados filtrados
st.subheader("📄 Datos Filtrados")
st.write(f"Filas encontradas: {df.shape[0]}")
st.dataframe(df)
