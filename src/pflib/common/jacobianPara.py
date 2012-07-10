#encoding:UTF-8  
'''
Created on 2012-6-28
Last updated on 2012-6-30

@author: Igor Wang
@contact: igor@igorw.org
@version: 0.0
'''

import numpy as np
from errors import isSameLength
        
#  Calculate the parameters in Cartesian coordinate system   

def Cartesianaii( Gi , e , Bi , f , i ):
    lengthArray = [ len(Gi) , len(e) , len(Bi) , len(f) ]    
    length = isSameLength( lengthArray )
    aii = 0
    for j in range(0,length):
        aii = aii + ( Gi[j,0]*e[j] - Bi[j,0]*f[j] )
    return aii[0,0]

def Cartesianbii( Bi , e , Gi , f , i ):
    lengthArray = [ len(Gi) , len(e) , len(Bi) , len(f) ]    
    length = isSameLength( lengthArray )
    bii = 0
    for j in range(0,length):
        bii = bii + ( Gi[j]*f[j] + Bi[j]*e[j] )
    return bii[0,0]

def CartesianHij( Bij , ei , Gij , fi ):
    return (-Bij*ei + Gij*fi)[0,0]

def CartesianNij( Gij , ei , Bij , fi ):
    return (Gij*ei + Bij*fi)[0,0]

def CartesianJij( Bij , ei , Gij , fi ):
    return -CartesianNij( Gij , ei , Bij , fi )

def CartesianLij( Gij , ei , Bij , fi ):
    return CartesianHij( Bij , ei , Gij , fi )

def CartesianHii( Bi , e , Gi , f , i ):
    Hii = -Bi[i]*e[i] + Gi[i]*f[i] + Cartesianbii( Bi , e , Gi , f , i )
    return Hii[0,0]

def CartesianNii( Gi , e , Bi , f , i ):
    Nii = Gi[i]*e[i] + Bi[i]*f[i] + Cartesianaii( Gi , e , Bi , f , i )
    return Nii[0,0]

def CartesianJii( Gi , e , Bi , f , i ):
    Jii = -Gi[i]*e[i] - Bi[i]*f[i] + Cartesianaii( Gi , e , Bi , f , i )
    return Jii[0,0]

def CartesianLii( Bi , e , Gi , f , i ):
    Lii = -Bi[i]*e[i] + Gi[i]*f[i] - Cartesianbii( Bi , e , Gi , f , i )
    return Lii[0,0]

def CartesianRii( fi ):
    return 2*fi[0,0]

def CartesianSii( ei ):
    return 2*ei[0,0]

#  Calculate the parameters in Polar coordinate system

def PolarHij( Ui , Uj , deltaij , Gij , Bij ):
    deltaij = deltaij*np.pi/180
    return (Ui*Uj*(Gij*np.sin(deltaij)-Bij*np.cos(deltaij)))[0,0]

def PolarJij( Ui , Uj , deltaij , Gij , Bij ):
    deltaij = deltaij*np.pi/180
    return (-Ui*Uj*(Gij*np.cos(deltaij)+Bij*np.sin(deltaij)))[0,0]

def PolarNij( Ui , Uj , deltaij , Gij , Bij ):
    return -PolarJij( Ui , Uj , deltaij , Gij , Bij )

def PolarLij( Ui , Uj , deltaij , Gij , Bij ):
    return PolarHij( Ui , Uj , deltaij , Gij , Bij )

def PolarHii( U , Gi , Bi , deltai , i ):
    lengthArray = [ len(U) , len(Gi) , len(Bi) , len(deltai) ]
    length = isSameLength( lengthArray )
    Hii = 0
    for j in range(0,length):
        tempDelta =  deltai[j]*np.pi/180
        Hii = Hii + U[j]*( Gi[j]*np.sin(tempDelta)-Bi[j]*np.cos(tempDelta) )
    tempDelta =  deltai[i]*np.pi/180
    Hii = Hii - U[i]*( Gi[i]*np.sin(tempDelta)-Bi[i]*np.cos(tempDelta) )
    Hii = -U[i]*Hii
    return Hii[0,0]

def PolarJii( U , Gi , Bi , deltai , i ):
    lengthArray = [ len(U) , len(Gi) , len(Bi) , len(deltai) ]
    length = isSameLength( lengthArray )
    Jii = 0
    for j in range(0,length):
        tempDelta =  deltai[j]*np.pi/180
        Jii = Jii + U[j]*( Gi[j]*np.cos(tempDelta)+Bi[j]*np.sin(tempDelta) )
    tempDelta =  deltai[i]*np.pi/180
    Jii = Jii - U[i]*( Gi[i]*np.cos(tempDelta)+Bi[i]*np.sin(tempDelta) )
    Jii = U[i]*Jii
    return Jii[0,0]

def PolarNii( U , Gi , Bi , deltai , i ):
    Nii = PolarJii( U , Gi , Bi , deltai , i )
    Nii = Nii + 2*U[i]*U[i]*Gi[i]
    return Nii[0,0]
    
def PolarLii( U , Gi , Bi , deltai , i ):
    Lii = PolarHii( U , Gi , Bi , deltai , i )
    Lii = -Lii - 2*U[i]*U[i]*Bi[i]
    return Lii[0,0]