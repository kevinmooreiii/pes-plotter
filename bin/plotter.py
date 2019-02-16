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


def buildmesh(x, y, nlin):
    """ Build the x,y mesh
    """

    xi = np.linspace(min(x),max(x),nlin)
    yi = np.linspace(min(y),max(y),nlin)
    xg, yg = np.meshgrid(xi,yi)

    return xg, yg


def buildgrid(x, y, z, xg, yg):
    """ Builds a grid for a set of points
    """

    # Place into arrays
    xy_arr = np.array(list(zip(x,y))) 
    z1_arr = np.array(z)
    
    # Build the grid
    zgrid = griddata(xy_arr, z_arr, (xg,yg), method='cubic')

    return zgrid


def determine_zero_contour_pts(contour): 
    """ Finds the x,y points on the zero contour levels and then
        uses interpolation to find the z values associated with the x,y points
    """
    
    xc, yc = [], []
    for contour in afcontour.collections:
        for path in contour.get_paths():
            data = path.vertices
            xc.append(data[:,0])
            yc.append(data[:,1])

    return xc, yc


def interp_zero_contour_vals(x, y, z, xc, yc): 
    """ Finds the x,y points on the zero contour levels and then
        uses interpolation to find the z values associated with the x,y points
    """
    # Place into arrays
    xy_arr = np.array(list(zip(x,y))) 
    z1_arr = np.array(z)

    # Interpolate the new set of points to get the z-values
    zint = griddata(xy_arr, z_arr, (xc,yc), method='cubic')
    
    return zint

##################################3


# Get the input data file and output plot PDF
inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

# Open the input file and read in the values
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
      if float(tmp[1]) <= 160.0: 
        x.append(float(tmp[1]))
        y.append(float(tmp[2]))
        z1.append(float(tmp[3]))
        z2.append(float(tmp[4]))
        z3.append(float(tmp[5]))
        r.append(float(tmp[0]))

z2rel = []
for i in range(len(z2)):
  z2rel.append((z2[i] - min(z2))*627.5095)
z3rel = []
for i in range(len(z3)):
  z3rel.append((z3[i] - min(z3))*627.5095)


# Obtain the grids for plotting
xg, yg = buildmesh(x, y, 50)
z1g = buildgrid(x, y, z1, xg, yg)
z2g = buildgrid(x, y, z2rel, xg, yg)
z3g = buildgrid(x, y, z3rel, xg, yg)

# Adjust cmap for easy visulazion of seem
cmap = cm.get_cmap('seismic')
zero_point = (-1.0*min(z1g)/(min(z1g)+max(x1g)))
shifted_cmap = shiftedColorMap(cmap, midpoint=zero_point, name='shifted')

# Set number of contours
ncontours = 75

# Set fonts
font = {'family' : 'normal',
#       'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)

# Create plot
fig = plt.figure()
af = fig.add_subplot(111)

# Set titles and axes labels
af.set_xlabel('N--O Distance (Ang.)')
af.set_ylabel('N-N-O Angle (Deg.)')

# Plot the contours for the difference potential
dif_contourf = af.contourf(xg, yg, z1g, ncontours, cmap=shifted_cmap)
dif_contour = af.contour(xg, yg, z1g, ncontours, levels=[0], color='black')

# Plot the colorbars for the difference
dif_pcolor = af.pcolor(xg, yg, z1g, cmap = shifted_cmap)
cbar1 = plt.colorbar(afpcolor, orientation='horizontal', shrink=0.8)
cbar1.set_label('E(trip)-E(sing) (kcal/mol)')

# Plot the triplet contours
trip_contour = af.contour(xg, yg, z2g, ncontours, colors='black')

# Place points for various points of interest; place legend for these points
# af.plot([1.45945826],[118.55168496], color='green', marker='o', markersize=14, label='T-SP')
# af.legend(loc="lower left", fontsize=20, markerscale=1.5, framealpha=1.0)

# Plot the contours for the difference potential
# afcontourf = af.contourf(xg, yg, z1g, ncontours, cmap=cmap)
# afpcolor = af.pcolor(xg, yg, z1g, cmap=cmap)
# cbar1 = plt.colorbar(afpcolor, orientation='horizontal', shrink=0.8)
# cbar1.set_label('H_SO (cm-1)')

# Write the interpolated values to a file
xc_zero, yc_zero = determine_zero_contour_pts(dif_contour): 
for i in range(len(xc_zero)):
    zint = interp_zero_contour_vals(x, y, z2rel, xc_zero[i], yc_zero[i]): 
    with open('interp'+str(i+1)+'.dat', 'w') as gridfile:
        for j in range(len(zint)):
            gridfile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xc_zero[i][j], yc_zero[i][j], zint[j]))

# Save the figure
fig.set_size_inches(16,9)
fig.savefig(outputfilename,dpi=300)

