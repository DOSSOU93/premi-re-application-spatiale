import streamlit as st
from processing import SpatialProcessor
import geemap.foliumap as geemap

st.set_page_config(layout="wide")
st.title("Mon Premier Portrail GEE")

# 1️⃣ Initialisation EE
engine = SpatialProcessor()  # initialise EE

# 2️⃣ Formulaire de saisie
with st.sidebar:
    st.header("Coordonnées")
    lat = st.number_input("Latitude", value=48.85, format="%.4f")
    lon = st.number_input("Longitude", value=2.35, format="%.4f")
    submit = st.button("Afficher la zone")

# 3️⃣ Crée la carte sans réinitialiser EE
m = geemap.Map(center=[lat, lon], zoom=12, add_google_map=False)

# 4️⃣ Ajouter l'image Sentinel-2
if submit:
    with st.spinner("Récupération de l'image..."):
        img = engine.get_satellite_image(lat, lon)
        if img:
            vis_params = {'bands': ['B4','B3','B2'], 'min':0, 'max':3000}
            m.addLayer(img, vis_params, 'Sentinel-2 Image')
            st.success(f"Image chargée pour {lat}, {lon}")
        else:
            st.warning("Aucune image disponible pour ces coordonnées et cette période.")

# 5️⃣ Affichage final
m.to_streamlit(height=600)