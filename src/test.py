#encoding:UTF-8  
#! /usr/bin/python
# Filename : test.py

'''
Created on 2012-7-11
Last updated on 2012-7-11 

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import core.newtonRaphson as nr
import numpy as np


Y=np.matrix([[  6.250-18.750j   ,-5.000+15.000j ,-1.250+3.750j  ,0              ,0              ],
             [  -5.000+15.000j  ,10.834-32.500j ,-1.667+5.000j  ,-1.667+5.000j  ,-2.500+7.500j  ],
             [  -1.250+3.750j   ,-1.667+5.000j  ,12.917-38.750j ,-10.00+30.00j  ,0              ],
             [  0               ,-1.667+5.000j  ,-10.00+30.00j  ,12.917-38.750j ,-1.250+3.750j  ],
             [  0               ,-2.500+7.500j  ,0              ,-1.250+3.750j  ,3.750-11.250j  ]
             ],dtype=np.complex)

S=np.matrix([[  0.20+0.20j  ],
             [  -0.45-0.15j ],
             [  -0.40-0.05j ],
             [  -0.60-0.10j ]
             ],dtype=np.complex)

UPri=np.matrix([[   1.06+0j ],
                [   1.00+0j ],
                [   1.00+0j ],
                [   1.00+0j ],
                [   1.00+0j ]])

UAccu=np.matrix([])

accu = 0.00001

[ U , output ] = nr.newtonRaphson(Y, S, UPri, UAccu, accu)

print U
print output
