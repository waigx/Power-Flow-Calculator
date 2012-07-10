#encoding:UTF-8  
'''
Created on 2012-6-28
Last updated on 2012-7-1 

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import numpy as np
import jacobianParaA as jpA
import nodeVoltageEquations as nve
import errors

def getJacobianMatrix( G , B , U , UAccu , isPolar=True ):
    """Get Jacobian Matrix from original Bus Admittance Matrix
    
    Args:
        G: matrix, Bus Admittance Matrix
        B: matrix,
        U: matrix,
        isPolar: boolean, (True by default)Indicate whether node-voltage equations are polar form, 
            if False, these equations are rectangular form.
        
    Returns:
        matrix, Generated Jacobian Matrix
    @TODO: The doc
    """
    order = errors.isSameLength([ errors.isSquareMatrix(G) , errors.isSquareMatrix(B) , U.shape[0] ])
    """
    @TODO: UAccu index 0 problem
    """
    subOrder = UAccu.shape[0]
    subOrder = 0
    tempJacMat = []
    if isPolar==False:
        upperBound1 = int(order - subOrder)
        upperBound2 = int(order)
        for i in range( 1 , upperBound1 ):
            tempArray = []
            for j in range( 1 , upperBound2 ):
                tempArray.append( jpA.CartesianHijA(B, U[:,0], G, U[:,1], i, j) )
                tempArray.append( jpA.CartesianNijA(B, U[:,0], G, U[:,1], i, j) )
            tempJacMat.append(tempArray)
            tempArray = []
            for j in range( 1 , upperBound2 ):
                tempArray.append( jpA.CartesianJijA(B, U[:,0], G, U[:,1], i, j) )
                tempArray.append( jpA.CartesianLijA(B, U[:,0], G, U[:,1], i, j) )
            tempJacMat.append(tempArray)
            
        for i in range( upperBound1 , upperBound2 ):
            tempArray = []
            for j in range( 1 , upperBound2 ):
                tempArray.append( jpA.CartesianHijA(B, U[:,0], G, U[:,1], i, j) )
                tempArray.append( jpA.CartesianNijA(B, U[:,0], G, U[:,1], i, j) )
            tempJacMat.append(tempArray)
            tempArray = []
            for j in range( 1 , upperBound2 ):
                tempArray.append( jpA.CartesianRijA(U[:,1], i, j) )
                tempArray.append( jpA.CartesianSijA(U[:,0], i, j) )
            tempJacMat.append(tempArray)
    """
    @TODO: The polar coordinate part
    """
    jacMat = np.matrix(tempJacMat)
    return jacMat

def difff( P , Q , B , G , U , UAccu ):
    """
    @TODO: doc
    @TODO: subOrder = 0
    @TODO: polar system
    """
    
    order = errors.isSameLength( [errors.isSquareMatrix(B) , errors.isSquareMatrix(G) , U.shape[0] , P.shape[0]+1 , Q.shape[0]+1] )
    subOrder = UAccu.shape[0]
    subOrder = 0
    deltaf = []
    upperBound1 = int( order - subOrder )
    upperBound2 = int( order )
    for i in range(1,upperBound1):
        deltaf.append( (P[i-1]-nve.CartesianPi(G, U[:,0], B, U[:,1], i))[0,0] )
        deltaf.append( (Q[i-1]-nve.CartesianQi(G, U[:,0], B, U[:,1], i))[0,0] )
    for i in range(upperBound1,upperBound2):
        deltaf.append( (P[i-upperBound1]-nve.CartesianPi(G, U[:,0], B, U[:,1], i))[0,0] )
        deltaf.append( UAccu[i-upperBound1]**2-U[i,0]**2-U[i,1]**2 )
    return np.matrix(deltaf).T

def creatx( U ):
    """
    @TODO: doc
    @TODO: polar system
    """
    U = np.roll( U , 1 , 1 )
    x = np.matrix( U.flat ).T

    return x

def restoreU( x ):
    """
    @TODO: doc
    @TODO: polar system
    """
    tempU = [[0,0]]
    length = int( len(x)/2 )
    for i in range( length ):
        tempU.append([x[i*2+1,0],x[i*2,0]])
    U = np.matrix(tempU)
    return U