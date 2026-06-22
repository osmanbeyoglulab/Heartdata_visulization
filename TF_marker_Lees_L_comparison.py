import streamlit as st
import os

st.markdown("<h2 style='text-align: center; color: black;'>TF Marker Lee's L Comparison</h2>", unsafe_allow_html=True)
st.write("")

# 1. Key must match what start.py stores (no sample prefix)
session_id_tm = "tm_names"

# 2. Guard against missing session state key
if session_id_tm not in st.session_state:
    data_path = "./data/TF_marker_Lees_L_comparison_both_samples"
    from pathlib import Path
    st.session_state[session_id_tm] = [
        f.replace("_mRNA_expression.png", "")
        for f in os.listdir(data_path)
        if f.endswith("_mRNA_expression.png")
    ]

tm_names = sorted(st.session_state[session_id_tm])

tabs_font_css = """
<style>
div[class*="stSelectbox"] label { color: purple; }
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

# 3. Use tm_option/tm_names consistently (was mixing tf_names/tf_img)
tm_option = st.selectbox(label='TF/Marker', options=tm_names)

tm_img = f"./data/TF_marker_Lees_L_comparison_both_samples/{tm_option}.png"
if os.path.exists(tm_img):
    st.image(tm_img)
else:
    st.warning(f"Missing: {os.path.basename(tm_img)}")
