"""
    Esteban Sierra Baccio
    24 Sep 2023
"""

#http://localhost:8501/?id_usuario=10&num_nivel=10&num_bloques=10&num_iteraciones=10&num_balas=10

# Run the code: streamlit run app.py

# Libraries
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import streamlit as st

#Functions
def mostrarTabla():
    conn = sqlite3.connect("prueba.db")
    df = pd.read_sql_query('SELECT * FROM leaderboard',conn)
    st.write(df)
    conn.close()

def borrarValores():
    conn = sqlite3.connect("prueba.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM leaderboard WHERE num_nivel > 0;")
    cur.close()
    conn.commit()
    conn.close()

# borrarValores()

def insertarValores(id_usuario=0,num_nivel=0,num_bloques=0,num_iteraciones=0,num_balas=0):
    conn = sqlite3.connect("prueba.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO leaderboard (id_usuario,num_nivel,num_bloques,num_iteraciones,num_balas) VALUES (?,?,?,?,?);",(id_usuario,num_nivel,num_bloques,num_iteraciones,num_balas))
    cur.close()
    conn.commit()
    conn.close()

def obtenerTabla(nivel):
    conn = sqlite3.connect("prueba.db")
    df = pd.read_sql_query('SELECT * FROM leaderboard WHERE num_nivel = ' + str(nivel),conn)
    return df
    conn.close()

# Configuración general de la página
st.set_page_config(
        page_title="Dino Blocks",
        page_icon="./resources/dinoIcon.png",
        layout="wide",
    )

# Lector de parámetros (en caso de no encontrar los normaliza)
variable = st.experimental_get_query_params()

if variable:
    try: user = variable["id_usuario"][0]
    except: user = 0
    try: nivel = variable["num_nivel"][0]
    except: nivel = 1
    try: bloques = variable["num_bloques"][0]
    except: bloques = 0
    try: itera = variable["num_iteraciones"][0]
    except: itera = 0
    try: balas = variable["num_balas"][0]
    except: balas = 0

else:
    user = 0
    nivel = 0
    bloques = 0
    balas = 0
    itera = 0

user = int(user)
nivel = int(nivel)
bloques = int(bloques)
itera = int(itera)
balas = int(balas)
#insertarValores(user,nivel,bloques,itera,balas)

# Llenar tabla con valores para demo
# for i in range (50):
#     user = np.random.randint(0,201)
#     nivel = np.random.randint(1,4)
#     bloques = np.random.randint(1,201)
#     itera = np.random.randint(1,501)
#     balas =  np.random.randint(1,1001)
#     insertarValores(user,nivel,bloques,itera,balas)


