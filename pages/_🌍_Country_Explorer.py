import streamlit as st
from utils.data_loader import load_countries

df = load_countries()

st.title("🌍 Country Explorer")

country = st.selectbox(
    "Choose a country",
    df["country"]
)

selected = df[df["country"] == country].iloc[0]

st.header(selected["country"])

st.write(f"🏛 Capital: {selected['capital']}")
st.write(f"💵 Currency: {selected['currency_name']}")
st.write(f"🗣 Languages: {selected['languages']}")
st.write(f"🌎 Region: {selected['region']}")
st.write(f"👥 Population: {selected['population']:,}")

st.success(selected["fun_facts"])
