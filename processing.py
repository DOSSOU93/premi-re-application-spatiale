import streamlit as st
import ee
# Optional, if you need it for displaying images
import matplotlib.image as mpimg

class SpatialProcessor:
    def __init__(self):
        """Initialise la connexion à Earth Engine via les secrets Streamlit"""
        try:
            # Vérifier si on est en local ou sur Streamlit Cloud
            if "earth_engine" in st.secrets:
                # Récupération des infos du fichier .streamlit/secrets.toml
                creds_dict = dict(st.secrets["earth_engine"])
                
                # Authentification par compte de service
                credentials = ee.ServiceAccountCredentials(
                    creds_dict['client_email'], 
                    key_data=creds_dict['private_key']
                )
                ee.Initialize(credentials=credentials)
            else:
                # Fallback pour le développement local classique
                ee.Initialize(project='app-teledetection')
        except Exception as e:
            st.error(f"Erreur d'initialisation Earth Engine : {e}")