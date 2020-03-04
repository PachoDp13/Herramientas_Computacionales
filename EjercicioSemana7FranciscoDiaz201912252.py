#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:01:15 2020

@author: olacevedo
"""
#%%
"""
En esta parte se define la clase base Balon
"""
class libre:
    "Este balón se mueve mediante el método de Euler"
    g=9.8 #aceleración en m/s^2
    def __init__(self,y0=0.0,vy0=0.0,m0=1.0):
        self.y=y0
        self.vy=vy0
        self.m=m0
    def CalculaFuerza(self):
        self.Fy=-self.m*self.g
    def muevete(self,dt):
        self.y += self.vy*dt
        self.vy += (self.Fy/self.m)*dt
    def imprime(self,t):
        return "{0:.3f}   {1:.3f}   {2:.3f}".format(t,self.y,self.vy)
#%%
print("Caida libre")       
cuerpo=libre()
cuerpo.CalculaFuerza()
t=0.0
dt=1.0e-2
f=open("./caidalibre.dat","w+")
while t < 1.0:    
    st=cuerpo.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo.muevete(dt)
    t+=dt
st=cuerpo.imprime(t)
print(st)
f.write(st)
f.close()
#%%
"""
Esta es una clase heredada. Incluye la fricción laminar del aire
a través de un coeficiente de fricción bet.
"""
class paracaidas(libre):
    def __init__(self,y0=0.0,vy0=0.0,m0=1.0,bet0=4):
        super().__init__(y0,vy0,m0)
        self.bet=bet0
        self.Fy=-self.m*self.g-self.bet*self.vy
    def muevete(self,dt):
        super().muevete(dt)
        self.Fy=-self.m*self.g-self.bet*self.vy
    def imprime(self,t):
        return "{0:.3f}   {1:.3f}   {2:.3f}".format(t,self.y,self.vy)
cuerpo=paracaidas(0)
t=0.0
dt=1.0e-2
f=open("./paracaidas.dat","w+")
while t < 1.0:    
    st=cuerpo.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo.muevete(dt)
    t+=dt
st=cuerpo.imprime(t)
print(st)
f.write(st)
f.close()
#%%
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#%%
"""
En esta parte leemos y graficamos los datos generados.
"""
## Leamos archivos
f=open("caidalibre.dat","r")
l1=f.readlines()
f.close()
f=open("paracaidas.dat","r")
l2=f.readlines()
f.close()
t1=[]
y1=[]
v1=[]
for i in range(len(l1)):
    x=l1[i].split()
    t1.append(float(x[0]))
    y1.append(float(x[1]))
    v1.append(float(x[2]))
t2=[]
y2=[]
v2=[]
for i in range(len(l2)):
    x=l2[i].split()
    t2.append(float(x[0]))
    y2.append(float(x[1]))
    v2.append(float(x[2]))
# Grafiquemos altura contra tiempo
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(t1,y1)
ax.plot(t2,y2)
ax.set(xlabel='t (s)', ylabel='y (m)',title='Altura contra tiempo')
fig.savefig("HvsT.png")
plt.close(fig)
# Grafiquemos velocidad contra tiempo
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(t1,v1)
ax.plot(t2,v2)
ax.set(xlabel='t (s)', ylabel='v (m/s)',title='Velocidad contra tiempo')
fig.savefig("VvsT.png")
plt.close(fig)



