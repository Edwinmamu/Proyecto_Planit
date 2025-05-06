

* Descripción del proyecto
* Estructura de carpetas
* Instrucciones de ejecución local y en Streamlit Cloud
* Enlace al repositorio de GitHub
* Dependencias
* `.gitignore` integrado como sección visible para facilitar referencia

---

### 📄 `README.md`

```markdown
# 📊 Proyecto Streamlit - Análisis de Ventas Globales

Este proyecto desarrollado con **Python y Streamlit** permite la carga, filtrado, análisis y visualización interactiva de datos de ventas globales. Utiliza herramientas modernas como `Pandas`, `Plotly`, `Seaborn`, `Matplotlib` y `NumPy`.

---

## 🌐 Demo en Streamlit

Accede a la versión en línea del proyecto:  
🔗 [Proyecto en Streamlit Cloud](https://streamlit.io/) *(agrega aquí tu URL personalizada si ya la tienes configurada)*

Repositorio en GitHub:  
📁 [https://github.com/Edwinmamu/Proyecto_Planit](https://github.com/Edwinmamu/Proyecto_Planit)

---

## 🗂 Estructura del Proyecto

```

Proyecto\_Planit/
│
├── .gitignore
├── requirements.txt
├── README.md
├── inicio.py                     # Página de bienvenida e introducción
├── pages/
│   ├── filtros.py               # Filtros interactivos de datos
│   ├── graficos\_interactivos.py # Visualizaciones con Plotly/Seaborn
│   └── cargar\_datos.py          # Visualización simple y descarga de dataset
├── data/
│   └── dataset.csv              # Archivo con los datos (no se sube al repositorio si está en .gitignore)
└── .streamlit/
└── config.toml              # Configuración de la app

````

---

## ▶️ Cómo Ejecutar Localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Edwinmamu/Proyecto_Planit.git
   cd Proyecto_Planit
````

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   streamlit run inicio.py
   ```

---

## 🚀 Despliegue en Streamlit Cloud

Para publicar tu aplicación:

1. Sube el proyecto a tu cuenta de GitHub.
2. Ve a [https://streamlit.io/cloud](https://streamlit.io/cloud) y conecta tu repositorio.
3. Asegúrate de incluir:

   * El archivo `requirements.txt`
   * El archivo principal (`inicio.py`)
   * La carpeta `data` con `dataset.csv` si deseas cargar datos directamente

---

## ✅ Dependencias utilizadas (`requirements.txt` generado)

```txt
streamlit
pandas
numpy
seaborn
matplotlib
plotly
```

Puedes actualizar este archivo automáticamente con:

```bash
pip freeze > requirements.txt
```

---

## 🛡 .gitignore

Este es el contenido del `.gitignore` recomendado:

```gitignore
# Python y entornos virtuales
__pycache__/
*.py[cod]
.venv/
env/
venv/
ENV/

# IDEs y editores
.vscode/
.idea/

# Mac/Windows
.DS_Store
Thumbs.db
desktop.ini

# Streamlit
.streamlit/config.toml
.streamlit/secrets.toml

# Archivos de datos (si deseas excluirlos)
# *.csv
# *.xlsx

# Logs
*.log
```

---

## ✍️ Créditos

Desarrollado por [Edwin Mamu](https://github.com/Edwinmamu) como parte del proyecto final para el módulo de Nuevas Tecnologías.

---

