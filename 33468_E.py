import streamlit as st

st.markdown("<h2 style='text-align: center; color: black;'>TF spatial</h1>", unsafe_allow_html=True)  
st.write("")


sample = "33468_E"
session_id = f"{sample}_tf_names"
print(type(session_id), session_id)

tf_names = st.session_state[session_id]
tf_names = sorted(tf_names)
# st.info("Visualize the spatial distribution of 14 transcriptional metaprograms within glioblastoma tissue samples. These metaprograms capture key malignant subtypes—such as mesenchymal, neural progenitor-like, and proliferative states—as well as important non-malignant populations, including immune, vascular, and glial cells. Use the interactive map to select and explore metaprograms, viewing their spatial localization alongside histology images.")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

option = st.selectbox(
    label='tf',
    options=tf_names,
    ) 

imgfile = f"./data/{sample}/spatial_tf/{option}_(TF_activity_and_mRNA_expression).png"
# st.image(imgfile)
import base64
from pathlib import Path
img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 800px;">
    </div>
""", unsafe_allow_html=True)

