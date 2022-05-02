#!/usr/bin/env python
# coding: utf-8

# In[4]:



import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import Point
from shapely.geometry import Polygon, mapping
from shapely.geometry.polygon import Polygon
import sys
import argparse
import csv
import os


#print(os.getcwd())
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', type=int, nargs=8,help='parameters for rubber geometry')
parser.add_argument('-r', type=int, nargs=1,help='parameters for insert geometry')
parser.add_argument('-c', type=int, nargs=1,help='counter for file name')
parser.add_argument('-i',type=str, nargs=1,help='counter for interation number')
args = parser.parse_args()

print(args.p,args.r,args.c,args.i)

Insert_config='circle'
fil_name=Insert_config+str(args.c[0])

N= 17
IR=15
OR=50
r= np.linspace(IR, OR, N)
thetasteps= 72
dt=2*np.pi/thetasteps
theta=  np.linspace(0, 2*np.pi-dt, thetasteps)

z_steps= 21
z=np.linspace(0,60,z_steps)

z_count=1
count=1

nodes=[]            #List to store nodes
metal=[]            #List to store metal nodes
rubber=[]           #List to store rubber nodes

for i in range(z_steps):
    for j in range(N):
        for k in range(thetasteps):
            nodes.append([count,
                                r[j]*np.cos(theta[k]),
                                r[j]*np.sin(theta[k]),
                                z[i]])
            count=count+1
               

e_list=[]
            

for m in range(0,z_steps-1):
    lis=np.arange(1+m*thetasteps*N,(m+1)*thetasteps*N-thetasteps+1,1)
    #print(len(lis),lis)
    for g in range(len(lis)):
        if lis[g]%thetasteps==0:
            #print(lis[g])
            n= int(lis[g]/thetasteps)
            e_list.append([z_count, 
                                lis[g], 
                                (lis[g]+1)%thetasteps +(n-1)*thetasteps, 
                                (lis[g]+thetasteps+1)%thetasteps+n*thetasteps, 
                                lis[g]+thetasteps,
                                lis[g]+ (N*thetasteps), 
                                (lis[g]+1)%thetasteps +(n-1)*thetasteps+ (N*thetasteps),
                                (lis[g]+thetasteps+1)%thetasteps+n*thetasteps+ (N*thetasteps), 
                                lis[g]+thetasteps + (N*thetasteps)])

        else:
            e_list.append([z_count, 
                                lis[g], 
                                (lis[g]+1), 
                                (lis[g]+thetasteps+1), 
                                lis[g]+thetasteps,
                                lis[g]+ (N*thetasteps), 
                                (lis[g]+1)+ (N*thetasteps),
                                (lis[g]+thetasteps+1)+ (N*thetasteps), 
                                lis[g]+thetasteps + (N*thetasteps)])
        z_count=z_count+1

ele=np.zeros(shape=(len(e_list),5,2))

for i in range(len(e_list)):
    ele[i]=[[nodes[e_list[i][1]-1][1],nodes[e_list[i][1]-1][2]],
              [nodes[e_list[i][2]-1][1],nodes[e_list[i][2]-1][2]],
              [nodes[e_list[i][3]-1][1],nodes[e_list[i][3]-1][2]],
              [nodes[e_list[i][4]-1][1],nodes[e_list[i][4]-1][2]],
              [nodes[e_list[i][1]-1][1],nodes[e_list[i][1]-1][2]]]
   
    
plt.rcParams['figure.figsize'] = [40, 40]



def polar1(x, y):
    """returns r, theta(degrees)
    """
    rads = (x ** 2 + y ** 2) ** .5
    theta_1 = math.degrees(math.atan2(y,x))
    theta_1 = (theta_1 + 360) % 360
    return round(rads,1), round(theta_1,2)

for i in range(len(ele)):

    radius,angle=(polar1(ele[i][0][0],ele[i][0][1]))
    if(round(radius,1)==round(r[-2],1)):      
        metal.append(i)
              
            
#plt.show()


# **The type of insert is mentioned # 1= Diamond, 2= Bezier diamond, 3= Ring, 4= square/rectangular insert** 
# 
# - **Diamond** - lx,by (points- (lx/2,0),(-l/2,0),(0,by/2),(0,-b/2)) 
# - **Bezier diamond** - lx,by,r,theta (x,y)  (points- (points- (lx/2,0),(x,y),(0,by/2),(-x,y),(-l/2,0),(-x,-y),(0,-b/2),(x,-y)))
# - **Ring** - r
# - **Rectange** - lx,by (points- points- ((lx/2,by/2),(-lx/2,by/2),(-lx/2,-by/2),(lx/2,-by/2))

