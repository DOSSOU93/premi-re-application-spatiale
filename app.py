import streamlit as st
import ee
import folium
from processing import SpatialProcessor

st.set_page_config(layout="wide")
st.title("Mon Premier Portrail GEE")

# Initialisation EE
engine = SpatialProcessor()

# Formulaire
with st.sidebar:
    lat = st.number_input("Latitude", value=48.85)
    lon = st.number_input("Longitude", value=2.35)
    submit = st.button("Afficher la zone")

# Carte Folium
m = folium.Map(location=[lat, lon], zoom_start=12)

if submit:
    img = engine.get_satellite_image(lat, lon)
    if img:
        map_id_dict = ee.Image(img).getMapId({'bands': ['B4','B3','B2'], 'min':0, 'max':3000})
        folium.raster_layers.TileLayer(
            tiles=map_id_dict['tile_fetcher'].url_format,
            attr='Google Earth Engine',
            overlay=True,
            name='Sentinel-2'
        ).add_to(m)
        st.success("Image chargée !")
    else:
        st.warning("Aucune image disponible")

# Affichage carte dans Streamlit
from streamlit_folium import st_folium
st_folium(m, width=700, height=500)