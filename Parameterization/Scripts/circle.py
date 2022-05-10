# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:04:02 2022

@author: SRAMESH3
"""

import os
import numpy as np
import time
import random

dir='../'

count=0

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
#for two straight lines 
p1_range=[0,3,6,9,12,15]
p2_range=[3,6,9,12,15,18]
circle_r_range=[0,4,9]
#counter=1

#parameter=[irp1, r1, t1, opr1, irp2, r2, t2, orp2]
s=time.time()
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
                r=random.choice(circle_r_range)  #selecting random outer radii among OR_list
                py="python "+dir+"gen_geo_circ.py"
                parameters=" -p "+str(i)+" 0 0 "+str(k)+" "+str(j)+" 0 0 "+str(l)+" "
                radius="-r "+str(r)
                count=count+1
                counter=" -c "+str(count)
                iter_n=" -i "+"Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l)
                cmd=py+parameters+radius+counter+iter_n
                os.system(cmd)
                #print("Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l))
                print(parameters)
print("Done")
print(time.time()-s)


#for one/two curved lines 
'''
r2=[5,8,12]
irp1_range=[0,3,6,9,12]
p2_range=[6,9,12,15,18]
angle=[15,30,45,60,75,90]
count=0
#parameter=[irp1, r1, t1, opr1, irp2, r2, t2, orp2]
s=time.time()
#for r in circle_r:
for i in irp1_range:
    for j in p2_range:
        if(i>j):
            continue
        if(i==j):
            continue
        for kc,k in enumerate(irp1_range):
            for l in p2_range:
                if(k>l):
                    continue
                if(k==l):
                    continue
                for m in r2:
                    for ac,n in enumerate(angle):
                        if(ac<kc):
                            continue 
                        #print(m)
                        py="python "+dir+"gen_geo_circ.py"
                        parameters=" -p "+str(i)+" 0 0 "+str(k)+" "+str(j)+" "+str(m)+" "+str(n)+" "+str(l)+" "
                        radius="-r "+str(0)
                        count=count+1
                        counter=" -c "+str(count)
                        iter_n=" -i "+"Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l)
                        cmd=py+parameters+radius+counter+iter_n
                        os.system(cmd)
                        #print("Iteration="+str(i)+","+str(j)+","+str(k)+","+str(l))
                        print(parameters,count)
print("Done")
print(time.time()-s)

#match opr1 with index if angle ie as opr1 increases skip smaller angles

'''