import os
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# cantidad de preguntascorrectamente en cada fase
data = {
    'Fase': ['1 Fuente', '11 Fuentes', '18 Fuentes'],
    'Preguntas Respondidas Correctamente': [1, 6, 10]
}

df = pd.DataFrame(data)

image_folder = "DATOS"

#Mapeo de fases a carpeta
fase_map = {
    '1 Fuente': 'UNAF',
    '11 Fuentes': 'DOSF',
    '18 Fuentes': 'TRESF'
}

#redimensionar imágenes
def redimensionar_imagen(imagen, width=300, height=300):
    return imagen.resize((width, height))

# Título
st.title("📊 Evaluación del Chatbot: Aumento de Fuentes y Capacidad de Respuesta")

# Side naveg
st.sidebar.title("📋 Navegación")
seccion = st.sidebar.radio("Selecciona una sección",
                           ["Introducción", "Metodología", "Resultados", "Discusión", "Conclusiones", "Preguntas Frecuentes"])

if seccion == "Introducción":
    st.header("🔍 Introducción")
    st.write("""
    Bienvenido a la evaluación del chatbot sobre reglas y tácticas del fútbol. Este experimento tiene como objetivo analizar cómo 
    el incremento en el número de fuentes de información puede mejorar la capacidad de respuesta del chatbot.

    ### Contexto
    En el ámbito deportivo, especialmente en fútbol, la precisión y la profundidad del conocimiento son esenciales. Los chatbots que pueden 
    proporcionar respuestas rápidas y correctas a preguntas complejas son herramientas valiosas tanto para aficionados como para profesionales.

    ### Objetivos del Experimento
    1. Evaluar la capacidad del chatbot para responder preguntas específicas con una sola fuente de información.
    2. Analizar cómo mejora esta capacidad al aumentar a once y dieciocho fuentes de información.
    3. Determinar el impacto de la diversidad de fuentes en la precisión y utilidad del chatbot.

    A continuación, detallamos la metodología empleada y los resultados obtenidos.
    """)

elif seccion == "Metodología":
    st.header("🔬 Metodología")
    st.write("""
    Para evaluar la capacidad del chatbot, se siguió el siguiente procedimiento:

    ### Fases de la Evaluación
    1. **Fase 1:** El chatbot tenía acceso a una única fuente de información.
    2. **Fase 2:** El chatbot contaba con once fuentes de información diferentes.
    3. **Fase 3:** Se incrementaron las fuentes de información a dieciocho.

    ### Proceso de Evaluación
    - **Selección de Preguntas:** Se formularon 10 preguntas específicas sobre reglas y tácticas del fútbol.
    - **Evaluación de Respuestas:** Cada respuesta del chatbot fue evaluada por su precisión y relevancia.
    - **Criterios de Evaluación:** Las respuestas se clasificaron como correctas o incorrectas basado en su exactitud.

    Este enfoque permite observar cómo el acceso a más información afecta la capacidad del chatbot para proporcionar respuestas precisas.
    """)

elif seccion == "Resultados":
    st.header("📈 Resultados")

    #fase para ver detalles
    fase_seleccionada = st.selectbox('Selecciona una fase para ver los detalles de las respuestas:', df['Fase'])

    st.subheader(f"Detalles de respuestas en {fase_seleccionada}")

    #Obtener la ruta de la carpeta seleccionada
    selected_folder = os.path.join(image_folder, fase_map[fase_seleccionada])

    #mostrar imág
    for image_file in sorted(os.listdir(selected_folder)):
        image_path = os.path.join(selected_folder, image_file)
        image = Image.open(image_path)
        image_resized = redimensionar_imagen(image)
        st.image(image_resized, caption=image_file, use_column_width=True)

    st.subheader("Tabla de Resultados")
    st.dataframe(df)

    st.subheader("Gráficos de Resultados")

    # Gráfico preguntas respondidas bien
    fig = px.bar(df, x='Fase', y='Preguntas Respondidas Correctamente',
                 title='Cantidad de Preguntas Respondidas Correctamente')
    st.plotly_chart(fig)

    st.subheader("Comparación Lado a Lado")
    pregunta_seleccionada = st.selectbox('Selecciona una pregunta para comparar:', [
        "¿Cuál es el procedimiento para hacer un saque inicial?",
        "¿Cuáles son las superficies del terreno de juego?",
        "¿Cuándo es válido un gol?",
        "¿Qué debe hacer el lanzador al ejecutar el saque de banda?",
        "¿Cuándo se considera completo un penal?",
        "¿Qué se necesita para jugar el 1-4-4-2?",
        "¿Cuál es la duración de los periodos de juego?",
        "¿Cuál es el procedimiento para ejecutar tiros libres?",
        "¿Qué es un fuera de juego?",
        "¿Cuáles son las causas que prolongan un juego?"
    ])

    # Mapeo de nombres de preguntas a nombres de archivos de imágenes
    pregunta_index = {
        "¿Cuál es el procedimiento para hacer un saque inicial?": "img.png",
        "¿Cuáles son las superficies del terreno de juego?": "img_1.png",
        "¿Cuándo es válido un gol?": "img_2.png",
        "¿Qué debe hacer el lanzador al ejecutar el saque de banda?": "img_3.png",
        "¿Cuándo se considera completo un penal?": "img_4.png",
        "¿Qué se necesita para jugar el 1-4-4-2?": "img_5.png",
        "¿Cuál es la duración de los periodos de juego?": "img_6.png",
        "¿Cuál es el procedimiento para ejecutar tiros libres?": "img_7.png",
        "¿Qué es un fuera de juego?": "img_8.png",
        "¿Cuáles son las causas que prolongan un juego?": "img_9.png"
    }

    columnas = st.columns(3)
    fases = ['1 Fuente', '11 Fuentes', '18 Fuentes']
    for i, fase in enumerate(fases):
        with columnas[i]:
            st.write(f"**{fase}**")
            image_file = pregunta_index[pregunta_seleccionada]
            image_path = os.path.join(image_folder, fase_map[fase], image_file)
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image_resized = redimensionar_imagen(image)
                st.image(image_resized, caption=image_file, use_column_width=True)
            else:
                st.write("Imagen no disponible")

