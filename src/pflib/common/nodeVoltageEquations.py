#encoding:UTF-8  
'''
Created on 2012-7-1
Last updated on 2012-7-1 

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import numpy as np
from errors import isSameLength

# Rectangular form

def CartesianPi( G , e , B , f , i ):
    lengthArray = [ len(G[i].T) , len(e) , len(B[i].T) , len(f) ]
    length = isSameLength( lengthArray )
    Pi = 0
    for j in range(0,length):
        Pi = Pi + e[i]*( G[i,j]*e[j] - B[i,j]*f[j] ) + f[i]*( G[i,j]*f[j] + B[i,j]*e[j] )
    return Pi[0,0]
    
def CartesianQi( G , e , B , f , i ):
    lengthArray = [ len(G[i].T) , len(e) , len(B[i].T) , len(f) ]
    length = isSameLength( lengthArray )
    Qi = 0
    for j in range(0,length):
        Qi = Qi + f[i]*( G[i,j]*e[j] - B[i,j]*f[j] ) - e[i]*( G[i,j]*f[j] + B[i,j]*e[j] )
    return Qi[0,0]

# Polar form

def PolarPi( U , G , B , delta , i ):
    lengthArray = [ len(G[i]) , len(U) , len(B[i]) , len(delta[i]) ]
    length = isSameLength( lengthArray )
    Pi = 0
    for j in range(0,length):
        tempDelta =  delta[i][j]*np.pi/180
        Pi = Pi + U[j]*( G[i][j]*np.cos(tempDelta) + B[i][j]*np.sin(tempDelta) )
    Pi = Pi*U[i]
    return Pi[0,0]
    
def PolarQi( U , G , B , delta , i ):
    lengthArray = [ len(G[i]) , len(U) , len(B[i]) , len(delta[i]) ]
    length = isSameLength( lengthArray )
    Qi = 0
    for j in range(0,length):
        tempDelta =  delta[i][j]*np.pi/180
        Qi = Qi + U[j]*( G[i][j]*np.sin(tempDelta) - B[i][j]*np.cos(tempDelta) )
    Qi = Qi*U[i]
    return Qi[0,0]