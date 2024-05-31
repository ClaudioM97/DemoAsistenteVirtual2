
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

st.title('👋 Cuenta Pública 2024: ¡Hazle preguntas al discurso!')

st.markdown('''
En casi 3 horas de discurso puede ser un poco complejo estar bien atento a ciertos temas específicos que te pueden interesar. Por eso, desarrollamos esta plataforma apoyada por Inteligencia Artificial para que puedas preguntar lo que quieras. 

Incluso puedes comparar algunos anuncios con los realizados en la Cuenta Pública de 2022 y 2023. Como guía, te dejamos un par de ejemplos:

¿Cuáles fueron los principales anuncios en materia de salud?
¿Puedes enumerar las frases donde se menciona “energías renovables”? 
¿Puedes resumir los anuncios en materia de crecimiento económico y compararlos con la Cuenta Pública del 2022 y 2023?
¿Cuántas veces mencionó la palabra “regiones” en su discurso?

Esta es una plataforma desarrollada por Brain Food, en una iniciativa en conjunto con PARLA.

¡Te invitamos a probarla!

Sobre Brain Food

XXX

Sobre PARLA

PARLA es una agencia integrada de comunicación estratégica, con más de 9 años apoyando a empresas y organizaciones a conectarse con su entorno y comunicar. Liderada por Rodrigo Frey, Francisco Derosas y Sebastián Jordana junto a un equipo multidisciplinario de más de 40 profesionales. Puedes conocer más en www.parla.cl.
            ''')

