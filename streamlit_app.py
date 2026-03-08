#import matplotlib.pyplot as plt
# import glob
#import pandas as pd

# from numpy.random import default_rng as rng
#import numpy as np
# from scipy.interpolate import interp1d

#import FirePackage as fp

import streamlit as st

############


st.header("Concrete deck deflection due to fire")

#datFiles=glob.glob('Data/*.dat')

# st.divider()
# st.write('Maximum deflection as a function of span. Fire assumed under full span')

# col1, col2, col3 = st.columns(3)
# with col1:
#      sp_min = st.number_input("Min. Span [m]:", min_value=0.0, value=0.01, step=0.5, format="%.2f")
# with col2:
#      sp_max = st.number_input("Max. Span [m]:", min_value=0.0, value=16.0, step=0.5, format="%.2f")
# with col3:
#      sp_step = st.number_input("no. steps [-]:", min_value=2, value=20, step=1, format="%i")

# col1, col2 = st.columns([1, 2])
# with col1:
#      ti = st.number_input("Time frame [s]:", min_value=0, max_value=7200, value=3600, step=100)
# with col2:
#     data = st.multiselect(
#         "Select (multiple) datasets for plot below",
#         datFiles,
#         default=datFiles
#         )



# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k' ]
# fig2, ax2 = plt.subplots()
# fig2.set_figheight(4)
# for no, datfile in enumerate(data):
#     pl = {'span': [],
#         'maxU': [],
#         'L50':[]}
#     for s in np.linspace(sp_min,sp_max,sp_step):
#         FSinp_p=[(0,s)]

#         res1=fdflect(span=s, FS=FSinp_p, Time=ti, datafile=datfile)
#         pl['span'].append(s)
#         pl['maxU'].append(res1['Umax'])
#         pl['L50'].append(-s/50)
#         #res=fdflect(span=sp)
#         #print('span [m]:'+str(sp), 'Umax: '+str(round(res['Umax'],2)), 'L/50 = '+str(sp/50))

#     color = colors[no]
#     #st.write(color)
#     plt.plot(pl['span'],pl['maxU'], color=color, lw=1.0, linestyle='solid', label=datfile)
#     #st.write("plot")


# plt.plot(pl['span'],pl['L50'], color='blue', lw=1.0, linestyle='dotted', label='span/50')

# plt.xlabel('Span [m]')
# plt.ylabel('max. Deflection [m]')
# plt.legend()
# plt.grid()
# st.pyplot(fig2)



# #####################################


# st.divider()

# col1, col2, col3 = st.columns(3)
# with col1:
#      dfile = st.selectbox('select datafile', tuple(datFiles), index=3)
# with col2:
#      sp = st.number_input("Span length [m]:", min_value=0.0, value=8.0, step=0.5, format="%.2f")
# with col3:
#      ti2 = st.number_input("Time frame [s]:", min_value=0, max_value=7200, value=ti, step=100, key='TimeSegments')

# fs1 = st.text_input("fire sections [m]:", value='(0,'+str(sp)+')', help='Use the format: (x1,x2); (x3,x4); ... to specify fire exposed segments between x1 and x2 and between x3 and x4, and no fire on the remaining segments')


# fs = fs1.split(';')

# FSinp=[]
# for i in fs:
#     FSinp.append(eval(i))

# #print(FSinp)

# res2=fdflect(span=sp, FS=FSinp, Time=ti2, datafile=dfile)
# #st.write("Maximum deflection", round(1000*res['Umax'],0), 'mm')

# st.metric(label = 'Max. Deflection', value=str(round(1000*res2['Umax'],0))+ 'mm')

# fig, ax = plt.subplots()
# fig.set_figheight(2)
# plt.plot([0, sp],[0, 0], color = 'blue', lw=1.0)

# for i in FSinp:
#         x = [i[0], i[1]]
#         y = [0, 0]
#         plt.plot(x,y, color='red', lw=2.0)


# plt.plot(res2['xc'],res2['yc'], color='blue', lw=1.0, linestyle='solid')
# plt.xlabel('position [m]')
# plt.ylabel('Deflection [m]')
# plt.grid()
# st.pyplot(fig)

# pl2 = {'Time': [],
#     'Umax': [],
#     }
# for ti3 in np.linspace(0,7200,20):
#     res3=fdflect(span=sp, FS=FSinp, Time=ti3, datafile=dfile)
#     pl2['Time'].append(ti3)
#     pl2['Umax'].append(res3['Umax'])

# fig3, ax3 = plt.subplots()
# fig3.set_figheight(2)

# plt.plot(pl2['Time'],pl2['Umax'], color='blue', lw=1.0, linestyle='solid')
# plt.xlabel('Time [m]')
# plt.ylabel('max. Deflection [m]')
# plt.grid()
# st.pyplot(fig3)


# st.divider()