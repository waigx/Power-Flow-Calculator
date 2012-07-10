#encoding:UTF-8  
'''
Created on 2012-6-30
Last updated on 2012-7-1

@author: Igor Wang
@contact: igor@igorw.org
@version: 0.0
'''

import jacobianPara

#  Calculate the parameters in Cartesian coordinate system   

def CartesianHijA( B , e , G , f , i , j ):
    if i==j:
        return jacobianPara.CartesianHii(B[i,:].T, e, G[i,:].T, f, i) 
    else:
        return jacobianPara.CartesianHij(B[i,j], e[i], G[i,j], f[i])

def CartesianNijA( B , e , G , f , i , j ):
    if i==j:
        return jacobianPara.CartesianNii(G[i,:].T, e, B[i,:].T, f, i)
    else:
        return jacobianPara.CartesianNij(G[i,j], e[i], B[i,j], f[i])

def CartesianJijA( B , e , G , f , i , j ):
    if i==j:
        return jacobianPara.CartesianJii(G[i,:].T, e, B[i,:].T, f, i)
    else:
        return jacobianPara.CartesianJij(B[i,j], e[i], G[i,j], f[i])

def CartesianLijA( B , e , G , f , i , j ):
    if i==j:
        return jacobianPara.CartesianLii(B[i,:].T, e, G[i,:].T, f, i)
    else:
        return jacobianPara.CartesianLij(G[i,j], e[i], B[i,j], f[i])

def CartesianRijA( f , i , j ):
    if i==j:
        return 2*f[i]
    else:
        return 0

def CartesianSijA( e , i , j ):
    if i==j:
        return 2*e[i]
    else:
        return 0

#  Calculate the parameters in Polar coordinate system

def PolarHijA( U , delta , G , B , i , j ):
    if i==j:
        return jacobianPara.PolarHii(U, G[i,:].T, B[i,:].T, delta[i], i)
    else:
        return jacobianPara.PolarHij(U[i], U[j], delta[i,j], G[i,j], B[i,j])

def PolarJijA( U , delta , G , B , i , j ):
    if i==j:
        return jacobianPara.PolarJii(U, G[i,:].T, B[i,:].T, delta[i], i)
    else:
        return jacobianPara.PolarJij(U[i], U[j], delta[i,j], G[i,j], B[i,j])

def PolarNijA( U , delta , G , B , i , j ):
    if i==j:
        return jacobianPara.PolarNii(U, G[i,:].T, B[i,:].T, delta[i], i)
    else:
        return jacobianPara.PolarNij(U[i], U[j], delta[i,j], G[i,j], B[i,j])

def PolarLijA( U , delta , G , B , i , j ):
    if i==j:
        return jacobianPara.PolarLii(U, G[i,:].T, B[i,:].T, delta[i], i)
    else:
        return jacobianPara.PolarLij(U[i], U[j], delta[i,j], G[i,j], B[i,j])
    