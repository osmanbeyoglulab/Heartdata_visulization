import streamlit as st

st.markdown("<h2 style='text-align: center; color: black;'>TF spatial</h1>", unsafe_allow_html=True)  
st.write("")


sample = "3172_3A"
session_id_tf = f"{sample}_tf_names"
session_id_ct = f"{sample}_ct_names"
# print(type(session_id_tf), session_id_tf)

tf_names = st.session_state[session_id_tf]
tf_names = sorted(tf_names)

marker_names = st.session_state[session_id_marker]
marker_names = sorted(marker_names)

ct_names = st.session_state[session_id_ct]
ct_names = sorted(ct_names)

# st.info("Visualize the spatial distribution of 14 transcriptional metaprograms within glioblastoma tissue samples. These metaprograms capture key malignant subtypes—such as mesenchymal, neural progenitor-like, and proliferative states—as well as important non-malignant populations, including immune, vascular, and glial cells. Use the interactive map to select and explore metaprograms, viewing their spatial localization alongside histology images.")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

c1,c2 = st.columns([2, 1])

option = c1.selectbox(
    label='TF',
    options=tf_names,
    ) 
option = c2.selectbox(
    label='mRNA Marker',
    options=marker_names,
    ) 

import base64
from pathlib import Path

imgfile = f"./data/{sample}/spatial_tf/{option}_(TF_activity_and_mRNA_expression).png"
c1.image(imgfile)

# img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
# c1.markdown(f"""
#     <div style="display: flex; justify-content: center;">
#         <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 800px;">
#     </div>
# """, unsafe_allow_html=True)

imgfile = f"./data/{sample}/spatial_tf/{option}__mRNA_expression.png"
c2.image(imgfile)

st.write("")
option = st.selectbox(
    label='Cell Type',
    options=ct_names,
    ) 

imgfile = f"./data/{sample}/Lee_TF_Marker_Figs/{option}_Lee's_L_between_TF_Marker.png"


img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1200px;">
    </div>
""", unsafe_allow_html=True)