# In[8]:


#Ring parameter  
# rad+val range= IR - OR-IR

#%matplotlib
rad_val = args.r[0]

#print(r[rad_val])

#polygon1 = Polygon(metal_polygon)

for i in range(len(ele)):
    
    radius,angle=(polar1(ele[i][0][0],ele[i][0][1]))
   
    if(round(radius,1) <= round(r[rad_val],1)): 
        metal.append(i)
            

#plt.plot([x[0] for x in metal_polygon],[x[1] for x in metal_polygon],color='black')

# **Parameter defenitions**  8 parameters [IRp1,r1,θ1,ORp1,IRp2,r2,θ2,ORp2] 
# 
# 
# - IRp1 = [0-17]
# -IRp2 = [0-17]
# -r1 =  [0-16]
# -θ1 = [0-90]
# -ORp1 = [0-17]
# -ORp2 = [0-17]
# -r2 =  [0-16]
# -θ2 = [0-90]
# 
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, (math.degrees(phi)+360)%360)

def pol2cart(rho, phi):
    x = rho * np.cos(math.radians(phi))
    y = rho * np.sin(math.radians(phi))
    return([x, y])


r1=r[2]
r2=r[14]
theta1=math.degrees(theta[0])
theta2=math.degrees(theta[10])


cordinate_list=[]

xs=[]
ys=[]
count=0

#visualizing just the first quadrant elements 
for i in range((N-1)*thetasteps):
    counter=0
    for j in range(4):
        counter=counter+1
        if(counter==4):
            xs,ys=zip(*ele[i])
            plt.plot(xs,ys,color='gray')
            #x_avg=xs[0]+xs[1]+xs[2]+xs[3]
            #y_avg=ys[0]+ys[1]+ys[2]+ys[3]
            cordinate_list.append(([xs[0],ys[0]]))


parameter=args.p  

#a,b = zip(*cordinate_list)
#plt.scatter(a,b,color='red')


polygon_list=[]


Geo_config=[0,0,0,0]

#if 1 is line
if (parameter[1]==0 and parameter[2]==0):
    Geo_config[0]=1
    polygon_list.append([cordinate_list[parameter[0]]])
    rads,thets=cart2pol(cordinate_list[(N-2)*thetasteps+parameter[3]][0],cordinate_list[(N-2)*thetasteps+parameter[3]][1])
    #print(pol2cart(rads+20,thets))
    polygon_list.append([pol2cart(rads+20,thets)])
    
#if 1 is curve
if (parameter[1]!=0 and parameter[2]!=0):
    Geo_config[1]=1
    polygon_list.append([cordinate_list[parameter[0]]])
    polygon_list.append([cordinate_list[int(thetasteps*(parameter[1]-1)+parameter[2]/(360/thetasteps))]])
    rads,thets=cart2pol(cordinate_list[(N-2)*thetasteps+parameter[3]][0],cordinate_list[(N-2)*thetasteps+parameter[3]][1])
    #print(pol2cart(rads+20,thets))
    polygon_list.append([pol2cart(rads+20,thets)])

#if 2 is line
if(parameter[5]==0 and parameter[6]==0):
    Geo_config[2]=1
    rads,thets=cart2pol(cordinate_list[(N-2)*thetasteps+parameter[7]][0],cordinate_list[(N-2)*thetasteps+parameter[7]][1])
    #print(pol2cart(rads+20,thets))
    polygon_list.append([pol2cart(rads+20,thets)])
    
    polygon_list.append([cordinate_list[parameter[4]]])

#if 2 is curve
if(parameter[5]!=0 and parameter[6]!=0):
    Geo_config[3]=1
    rads,thets=cart2pol(cordinate_list[(N-2)*thetasteps+parameter[7]][0],cordinate_list[(N-2)*thetasteps+parameter[7]][1])
    #print(pol2cart(rads+20,thets))
    polygon_list.append([pol2cart(rads+20,thets)])
    polygon_list.append([cordinate_list[int(thetasteps*(parameter[5]-1)+parameter[6]/(360/thetasteps))]])
    polygon_list.append([cordinate_list[parameter[4]]])

    
polygon_list.append(polygon_list[0])

polygon1=[]
polygon2=[]
polygon3=[]
polygon4=[]

for x in polygon_list:
    polygon1.append((round(x[0][0],2),round(x[0][1],2)))
    polygon2.append((round(-x[0][0],2),round(x[0][1],2)))
    polygon3.append((round(-x[0][0],2),round(-x[0][1],2)))
    polygon4.append((round(x[0][0],2),round(-x[0][1],2)))