elif seccion == "Discusión":
    st.header("💬 Discusión")
    st.write("""
    Los resultados de este experimento proporcionan una visión valiosa sobre cómo la cantidad de fuentes de información puede influir en la capacidad del chatbot.

    ### Observaciones Clave
    - **Incremento en Precisión:** Se observó una mejora significativa en la capacidad del chatbot para responder preguntas correctamente al aumentar el número de fuentes.
    - **Diversidad de Información:** Las fuentes adicionales permitieron al chatbot cubrir una mayor variedad de temas y proporcionar respuestas más completas.

    ### Limitaciones del Estudio
    - **Calidad vs. Cantidad:** Aunque se incrementó la cantidad de fuentes, la calidad de las mismas también es un factor crucial que debe considerarse.
    - **Especificidad de las Preguntas:** Algunas preguntas pueden requerir fuentes más especializadas para obtener respuestas precisas.

    Estos hallazgos subrayan la importancia de no solo aumentar la cantidad de fuentes, sino también asegurar que estas sean de alta calidad y relevancia.
    """)

elif seccion == "Conclusiones":
    st.header("🏁 Conclusiones")
    st.write("""
    ### Resultados Clave
    1. **Mejora Significativa:** Incrementar el número de fuentes de información amplía la capacidad del chatbot para responder más preguntas correctamente.
    2. **Diversidad y Precisión:** Las fuentes adicionales permiten cubrir una mayor diversidad de temas, mejorando la precisión y utilidad del chatbot.
    3. **Relevancia de la Calidad:** La calidad de las fuentes es tan importante como la cantidad. Fuentes confiables y específicas son cruciales para maximizar el desempeño.

    ### Recomendaciones para Futuros Estudios
    - **Evaluar la Calidad de las Fuentes:** Realizar estudios que enfoquen en la calidad y no solo en la cantidad de las fuentes de información.
    - **Ampliar el Rango de Preguntas:** Incluir una mayor variedad de preguntas para obtener una evaluación más exhaustiva.
    - **Integración de Feedback:** Implementar un sistema de feedback continuo para mejorar las respuestas del chatbot basado en la interacción con los usuarios.

    En resumen, este estudio demuestra que un aumento en las fuentes de información mejora notablemente la capacidad de respuesta del chatbot, aunque es crucial considerar la calidad de las mismas.
    """)
elif seccion == "Preguntas Frecuentes":
    st.header("❓ Preguntas Frecuentes (FAQ)")
    st.write("""
    Aquí respondemos algunas de las preguntas más frecuentes sobre el estudio y el chatbot.

    ### ¿Cuál es el objetivo del estudio?
    El objetivo es analizar cómo el incremento en el número de fuentes de información puede mejorar la capacidad de respuesta del chatbot.

    ### ¿Cómo se evaluó el chatbot?
    Se formularon 10 preguntas específicas sobre reglas y tácticas del fútbol, y se evaluó la precisión y relevancia de las respuestas proporcionadas por el chatbot en diferentes fases.

    ### ¿Qué se entiende por una fuente de información?
    Una fuente de información puede ser un artículo, libro, base de datos o cualquier recurso que proporcione información relevante sobre el tema en cuestión.

    ### ¿Cómo se planean implementar las mejoras propuestas?
    Las mejoras se implementarán en fases, comenzando con la incorporación de fuentes adicionales y mejoras en el algoritmo de procesamiento del lenguaje natural.
    """)


#comentarios
st.sidebar.header("💬 Comentarios y Evaluaciones")
comentarios = st.sidebar.text_area("Deja tus comentarios sobre la evaluación:")
if st.sidebar.button("Enviar"):
    if comentarios:
        with open("comentarios.txt", "a") as f:
            f.write(comentarios + "\n")
        st.sidebar.write("Gracias por tus comentarios!")
    else:
        st.sidebar.write("Por favor, escribe un comentario antes de enviar.")
