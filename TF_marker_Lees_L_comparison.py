import streamlit as st
import os

st.markdown("<h2 style='text-align: center; color: black;'>TF Marker Lee's L Comparison</h2>", unsafe_allow_html=True)
st.write("")


session_id_tm = "tm_names"

tm_names = sorted(st.session_state[session_id_tm])

tabs_font_css = """
<style>
div[class*="stSelectbox"] label { color: purple; }
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)


tm_option = st.selectbox(label='TF/Marker', options=tm_names)

tm_img = f"./data/TF_marker_Lees_L_comparison_both_samples/{tm_option}.png"
_,c,_ = st.columns([1,4,1])
if os.path.exists(tm_img):
    c.image(tm_img)
else:
    st.warning(f"Missing: {os.path.basename(tm_img)}")
