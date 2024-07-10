
import matplotlib.pyplot as plt
import numpy as np
import random
import math

#Initial Position Assignment
def create_pos (npart):
  a=np.zeros((npart,3))
  #sigma=1.1 
  k=0
  n=6
  for z in range(n):
    for i in range(n):
      for j in range(n):
        if (k< npart):
          a[k][0]=i*1.1
          a[k][1]=(j)*1.1
          a[k][2]=z*1.1
          k+=1
          if(z<n-1 and j<n-1):
            a[k][0]=i*1.1
            a[k][1]=0.55+j*1.1
            a[k][2]=0.55+z*1.1
            k+=1
          if (i<n-1 and j<n-1):
            a[k][0]=0.55+i*1.1
            a[k][1]=0.55+j*1.1
            a[k][2]=z*1.1
            k+=1
          if ( i<n-1 and z<n-1):
            a[k][0]=0.55+i*1.1
            a[k][1]=j*1.1
            a[k][2]=0.55+z*1.1
            k+=1
        else:
          break
 
  return a

#Initial velocity assignment
def create_vel(a,npart,temp,dt):
  vel= np.random.rand(npart,3) - 0.5
  sumvx=sumvy=sumvz=0
  sumvx2=sumvy2=sumvz2=0

  for i in range (npart):
    sumvx = sumvx + vel[i][0]
    sumvy = sumvy + vel[i][1]
    sumvz = sumvz + vel[i][2]
    sumvx2 = sumvx2 + vel[i][0]**2
    sumvy2 = sumvy2 + vel[i][1]**2
    sumvz2 = sumvz2 + vel[i][2]**2

  sumvx=sumvx/npart
  sumvy=sumvy/npart
  sumvz=sumvz/npart
  sumvx2=sumvx2/npart
  sumvy2=sumvy2/npart
  sumvz2=sumvz2/npart
 
  #Scale factors for velocities
  fsx=math.sqrt(3*temp/sumvx2)
  fsy=math.sqrt(3*temp/sumvy2)
  fsz=math.sqrt(3*temp/sumvz2)
 
  #Array for storing positions in previous time step
  am=np.zeros((npart,3))

  for i in range (npart):
    vel[i][0]=(vel[i][0]-sumvx)*fsx
    vel[i][1]=(vel[i][1]-sumvy)*fsy
    vel[i][2]=(vel[i][2]-sumvz)*fsz
    am[i][0]=a[i][0]-vel[i][0]*dt
    am[i][1]=a[i][1]-vel[i][1]*dt
    am[i][2]=a[i][2]-vel[i][2]*dt
  
  return vel,am


def force(a,box):
    pnrg=0
    f = np.zeros((len(pos),3))
    fij=Vm=0
    
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
              dx=a[i][0]-a[j][0]
              dy=a[i][1]-a[j][1]
              dz=a[i][2]-a[j][2]
             
              if abs(dx)> (box/2):
                   dx=(box-abs(dx))*(-dx)/(abs(dx))
              if abs(dy)> (box/2):
                   dy=(box-abs(dy))*(-dy)/(abs(dy))
              if abs(dz)> (box/2):
                   dz=(box-abs(dz))*(-dz)/(abs(dz))
              r = math.sqrt((dx**2)+(dy**2)+(dz**2))
              
              if r <= rc :
                fij =(24/r**7)*((2/r**6) - 1)   #sigma = 1 and epsilon = 1
                f[i][0] += fij*(dx/r)
                f[i][1] += fij*(dy/r)
                f[i][2] += fij*(dz/r)
                f[j][0] -= fij*(dx/r)
                f[j][1] -= fij*(dy/r)
                f[j][2] -= fij*(dz/r)
                V= 4*((1/r**12)-(1/r**6))
                Vm=V-Vc
                pnrg+=Vm
  
    return f,pnrg


