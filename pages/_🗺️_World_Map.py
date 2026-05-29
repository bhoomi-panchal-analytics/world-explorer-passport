import streamlit as st
import plotly.express as px
from utils.data_loader import load_countries

df = load_countries()

st.title("🗺️ World Map")

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="region",
    hover_name="country"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
