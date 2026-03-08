# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:29:41 2026

@author: JNHR
"""
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


def fdflect(Time=3600, 
            datafile='Data/Ex32.dat',
            #Height = 0.32,
            span = 8,
            Total_points=1200,
            FS=[],
            showPlot = False,
            ):
    
    Height = float(datafile.split('Ex')[1].split('.')[0])/100
    #datafile.split('Ex')

    if len(FS) < 1:
        FS=[(0, span)]
        
    data = np.genfromtxt(datafile, names=True)
    
    f_bot = interp1d(data['Time'], data['Bottom'], 'cubic')
    f_top = interp1d(data['Time'], data['Top'], 'cubic')
    
    delta_strain = f_bot(Time)-f_top(Time)
    
    R = Height/delta_strain
       
    sp=np.linspace(0, span, Total_points)
    for i in FS:
        sp=np.append(sp,i)   
    sp=np.sort(np.unique(sp)) # 
    
    Kt = 0 # tangent slope
    s0 = 0
    dvec = [[0],[0]]
    vec = [[0],[0]]
    dtheta=0
    flag1 = True
    xcoord = [0]
    ycoord = [0]
    for s1 in sp[1:]:
        ds =s1-s0
        #if 0 <= s1 <= 2 or 5 <= s1 <= 8: # Fire exposed, circular area
        if any(start <= s1 <= end for start, end in FS):
            dtheta = ds/R
            T = [[np.cos(dtheta), -np.sin(dtheta)],[np.sin(dtheta), np.cos(dtheta)]]
            if flag1:
                dvec = np.array([[R*np.sin(dtheta)],[R*(1-np.cos(dtheta))]])
                flag1=False
            else:
                dvec=np.dot(T,dvec)        
            vec = vec+dvec
            Kt = dvec[1][0]/dvec[0][0]
        else: # non-fire, linear area
            dvec = [[ds],[Kt*ds]]
            vec = np.add(vec,dvec)
    
        s0=s1
        xcoord.append(float(vec[0][0]))
        ycoord.append(float(vec[1][0]))
        
    xc = np.array(xcoord)*span/xcoord[-1]
    yc = np.array(ycoord)-ycoord[-1]*xc/span
    
    
    if showPlot:
        plt.plot(xc,yc)
        plt.xlabel('position [m]')
        plt.ylabel('Deflection [m]')
        plt.grid()
        lw=2.0
        fig = plt.plot([0, span],[0, 0], color = 'blue', lw=lw)
        
        for i in FS:
            x = [i[0], i[1]]
            y = [0, 0]
            plt.plot(x,y, color='red', lw=2*lw)
        
        delta = np.min(yc)
        plt.text(span/2, delta/5, 'max_deflection = '+str(round(1000*delta,2))+' mm', horizontalalignment='center')
        plt.text(span/2, delta/5+0.3*delta/5, 'Time frame = '+str(round(Time,0))+' sec', horizontalalignment='center')
                
        plt.plot(abq1[:,0], abq1[:,1])
        
        plt.show()
        
    out = {}
    out['xc']=xc
    out['yc']=yc
    out['Umax']=np.min(yc)
    return out

# for sp in np.linspace(0,16,32+1):
#     res=fdflect(span=sp, FS=[(0,0.5*sp)])
#     #res=fdflect(span=sp)
#     print('span [m]:'+str(sp), 'Umax: '+str(round(res['Umax'],2)), 'L/50 = '+str(sp/50))



