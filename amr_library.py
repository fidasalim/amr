# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:37:52 2021

@author: fida
"""


import numpy as np
import matplotlib.pyplot as plt
import math as m

def graph_plot(X,Y,N,x,y,u,v,n,b,c):
    fig, ax = plt.subplots()
    if n == 1:
        ax.stem(X, Y, markerfmt=' ',linefmt = 'purple',basefmt = ' ')
    elif n == 2:
        ax.stem(X, Y, markerfmt=' ',linefmt = 'navy',basefmt = ' ')
    elif n == 3:
        ax.stem(X, Y, markerfmt=' ',linefmt = 'red',basefmt = ' ')
    elif n == 4:
        ax.stem(X, Y, markerfmt=' ',linefmt = 'green',basefmt = ' ')
    else:
        ax.stem(X, Y, markerfmt=' ')
    if abs(b)<abs(c):
        plt.title('Dimension of matrix N ,|E_1-E_2|, b= '+str(N)+', '+str(c)+', '+str(b))
    else:
        plt.title('Dimension of matrix N , |E_1-E_2| , b= '+str(N)+', '+str(b)+', '+str(c))
    plt.xlabel(x)
    plt.ylabel(y)
    #plt.xlim(u-1,v+1)
    plt.savefig('Q_'+str(n)+'/'+str(b)+'/'+str(c)+'/fig_'+str(n)+'_'+str(N)+'.png')
    plt.show()
    
def y_matrix(U):
    Y = []   
    X = []
    import math as m
    E_max = max(U)
    E_min = min(U)
    dE = (E_max - E_min)/100
    y = E_min -1
    for i in range(100):
        x1 = E_min + i*dE
        x2 = x1 + dE
        n = 0
        X.append(x1)
        for x in U:
            if x >= x1 and x<x2:
                n += 1
            else:
                continue
        Y.append(n)
    return(X,Y)


def create_matrix(N,a,b):
    A = np.zeros((N,N))
    for i in range(0,N):
        A[i,i] = a
        if (i>0):
            A[i-1,i] = b
        if (i<N-1):
            A[i+1,i] = b
    return(A)

def create_matrix2(N,a,b,c):
    A = np.zeros((N,N))
    for i in range(0,N):
        if i%2 == 0:
            A[i,i] = a
        else:
            A[i,i] = b
        if (i>0):
            A[i-1,i] = c
        if (i<N-1):
            A[i+1,i] = c  
    return(A)

def create_matrix3(N,a,b):
    A = np.zeros((N,N))
    for i in range(0,N):
        A[i,i] = a
        if (i>0):
            A[i-1,i] = b
        if (i<N-1):
            A[i+1,i] = b
        A[0,N-1] = b
        A[N-1,0] = b
    return(A)

def create_matrix4(N,a,b,c):
    A = np.zeros((N,N))
    
    for i in range(0,N):
        if i%2 == 0:
            A[i,i] = a
        else:
            A[i,i] = b
        if (i>0):
            A[i-1,i] = c
        if (i<N-1):
            A[i+1,i] = c  
        A[0,N-1] = c
        A[N-1,0] = c
    return(A)