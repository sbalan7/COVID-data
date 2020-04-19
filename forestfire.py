# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:25:09 2020

Author: Aalaap Nair

Description: Generates forest fire plots to model the spatial distribution of a disease in time

"""

"""
Colour Map:
0--Blue
1--Light Grey
2--Dark Grey
3--Red
4--Green
5--Yellow
6--Dark Red
"""

import numpy as np
from random import randint
import matplotlib.pyplot as plt
import time


#specifies lockdown zones by start vertex coordinates(x_start,y_start) and side-length(a) 
def lockdown(X,x_start,y_start,a):
    
    X[x_start:x_start+a+1,y_start]=0
    X[x_start,y_start:y_start+a+1]=0
    X[x_start+a,y_start:y_start+a+1]=0
    X[x_start:x_start+a+1,y_start+a]=0
    

#likelihood of disease for an exposed individual
def likelihood_disease():
    m=randint(1,14)
    if m<=7:
        return 0
    else:
        return 1
 
#likelihood of whether the infecteded individual recovers(0), dies(1) or remains infected(2)
def likelihood_severe():
    m=randint(1,100)
    if m<=11:
        return 0
    elif m>=97:
        return 1
    else:
        return 2

#returns the first neighbours of an individual cell, offers edge and corner control
def neighb(X,i,j):
    
    
    if i>0 and j>0:
        return X[i-1:i+2,j-1:j+2]
        
    elif i==0 and j!=0:
        return X[:i+2,j-1:j+2]
    
    elif i!=0 and j==0:
        return X[i-1:i+2,:j+2]
    
    else:
        return X[:i+2,:j+2]
    
        
#changes the state of the frame X to the next point in time
def state_change(X,T):
    
    Y=X.copy()
    for i in range(len(X)):
        for j in range(len(X)):
            
            if X[i,j]==1:
                temp=neighb(X,i,j)
                if 3 in temp:
                    Y[i,j]=5
                    T[i,j]+=1
                
            elif X[i,j]==5:
                if T[i,j]<=14:
                    if likelihood_disease()==1:
                        Y[i,j]=3
                if T[i,j]==15:
                    Y[i,j]=1
                T[i,j]+=1
            
            elif X[i,j]==3:
                if T[i,j]>=14:
                    if likelihood_severe()==0:
                        Y[i,j]=4
                    elif likelihood_severe()==1:
                        Y[i,j]=2
                    else:
                        Y[i,j]=3 
                
                
                Y[i,j]=6
                T[i,j]+=1
                
            elif Y[i,j]==6:
                if likelihood_severe()==0:
                    Y[i,j]=4
                elif likelihood_severe()==1:
                    Y[i,j]=2
                else:
                    Y[i,j]=6
                T[i,j]+=1
            
    return Y
 
#maps the entries of X to a forest fire plot                   
def render(X):
    
    C=np.zeros((len(X),len(X),3))
    for i in range(len(X)):
        for j in range(len(X)):
            
            if X[i,j]==0:
                C[i,j,0]=51/256
                C[i,j,1]=153/256
                C[i,j,2]=255/256
                
            elif X[i,j]==1:
                C[i,j,0]=224/256
                C[i,j,1]=224/256
                C[i,j,2]=224/256
                
            elif X[i,j]==2:
                C[i,j,0]=0/256
                C[i,j,1]=0/256
                C[i,j,2]=0/256
                
            elif X[i,j]==3:
                C[i,j,0]=255/256
                C[i,j,1]=128/256
                C[i,j,2]=0/256
                
            elif X[i,j]==4:
                C[i,j,0]=0/256
                C[i,j,1]=204/256
                C[i,j,2]=0
                
            elif X[i,j]==5:
                C[i,j,0]=255/256
                C[i,j,1]=255/256
                C[i,j,2]=0
                
            else:
                C[i,j,0]=255/256
                C[i,j,1]=0
                C[i,j,2]=0
                
    fig, ax = plt.subplots()

    im = ax.imshow(C,extent=(1,len(X),1,len(X))) 
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig.tight_layout()

    return C

#****************************************************************************            

N=11 #size of pupulation = N**2

X=np.array([[1]*N]*N)
T=np.array([[0]*N]*N)

#Initial conditions:
X[int(round(N/2)-1),int(round(N/2)-1)]=3

#X[24,24]=3
#X[74,74]=3
#X[24,74]=3
#X[74,24]=3
#lockdown(X,14,14,20)
#lockdown(X,64,64,20)
#lockdown(X,14,64,20)
#lockdown(X,64,14,20)


C=render(X)
plt.savefig("fig0.png")


time.sleep(5)
lim=60 #number of days

for k in range(lim):
    
    X=state_change(X,T)
    if k%1==0:
        C=render(X)
        plt.savefig("fig"+str(k+1)+".png")
    if k==1:
        lockdown(X,2,2,6)


