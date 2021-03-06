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

def shiftedColorMap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero.

    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower offset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to 
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax / (vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highest point in the colormap's range.
          Defaults to 1.0 (no upper offset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False), 
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)

    return newcmap

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

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
#      if float(tmp[1]) >= 1.1 and float(tmp[2]) <= 150.0: 
#      if float(tmp[1]) <= 160.0: 
        x.append(float(tmp[1]))
        y.append(float(tmp[2]))
        z1.append(float(tmp[3]))
        z2.append(float(tmp[4]))
        z3.append(float(tmp[5]))

z2rel = []
for i in range(len(z2)):
  z2rel.append((z2[i] - min(z2))*627.5095)
z3rel = []
for i in range(len(z3)):
  z3rel.append((z3[i] - min(z3))*627.5095)

xi = np.linspace(min(x),max(x))
yi = np.linspace(min(y),max(y))
xg, yg = np.meshgrid(xi,yi)

xyarr = np.array( list( zip(x,y) ) ) 
z1arr = np.array( z1 )
z2arr = np.array( z2rel )
z3arr = np.array( z3rel )


z1g = griddata(xyarr, z1arr, (xg,yg), method='cubic')
z2g = griddata(xyarr, z2arr, (xg,yg), method='cubic')
z3g = griddata(xyarr, z3arr, (xg,yg), method='cubic')

# Adjust cmap for easy visulazion of seem
cmap = cm.get_cmap('seismic')
shifted_cmap = shiftedColorMap(cmap, midpoint=0.375, name='shifted')

# Set number of contours
ncontours = 20

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
#af.set_title('Difference Potential for Triplet/Singlet')
af.set_xlabel('N--O Distance (Ang.)')
af.set_ylabel('N-N-O Angle (Deg.)')

# Plot the contours for the difference potential
#afcontour = af.contour(xg, yg, z1g, ncontours, cmap=shifted_cmap)
afcontourf = af.contourf(xg, yg, z1g, ncontours, cmap=shifted_cmap)

# Plot the colorbars
afpcolor = af.pcolor(xg, yg, z1g, cmap = shifted_cmap)
cbar1 = plt.colorbar(afpcolor, orientation='horizontal', shrink=0.8)
cbar1.set_label('E(trip)-E(sing) (kcal/mol)')

# Plot the triplet contours
bfcontour = af.contour(xg, yg, z2g, ncontours, colors='black')

# Place points for various points of interest; place legend for these points
#af.plot([1.71],[152.0], color='green', marker='o', markersize=14)
#af.plot([1.69],[145.0], color='green', marker='o', markersize=14)

fig.set_size_inches(16,9)
fig.savefig(outputfilename,dpi=300)

