#http://localhost:8501/?id_usuario=123&num_nivel=123&num_bloques=0&num_iteraciones=0&


# Run the code: streamlit run pruebahack.py

import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

with col1:   
    def mostrarTabla1():
        conn = sqlite3.connect("prueba.db")
        df = pd.read_sql_query('SELECT * FROM leaderboard WHERE nivel == 1',conn)
        st.write(df)
        conn.close()

with col2:   
    def mostrarTabla2():
        conn = sqlite3.connect("prueba.db")
        df = pd.read_sql_query('SELECT * FROM leaderboard WHERE nivel == 2',conn)
        st.write(df)
        conn.close()

with col3:   
    def mostrarTabla2():
        conn = sqlite3.connect("prueba.db")
        df = pd.read_sql_query('SELECT * FROM leaderboard WHERE nivel == 3',conn)
        st.write(df)
        conn.close()

variable = st.experimental_get_query_params()

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

def insertarValores(id_usuario=0,num_nivel=0,num_balas=0,num_bloques=0,num_iteraciones=0):
    conn = sqlite3.connect("prueba.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO leaderboard (id_usuario,num_nivel,num_bloques,num_iteraciones, num_balas,nivel) VALUES (?,?,?,?,?,?);",(user,nivel,bloques,itera,balas,nivel))
    cur.close()
    conn.commit()
    conn.close()

mostrarTabla()
insertarValores(variable)
mostrarTabla()

st.title("Aplicación de Streamlit con SQLite")


variable = st.experimental_get_query_params()

print(user) #Foreign key
#variable["num_nivel"]
#variable["num_tiempo"]
#variable["num_bloques"]
#variable["num_iteraciones"]

st.write("HELLO WORLD")
