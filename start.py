import streamlit as st
from style import page_style, footer
import pandas as pd
from style import define_layout
import os
# st.cache_data.clear()
# st.cache_resource.clear()


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

def get_marker_names(directory):
    marker_names = []
    for fname in os.listdir(directory):
        if fname.endswith("_mRNA_expression.png"):
            xxx = fname.replace("_mRNA_expression.png", "")
            marker_names.append(xxx)
    return marker_names    
        
def get_celltype_names(directory):
    ct_names = []
    for fname in os.listdir(directory):
        if fname.endswith("_Lee's_L_between_TF_Marker.png"):
            xxx = fname.replace("_Lee's_L_between_TF_Marker.png", "")
            ct_names.append(xxx)
    return ct_names    

def get_tfmarker_names(directory):
    tm_names = []
    for fname in os.listdir(directory):
        if fname.endswith("_mRNA_expression.png"):
            xxx = fname.replace("_mRNA_expression.png", "")
            tm_names.append(xxx)
    return tm_names 
        
for sample in ["33468_E", "3172-3A"]:
        session_id_tf = f"{sample}_tf_names"
        session_id_marker = f"{sample}_marker_names"
        session_id_ct = f"{sample}_ct_names"
        
        
        if session_id_tf not in st.session_state:
            data_path = f"./data/{sample}/spatial_tf"
            st.session_state[session_id_tf] = get_tf_names(data_path)
                
        if session_id_marker not in st.session_state:
            data_path = f"./data/{sample}/Marker_expr_figs"
            st.session_state[session_id_marker] = get_marker_names(data_path)    
                
        if session_id_ct not in st.session_state:
            data_path = f"./data/{sample}/Lee_TF_Marker_Figs"
            st.session_state[session_id_ct] = get_celltype_names(data_path)

session_id_tm = "tm_names"
if session_id_tm not in st.session_state:
    data_path = f"./data/TF_marker_Lees_L_comparison_both_samples"
    st.session_state[session_id_tm] = get_tfmarker_names(data_path)   
        
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
TF_marker_compare_page = st.Page(
    page = "TF_marker_Lees_L_comparison.py",
    title = "TF_marker_Lees_L_comparison",
    icon = emoji
)    


# -- NAVIGATION --



pg = st.navigation(
    {
       "": [sample1_page, sample2_page, TF_marker_Lees_L_comparison_page],
    }
)

pg.run()
