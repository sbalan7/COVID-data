# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:25:09 2020

@author: Aalaap Nair
"""

"""
0--Blue
1--White
2--Black
3--Red
4--Green
5--Yellow
6--Dark Red
"""

import numpy as np
from random import randint
import matplotlib.pyplot as plt
import imageio as io

def likelihood_disease():
    m=randint(1,14)
    if m<=7:
        return 0
    else:
        return 1
    
def likelihood_severe():
    m=randint(1,100)
    if m<=11:
        return 0
    elif m>=97:
        return 1
    else:
        return 2

def neighb(X,i,j):
    
    
    if i>0 and j>0:
        return X[i-1:i+2,j-1:j+2]
        
    elif i==0 and j!=0:
        return X[:i+2,j-1:j+2]
    
    elif i!=0 and j==0:
        return X[i-1:i+2,:j+2]
    
    else:
        return X[:i+2,:j+2]

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
                if T[i,j]>=21:
                    if likelihood_severe()==0:
                        Y[i,j]=4
                    elif likelihood_severe()==1:
                        Y[i,j]=2
                    else:
                        Y[i,j]=3 
                T[i,j]+=1
            
    return Y
                    
def render(X, count):
    
    C=np.zeros((len(X),len(X),3))
    for i in range(len(X)):
        for j in range(len(X)):
            
            if X[i,j]==0:
                C[i,j,0]=0
                C[i,j,1]=0
                C[i,j,2]=255
            
            elif X[i,j]==1:
                C[i,j,0]=255
                C[i,j,1]=255
                C[i,j,2]=255
            
            elif X[i,j]==2:
                C[i,j,0]=0
                C[i,j,1]=0
                C[i,j,2]=0
            
            elif X[i,j]==3:
                C[i,j,0]=255
                C[i,j,1]=0
                C[i,j,2]=0
            
            elif X[i,j]==4:
                C[i,j,0]=0
                C[i,j,1]=204
                C[i,j,2]=0
            
            elif X[i,j]==5:
                C[i,j,0]=255
                C[i,j,1]=255
                C[i,j,2]=0
            
            else:
                C[i,j,0]=0
                C[i,j,1]=0
                C[i,j,2]=0
                
    fig, ax = plt.subplots()
    
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.grid(b=1,which="major",axis="both",linewidth=2)

    ax.imshow(C,extent=(1,len(X),1,len(X)))
    filename = str(str(count) + ".png")
    plt.savefig(filename)

    return filename
#    plt.show(bbox_inches="tight")
    
def gifize(pics):
    
    images = []
    for img in pics:
        images.append(io.imread(img))
    io.mimsave("gif2.gif", images)


pics = []
N=11 #size of pupulation = N**2

X=np.array([[1]*N]*N)
T=np.array([[0]*N]*N)
X[int(round(N/2)-1),int(round(N/2)-1)]=3
X[2:9,2]=0
X[2,2:9]=0
X[8,2:9]=0
X[2:9,8]=0

render(X, 0)
lim=50

for k in range(10):
    pics.append("0.png")

for k in range(lim):
    
    X=state_change(X,T)
    C = render(X, k)
    pics.append(C)

for k in range(10):
    pics.insert(10, "0.png")

gifize(pics)