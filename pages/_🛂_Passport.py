import streamlit as st
from utils.data_loader import load_countries

df = load_countries()

st.title("🛂 Digital Passport")

if "visited" not in st.session_state:
    st.session_state.visited = []

country = st.selectbox(
    "Select country to visit",
    df["country"]
)

if st.button("✈️ Visit Country"):

    if country not in st.session_state.visited:
        st.session_state.visited.append(country)

        st.success(
            f"Passport stamp collected for {country}"
        )

st.subheader("Collected Stamps")

for item in st.session_state.visited:
    st.markdown(f"🛂 {item}")

st.metric(
    "Countries Visited",
    len(st.session_state.visited)
)
