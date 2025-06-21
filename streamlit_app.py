import streamlit as st
import pandas as pd
import math
from pathlib import Path


# Set up a minimal layout with no sidebar
st.set_page_config(
    page_title="Blog.Viz",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Optional: Hide default Streamlit UI elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Optional: Page title (you can remove this too)
st.title("📘 Blog.Viz")

# --- You can add blog sections or content here ---
# st.markdown("Welcome to my minimal blog site.")

# --- Or leave it totally blank ---
