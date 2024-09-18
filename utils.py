import pickle
import streamlit as st
from keras.models import load_model
import tensorflow as tf
import numpy as np
import pandas as pd
import time
from io import BytesIO

def predict_flores(data):
    # Cargar el modelo previamente entrenado para predecir el tipo de flor
    model = pickle.load(open('models/iris_model.pkl', "rb"))
    # Realizar la predicción con los datos proporcionados
    predictions = model.predict(data) 
    return predictions

def predict_imagen(imagen):
    # Añadir una dimensión extra (lote)
    imagen = imagen.reshape((1, 32, 32, 3))
    # Cargar el modelo desde el archivo
    model = load_model('models/modelo_cifar_10.h5')
    # Realizar la predicción
    predictions = model.predict(imagen)
    predicted_class = tf.argmax(predictions[0]).numpy()
    # Obtener el nombre de la clase predicha
    class_names = ['avión', 'automóvil', 'pájaro', 'gato', 'ciervo', 'perro', 'rana', 'caballo', 'barco', 'camión']
    return class_names[predicted_class]

def check_client_id(client_id):
    # Simulación
    # Cargar credenciales para la BBDD de la empresa y consultar si el identificador del cliente está activo 
    api_key = st.secrets["DB_USERNAME"]
    ls_ids = [123,12345,12345678]
    return True if client_id in ls_ids else False

def perform_analysis_and_generate_csv():
    # Simular la generación de datos
    data = {
        'ID': range(1, 101),
        'Producto': [f'Producto {i}' for i in range(1, 101)],
        'Ventas': np.random.randint(100, 1000, 100),
        'Categoria': np.random.choice(['A', 'B', 'C'], 100)
    }
    df = pd.DataFrame(data)

    # Simular análisis
    time.sleep(2)  # Simula un proceso que toma tiempo
    result = df.groupby('Categoria').agg({
        'Ventas': ['sum', 'mean', 'count']
    })


def analyze_image(image):
    """
    Simula el análisis de una imagen.
    
    Args:
    image (PIL.Image): La imagen a analizar.
    
    Returns:
    str: El resultado del análisis.
    """
    # Simulamos un análisis de la imagen
    time.sleep(2)  # Simulamos un tiempo de procesamiento
    return "El modelo que has introducido es el Victoria de Roca"