#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.colors
from mpl_toolkits.mplot3d import Axes3D
import pyparsing
import numpy as np
import sys
from scipy.interpolate import griddata
from scipy.interpolate.rbf import Rbf

inputfilename = sys.argv[1]

with open(inputfilename,'r') as infile:
  data = infile.readlines()

# Put content of input file into various list to be altered later.
x = []
y = []
z1 = []
z2 = []
z3 = []
r = []
for i in range(1,len(data)):
  if '#' not in data[i].strip():
    tmp = data[i].strip().split()
    if tmp[3] != '0.000':
#      if float(tmp[1]) >= 1.1 and float(tmp[2]) <= 150.0: 
#      if float(tmp[1]) <= 160.0: 
        x.append(float(tmp[0]))
        y.append(float(tmp[1]))
        z1.append(float(tmp[2]))
        z2.append(float(tmp[3]))
        z3.append(float(tmp[4]))
#        r.append(float(tmp[0]))

zrel = []
for i in range(len(z3)):
  zrel.append((z3[i] - z2[i])*627.5095)
z2rel = []
for i in range(len(z2)):
  z2rel.append((z2[i] - min(z2))*627.5095)

# Build the x,y mesh
xi = np.linspace(min(x),max(x),500)
yi = np.linspace(min(y),max(y),500)
xg, yg = np.meshgrid(xi,yi)

# Place into arrays
xarr = np.array(x) 
yarr = np.array(y) 
xyarr = np.array(list(zip(x,y))) 
zarr = np.array(zrel)
zarr2 = np.array(z2rel)
zarr1 = np.array(z1)

# Build the grid
zg = griddata(xyarr, zarr, (xg,yg), method='cubic')

# Adjust cmap for easy visulazion of seem
cmap = cm.get_cmap('seismic')

# Set number of contours
ncontours = 75

# Set fonts
font = {'family' : 'normal',
#       'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)

# get contours 
fig = plt.figure()
af = fig.add_subplot(111)
af.set_xlabel('N--O Distance (Ang.)')
af.set_ylabel('N-N-O Angle (Deg.)')
afcontourf = af.contourf(xg, yg, zg, ncontours, cmap=cmap)
afcontour = af.contour(xg, yg, zg, ncontours, levels=[0], color='black')

# Get the zero contours
xv = []
yv = []
for contour in afcontour.collections:
    for path in contour.get_paths():
        data = path.vertices
        xv.append(data[:,0])
        yv.append(data[:,1])

# interpolate with griddata
#zint = griddata(xyarr, zarr2, (xv[1],yv[1]), method='cubic')
#zint2 = griddata(xyarr, zarr2, (xv[0],yv[0]), method='cubic')
zint = griddata(xyarr, zarr1, (xv[1],yv[1]), method='cubic')
zint2 = griddata(xyarr, zarr1, (xv[0],yv[0]), method='cubic')

with open('gd_seam1.dat', 'w') as gridfile:
    for i in range(len(zint)):
        gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zint[i]))
with open('gd_seam2.dat', 'w') as gridfile:
    for i in range(len(zint2)):
        gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[0][i], yv[0][i], zint2[i]))

# interpolate with rbf
rbf_2d = Rbf(xarr, yarr, zarr2, function='gaussian')
xgc, ygc = np.meshgrid(xv[0],yv[0])
zgc = rbf_2d(xgc, ygc)

#for i in range(len(zgc)):
#    for j in range(len(zgc[i])):
#        print('{0}\t{1}\t{2}'.format(str(xgc[i][j]), str(ygc[i][j]), str(zgc[i][j])))

with open('rbf_seam2.dat', 'w') as gridfile:
    for i in range(len(zgc)):
        for j in range(len(zgc[i])):
            gridfile.write('{0}\t{1}\t{2}\n'.format(str(xgc[i][j]), str(ygc[i][j]), str(zgc[i][j])))
#        gridfile.write('{0}   {1}   {2}\n'.format(xgc[i], ygc[i], zgc[i]))

# plot 
with open('tripe.dat', 'w') as gridfile:
    for i in range(len(z2rel)):
        gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(x[i], y[i], zarr2[i]))


