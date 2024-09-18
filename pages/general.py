import streamlit as st
import pandas as pd
from utils import predict_flores
from utils import perform_analysis_and_generate_csv

# Título de la aplicación
st.title('Análisis general')


# Widget para cargar un archivo CSV
# Texto introductorio
st.write('**Introduce los datos del cliente:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características de la flor
columns = ['Número de cliente']

st.image('fontanero.png', use_column_width=True)

# Bucle para recorrer las columnas y obtener los datos de entrada
for col in columns:
    # Widget de entrada numérica para cada característica
    input_data[col] = st.text_input(col)

# Botón para realizar la predicción
if st.button('Realizar análisis'):
    with st.spinner('Realizando análisis...'):
        csv_result = perform_analysis_and_generate_csv()
    
    st.success('Análisis completado!')
    # st.download_button(
    #     label="Descargar resultados como CSV",
    #     data=csv_result,
    #     file_name="resultados_analisis.csv",
    #     mime="text/csv"
    # )