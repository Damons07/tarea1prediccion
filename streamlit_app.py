import streamlit as st
import pandas as pd
from pymongo import MongoClient

#Conexion MongoDB
client = MongoClient("mongodb+srv://"+st.secrets["DB_USERNAME"]+":"+st.secrets["DB_PASSWORD"]+"@prediccion2024.htxnzwm.mongodb.net/")
db = client.sample_geospatial
collection = db.shipwrecks

#Cachear la carga de recursos
@st.cache_resource()
#Cachear la creación del DataFrame con un tiempo de vida de caché de 60 segundos
@st.cache_data(ttl=60)
def cargar_datos_desde_mongodb():
    #Obtene datos de la colección
    return pd.DataFrame(list(collection.find()))

df = cargar_datos_desde_mongodb()

#opciones
opciones = ["Sin limpieza", "Con limpieza"]
opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción:", opciones)

#sucio
if opcion_seleccionada == "Sin limpieza":
    st.write("Dataframe sin limpieza:")
    st.write(df)
else:
    #aquí se limpia y se muestra
    df_limpio = df[["recrd", "latdec", "londec", "depth", "watlev", "feature_type"]]
    df_limpio.columns = ["Registro", "LAT", "LON", "Profundidad", "Nivel del agua", "Tipo de característica"]
    st.write("Dataframe con limpieza:")
    st.write(df_limpio)

    #Mapa
    st.map(df_limpio, color="#00BFBF")

    #Formulario
    st.header("FORMULARIO")
    st.write("Agregar nuevos datos")

    nuevo_registro = st.text_input("Registro")
    nueva_latitud = st.number_input("Latitud")
    nueva_longitud = st.number_input("Longitud")
    nueva_profundidad = st.number_input("Profundidad")
    nuevo_nivel_agua = st.text_input("Nivel de agua")
    nuevo_tipo_caracteristica = st.text_input("Tipo de característica")

    if st.button("Agregar"):
        nuevo_dato = {
            "recrd": nuevo_registro,
            "latdec": nueva_latitud,
            "londec": nueva_longitud,
            "depth": nueva_profundidad,
            "watlev": nuevo_nivel_agua,
            "feature_type": nuevo_tipo_caracteristica
        }
        collection.insert_one(nuevo_dato)
        st.success("Datos agregados correctamente")

    #Buscador por registro
    if opcion_seleccionada == "Con limpieza":
        st.header("Buscar por registro")
        registro_buscar = st.text_input("Ingrese el registro que desea buscar:")

        if registro_buscar:
            resultado = collection.find_one({"recrd": registro_buscar})
            if resultado:
                st.write("Resultado de la búsqueda:")
                st.write(resultado)
            else:
                st.write("No se encontraron resultados para el registro:", registro_buscar)
