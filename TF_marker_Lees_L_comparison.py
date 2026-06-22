import streamlit as st
import os
import base64
from pathlib import Path

st.markdown("<h2 style='text-align: center; color: black;'>TF spatial</h2>", unsafe_allow_html=True)
st.write("")

sample = "3172-3A"
session_id_tm = f"{sample}_tm_names"


tm_names = sorted(st.session_state[session_id_tm])


tabs_font_css = """
<style>
div[class*="stSelectbox"] label { color: purple; }
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)



tm_option = st.selectbox(label='TF/Marker', options=tf_names)


# TF_marker lees L comparison image
tm_img = f"./data/TF_marker_Lees_L_comparison_both_samples/{tm_option}.png"
if os.path.exists(tm_img):
    st.image(tf_img)
else:
    st.warning(f"Missing: {os.path.basename(tf_img)}")

