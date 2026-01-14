import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages
CROSS JOIN food_items
'''

solution = duckdb.sql(answer).df() #Ceci est la solution attendue


#ENtre les deux hastags on a rajouté la barre
# On a rajouté le with afin de le mettre sur le coté et on l'indente avec un tab
with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Join", "GroupBy", "Windows functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected:",option)
#

st.header("Enter yout code") #C'est juste une entete
query = st.text_area(label="Votre code sql ici", key="user_input") # le text au dessus de l'input ainsi que la barre ou on écris

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables","Solution"]) #ceci est les onglets



with tab2:
    st.write("table: beverages") # Nous permet d'avoir une entete au dessus de notre table
    st.dataframe(beverages) #AFfiche la table
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)