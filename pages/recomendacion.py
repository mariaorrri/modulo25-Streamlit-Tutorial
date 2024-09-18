import streamlit as st
import pandas as pd
from utils import predict_flores
from utils import perform_analysis_and_generate_csv

# Título de la aplicación
st.title('Recomendaciones')


# Widget para cargar un archivo CSV
# Texto introductorio
st.write('**Introduce los códigos de los artículos:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características de la flor
columns = ['Número de cliente', 'árticulo 1', 'árticulo 2', 'árticulo 3', 'artículo 4']

# Bucle para recorrer las columnas y obtener los datos de entrada
for col in columns:
    # Widget de entrada numérica para cada característica
    input_data[col] = st.text_input(col)

# Botón para realizar la predicción
if st.button('Proponer recomendación'):
    # with st.spinner('Quizás quiera comprar...'):
    #     csv_result = perform_analysis_and_generate_csv()
    
    # st.success('Análisis completado!')
    st.write('**Quizás quiera comprar...**')
    st.write('Recomendación 1: grifo Victoria')
    st.write('Recomendación 2: fregadero Henares')
    