import streamlit as st
import pandas as pd
from pymongo import MongoClient

#Conexion MongoDB
client = MongoClient("mongodb+srv://"+st.secrets["DB_USERNAME"]+":"+st.secrets["DB_PASSWORD"]+"@prediccion2024.htxnzwm.mongodb.net/")
db = client.sample_geospatial
collection = db.shipwrecks

#Obtener datos dl colección
df = pd.DataFrame(list(collection.find()))

#opciones
opciones = ["Sin limpieza", "Con limpieza"]
opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción:", opciones)

#sucio
if opcion_seleccionada == "Sin limpieza":
    st.write("Dataframe sin limpieza:")
    st.write(df)
else:
    #aqui se limpia y se muestra
    df_limpio = df[["recrd", "latdec", "londec", "depth", "watlev", "feature_type"]]
    df_limpio.columns = ["Registro", "LAT", "LON", "Profundidad", "Nivel del agua", "Tipo de característica"]
    st.write("Dataframe con limpieza:")
    st.write(df_limpio)

    #Mapa
    st.map(df_limpio, color="#00BFBF")
