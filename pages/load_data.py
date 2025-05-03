import streamlit as st
import pandas as pd

# Función para cargar los datos
def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    return df

# Título de la pestaña
st.title("📂 Cargar Datos")

# Cargar los datos
df = cargar_datos("data/dataset.csv")  # Asegúrate que el archivo esté en /data/

# Mostrar los primeros 10 registros si el DataFrame no está vacío
if not df.empty:
    st.subheader("📊 Datos Cargados")
    st.write(f"Filas encontradas: {df.shape[0]}")
    st.dataframe(df.head(10))  # Muestra las primeras 10 filas

    # Opción para descargar los datos en formato CSV
    st.subheader("🔽 Descargar Datos")
    csv = df.to_csv(index=False)  # Convierte el DataFrame a CSV sin el índice
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name="dataset.csv",
        mime="text/csv"
    )
else:
    st.error("No se pudieron cargar los datos. Verifica la ruta del archivo.")
