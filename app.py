import ee
import streamlit as st

class SpatialProcessor:
    def __init__(self):
        """Initialise la connexion à Earth Engine via les secrets Streamlit"""
        try:
            # 1️⃣ Récupérer les secrets
            creds_dict = st.secrets["earth_engine"]
            
            # 2️⃣ Conversion \n en vrais retours à la ligne
            credentials = ee.ServiceAccountCredentials(
                creds_dict['client_email'],
                key_data=creds_dict['private_key'].replace('\\n', '\n')
            )
            
            # 3️⃣ Initialisation d'Earth Engine
            ee.Initialize(credentials=credentials)
            
        except Exception as e:
            st.error(f"Erreur d'initialisation Earth Engine : {e}")

    def get_satellite_image(self, lat, lon):
        """Exemple de récupération d'une image Sentinel-2"""
        point = ee.Geometry.Point([lon, lat])
        image = (ee.ImageCollection("COPERNICUS/S2_SR")
                 .filterBounds(point)
                 .sort('SYSTEM:TIME_START', False)
                 .first())
        return image