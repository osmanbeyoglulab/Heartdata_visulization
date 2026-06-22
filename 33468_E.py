import streamlit as st
import os
import base64
from pathlib import Path

st.markdown("<h2 style='text-align: center; color: black;'>TF spatial</h2>", unsafe_allow_html=True)
st.write("")

sample = "33468_E"
session_id_tf = f"{sample}_tf_names"
session_id_marker = f"{sample}_marker_names"
session_id_ct = f"{sample}_ct_names"

tf_names = sorted(st.session_state[session_id_tf])
marker_names = sorted(st.session_state[session_id_marker])
ct_names = sorted(st.session_state[session_id_ct])

tabs_font_css = """
<style>
div[class*="stSelectbox"] label { color: purple; }
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

c1,_, c2,_ = st.columns([2, 0.2, 0.94, 0.02])


tf_option = c1.selectbox(label='TF', options=tf_names)
marker_option = c2.selectbox(label='mRNA Marker', options=marker_names)

# TF image
tf_img = f"./data/{sample}/spatial_tf/{tf_option}_(TF_activity_and_mRNA_expression).png"
if os.path.exists(tf_img):
    c1.image(tf_img)
else:
    c1.warning(f"Missing: {os.path.basename(tf_img)}")

# Marker image
marker_img = f"./data/{sample}/Marker_expr_figs/{marker_option}_mRNA_expression.png"
if os.path.exists(marker_img):
    c2.image(marker_img)
else:
    c2.warning(f"Missing: {os.path.basename(marker_img)}")

st.write("")

# Cell-type image
ct_option = st.selectbox(label='Cell Type', options=ct_names)
ct_img = f"./data/{sample}/Lee_TF_Marker_Figs/{ct_option}_Lee's_L_between_TF_Marker.png"
if os.path.exists(ct_img):
    img_b64 = base64.b64encode(Path(ct_img).read_bytes()).decode()
    st.markdown(
        f'<div style="display:flex;justify-content:center;">'
        f'<img src="data:image/png;base64,{img_b64}" style="max-width:100%;width:1200px;"></div>',
        unsafe_allow_html=True,
    )
else:
    st.warning(f"Missing: {os.path.basename(ct_img)}")
