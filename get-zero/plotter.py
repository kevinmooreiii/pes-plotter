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

### estimator ###

class Estimation():
    def __init__(self,datax,datay,dataz):
        self.x = datax
        self.y = datay
        self.v = dataz

    def estimate(self,x,y,using='ISD'):
        """
        Estimate point at coordinate x,y based on the input data for this
        class.
        """
        if using == 'ISD':
            return self._isd(x,y)

    def _isd(self,x,y):
        d = np.sqrt((x-self.x)**2+(y-self.y)**2)
        if d.min() > 0:
            v = np.sum(self.v*(1/d**2)/np.sum(1/d**2))
            return v
        else:
            return self.v[d.argmin()]


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

z2rel = []
for i in range(len(z2)):
  z2rel.append((z2[i] - min(z2))*627.5095)
z3rel = []
for i in range(len(z3)):
  z3rel.append((z3[i] - min(z3))*627.5095)


# Build the x,y mesh
xi = np.linspace(min(x),max(x),100)
yi = np.linspace(min(y),max(y),100)
xg, yg = np.meshgrid(xi,yi)

# Place into arrays
xy_arr = np.array(list(zip(x,y))) 
z_arr = np.array(z1)

# Build the grid
z1g = griddata(xy_arr, z_arr, (xg,yg), method='cubic')

# Adjust cmap for easy visulazion of seem
cmap = cm.get_cmap('seismic')
shifted_cmap = shiftedColorMap(cmap, midpoint=0.310, name='shifted')

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
#af.set_title('Difference Potential for Triplet/Singlet')
af.set_xlabel('N--O Distance (Ang.)')
af.set_ylabel('N-N-O Angle (Deg.)')

# Plot the contours for the difference potential
afcontourf = af.contourf(xg, yg, z1g, ncontours, cmap=shifted_cmap)
afcontour = af.contour(xg, yg, z1g, ncontours, levels=[0], color='black')

# Plot the colorbars
afpcolor = af.pcolor(xg, yg, z1g, cmap = shifted_cmap)
cbar1 = plt.colorbar(afpcolor, orientation='horizontal', shrink=0.8)
cbar1.set_label('E(trip)-E(sing) (kcal/mol)')

# Plot the triplet contoursi
#bf = fig.add_subplot(122)
#bfcontour = bf.contourf(xg, yg, z2g, ncontours, cmap='autumn')
#bfpcolor = bf.pcolor(xg, yg, z2g, cmap= 'autumn') 
#cbar2 = plt.colorbar(bfpcolor, orientation='horizontal', shrink=0.8)
#cbar2.set_label('E(trip)-E(sing) (kcal/mol)')

xv = []
yv = []
for contour in afcontour.collections:
    for path in contour.get_paths():
        data = path.vertices
        xv.append(data[:,0])
        yv.append(data[:,1])
        #plt.plot(data[:,0], data[:,1],
        #         color='black',  linewidth=c.get_linewidth()[0])

# energy
#zint = griddata(xyarr, z2arr, (xv[1],yv[1]), method='cubic')
#with open('griddata_e', 'w') as gridfile:
#    for i in range(len(zint)):
#        gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zint[i]))
#
#
## Set Estimate object
#z2_est = Estimation(np.array(x), np.array(y), np.array(z2rel))
#with open('seam_e.dat', 'w') as efile:
#    for i in range(len(xv[1])):
#        zv = z2_est.estimate(xv[1][i], yv[1][i])
#        efile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zv))
#with open('trip_e.dat', 'w') as tripfile:
#    for i in range(len(x)):
#        tripfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(x[i], y[i], z2rel[i]))
#z2_est = Estimation(np.array(x), np.array(y), np.array(r))
#with open('seam_r.dat', 'w') as efile:
#    for i in range(len(xv[1])):
#        zv = z2_est.estimate(xv[1][i], yv[1][i])
#        efile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zv))
#with open('trip_r.dat', 'w') as tripfile:
#    for i in range(len(x)):
#        tripfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(x[i], y[i], r[i]))
    
# Save the figure
fig.set_size_inches(16,9)
fig.savefig(outputfilename,dpi=300)

