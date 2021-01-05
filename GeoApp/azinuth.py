#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:15:34 2020

@author: orbinman
"""
import sys
import math
try:
    east1     = int(sys.argv[1])
    north1    = int(sys.argv[2])
    east2     = int(sys.argv[3])
    north2    = int(sys.argv[4])
    converge  = int(sys.argv[5])
    #X1=170#input
    #Y1=100#input
    #X2=120#input
    #Y2=150#input
    D=4.85
    C=2#input
    crad=converge*(math.pi/180)
    G=D-crad
    dx=east2-east1
    dy=north2-north1
    if dx>0:
        if dy>0:
            a=abs(math.atan(dy/dx))
        else:
            a=2*math.pi-abs(math.atan(dy/dx))
    else:
        if dy>0:
             a=math.pi-abs(math.atan(dy/dx))
        else:
             a=math.pi+abs(math.atan(dy/dx))
       
    Agrid=a*(180/math.pi)
    if east2>219529.584:
        Ageo=(a+crad)*(180/math.pi)
    else:
        Ageo=(a-crad)*(180/math.pi)
    Amag=Ageo-D
    print(round(Agrid, 4))
    print(round(Amag, 4))
    print(round(Ageo, 4))
except:
    print("Not Enough Data")
