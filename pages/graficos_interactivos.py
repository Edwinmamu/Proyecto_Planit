import streamlit as st
import pandas as pd
import plotly.express as px

# Función para cargar datos directamente
@st.cache_data
def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

# Carga de datos
df = cargar_datos("data/dataset.csv")  # Asegúrate que el archivo esté en /data/

st.title("📊 Gráficos Interactivos")

# Filtro por Región
region_seleccionada = st.selectbox("Selecciona una Región", options=["Todas"] + sorted(df["Region"].unique().tolist()))
if region_seleccionada != "Todas":
    df = df[df["Region"] == region_seleccionada]

# Filtro por Tipo de Artículo
item_type_seleccionado = st.selectbox("Selecciona Tipo de Artículo", options=["Todos"] + sorted(df["Item Type"].unique().tolist()))
if item_type_seleccionado != "Todos":
    df = df[df["Item Type"] == item_type_seleccionado]

# Filtro por Canal de Venta
canal_seleccionado = st.selectbox("Selecciona Canal de Venta", options=["Todos"] + sorted(df["Sales Channel"].unique().tolist()))
if canal_seleccionado != "Todos":
    df = df[df["Sales Channel"] == canal_seleccionado]

# Gráfico interactivo de barras: Total Revenue por País
st.subheader("📈 Total Profit a lo largo del tiempo")
df_profit_fecha = df.groupby("Order Date")["Total Profit"].sum().reset_index()
fig_profit = px.line(
    df_profit_fecha,
    x="Order Date",
    y="Total Profit",
    title="Ganancias Totales por Fecha"
)
st.plotly_chart(fig_profit, use_container_width=True)