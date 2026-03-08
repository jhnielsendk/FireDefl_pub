import streamlit as st
import glob

st.header("Concrete deck deflection due to fire")
datFiles=glob.glob('Data/*.dat')

st.divider()
st.write('Maximum deflection as a function of span. Fire assumed under full span')

col1, col2, col3 = st.columns(3)
with col1:
     sp_min = st.number_input("Min. Span [m]:", min_value=0.0, value=0.01, step=0.5, format="%.2f")
with col2:
     sp_max = st.number_input("Max. Span [m]:", min_value=0.0, value=16.0, step=0.5, format="%.2f")
with col3:
     sp_step = st.number_input("no. steps [-]:", min_value=2, value=20, step=1, format="%i")


col1, col2 = st.columns([1, 2])
with col1:
     ti = st.number_input("Time frame [s]:", min_value=0, max_value=7200, value=3600, step=100)
with col2:
    data = st.multiselect(
        "Select (multiple) datasets for plot below",
        datFiles,
        default=datFiles
        )