#Francisco Javier Díaz  Perd
print ("Primera Parte")
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
class tiropar(libre):
    def __init__(self,y0=0.0,vy0=0.0,m0=1.0,x0=0.0, vx0=0.0):
        super().__init__(y0,vy0,m0)
        self.x=x0
        self.vx=vx0
    def muevete(self,dt):
        super().muevete(dt)
        self.x += dt*self.vx
    def imprime(self,t):
        return "{0:.5f}   {1:.5f}   {2:.5f}   {3:.5f}   {4:.5f}".format(t,self.y,self.vy,self.x, self.vx)

vxp= 7 *(((2)**(1/2))/2)
vyp = vxp
cuerpo=tiropar(0.0, vxp, 1.0, 0.0,vyp)
cuerpo.CalculaFuerza()
t=0.0
dt=1.0e-2

f=open("./parabolico.dat","w+")
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

print ("Segunda Parte")
class parabfric(tiropar):
    def __init__(self,y0=0.0,vy0=0.0,m0=1.0,x0=0.0, vx0=0.0,bet0=2.0, Fy0=0):
        super().__init__(y0,vy0,m0,x0,vx0)
        self.bet=bet0
        self.Fy=Fy0-self.m*self.g-self.bet*self.vy
        self.Fx =0
    def muevete(self,dt):
        super().muevete(dt)
        self.Fy=-self.m*self.g-self.bet*self.vy
        self.vx +=(self.Fx/self.m)*dt
        self.Fx = (self.vx*self.bet)*(-1)
    def imprime(self,t):
        return "{0:.5f}   {1:.5f}   {2:.5f}   {3:.5f}   {4:.5f}".format(t,self.y,self.vy,self.x, self.vx)

vxp= 7 *(((2)**(1/2))/2)
vyp = vxp
cuerpo2=parabfric(0.0, vyp, 1.0, 0.0,vxp,2.0,0.0)
cuerpo2.CalculaFuerza()
t=0.0
dt=1.0e-2
f=open("./parabfric.dat","w+")
while t < 1.0:    
    st=cuerpo2.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo2.muevete(dt)
    t+=dt
st=cuerpo2.imprime(t)
print(st)
f.write(st)
f.close()

print ("Tercera Parte")
class cohete(paracaidas):
    def __init__(self,y0=0.0,vy0=0.0,m0=2.0,bet0=4, u0=0,mu0=0):
        super().__init__(y0,vy0,m0,bet0)
        self.u=u0
        self.mu=mu0
    def muevete(self,dt):
        self.Fy =-self.vy*self.bet-self.m*self.g+self.mu*self.u
        self.m +=-dt*self.mu
    def imprime(self,t):
        return "{0:.4f}   {1:.4f}   {2:.4f}   {3:.4f}".format(t,self.y,self.vy,self.m)

vyc = 10
cuerpo3=cohete(0.0, vyc, 2.0,1.0,1.0,2.0)
cuerpo3.CalculaFuerza()
t=0.0
dt=1.0e-2
f=open("./cohete.dat","w+")
while t < 1.0:    
    st=cuerpo3.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo3.muevete(dt)
    t+=dt
st=cuerpo3.imprime(t)
print(st)
f.write(st)
f.close()

print("Caida libre")       
cuerpo4=libre()
cuerpo4.CalculaFuerza()
t=0.0
dt=1.0e-2
f=open("./libre.dat","w+")
while t < 1.0:    
    st=cuerpo4.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo4.muevete(dt)
    t+=dt
st=cuerpo4.imprime(t)
print(st)
f.write(st)
f.close()
#%%

print("Paracaidas")       
cuerpo5=paracaidas()
cuerpo5.CalculaFuerza()
t=0.0
dt=1.0e-2
f=open("./paracaidas.dat","w+")
while t < 1.0:    
    st=cuerpo5.imprime(t)
    print(st)
    f.write(st+"\n")
    cuerpo5.muevete(dt)
    t+=dt
st=cuerpo5.imprime(t)
print(st)
f.write(st)
f.close()
#%%

#%%
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#%%
print("Bono: )
"""
En esta parte leemos y graficamos los datos generados.
"""
## Leamos archivos
f=open("caidalibre.dat","r")
l1=f.readlines()
f.close()
f=open("parabolico.dat","r")
l2=f.readlines()
f.close()
t1=[]
x1=[]
vx1=[]
y1=[]
vy1=[]
for i in range(len(l1)):
    x=l1[i].split()
    t1.append(float(x[0]))
    y1.append(float(x[1]))
    vy1.append(float(x[2]))
    x1.append(float(x[3]))
    vx1.append(float(x[4]))
t2=[]
y2=[]
vy2=[]
x2=[]
vx2=[]
for i in range(len(l2)):
    x=l2[i].split()
    t2.append(float(x[0]))
    y2.append(float(x[1]))
    v2.append(float(x[2]))
    x2.append(float(x[3]))
    vx2.append(float(x[4]))
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
ax.plot(t1,vy1)
ax.plot(t2,vy2)
ax.set(xlabel='t (s)', ylabel='vy (m/s)',title='Velocidad en Y contra tiempo')
fig.savefig("VvsT.png")
plt.close(fig)



