import streamlit as st
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Conexion MongoDB
client = MongoClient('mongodb+srv://damons07:mNcsCwuuA8vYuxB9@prediccion2024.htxnzwm.mongodb.net/')
db = client.sample_geospatial
collection = db.shipwrecks

#Obtener datos de la colección
df = pd.DataFrame(list(collection.find()))

#Mostrar opciones para el combo
opciones = ["Sin limpieza", "Con limpieza"]
opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción:", opciones)

# Mostrardataframe
if opcion_seleccionada == "Sin limpieza":
    st.write("Dataframe sin limpieza:")
    st.write(df)
else:
    #Seleccionar las colunas
    df_limpio = df[["recrd", "latdec", "londec", "depth", "watlev", "feature_type"]]
    df_limpio.columns = ["Registro", "Latitud", "Longitud", "Profundidad", "Nivel del agua", "Tipo de característica"]
    st.write("Dataframe con limpieza:")
    st.write(df_limpio)

    #grafico de pastel
    tipocarac = df_limpio['Tipo de característica'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(tipocarac, labels=tipocarac.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Porcentaje de Tipo de Característica')
    st.pyplot(fig)
