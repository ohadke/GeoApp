#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:15:34 2020

@author: orbinman
"""
import math
X1=170#input
Y1=100#input
X2=120#input
Y2=150#input
D=4.85
C=2#input
crad=C*(math.pi/180)
G=D-crad
dx=X2-X1
print(dx)
dy=Y2-Y1
print(dy)
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
print(a)        
Agrid=a*(180/math.pi)
if X2>219529.584:
    Ageo=(a+crad)*(180/math.pi)
else:
    Ageo=(a-crad)*(180/math.pi)
Amag=Ageo-D
print(Ageo,Agrid,Amag)