import streamlit as st
import requests

def main():
    st.title("Predicción de resultados")

    st.write("Por favor, ingresa los detalles para realizar la predicción:")

    age = st.number_input("Edad", min_value=18, max_value=100, value=30)
    job = st.selectbox("Trabajo", ["technician", "blue-collar", "services", "management", "retired", "admin.", "housemaid", "unemployed", "entrepreneur", "self-employed", "student"])
    marital = st.selectbox("Estado Civil", ["married", "single", "divorced"])
    education = st.selectbox("Educación", ["professional", "basic.9y", "high.school", "basic.4y", "basic.6y", "unknown", "university.degree", "illiterate"])
    default = st.selectbox("Incumplimiento crediticio", ["no", "unknown", "yes"])
    housing = st.selectbox("Préstamo de vivienda", ["yes", "no", "unknown"])
    loan = st.selectbox("Préstamo personal", ["no", "yes", "unknown"])
    contact = st.selectbox("Contacto", ["cellular", "telephone"])
    month = st.selectbox("Mes", ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
    day_of_week = st.selectbox("Día de la semana", ["mon", "tue", "wed", "thu", "fri"])
    duration = st.number_input("Duración de la última llamada", min_value=0, value=0)
    campaign = st.number_input("Número de contactos realizados durante esta campaña", min_value=1, value=1)
    pdays = st.number_input("Número de días que han pasado desde que el cliente fue contactado por última vez", min_value=0, value=999)
    previous = st.number_input("Número de contactos realizados antes de esta campaña", min_value=0, value=0)
    poutcome = st.selectbox("Resultado de la campaña anterior", ["nonexistent", "failure", "success"])
    emp_var_rate = st.number_input("Tasa de variación del empleo", value=-1.8)
    cons_price_idx = st.number_input("Índice de precios al consumidor", value=92.893)
    cons_conf_idx = st.number_input("Índice de confianza del consumidor", value=-46.2)
    euribor3m = st.number_input("Euribor a 3 meses", value=1.299)
    nr_employed = st.number_input("Número de empleados", value=5099.1)

    if st.button("Predecir"):
        url = "http://f4b872f2-c90f-46c7-bd0f-9794ab21d04b.eastus.azurecontainer.io/score"

        data = {
          "Inputs": {
            "data": [
              {
                "age": age,
                "job": job,
                "marital": marital,
                "education": education,
                "default": default,
                "housing": housing,
                "loan": loan,
                "contact": contact,
                "month": month,
                "day_of_week": day_of_week,
                "duration": duration,
                "campaign": campaign,
                "pdays": pdays,
                "previous": previous,
                "poutcome": poutcome,
                "emp.var.rate": emp_var_rate,
                "cons.price.idx": cons_price_idx,
                "cons.conf.idx": cons_conf_idx,
                "euribor3m": euribor3m,
                "nr.employed": nr_employed
              }
            ]
          },
          "GlobalParameters": {
            "method": "predict"
          }
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            prediction = response.json()
            st.write("El resultado de la predicción es:", prediction)
        else:
            st.write("Error al realizar la predicción. Código de estado:", response.status_code)


if __name__ == "__main__":
    main()
