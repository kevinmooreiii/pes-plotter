#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D
import pyparsing
import numpy as np
import sys
from scipy.interpolate import griddata


# Read data from energy file
inputfilename = sys.argv[1]
with open(inputfilename,'r') as infile:
  data = infile.readlines()

# Put content of input file into various list to be altered later.
x = []
y = []
z1 = []
z2 = []
z3 = []
for i in range(1,len(data)):
  if '#' not in data[i].strip():
    tmp = data[i].strip().split()
    if tmp[3] != '0.000':
#        print(tmp[0][3])
      if (tmp[0][3] == '0' or tmp[0][3] == '5') and float(tmp[1]) % 2 == 0: 
        print(tmp[0]+'\t'+tmp[1])
        x.append(float(tmp[0]))
        y.append(float(tmp[1]))
        z1.append(float(tmp[2]))
        z2.append(float(tmp[3]))

#for val in y:
#    print(val)

# Get relative energies
z2rel = []
for i in range(len(z2)):
  z2rel.append((z2[i] - min(z2))*627.5095)

# Build the x,y mesh
xi = np.linspace(min(x),max(x),100)
yi = np.linspace(min(y),max(y),100)
xg, yg = np.meshgrid(xi,yi)

# Place into arrays
xyarr = np.array(list(zip(x,y))) 
zarr = np.array(z1)
z2arr = np.array(z2rel)

# Build the grid
z1g = griddata(xyarr, zarr, (xg,yg), method='cubic')
z2g = griddata(xyarr, z2arr, (xg,yg), method='cubic')

# Contours
fig = plt.figure()
af = fig.add_subplot(111)
ncontours = 75
afcontour = af.contour(xg, yg, z1g, ncontours, levels=[0])

# Get x,y points for the zero contour
xv = []
yv = []
for contour in afcontour.collections:
    for path in contour.get_paths():
        data = path.vertices
        xv.append(data[:,0])
        yv.append(data[:,1])

# Interpolate z-values in a new z-range for the x,y points
zint = griddata(xyarr, z2arr, (xv[0],yv[0]), method='cubic')

# Write the x,y, and z points to a file
with open('griddata_e', 'w') as gridfile:
    for i in range(len(zint)):
        gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[0][i], yv[0][i], zint[i]))