if nivel < 1:
     # Agregar HTML y CSS personalizado para posicionar la imagen en la esquina superior derecha
    st.markdown(
        """
        <style>
        /* Estilo para el contenedor principal */
        .image-container {
            position: relative;
        }

        /* Estilo para la imagen */
        .image-container img {
            position: absolute;
            right: 10px; /* Ajusta el valor para cambiar la posición horizontal */
            max-width: 500px; /* Ajusta el valor para cambiar el tamaño máximo */
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Mostrar la imagen dentro del contenedor personalizado
    with st.container():
        st.markdown('<div class="image-container"><img src="https://danaesg.github.io/HACK2023/resources/dinoIcon.png"></div>', unsafe_allow_html=True)

    st.title("Dino Blocks")
    import streamlit as st

    # Agregar CSS personalizado para estilizar el botón
    st.markdown(
        """
        <style>
        /* Estilo para el botón de enlace */
        .custom-link-button {
            background-color: #A56CC1;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            font-size: 30px;
            margin: 10px;
        }

        /* Estilo para el botón de enlace al pasar el mouse sobre él */
        .custom-link-button:hover {
            background-color: #0056b3;
        }

        .custom-link-button:active,
        .custom-link-button:visited {
        color: white;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Enlace de botón personalizado
    st.markdown('<a href="http://localhost:8501/?num_nivel=1" class="custom-link-button">Begin</a>', unsafe_allow_html=True)

else:
    # Agregar HTML y CSS personalizado para posicionar la imagen en la esquina superior derecha
    st.markdown(
        """
        <style>
        /* Estilo para el contenedor principal */
        .image-container {
            position: relative;
        }

        /* Estilo para la imagen */
        .image-container img {
            position: absolute;
            right: 10px; /* Ajusta el valor para cambiar la posición horizontal */
            max-width: 200px; /* Ajusta el valor para cambiar el tamaño máximo */
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Mostrar la imagen dentro del contenedor personalizado
    with st.container():
        st.markdown('<div class="image-container"><img src="https://danaesg.github.io/HACK2023/resources/dinoIcon.png"></div>', unsafe_allow_html=True)

    st.title("Dino Blocks")

    # body
    st.header("Datos del nivel " + str(nivel))

    #Columnas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h3>Proyectiles</h3>", unsafe_allow_html=True)
        # grafica
        x1 = obtenerTabla(int(nivel))['num_balas']
        
        hist_data = [x1]
    
        group_labels = ['Proyectiles']
        colors = ['#A56CC1']
            
        # Create distplot with curve_type set to 'normal'
        fig = px.histogram(hist_data,  x=x1, color_discrete_sequence=colors)

    # Obtén el valor máximo de la frecuencia en el histograma
        max_frecuencia = x1.value_counts().max()

        # Obtén el valor del último registro
        ultimo_registro = x1.iloc[-1]

        # Agrega una línea vertical en la posición del último registro
        fig.add_shape(
            type='line',
            x0=ultimo_registro,
            x1=ultimo_registro,
            y0=0,
            y1=max_frecuencia,  
            line=dict(color='red', width=2)  # Puedes personalizar el color y el grosor de la línea.
        )

        st.plotly_chart(fig, use_container_width=True)

        if(int(nivel)-1 >= 1):
            st.link_button("Previous Level", "./?num_nivel=" + str(int(nivel)-1))

    with col2:
        st.markdown("<h3>Ciclos</h3>", unsafe_allow_html=True)
        # grafica
        x2 = obtenerTabla(int(nivel))['num_iteraciones']
        hist_data2 = [x2]
        group_labels2 = ['Ciclos']
        colors2 = ['#A6ACEC']
        # Create distplot with curve_type set to 'normal'
        fig2 = px.histogram(hist_data2,  x=x2, color_discrete_sequence=colors2)

    # Obtén el valor máximo de la frecuencia en el histograma
        max_frecuencia = x2.value_counts().max()

        # Obtén el valor del último registro
        ultimo_registro = x2.iloc[-1]

        # Agrega una línea vertical en la posición del último registro
        fig2.add_shape(
            type='line',
            x0=ultimo_registro,
            x1=ultimo_registro,
            y0=0,
            y1=max_frecuencia,  
            line=dict(color='red', width=2)  # Puedes personalizar el color y el grosor de la línea.
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.link_button("Launch Game", "https://danaesg.github.io/HACK2023/Dinosaurio/index.html")
        
    with col3:
        st.markdown("<h3>Bloques</h3>", unsafe_allow_html=True)
        # grafica
        x3 = obtenerTabla(int(nivel))['num_bloques']
        hist_data3 = [x3]
        group_labels3 = ['Bloques']
        colors3 = ['#63F5EF']

        # Create distplot with curve_type set to 'normal'
        fig3 = px.histogram(hist_data3, x=x3, color_discrete_sequence=colors3)

        # Obtén el valor máximo de la frecuencia en el histograma
        max_frecuencia = x3.value_counts().max()

        # Obtén el valor del último registro
        ultimo_registro = x3.iloc[-1]

        # Agrega una línea vertical en la posición del último registro
        fig3.add_shape(
            type='line',
            x0=ultimo_registro,
            x1=ultimo_registro,
            y0=0,
            y1=max_frecuencia,  
            line=dict(color='red', width=2)  # Puedes personalizar el color y el grosor de la línea.
        )

        st.plotly_chart(fig3, use_container_width=True)

        if(int(nivel)+1 <= 3):
            st.link_button("Next Level", "./?num_nivel=" + str(int(nivel)+1))

    st.markdown("<h4>En este primer reto aprenderás del uso de bloques para modificar las propiedades de tu nave. Debes de ayudar a Rexington a destruir todos los meteoritos que se dirigen a su planeta. Utiliza el botón “Mostrar Code” para ver las herramientas que tienes a tu disposición, podrás usar Bloques Condicionales, Temporizadores, y modificadores de propiedades para controlar el comportamiento de tu nave.</h4>", unsafe_allow_html=True)
