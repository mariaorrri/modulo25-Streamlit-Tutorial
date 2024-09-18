import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Bienvenidos al analizador de fontaneros!')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')
    
    opcion = st.radio('', 
                      ('Análisis general', 'Recomendación', '¿Qué tipo de WC tengo?'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Análisis general':
        switch_page("general")
    elif opcion == 'Recomendación':
        switch_page("recomendacion")
    elif opcion == '¿Qué tipo de WC tengo?':
        switch_page("tipo")
    



if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2