# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:57:30 2018

@author: kbs1
"""

import numpy as np
import matplotlib.pyplot as plt
import os

ca_list=[[20.3, 19.75],[19.7,27.625]] # [Voltage, Distance] CA, OA in inches
cb_list=[[12.6,19.75],[11.8,27.625]]

C0A = np.array(ca_list)
C0B = np.array(cb_list)

C0A[0,1]=C0A[0,1]*2.54 # to cm
C0A[1,1]=C0A[1,1]*2.54 # to cm

C0B[0,1]=C0B[0,1]*2.54 # to cm
C0B[1,1]=C0B[1,1]*2.54 # to cm

Top_to_C0A=2 #cm
Top_to_C0B=6 #cm

C0A[0,1]=C0A[0,1]-Top_to_C0A
C0A[1,1]=C0A[1,1]-Top_to_C0A

C0B[0,1]=C0B[0,1]-Top_to_C0B
C0B[1,1]=C0B[1,1]-Top_to_C0B

dyA=C0A[1,1]-C0A[0,1]
dxA=C0A[1,0]-C0A[0,0]

mA=dyA/dxA
bA=C0A[1,1]-mA*C0A[1,0]

dyB=C0B[1,1]-C0B[0,1]
dxB=C0B[1,0]-C0B[0,0]

mB=dyB/dxB
bB=C0B[1,1]-mB*C0B[1,0]

t=np.arange(0,25,1)

plt.rc('font', weight='bold')
plt.rcParams['axes.linewidth']=2
plt.rcParams['figure.figsize'] = (16,9)

Title='C0 Lens Characterization'

fig = plt.figure()
fig.suptitle(Title, fontsize=36, fontweight='bold')

ax = fig.add_subplot(111)

ax.set_xlabel('Applied Voltage (V)', fontsize=36, fontweight='bold')
ax.set_ylabel('Focal Length (cm)', fontsize=36, fontweight='bold')

ax.tick_params(axis='both', which='major', labelsize=18, width=2, length=6)
ax.tick_params(axis='both', which='minor', labelsize=18, width=2, length=6)
ax.xaxis.get_offset_text().set_visible(False)

fig=plt.plot(mA*t+bA,'b-',label='C0A')
fig=plt.plot(mB*t+bB,'g-',label='C0B')

leg=plt.legend(fontsize=30, loc='best', frameon=False)

save_loc= Title + '.png'
plt.savefig(save_loc)

#plt.show

