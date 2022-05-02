# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:04:02 2022

@author: SRAMESH3
"""

import os
import numpy as np
import time

dir='../'

count=0

angles=np.linspace(0,90,19)
theta_spaces=np.linspace(0,17,18)
#IR2_theta_spaces=

#print(theta_spaces)

'''
a --> IRp1 = [0-17]
b --> IRp2 = [0-17]
c --> -r1 =  [0-16]
d --> -θ1 = [0-90]
e --> -ORp1 = [0-17]
f --> -ORp2 = [0-17]
g --> -r2 =  [0-16]
h --> -θ2 = [0-90]
i --> r = [1-13]
'''

#for d in angles:
#    print(d)
#    theta2=np.linspace(int(d),90,(17-int(d))+1)
#    print(theta2)
    #for h in theta2:
    #    print(d,h)


'''
for a in range(0,16):
    for b in range(a+1,17):
        for c in theta_spaces:
            for n,d in enumerate(angles):    
                for e in range(0,16):
                    for f in range(e+1,17):
                        for g in theta_spaces:
                            for h in range(n,len(angles))
                                for i in range(1,13)
'''

p1_range=[0,3,6,9,12,15]
p2_range=[3,6,9,12,15,18]

counter=1


#parameter=[irp1, r1, t1, opr1, irp2, r2, t2, orp2]


for i in p1_range:
    for j in p2_range:
        if(i>j):
            continue
        if(i==j):
            continue
        for k in p1_range:
            for l in p2_range:
                if(k>l):
                    continue
                if(k==l):
                    continue
                py="python "+dir+"gen_geo_circ.py"
                parameters=" -p "+str(i)+" 0 0 "+str(k)+" "+str(j)+" 0 0 "+str(l)+" "
                radius="-r 5"
                count=count+1
                counter=" -c "+str(count)
                iter_n=" -i "+"Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l)
                cmd=py+parameters+radius+counter+iter_n
                os.system(cmd)
                print("Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l))
        

