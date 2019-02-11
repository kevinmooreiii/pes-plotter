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

### FUNCTIONS FOR PLOTTING CERTAIN 3D Images ###

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

with open(inputfilename,'r') as infile:
  data = infile.readlines()

# Put content of input file into various list to be altered later.
x = []
y = []
z1 = []
for i in range(1,len(data)):
  if '#' not in data[i].strip():
    tmp = data[i].strip().split()
    if float(tmp[0]) >= 1.1 and float(tmp[1]) <= 150.0:
        x.append(float(tmp[0]))
        y.append(float(tmp[1]))
        z1.append(float(tmp[2]))

xi = np.linspace(min(x),max(x))
yi = np.linspace(min(y),max(y))
xg, yg = np.meshgrid(xi,yi)

xyarr = np.array( list( zip(x,y) ) ) 
z1arr = np.array( z1 )


z1g = griddata(xyarr, z1arr, (xg,yg), method='cubic')

# Adjust cmap for easy visulazion of seem
cmap = cm.get_cmap('autumn')

# Set number of contours
ncontours = 75

# Set fonts
font = {'family' : 'normal',
 #       'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)


# Create plot
fig = plt.figure()

#### Create subplot for difference potential ###
af = fig.add_subplot(111)

# Set titles and axes labels
#af.set_title('Spin-orbit Coupling')
af.set_xlabel('N--O Distance (Ang.)')
af.set_ylabel('N-N-O Angle (Deg.)')

# Plot the contours for the difference potential
afcontour = af.contour(xg, yg, z1g, ncontours, cmap=cmap)
#afcontourf = af.contourf(xg, yg, z1g, ncontours, cmap=cmap)

# Plot the colorbars
afpcolor = af.pcolor(xg, yg, z1g, cmap=cmap)
cbar1 = plt.colorbar(afpcolor, orientation='horizontal', shrink=0.8)
cbar1.set_label('H_SO (cm-1)')

# Plot the triplet contours
#bfcontour = af.contour(xg, yg, z2g, ncontours, colors='black')

# Place points for various points of interest; place legend for these points
#af.plot([1.45945826],[118.55168496], color='green', marker='o', markersize=14, label='T-SP')
#af.plot([],[], color='green', marker='o', markersize=14, label='S-SP')
#af.plot([],[], color='green', marker='o', markersize=14, label='MSX')
af.legend(loc="lower left", fontsize=20, markerscale=1.5, framealpha=1.0)

fig.set_size_inches(16,9)
fig.savefig(outputfilename,dpi=300)

