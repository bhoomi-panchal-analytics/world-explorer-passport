import streamlit as st

st.set_page_config(
    page_title="World Explorer Passport",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 World Explorer Passport")

st.markdown("""
Welcome to World Explorer Passport!

Explore countries, collect passport stamps,
learn languages and currencies, and test
your geography knowledge.

Use the sidebar to navigate.
""")

st.image(
    "https://images.unsplash.com/photo-1521295121783-8a321d551ad2",
    use_container_width=True
)
