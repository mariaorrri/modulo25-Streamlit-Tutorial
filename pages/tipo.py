import streamlit as st
from PIL import Image
from utils import analyze_image

st.title("Analizador de Imágenes")

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    
    if st.button('Analizar imagen'):
        with st.spinner('Analizando...'):
            resultado = analyze_image(image)
        
    st.write('Es un vater')    
    