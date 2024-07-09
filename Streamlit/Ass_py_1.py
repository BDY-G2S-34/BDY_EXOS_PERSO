import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

#from streamlit_dynamic_filters import DynamicFilters

# Import des fichiers CSV
carac = pd.read_csv("../bdd/caracteristiques.csv", sep = ';')
lieux= pd.read_csv("../bdd/lieux.csv", sep = ";")
usagers = pd.read_csv("../bdd/usagers.csv", sep = ';')
vehic = pd.read_csv("../bdd/vehicules.csv", sep = ';')

# Agrandissement auto à la taille de l'écran
st.set_page_config(layout="wide")
# Titre de mon tableau de bord
st.title("Étude et analyse des accidents corporels de la circulation routière")

# Définition d'onglets
tab1, tab2 = st.tabs(["Graphiques", "Carte interractive"])
with tab1:
    st.header("Analyse graphique des accidents référencés")
    col1, col2 = st.columns(2)
    with col1:
        # Le nombre d'accidents par jour.
        acc1 = carac[['Accident_Id','jour','mois','an']]
        acc1['Date'] = acc1['an'].astype(str) + '/' + acc1['mois'].astype(str) + '/' + acc1['jour'].astype(str)
        acc1['Date'] = pd.to_datetime(acc1['Date'])
        acc1_g1 = acc1[['Date', 'Accident_Id']].groupby(by='Date').count().reset_index()
        st.write("Nombre d'accidents par jour")
        # st.dataframe(acc1_g1)
        st.line_chart(acc1_g1,x='Date', y='Accident_Id')
 
        # La répartition des obstacles mobiles heurtés (véhicule, piéton, animal, etc).
        carac_obs = vehic[['Num_Acc','obs']]
        carac_obs = carac_obs.drop(carac_obs[carac_obs['obs'] == -1].index)
        carac_obs_g1 = carac_obs.groupby(by=['obs']).count()
        st.write("Répartition des obstacles mobiles heurtés (véhicule, piéton, animal, etc)")
        # st.dataframe(carac_obs_g1)
        st.bar_chart(carac_obs_g1)

    with col2:
        # Le nombre d'usagers par gravité d'accident.
        usagers1 = usagers[['id_usager','grav']]
        usagers_g1 = usagers1.groupby(by='grav').count()
        st.write("Nombre d'usagers par gravité d'accident")
        # st.dataframe(usagers_g1)
        st.bar_chart(usagers_g1)

        # La répartition des usagers par sexe.
        usagers2 = usagers[['id_usager','sexe']]
        usagers_g2 = usagers2.groupby(by='sexe').count()
        st.write("Répartition des usagers par sexe")
        # st.dataframe(usagers_g2)
        st.bar_chart(usagers_g2)

with tab2:
    st.header("Carte de répartition des accidents")
    # Statistiques descriptives
    # Le nombre d'usagers impliqués
    nb_usagers = usagers2['id_usager'].count()
    st.metric("Nombre d'usagers impliqués",nb_usagers)

    # Map interractive
    # Le positonnement des accident sur la carte.
    acc2 = carac[['dep','atm','lat','long']].rename(columns={'long': 'lon'}).replace(",",".", regex=True).astype({'lon':float,'lat':float})
    acc3 = acc2

    # Tables de correspondance :
    # Table de correspondance Conditions atmosphériques
    liste_val_cond_atm = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    liste_lib_cond_atm = ["Non renseigné", "Normale", "Pluie légère", "Pluie forte", "Neige - grêle",
        "Brouillard - fumée", "Vent fort - tempête", "Temps éblouissant", "Temps couvert", "Autre"]
    dic_cond_atm = dict(zip(liste_lib_cond_atm, liste_val_cond_atm))

    # Filtres, en sidebar
    num_dep_sel = st.selectbox("Département", ["Tous"] + sorted(acc2['dep'].unique()),index=0) # Filtre par département
    cond_atm_sel = st.selectbox("Conditions atmosphériques",["Toutes"] + liste_lib_cond_atm,index=0) # Filtre par conditions atmosphérique
    st.write(cond_atm_sel)

    # Dataframe filtré
    if num_dep_sel != "Tous":
        acc3 = acc2[(acc2['dep'] == num_dep_sel)]
    if cond_atm_sel != "Toutes":
        acc3 = acc2[(acc2['atm'] == dic_cond_atm.get(cond_atm_sel))]
    # st.dataframe(acc2)
    st.map(acc3[['lat','lon']])



