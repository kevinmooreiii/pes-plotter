#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import pyparsing
import numpy as np
import sys

### FUNCTIONS FOR PLOTTING CERTAIN 3D Images ###

def plot_one_graph(choice1, x_axis_name, y_axis_name, z_axis_name, choice, x, y, z, xi, yi, zi, colormap, outputfilename):

  fig = plt.figure()

  if choice1 == 'surface' or choice1 == 'scatter':
    af = fig.add_subplot(111, projection='3d')
    af.set_zlabel(z_axis_name)
  else:
    af = fig.add_subplot(111)
  
  af.set_xlabel(x_axis_name)
  af.set_ylabel(y_axis_name)

  if choice1 == 'surface':
    cmap = cm.get_cmap(colormap)  
    plot_surface(af, x, y, z, cmap)
  elif choice1 == 'scatter':
    plot_scatter(af, x, y, z)
  elif choice1 == 'contour':
    cmap = cm.get_cmap(colormap)  
    plot_contour(af, xi, yi, zi, cmap)
  elif choice1 == 'pcolor':
    cmap = cm.get_cmap(colormap)  
    plot_pcolor(af, xi, yi, zi, cmap)

  create_plot(outputfilename)

  return None

def plot_two_graphs(choice1, choice2, x_axis_name, y_axis_name, z_axis_name, choice, x, y, z, xi, yi, zi, colormap, outputfilename,a):

  fig = plt.figure()

  if choice1 == 'surface' or choice1 == 'scatter':
    af = fig.add_subplot(121, projection='3d')
    af.set_zlabel(z_axis_name)
  else:
    af = fig.add_subplot(122)
  
  af.set_xlabel(x_axis_name)
  af.set_ylabel(y_axis_name)

  if choice1 == 'surface':
    cmap = cm.get_cmap(colormap)  
    plot_surface(af, x, y, z, cmap)
  elif choice1 == 'scatter':
    plot_scatter(af, x, y, z)
  elif choice1 == 'contour':
    cmap = cm.get_cmap(colormap)  
    plot_contour(af, xi, yi, zi, cmap,a)
  elif choice1 == 'pcolor':
    cmap = cm.get_cmap(colormap)  
    plot_pcolor(af, xi, yi, zi, cmap)

  if choice2 == 'surface' or choice2 == 'scatter':
    bf = fig.add_subplot(121, projection='3d')
    bf.set_zlabel(z_axis_name)
  else:
    bf = fig.add_subplot(122)
  
  bf.set_xlabel(x_axis_name)
  bf.set_ylabel(y_axis_name)

  if choice2 == 'surface':
    cmap = cm.get_cmap(colormap)  
    plot_surface(bf, x, y, z, cmap,a)
  elif choice2 == 'scatter':
    plot_scatter(bf, x, y, z)
  elif choice2 == 'contour':
    cmap = cm.get_cmap(colormap)  
    plot_contour(bf, xi, yi, zi, cmap)
  elif choice2 == 'pcolor':
    cmap = cm.get_cmap(colormap)  
    plot_pcolor(bf, xi, yi, zi, cmap)

  create_plot(outputfilename)

  return None

def plot_surface(sub, x, y, z, cmap,a):

  sub.plot_trisurf(x, y, z, cmap = cmap, linewidth = 0.2)
  #plt.plot(a,'yo')
  
  return None

def plot_scatter(sub, x, y, z):

  sub.scatter(x, y, z, s = 10, c = 'b')

  return None

def plot_contour(sub, xi, yi, zi, cmap,a):

  sub_contour = sub.contour(xi, yi, zi, cmap = cmap)
  sub_contourf = sub.contourf(xi, yi, zi, cmap = cmap)
  #plt.plot(a,'yo')
  plt.colorbar(sub_contourf, orientation='horizontal', shrink=0.8)

  return None

def plot_pcolor(sub, xi, yi, zi, cmap):

  sub_pcolor = sub.pcolor(xi, yi, zi, cmap = cmap)
  plt.colorbar(sub_pcolor, orientation='horizontal', shrink=0.8)

  return None

def create_plot(outputfilename):

  fig = plt.gcf()
  fig.set_size_inches(16,9)
  fig.savefig(outputfilename,dpi=300)

  return None

### END OF FUNCTION DECLARATIONS

# Open the file and read in the basic plot paramters.

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

with open(inputfilename,'r') as infile:
  data = infile.readlines()

plot_title = data[0].strip()
x_axis_name = data[1].strip()
y_axis_name = data[2].strip()
z_axis_name = data[3].strip()
if '#' not in data[4].strip():
  axes_scale = data[4].strip().split()
  x1 = float(axes_scale[0])
  x2 = float(axes_scale[1])
  y1 = float(axes_scale[2])
  y2 = float(axes_scale[3])
if '#' not in data[5].strip():
  colormap =  data[5].strip()
choice = data[6].strip().split()

# Put content of input file into various list to be altered later.
x = []
y = []
z = []

for i in range(9, len(data)):
  if '$end' not in data[i]:
    tmp = data[i].strip().split()
#    x.append(float(tmp[0]))
#    y.append(float(tmp[1]))
#    z.append(float(tmp[2]))
    if float(tmp[1]) >= 2.3 and float(tmp[1]) <= 3.4 and float(tmp[0]) >= 140:
#    if float(tmp[2]) <= 0.7:
      x.append(float(tmp[0]))
      y.append(float(tmp[1]))
      z.append(float(tmp[2]))

g = z.index(min(z))
a = [x[g],y[g]]

print(g)
print(a)

# Format lists for plotting

xi = np.linspace(min(x),max(x))
yi = np.linspace(min(y),max(y))
zi = mlab.griddata(x, y, z, xi, yi)
#xim, yim = np.meshgrid(xi,yi)

# Call the functions to generate the plots

if len(choice) == 1:
  plot_one_graph(choice[0], x_axis_name, y_axis_name, z_axis_name, choice, x, y, z, xi, yi, zi, colormap, outputfilename)
elif len(choice) == 2:
  plot_two_graphs(choice[0], choice[1], x_axis_name, y_axis_name, z_axis_name, choice, x, y, z, xi, yi, zi, colormap, outputfilename,a)
else:
  print('Plot choice invalid. Only 1 or 2 is allowed.')
