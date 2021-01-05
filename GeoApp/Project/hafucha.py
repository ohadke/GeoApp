#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:42:03 2020

@author: orbinman
"""

from pyproj import Geod
geod = Geod(ellps="WGS84")
lons1=-71-(7./60.)
#קוו אורך נקודה 1
lats1=42+(15./60.)
#קו רוחב נקודה 1
lons2=-123-(41./60.)
#קוו אורך נקודה 2
lats2=45+(31./60.)
#קוו רטחב נקודה 2 
# compute latitude, longitude and back azimuth of second Point,
 # given first point lat/lon, forward azimuth and distance to second point.
forward_az,back_az,distance=geod.inv(lons1, lats1, lons2, lats2)
print(forward_az, back_az,distance)