plt.plot(*zip(*polygon1),color='k')
plt.plot(*zip(*polygon2),color='k')
plt.plot(*zip(*polygon3),color='k')
plt.plot(*zip(*polygon4),color='k')


polygon1 = Polygon(polygon1)
polygon2 = Polygon(polygon2)
polygon3 = Polygon(polygon3)
polygon4 = Polygon(polygon4)


plt.savefig("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/2D_cross_sec_images/circle_insert/"+fil_name+"_polygon_view.png")


plt.clf()


#____________ append rubber node list on all 4 quadrants ______________________


for i in range(len(ele)):
    p1_counter=p2_counter=p3_counter=p4_counter=0
    for j in range(4):
        if(i in metal):
            pass
        else:
            if(polygon1.contains(Point(ele[i][j][0], ele[i][j][1]))): 
                p1_counter=p1_counter+1
                if(p1_counter==2):
                    rubber.append(i)
            if(polygon2.contains(Point(ele[i][j][0], ele[i][j][1]))): 
                p2_counter=p2_counter+1
                if(p2_counter==2):
                    rubber.append(i)
            if(polygon3.contains(Point(ele[i][j][0], ele[i][j][1]))): 
                p3_counter=p3_counter+1
                if(p3_counter==2):
                    rubber.append(i)
            if(polygon4.contains(Point(ele[i][j][0], ele[i][j][1]))): 
                p4_counter=p4_counter+1
                if(p4_counter==2):
                    rubber.append(i)

            
for i in range(((N-1)*thetasteps)):
    xs,ys=zip(*ele[i])
    plt.fill(xs, ys, "lightskyblue")   
    if(i in rubber):
        xs,ys=zip(*ele[i])
        plt.fill(xs, ys, "darksalmon")
    if(i in metal):
        xs,ys=zip(*ele[i])
        plt.fill(xs, ys, "gray")
    
plt.rcParams['figure.figsize'] = [40, 40]
plt.axis('off')
plt.savefig("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/2D_cross_sec_images/circle_insert/"+fil_name+".svg")
plt.savefig("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/2D_cross_sec_images/circle_insert/"+fil_name+".png")


#__________________________________________ writing .inp file _______________________________________

f = open("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/Abaqus_input_files/C_insert/"+fil_name+".inp", "w")
f.write("**\n*HEADING\n**\n**\n**\n**\n*NODE\n")

for i in range(len(nodes)):
    f.write(str(nodes[i][0])+",\t"+str(nodes[i][1])+",\t"+str(nodes[i][2])+",\t"+str(nodes[i][3])+"\n")
    
f.write("25705,   1.1264095622397384E-16,   1.8471775856967138E-16,       30.000000000000124\n")
f.write("25706,   1.5276059869443072E-15,   3.2126914703875426E-16,        30.00000000000026\n")

f.write("**\n** SOLID ELEMENTS\n**\n")
        
f.write("*ELEMENT, TYPE=C3D8H, ELSET=SOLID_RUBBER\n")
for i in range(len(rubber)):
    f.write(str(e_list[rubber[i]][0])+",\t"+
            str(e_list[rubber[i]][1])+",\t"+
            str(e_list[rubber[i]][4])+",\t"+
            str(e_list[rubber[i]][3])+",\t"+
            str(e_list[rubber[i]][2])+",\t"+
            str(e_list[rubber[i]][5])+",\t"+
            str(e_list[rubber[i]][8])+",\t"+
            str(e_list[rubber[i]][7])+",\t"+
            str(e_list[rubber[i]][6])+"\n")


f.write("*ELEMENT, TYPE=C3D8, ELSET=SOLID_METAL\n")
for i in range(len(metal)):
    f.write(str(e_list[metal[i]][0])+",\t"+
            str(e_list[metal[i]][1])+",\t"+
            str(e_list[metal[i]][4])+",\t"+
            str(e_list[metal[i]][3])+",\t"+
            str(e_list[metal[i]][2])+",\t"+
            str(e_list[metal[i]][5])+",\t"+
            str(e_list[metal[i]][8])+",\t"+
            str(e_list[metal[i]][7])+",\t"+
            str(e_list[metal[i]][6])+"\n")


# The static part of the file which remains constant for all geometeries 
f_1 = open("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/static_text_for_inp_with_MPC.txt", "r")
f.write(f_1.read())
f.close()

# In[14]:
    
file = open("C:/Users/SRAMESH3/Thesis_ML_rubber_design/Parameterization/Meta_data/circle_dat.csv", "a+")
writer = csv.writer(file)


writer.writerow([fil_name,Insert_config,Geo_config,polygon_list,args.i,args.p])

file.close()

print(fil_name+" witten")


