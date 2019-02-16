""" 
Contour libs. 
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-31"

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors
from mpl_toolkits.mplot3d import Axes3D
#import pyparsing
import numpy as np
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

# example
#z2_est = Estimation(np.array(x), np.array(y), np.array(z2rel))
#with open('seam_e.dat', 'w') as efile:
#    for i in range(len(xv[1])):
#        zv = z2_est.estimate(xv[1][i], yv[1][i])
#        efile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zv))





