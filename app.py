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
import numpy as np
import scipy
import plotly.express as px


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
        page_icon="./resources/dinoIcon.jpg",
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
    nivel = 1
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

# body
st.title("Datos del nivel " + str(nivel))

#Columnas
col1, col2, col3 = st.columns(3)
with col1:
    mostrarTabla()
    st.header("Proyectiles")
    # grafica
    x1 = obtenerTabla(int(nivel))['num_balas']
    
    hist_data = [x1]
   
    group_labels = ['Proyectiles']
    colors = ['#A56CC1']
    	
    x1
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

    # Add title
    fig.update_layout(title_text='Proyectiles')
    st.plotly_chart(fig, use_container_width=True)

    if(int(nivel)-1 > 1):
        st.link_button("Previous Level", "./?num_nivel=" + str(int(nivel)-1))

with col2:
    st.header("Ciclos")
    # grafica
    x2 = obtenerTabla(int(nivel))['num_iteraciones']
    hist_data2 = [x2]
    group_labels2 = ['Ciclos']
    colors2 = ['#A6ACEC']
    x2
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
    # Add title
    fig2.update_layout(title_text='Ciclos')
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    st.header("Bloques")
    # grafica
    x3 = obtenerTabla(int(nivel))['num_bloques']
    hist_data3 = [x3]
    group_labels3 = ['Bloques']
    colors3 = ['#63F5EF']
    x3

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


    # Add title
    fig3.update_layout(title_text='Bloques')
    st.plotly_chart(fig3, use_container_width=True)

    if(int(nivel)+1 <= 3):
        st.link_button("Next Level", "./?num_nivel=" + str(int(nivel)+1))

"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Consequat ac felis donec et. A lacus vestibulum sed arcu non. Morbi tristique senectus et netus et malesuada fames. In eu mi bibendum neque egestas congue. Massa placerat duis ultricies lacus sed. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Lorem ipsum dolor sit amet consectetur. Quisque egestas diam in arcu cursus euismod quis viverra. Ultrices sagittis orci a scelerisque purus semper eget duis at. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Est velit egestas dui id ornare arcu. Sed cras ornare arcu dui vivamus arcu felis bibendum ut. Malesuada pellentesque elit eget gravida cum sociis natoque. Eu augue ut lectus arcu bibendum at. Vivamus arcu felis bibendum ut tristique et egestas quis ipsum. Quam pellentesque nec nam aliquam. Elit at imperdiet dui accumsan sit. Tempus imperdiet nulla malesuada pellentesque elit. Mattis nunc sed blandit libero volutpat sed cras ornare arcu.

Dui sapien eget mi proin sed libero enim sed faucibus. Ultrices neque ornare aenean euismod elementum. Purus sit amet volutpat consequat mauris nunc congue nisi. Pellentesque diam volutpat commodo sed egestas egestas. Aliquet porttitor lacus luctus accumsan tortor posuere. A diam maecenas sed enim ut sem viverra aliquet eget. Quam id leo in vitae. Consequat id porta nibh venenatis cras sed. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Amet porttitor eget dolor morbi non arcu risus. Sed sed risus pretium quam vulputate dignissim suspendisse in est. Sollicitudin nibh sit amet commodo. Non curabitur gravida arcu ac tortor dignissim convallis aenean et.
"""
