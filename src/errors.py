'''
Created on 2012-6-30
Last updated on 2012-6-30

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import numpy as np

class matrixFormatException(Exception):
    '''It defined a class of matrix format error'''
    def __init__(self, rowMajorOrder , columnMajorOrder ):
        Exception.__init__(self)
        self.rowMajorOrder = rowMajorOrder
        self.columnMajorOrder = columnMajorOrder
        
class arrayUnequalException(Exception):
    '''Defined a class indicate that two arrays have different length'''
    def __init__( self ):
        Exception.__init__(self)
        

def isSameLength( arr ):
    """This function determine whether the elements in specified array are equal,
    and it will raise an error if not.
    
    Args:
        arr: The array to be check.
        
    Returns:
        int: Elements ( positive ) value if all elements are the same, or -1 if not.
    """
    
    try:
        if np.std(arr)!= 0:
            raise arrayUnequalException()
    except arrayUnequalException:
        print "The Lengths of inputed arrays are not equal, data could not be process."
        return -1
    return int( np.mean(arr) )

def isSquareMatrix( m ):
    """This function determine whether the matrix is a square Matrix,
    and it will raise an error if not.
    
    Args:
        m: The matrix to be check.
        
    Returns:
        int: order ( positive ) of the matrix if it's a square one, or -1 if not.
    """
    try:
        if m.shape[0]!=m.shape[1]:
            raise matrixFormatException( m.shape[0] , m.shape[1] )
    except matrixFormatException:
        print "Error: The Bus Admittance Matrix must be a Square Matrix."
        return -1
    return int( m.shape[0] )