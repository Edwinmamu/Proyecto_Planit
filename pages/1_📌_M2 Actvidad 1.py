import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# Mostrar título en la aplicación
st.title("Nuevas Tecnologias"
"Actividad 1 - Creación de DataFrames")

# Agregar una descripción debajo del título
st.write("En esta actividad, aprenderemos a crear y manipular DataFrames usando la librerías")

libros = {
    "título": ["El señor de los anillos", "Matar a un ruiseñor", "El principito", "Don Quijote de la Mancha"],
    "autor": ["J.R.R. Tolkie", "Harper Lee", "Antoine de Saint-Exupéry", "Miguel de Cervantes"],
    "año de publicación": [1954, 1960, 1943, 1605],
    "género": ["Fantasía épica", "Ficción literaria", "Fábula", "Novela clásica"]
}

df_libros = pd.DataFrame(libros)

st.write("### DataFrame de Libros")
st.dataframe(df_libros)


st.title("Actividad 2 - Creación de DataFrames con Lista de Diccionarios")
st.write("En esta actividad, trabajaremos con una lista de diccionarios para representar información sobre ciudades.")

ciudades = [
    {"nombre": "Medellin", "población": 22634570, "país": "Colombia"},
    {"nombre": "Ciudad de Mexico", "población": 929944, "país": "Mexico"},
    {"nombre": "París", "población": 2148000, "país": "Francia"},
    {"nombre": "Buenos Aires", "población": 2890151, "país": "Argentina"}
]

df_ciudades = pd.DataFrame(ciudades)

st.write("### Información de Ciudades")
st.dataframe(df_ciudades)
