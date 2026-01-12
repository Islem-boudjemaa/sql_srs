import streamlit as st
import pandas as pd
import duckdb


# import scipy CE qui est intéressant avec l'éditeur de code c'est qu'il nous affiche en rouge si par exemple le package n'est pas telecharger
# DE plus une autocomplession est proposé en fonction des packages

st.write("""
SQL SRS 
Spaced Repetition System SQL practise
""")

option = st.selectbox(
    "What would you like to review?",
    ("Join", "GroupBy", "Windows functions"),
    index=None,
    placeholder="Select a theme",
)

st.write("You selected:",option)


data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6]}
df = pd.DataFrame(data)


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    #input_text = st.text_area(label="Entrez votre input")
    #st.write(input_text)
    #st.dataframe(df) #Toute la partie enyte tab1 et ce hashtag est juste pour du texte
    sql_query = st.text_area(label="Entrez votre requète")
    result = duckdb.query(sql_query)
    st.write(f"VOus avez entrez la query suivantes :{sql_query}") #LA f_string signifie format string et donc nous permet d'inserer des variables python à l'interieur avec du texte
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab2:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)