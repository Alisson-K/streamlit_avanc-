import streamlit as st
import pandas as pd 
from datetime import date
from datetime import time
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Sécurisation de notre streamlit 

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page")
      st.image("https://euradio-dev.s3.fr-par.scw.cloud/assets/images/news/dou-ca-vient-les-applaudissements-38348.jpg")


if st.session_state["authentication_status"]:
    # Sidebar
    with st.sidebar:
        # Affichage du bouton de déconnexion
        authenticator.logout("Déconnexion")

        # Affichage du message de bienvenue avec le nom de l'utilisateur
        user_name = st.session_state["name"]
        st.write(f"Bienvenue, {user_name}")

        # Menu avec les options Accueil et Mes photos
        choix = option_menu(
            menu_title="Menu",  # Titre du menu
            options=["Accueil", "Mes photos"],  # Options du menu
            icons=["house", "image"],  # Icônes des options
            default_index=0,  # L'index par défaut
            orientation="vertical",  # Disposition verticale
        )
    
    # Affichage de l'accueil selon le choix de l'utilisateur
    if choix == "Accueil":
        accueil()
    
    elif choix == "Mes photos":
        # Mise en page avec 3 colonnes
        col1, col2, col3 = st.columns(3)

        # Image dans la première colonne
        with col1:
            st.header("A cat")
            st.image("https://cdn-s-www.leprogres.fr/images/0FED0854-A549-4207-B5FB-89685C6F271B/NW_raw/parmi-les-quelque-200-especes-que-menacent-le-chat-22-sont-des-oiseaux-photo-adobe-stock-1687166465.jpg")

        # Image dans la deuxième colonne
        with col2:
            st.header("A dog")
            st.image("https://www.vetbotanic.com/wp-content/uploads/2023/12/conseils-poil-chien-scaled.jpg")

        # Image dans la troisième colonne
        with col3:
            st.header("A parrot")
            st.image("https://makocreations.fr/cdn/shop/articles/photo_de_perroquet_ara_bleu_1024x1024.jpg?v=1690285986")
            
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le mot de passe est incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis.')
