#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""
import sys
from pyproj import Geod
geod = Geod(ellps="WGS84")
#lons=-71-(7./60.)
#קו אורך
#lats=42+(15./60.)
#קו רוחב
#forwad_az=-66.531
#אזימוט קדמי
#distance=4164192.708
#מרחק
try:
    lons      = sys.argv[1]
    lats      = sys.argv[2]
    forwad_az = sys.argv[3]
    distance  = sys.argv[4]

    #lons      = -71.1166
    #lats      = 42.25
    #forwad_az = -66.531
    #distance  = 4164192.708

    # compute latitude, longitude and back azimuth of Point,
    # given another lat/lon, forward azimuth and distance to first point.
    X,Y,back_az=geod.fwd(lons,lats,forwad_az,distance)
    #print(X,Y,back_az)
    print(round(X, 4))
    print(round(Y, 4))
    print(round(back_az, 4))
except:
    print("Not Enough Data")
