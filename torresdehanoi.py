#!/usr/python3
# -*- coding: utf-8 -*-
#%%
### Esta función crea la torre de Hanoi inicial, con todos los dicos
## en la columna 0
def llinit(n):
    ll=[list(range(1,n+1))]
    ll.append([0]*n)
    ll.append([0]*n)
    return ll

### Esta función muestra las torres de Hanoi como unos números en columnas
def mostrar(ll):
    n=len(ll[0])
    for i in range(n):
        print("|",ll[0][i],"|",ll[1][i],"|",ll[2][i],"|")
    print("-------------\n")

## Esta función averigua en qué columna está el disco k
def dondeesta(k,ll):
    pos=0
    for i in range(3):
        if k in ll[i]:pos=i
    return pos

## Esta función averigua cual es el primer lugar libre en la columna pos
def llegada(pos,ll):
    u=ll[pos]
    n=len(u)
    lleg=-1
    for i in range(n):
        if u[i] == 0: lleg=i
    return lleg

### Esta función averigua si el disco k se puede puede mover.
### Y en caso afirmativo da las posiciones de salida y de llegado.
### Se trata de la función más intrincada de todo el algoritmo puesto
### que se deben cumplir varias condiciones para poder moder un disco.
def sepuedemover(k,ll,prev):
    antes=dondeesta(k,ll)
    sali=ll[antes].index(k)
### Se asume por defecto que el disco k no se puede mover 
    puede=False
### Si k=1 se sabe que se puede mover
    if k==1:
        despues=(antes+1)%3
        lleg=llegada(despues,ll)
        puede=True     
    else:
        ### Se definen unas salidas por defecto
        despues,lleg=antes,sali
        
        ### Si k>1 se averigua primero si el disco k está ocupado
        if ll[antes][sali-1] != 0:
            pass
        else:
            ### Ahora se averigua si hay un lugar a donde mover el disco k
            ### Teniendo en cuenta que el nuevo lugar no debe corresponder
            ### al movimiento inmediatamente anterior
            n=len(ll[0])
            for j in range(1,3):
                desp=(antes+j)%3
                llegj=llegada(desp,ll)
                if llegj== n-1 and prev != [k,desp] : 
                    puede = True
                    despues = desp
                    lleg = llegj
                elif llegj < n-1 and prev != [k,desp] : 
                    if ll[desp][llegj+1]>k:
                        puede = True
                        despues = desp
                        lleg = llegj
                    else:
                        pass
                else:
                    pass
    return puede,antes,sali,despues,lleg

## Esta es la función que de verdad es recursiva.
## Intenta mover el disco k, si no puede, intenta mover el disco k-1           
def mover(ll,prev,k):
    puede,antes,sali,despues,lleg=sepuedemover(k,ll,prev)
    if puede:
        #movemos el disco
        ll[antes][sali]=0
        ll[despues][lleg]=k
        #actualizamos el movimiento previo
        prev[0]=k
        prev[1]=antes
        mostrar(ll)
    else:
        mover(ll,prev,k-1)

## Esta función juega a las Torres de Hanoi con una altura de torre n
def torresdehanoi(n):
    ## Se inicia el juego y se muestra el estado inicial
    ll=llinit(n)
    mostrar(ll)
    ## Se crea un movimiento previo irrelevante
    prev=[0,0]
    ## se juega. El juego completo dura 2^n-1 pasos intermedios
    for i in range(2**n-1):
        mover(ll,prev,n)

torresdehanoi(4)
#%%