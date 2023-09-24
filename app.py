"""
    Esteban Sierra Baccio
    24 Sep 2023
"""

#http://localhost:8501/?id_usuario=10&num_nivel=10&num_bloques=10&num_iteraciones=10&num_balas=10


# Run the code: streamlit run pruebahack.py

import streamlit as st
import pandas as pd
import sqlite3

def mostrarTabla():
    conn = sqlite3.connect("prueba.db")
    df = pd.read_sql_query('SELECT * FROM leaderboard',conn)
    st.write(df)
    conn.close()

def insertarValores(id_usuario=0,num_nivel=0,num_bloques=0,num_iteraciones=0,num_balas=0):
    conn = sqlite3.connect("prueba.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO leaderboard (id_usuario,num_nivel,num_bloques,num_iteraciones) VALUES (?,?,?,?);",(user,nivel,bloques,itera))
    cur.close()
    conn.commit()
    conn.close()

st.title("Datos de Hack2023")

variable = st.experimental_get_query_params()
mostrarTabla()

if variable:
    print("Un nuevo registro!")
    user = variable["id_usuario"] 
    user = user[0]#Foreign key
    nivel = variable["num_nivel"]
    nivel = nivel[0]
    bloques = variable["num_bloques"]
    bloques = bloques[0]
    itera = variable["num_iteraciones"]
    itera = itera[0]
    balas = variable["num_balas"]
    balas = balas[0]
    insertarValores(user,nivel,bloques,itera,balas)
else:
    print("una nueva vista")




mostrarTabla()


st.write("HELLO WORLD")