#Updation of position and velocity
def integ(a,am,f,dt,npart):   
  krg=sumv2=0
  af= np.zeros((npart,3))
  for i in range (npart):
    af[i][0]= 2*a[i][0] - am[i][0] + (f[i][0]*dt*dt)         #Verlet Algorithm ; m=1
    af[i][1]= 2*a[i][1] - am[i][1] + (f[i][1]*dt*dt)
    af[i][2]= 2*a[i][2] - am[i][2] + (f[i][2]*dt*dt)
    
    if af[i][0]>bl or af[i][0]<0:
       af[i][0]%=bl
    if af[i][1]>bl or af[i][1]<0:
       af[i][1]%=bl
    if af[i][2]>bl or af[i][1]<0:
       af[i][2]%=bl
      
    vel[i][0]= (af[i][0]-am[i][0])/(2*dt)  #vel is a global variable
    vel[i][1]= (af[i][1]-am[i][1])/(2*dt)
    vel[i][2]= (af[i][2]-am[i][2])/(2*dt)
    sumv2 +=((vel[i][0])**2+(vel[i][1])**2+(vel[i][2])**2)
    
  krg= 0.5*sumv2
  tem=sumv2/(3*npart)
  am=a
  a=af
  return am,a,vel,krg,tem

#Main body
temp=3  #Temperature
dt=0.0009  #Timestep
npart=500
bl=6.6
rc=bl/2.5
Vc=(4/rc**6)*((1/rc**6)-1)
steps=500
pos = create_pos(npart)

f = open("fcc_pos.xyz", "w")
f.write("%s \n" %(str(npart)))
for i in range(npart):
  f.write("\n He %s  %s  %s" %(str(round (pos[i][0],3)),str(round(pos[i][1],3)),str(round(pos[i][2],3))))
f.close()

vel,posm= create_vel(pos,npart,temp,dt)

f = open("fcc_vel.txt", "w")
f.write("(x,y,z component velocity respecticely (2nd,3rd,4th coulumn) \n")
for i in range(npart):
  f.write("\n %s %s  %s  %s" %(str(i+1),str(round(vel[i][0],6)),str(round(vel[i][1],6)),str(round(vel[i][2],6))))
f.close()

#gro file writing
f = open("fcc_p_v.gro", "w")
f.write(" Adithya He \n        500")
for i in range(npart):
  f.write("\n    %sHe He       %s  %s %s %s %s %s %s" %(str(i+1),str(i+1),str(round (pos[i][0],3)),str(round(pos[i][1],3)),str(round(pos[i][2],3)),str(round(vel[i][0],6)),str(round(vel[i][1],6)),str(round(vel[i][2],6))))
f.close()


prg=knrg=0
pe=np.zeros((steps,1))
ke=np.zeros((steps,1))
itr=np.zeros((steps,1))
t = np.zeros((steps,1))
tot = np.zeros((steps,1))
for i in range (steps):
  f , prg = force(pos,bl)
  pe[i]=prg/npart
  posm,pos,vel,knrg,temp=integ(pos,posm,f,dt,npart)
  t[i] = temp
  ke[i]=knrg/npart
  tot[i]=ke[i]+pe[i]
  itr[i]=i

#PE plotting
plt.figure(1,figsize=(18, 6))
plt.xlabel('Iteration')
plt.ylabel('PE')
plt.title('PE curve')
plt.scatter(itr[:],pe[:],s=10)


#KE plotting 
plt.figure(2,figsize=(18, 6))
plt.xlabel('iteration')
plt.ylabel('KE')
plt.title('KE curve')
plt.scatter(itr[:],ke[:],s=10)

#Temp plotting
plt.figure(3,figsize=(18, 6))
plt.xlabel('iteration')
plt.ylabel('Temp')
plt.title('Temp curve')
plt.scatter(itr[:],t[:],s=10)

#Total Energy
plt.figure(4,figsize=(18, 6))
plt.xlabel('iteration')
plt.ylabel('TE')
plt.title('TE curve')
plt.scatter(itr[:],tot[:],s=10)

f = open("data_md.csv", "w")
for i in range (steps):
  f.write("\n%s,%s,%s,%s,%s" %(str(i+1),str(round(pe[i][0],6)),str(round(ke[i][0],6)),str(round(tot[i][0],6)),str(round(t[i][0],5))))
f.close()

