import streamlit as st
from style import page_style, footer
import pandas as pd
from style import define_layout
import os
# st.cache_data.clear()
# st.cache_resource.clear()

st.set_page_config(layout="wide") 

# --- PAGE SETUP ----

st.set_page_config(
        page_title='Data Visulization',
        initial_sidebar_state="expanded",
        # layout="wide" 
)

# max_width_str = f"max-width: {80}%;"

# st.markdown(f"""
#         <style>
#         .appview-container .main .block-container{{{max_width_str}}}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

define_layout(max_width='80%', padding_top='2rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem')

# Get the directory where the script is located

def get_tf_names(directory):
    tf_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") and "_(" in filename:
            tf_names.append(filename.split("_(")[0])
    return tf_names

def get_celltype_names(directory):
    ct_names = []
    for fname in os.listdir(directory):
        if fname.endswith("_Lee's_L_between_TF_Marker.png"):
            xxx = fname.replace("_Lee's_L_between_TF_Marker.png", "")
            ct_names.append(xxx)
    return ct_names    

sample = "33468_E"
session_id_tf = f"{sample}_tf_names"
session_id_ct = f"{sample}_ct_names"

if session_id_tf not in st.session_state:
    data_path = f"./data/{sample}/spatial_tf"
    st.session_state[session_id_tf] = get_tf_names(data_path)
if session_id_ct not in st.session_state:
    data_path = f"./data/{sample}/Lee_TF_Marker_Figs"
    st.session_state[session_id_ct] = get_celltype_names(data_path)

    
# ---- start main ---

emoji = "🔹" #"🔸" #"💠" #"🔹" # # #
sample1_page = st.Page(
    page = "33468_E.py",
    title = "33468_E",
    icon = emoji,   #":material/chevron_right:"  ,
    default= True,
)

sample2_page = st.Page(
    page = "3172_3A.py",
    title = "3172_3A",
    icon = emoji
)


# -- NAVIGATION --



pg = st.navigation(
    {
       "": [sample1_page, sample2_page],
    }
)

pg.run()
