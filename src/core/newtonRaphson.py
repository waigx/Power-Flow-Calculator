#encoding:UTF-8  
'''
Created on 2012-6-28
Last updated on 2012-7-11 

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import common.matrixHandler as mh
import numpy as np

def newtonRaphson( Y , S , UPri , UAccu , accu , echoLevel=1 , maxIteration=99 , isPolar=False ):
    """
    @TODO: DOCS
    @TODO: Polar System
    """
    
    output = ""
    
    G = Y.real
    B = Y.imag
    P = S.real
    Q = S.imag

    U = np.matrix( [np.array(UPri.real.flat),np.array(UPri.imag.flat)] ).T
    
    iterationTimes=0
    
    while iterationTimes<maxIteration:
        
        JM = mh.getJacobianMatrix(G, B, U, UAccu, isPolar)
        deltaf = mh.difff(P, Q, B, G, U, UAccu)
        deltaU = JM.I * deltaf        
        
        if echoLevel>1:
                output = output + "Maximum error after " + str(iterationTimes+1) + " times iteration: " + str(mh.creatx(deltaU).max()) + "\n\n"
        
        if np.abs( mh.creatx(deltaU).max() )<=accu:
            break

        U = U + mh.restoreU( deltaU )
        iterationTimes = iterationTimes + 1
        
        if echoLevel>2:
            output = output + "Node voltage after " + str(iterationTimes) + " times iteration:\n" + str(U[:,0]+U[:,1]*1j) + "\n"
            output = output + "Power and squared voltage error after " + str(iterationTimes) + " times iteration:\n" + str(deltaf) + "\n\n"
        
        if echoLevel>3:
            output = output + "Jacobian matrix after " + str(iterationTimes) + " times iteration:\n" + str(JM) + "\n"
            output = output + "Correction incremental after " + str(iterationTimes) + " times iteration:\n" + str(deltaU) + "\n\n"
            
        if echoLevel>2:
            output = output + "---------------\n\n"
        
    if echoLevel>0:
        if iterationTimes==maxIteration:
            output = output + "Max iterative times ( "  + str(maxIteration) + " ) limit exceeded.\n\n"
        output = output + "------Iterated " + str(iterationTimes+1) + " times.------\n\n"
    
    return U[:,0]+U[:,1]*1j,output