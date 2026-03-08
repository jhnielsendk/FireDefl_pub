import streamlit as st
#st.set_page_config(layout="wide")
import glob
import matplotlib.pyplot as plt
import numpy as np
from src.FirePackage import fdflect
#from scipy.interpolate import interp1d

pg = st.navigation([
    st.Page("0_About_the_model.py"), 
    st.Page("1_Uniformly_distributed_fire.py"), 
    st.Page("2_Segments_exposed_to_fire.py")
                    ])

#st.sidebar.selectbox("Group", ["A","B","C"], key="group")
#st.sidebar.slider("Size", 1, 5, key="size")

pg.run()



