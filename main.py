import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

df = pd.read_csv("largest_companies_by_number_of_employees.csv")

df = df.drop(["Symbol","price (USD)"], axis=1)
df.drop(df[df['employees_count'] == 0].index, inplace=True)

count_by_country = pd.DataFrame(df.groupby('country')['employees_count'].sum().sort_values(ascending = False).reset_index())
top_10_countries = count_by_country[:10]

st.title("Etude sur les plus grosses entreprises au monde en fonction de leur nombre d'employés")

fig = px.bar(top_10_countries,top_10_countries['country'],top_10_countries['employees_count'], title="Pays avec les plus grosses entreprises")
fig.update_layout(xaxis_title="Pays", yaxis_title="Nombre d'employés")
st.header("Les 10 pays hébergeant les plus grosses entreprises au monde")
st.plotly_chart(fig)

pays = sorted(df['country'].astype(str).unique())
st.header('Liste des 10 plus grosses entreprises par pays')

pays_choisi = st.selectbox("Sélectionner un pays",pays)

df_par_pays = df[df['country']==pays_choisi]

df_10_par_pays = df_par_pays[:10]

st.table(df_10_par_pays)


