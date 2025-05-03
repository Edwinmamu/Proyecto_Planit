import os
import requests

# URL del archivo raw en GitHub
url = "https://raw.githubusercontent.com/azhar2ds/DataSets/master/10000%20Sales%20Records.csv"

# Crear carpeta "data" si no existe
os.makedirs("data", exist_ok=True)

# Ruta destino
ruta_destino = os.path.join("data", "dataset.csv")

# Descargar el archivo
print("Descargando archivo...")
respuesta = requests.get(url)

if respuesta.status_code == 200:
    with open(ruta_destino, "wb") as f:
        f.write(respuesta.content)
    print(f"✅ Archivo descargado correctamente en: {ruta_destino}")
else:
    print(f"❌ Error al descargar el archivo. Código de estado: {respuesta.status_code}")
