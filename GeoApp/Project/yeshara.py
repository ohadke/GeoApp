#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""
from pyproj import Geod
geod = Geod(ellps="WGS84")
lons=-71-(7./60.)
#קו אורך
lats=42+(15./60.)
#קו רוחב
forwad_az=-66.531
#אזימוט קדמי
distance=4164192.708
#מרחק
# compute latitude, longitude and back azimuth of Point,
# given another lat/lon, forward azimuth and distance to first point.
X,Y,back_az=geod.fwd(lons,lats,forwad_az,distance)
print(X,Y,back_az)