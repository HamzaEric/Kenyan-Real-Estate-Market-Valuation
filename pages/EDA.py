import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Exploratory Data Analysis")
st.markdown("---")

col1,col2=st.columns(2)
with col1:
    st.image("images/real estate.jpg")
with col2:
    st.write("Explore Nairobi real estate data through interactive visualizations to uncover market trends, pricing patterns, and key property insights.")
    st.image("images/Nairobi, Kenya.jpg",width=450)
st.markdown("---")
st.subheader("Jupyter Notebook")
html_file = Path(r"html_files/Nairobi_Houses_EDA.html")
components.html(html_file.read_text(), height=1000, scrolling=True)
st.markdown("---")