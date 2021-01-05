#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:31:19 2020

@author: orbinman
"""

import numpy as np
import pandas as pd
import math 
    
def datum1 (x,y,z):
    "netuney datum"
    a=6378137
    b=6356752
    k0=1.0000067
    phi0=0.55386965463774187
    lam0=0.61443473225468920
    esq=0.006694380004260807
    E0=219529.584
    N0=626907.390
    A0=1-(esq/4)-((3*(esq**2))/64)-((5*(esq**3))/256)
    A2=(3/8)*(esq+((esq**2)/4)+((15*esq**3)/128))
    A4=15/256*(esq**2+(3*esq**3)/4)
    A6=(35*(esq**3))/3072
    m0=a*(A0*phi0-A2*(math.sin(2*phi0))+A4*(math.sin(4*phi0))-A6*(math.sin(6*phi0)))
    "hitel"
    Ntag=y-N0
    mtag=m0+(Ntag/k0)
    n=(a-b)/(a+b)
    G=a*(1-n)*(1-(n**2))*(1+((9*(n**2))/4)+((225*n**4)/64))*(math.pi/180)
    sig=(mtag*(math.pi))/(180*G)
    phitag=sig+((3*n/2)-((27*n**3)/32))*(math.sin(2*sig))+(((21*(n**2))/16)-((55*(n**4))/32))*(math.sin(4*sig))+(151*(n**3)/96)*(math.sin(6*sig))+((1097*(n**4))/512)*math.sin(8*sig) 
    rotag=(a*(1-esq))/((1-esq*((math.sin(phitag))**2))**1.5)
    nitag=a/(math.sqrt(1-esq*((math.sin(phitag))**2)))
    psytag=nitag/rotag
    ttag=math.tan(phitag)
    Etag=x-E0
    xx=Etag/(k0*nitag)
    "tikun phi"
    term1=(ttag/(k0*rotag))*((Etag*xx)/2)
    term2=(ttag/(k0*rotag))*((Etag*(xx**3))/24)*(-4*(psytag**2)+9*psytag*(1-(ttag**2))+12*(ttag**2))
    term3=(ttag/(k0*rotag))*((Etag*(xx**5))/720)*(8*(psytag**4)*(11-24*(ttag**2))-12*(psytag**3)*(21-71*ttag**2)+15*(psytag**2)*(15-(98*ttag**2)+15*(ttag**4))+180*psytag*(5*(ttag**2)-3*(ttag**4))+360*(ttag**4))
    term4=(ttag/(k0*rotag))*(Etag*xx**7/40320)*(1385+3633*ttag**2+4095*ttag**4+1575*ttag**6)
    phi=phitag-term1+term2-term3+term4
    "tikun lamda"
    Term1=xx*(1/(math.cos(phitag)))
    Term2=(xx**3)*(1/(6*math.cos(phitag)))*(psytag+2*ttag**2)
    Term3=(xx**5)*(1/(120*math.cos(phitag)))*(-4*psytag**3*(1-6*ttag**2)+psytag**2*(9-68*ttag**2)+72*psytag*ttag**2+24*ttag**4)
    Term4=(xx**7)*(1/(5040*math.cos(phitag)))*(61+662*ttag**2+1320*ttag**4+720*ttag**6)
    lam=lam0+Term1-Term2+Term3-Term4
    "print(phi*180/math.pi, lam*180/math.pi)"
    "hatmara le geocentry"
    Nnew=a/(math.sqrt(1-esq*(math.sin(phi)**2)))
    U=(Nnew+z)*math.cos(phi)*math.cos(lam)
    V=(Nnew+z)*math.cos(phi)*math.sin(lam)
    W=(Nnew*(1-esq)+z)*math.sin(phi)
    "print(U, V, W)"
    m = 1.0000054248
    Rz = 0.0000080949
    Ry = -0.0000089821
    Rx = -0.0000016003
    dx=-24.0024
    dy=-17.1032
    dz=-17.8444
    b = np.array([[U],[V],[W]]) 
    A = np.array([[m, Rz, -Ry],[Rz, m, Rx],[Ry ,-Rx ,m]])
    l=np.array([[dx],[dy],[dz]])
    a1=np.linalg.inv(A)
    c=b-l
    X=np.matmul(a1,c)
    x1=X[0]
    y1=X[1]
    z1=X[2]
    "print(x1, y1, z1)"
    lamnew=math.atan(y1/x1)
    ro=math.sqrt(x1**2+y1**2)
    p0=math.atan((z1/ro)*(1-esq)**-1) 
    N1=a/(math.sqrt(1-esq*(math.sin(p0)**2)))
    h1=(ro/math.cos(p0))-N1
    p1=math.atan((z1/ro)*(1-esq*(N1/(N1+h1)))**-1)
    N2=a/(math.sqrt(1-esq*(math.sin(p1)**2)))
    h2=(ro/math.cos(p1))-N2
    p2=math.atan((z1/ro)*(1-esq*(N2/(N2+h2)))**-1)
    N3=a/(math.sqrt(1-esq*(math.sin(p2)**2)))
    h3=(ro/math.cos(p2))-N3
    p3=math.atan((z1/ro)*(1-esq*(N3/(N3+h3)))**-1)
    N4=a/(math.sqrt(1-esq*(math.sin(p3)**2)))
    h4=(ro/math.cos(p3))-N4
    p4=math.atan((z1/ro)*(1-esq*(N4/(N4+h4)))**-1)*(180/math.pi)
    lamnew1=lamnew*(180/math.pi)
    R=np.array([[lamnew1],[p4],[h4]]) 
    return R

df=pd.read_csv('project.csv')
li1=df.to_numpy()
a=len(li1)
solution=np.zeros((a,3))

for i in range(a):
    x=(datum1(li1[i,2],li1[i,1],li1[i,0])) 
    solution[i,0]=x[0]
    solution[i,1]=x[1]
    solution[i,2]=x[2]
pd.DataFrame(solution).to_csv("solution.csv")
print(solution)
