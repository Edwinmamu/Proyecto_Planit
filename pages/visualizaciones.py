import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from pages.load_data import cargar_datos

st.header("📈 Visualizaciones")

df = cargar_datos("data/dataset.csv")

# Gráfico de correlación
st.subheader("Mapa de calor de correlación")

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu", ax=ax)
st.pyplot(fig)
