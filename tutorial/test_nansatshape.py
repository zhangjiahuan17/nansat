#!/usr/bin/env python
# Name:    nansatshape_test.py
# Purpose: Tutorial for nansatshape class
# Authors:      Asuka Yamakawa, Anton Korosov, Knut-Frode Dagestad,
#               Morten W. Hansen, Alexander Myasoyedov,
#               Dmitry Petrenko, Evgeny Morozov
# Created:      29.06.2011
# Copyright:    (c) NERSC 2011 - 2013
# Licence:
# This file is part of NANSAT.
# NANSAT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# http://www.gnu.org/licenses/gpl-3.0.html
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


import inspect, os
import numpy as np

from nansat import Nansat, Domain, Nansatshape

try:
    from osgeo import gdal, osr, ogr
except:
    import gdal, osr, ogr

# input and output file names
from testio import testio
iPath, oPath = testio()
iFileName = os.path.join(iPath, 'gcps.tif')
shpFileName = os.path.join(iPath, 'points.shp')
print 'Input file: ', iFileName, '; ', shpFileName
oFileName = os.path.join(oPath, 'output_nansatshape_')
print 'Output file:', oFileName

''' Nansatshape class read and write ESRI-shape files

The core of Nansatshape is a OGR. the main functions of the class are
1. Create empty object in memory and add data (fields and geometory).
2. Open shape file and read the data.

Nansatshape support points, line and ploygons. (not mupti-polygon)

'''

# Create a nansatShape object with line geometry
nansatOGR = Nansatshape(wkbStyle=ogr.wkbLineString)

# Create polygon geometry and set them to featuers
nansatOGR.add_features(coordinates=[[100, 150, 200, 500, 600, 800],
                                    [20, 30, 60, 30, 60, 90]],
                       geoFeatureID=[0, 0, 0, 1, 1, 1])

# Create structured numpy array
fieldValues = np.zeros(3, dtype={'names':['INT', 'STR','FLOAT1','FLOAT2'],
                                 'formats':['i4','a10','f8','f8']})
fieldValues['INT'] = [10, 20, 30]
fieldValues['STR'] = ['CHAR0', 'CHAR1', 'CHAR2']
fieldValues['FLOAT1'] = [0.0, 3.5, 5.8]
fieldValues['FLOAT2'] = [24.5, 15.4, 36.4]

# add fields to the feature and geometry at once
nansatOGR.add_features(values=fieldValues,
                       fieldFeatureID=[0, 1, 2],
                       coordinates=[[300, 700, 750],[80, 50, 60]],
                       geoFeatureID=[2, 2, 2])

# save to a file
ogr.GetDriverByName("ESRI Shapefile").CopyDataSource(nansatOGR.datasource,
                                                     oFileName+'Lines.shp')

# Create a nansatShape from shape file
nansatOGR = Nansatshape(shpFileName)
# Get corner points (geometries of featuers) in the layer
points, latlon = nansatOGR.get_corner_points(latlon=False)
# print corner points
print 'Corner Points ---'
for iPoint in points:
    print iPoint

print '\n*** nansatshape_test completed successfully. Output files are found here:' + oFileName

