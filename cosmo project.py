import numpy as np
import matplotlib.pyplot as plt
import os
import panda as pd


os.chdir(r'E:\School\Galaxies & Cosmology\Python Project')
s = pd.read_csv('NewList.csv' , sep=',' , header=None)
x,y,q,w,e,r,t,g,u,i,o,p=np.hsplit(s,12)

# the above variables correspond to the following respectively
# name, alt_name_1, ra, dec, morph_type, log_d25, log_ae, phot_mag
# surf_brtness_d25, h_21cm_w20, radial_velocity_gsr, class

H = 70
rr = r.astype(float)
r1 = 10**rr
r2 = (r1*0.0000290888)/2 #arcmin to radian & and whole angle divided by 2
R = np.tan(r2)
R = np.asarray(R)
Re = (R*H)/o
Re1 = Re.astype(float)
Re2 = np.log(Re1)

plt.figure()
plt.plot(u,Re2,'o')
plt.title('log(Effective Radius) vs Average Surface Brightness of Various Elliptical Galaxies')
plt.ylabel('log(Effective Radius)')
plt.xlabel('Average Surface Brightness')
plt.show()