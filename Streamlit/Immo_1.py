import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("D:/Bruno/Programmation/Data/Immobilier/full.csv/full_2023.csv")

data_SG = data.loc[(data['nom_commune'] == "Saint-Guiraud"),['nom_commune','adresse_numero','adresse_nom_voie','surface_terrain','valeur_fonciere','longitude','latitude']]
data_SG_Ll = data_SG[['longitude','latitude']].rename(columns={'longitude': 'lon', 'latitude': 'lat'})

# Agrandissement auto à la taille de l'écran
st.set_page_config(layout="wide")
# Titre de mon tableau de bord
st.title("Logements vendus dans mon village")

st.write(data_SG)
st.map(data_SG_Ll,size=2)