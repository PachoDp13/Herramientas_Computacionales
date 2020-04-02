#!bin/bash/python3
# coding: utf-8
#Francisco Javier Díaz Perdomo  COD:201912252
print ("Primera parte, función factorial:")

def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))
    
for i in range (1,6):
    print ("El factorial de",i,"es:", factorial(i) ) 

print ("Segunda parte, secuencia de Fibonacci:")

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range (1,6):
    print ("El término en la posición",i,"de Fibonacci es:", fibonacci(i)) 
    
print ("Tercera parte, pasar a base k:")

def basek(n, k):
    conversion = ''
    if(n<k):
        return str(n)
    else:
        return str(basek(n//k,k))+ str(n%k)    
for i in range (1,6):
    print ("El número",i, "en base 3 es:" ,basek(i,3))
    
print ("Cuarta parte, algoritmo de multiplicación:")

def prod(m,n):
    if(m==1):
        return n
    elif ((m%2)==0):
        return prod(m/2,2*n)
    elif (m>1):
        return (prod((m-1)/2, 2*n) + n)
m,n= 23,37
a,b=m,n


while (m>=1):
    if((m%2)==0):
        estado= "par"
    else:
        estado = "impar"
    print("El valor de m es",m ,"el de n es", n, "y m es",estado)
    if(m!=2):
        m=(m-1)/2
    else:
        m=m-1
    n=n*2
print ("El resultado de",a,"x",b,"es:",prod(a,b))     
