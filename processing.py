import ee
import streamlit as st

class SpatialProcessor:
    def __init__(self):
        """Initialise la connexion à Earth Engine via les secrets Streamlit"""
        try:
            creds_dict = st.secrets["earth_engine"]
            credentials = ee.ServiceAccountCredentials(
                creds_dict['client_email'],
                key_data=creds_dict['private_key'].replace('\\n', '\n')  # <- très important
            )
            ee.Initialize(credentials=credentials)
        except Exception as e:
            st.error(f"Erreur d'initialisation Earth Engine : {e}")

    def get_satellite_image(self, lat, lon):
        """Récupère la dernière image Sentinel-2 pour un point donné"""
        point = ee.Geometry.Point([lon, lat])
        image = (ee.ImageCollection("COPERNICUS/S2_SR")
                 .filterBounds(point)
                 .filterDate('2023-01-01', '2023-12-31')
                 .sort('SYSTEM:TIME_START', False)
                 .first())
        return image