import streamlit as st
import glob
import matplotlib.pyplot as plt
import numpy as np
from src.FirePackage import fdflect


datFiles=glob.glob('Data/*.dat')

st.header("Concrete deck exposed to uniformly distributed fire")
st.markdown(''' 
    This page allows you to estimate the deflection for a span fully exposed to fire. You can set the time the fire have lasted and select the datasets (different cross sections) to be used.
    ''')
st.divider()


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
    
# res = fdflect()
# st.write(res['Umax'])
st.divider()
st.write('Maximum deflection as a function of span:')
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k' ]
fig2, ax2 = plt.subplots()
fig2.set_figheight(4)
for no, datfile in enumerate(data):
    pl = {'span': [],
        'maxU': [],
        'L50':[]}
    for s in np.linspace(sp_min,sp_max,sp_step):
        FSinp_p=[(0,s)]

        res1=fdflect(span=s, FS=FSinp_p, Time=ti, datafile=datfile)
        pl['span'].append(s)
        pl['maxU'].append(res1['Umax'])
        pl['L50'].append(-s/50)
        #res=fdflect(span=sp)
        #print('span [m]:'+str(sp), 'Umax: '+str(round(res['Umax'],2)), 'L/50 = '+str(sp/50))

    color = colors[no]
    #st.write(color)
    plt.plot(pl['span'],pl['maxU'], color=color, lw=1.0, linestyle='solid', label=datfile)
    #st.write("plot")


plt.plot(pl['span'],pl['L50'], color='blue', lw=1.0, linestyle='dotted', label='span/50')

plt.xlabel('Span [m]')
plt.ylabel('max. Deflection [m]')
plt.legend()
plt.grid()
st.pyplot(fig2)


st.divider()

st.write('Cross sections for selected data:')

for dfile in data:
     img = dfile.replace('.dat','.png')
     st.image(img, caption=['Concrete deck cross-section for: '+dfile])

st.divider()