import streamlit as st
import pandas as pd

# Cargar los datos
@st.cache_data
def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    return df

# Título y descripción
st.title("📊 Análisis de Ventas Interactivo")
st.write("Bienvenido a la aplicación de análisis de ventas. Puedes usar las pestañas del menú superior para interactuar con los datos.")

# Cargar los datos
df = cargar_datos("data/dataset.csv")  # Asegúrate que el archivo esté en /data/

# Mostrar un resumen de las primeras filas de datos
st.subheader("📝 Resumen de Datos Cargados")
st.write(f"Filas encontradas: {df.shape[0]}")
st.dataframe(df.head(10))  # Mostrar solo las primeras 10 filas para no sobrecargar la vista

# Mostrar un gráfico general de las ventas por región (sin filtros)
import plotly.express as px

# Agrupar por región y calcular la suma de las ventas
ventas_por_region = df.groupby("Region")["Total Revenue"].sum().reset_index()

# Crear un gráfico de barras de ventas por región
fig = px.bar(ventas_por_region, x="Region", y="Total Revenue", title="Ventas Totales por Región", labels={"Total Revenue": "Ventas Totales"})
st.plotly_chart(fig)

# Agregar un botón para redirigir al usuario a la pestaña de filtros
st.markdown("### ¿Quieres aplicar filtros a los datos?")
st.button("Ir a la pestaña de Filtros", on_click=lambda: st.session_state.selected_page("filtros"))
