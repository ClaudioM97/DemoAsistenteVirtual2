
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import streamlit as st
from PIL import Image
import base64

with open( "app/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.markdown(
    """
        <style>
            [data-testid="stSidebar"] {
                background-image: url("https://brainfood.cl/wp-content/themes/theme_brainfood/assets/svgs/imagotipo-brainfood.svg");
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 20px -20px;
                background-size: 170px 170px; 
            }
        </style>
        """,
    unsafe_allow_html=True,
)  


page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://brainfood.cl/wp-content/uploads/2023/02/header-estrategia.svg");
background-size: cover;
background-position: bottom 300px right -850px;
background-repeat: no-repeat;
}
[data-testid="stSidebar"]{
background-color:rgba(64, 64, 64, 1)

}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <style>
    .spacer {
        margin-top: 150px; 
    }
    </style>
    <div class="spacer"></div>
    ¿Quieres saber más de nosotros? <br><br>
    Visita <a href="https://brainfood.cl" target="_blank">Brain Food</a> para más información.<br>
    También puedes seguirnos en <a href="https://cl.linkedin.com/company/brain-food-spa" target="_blank">Linkedin</a>.
    """,
    unsafe_allow_html=True
)

st.title('👋 ¡Bienvenido al Asistente IA de Brain Food!')

st.markdown('''Esta aplicación basada en Inteligencia Artificial Generativa (GenAI) consiste en un chatbot en el cual puedes realizarle preguntas sobre cualquier cosa que quieras saber sobre el contenido de los discursos presidenciales de los años 2022 y 2023.
    Ten presente que es un prototipo y por ende puede que algunas preguntas no las conteste correctamente. ¡Está en mejora continua!
            ''')

