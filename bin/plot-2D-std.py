#!/usr/bin/env python

import os
from pylab import *
import matplotlib.pyplot as plt
import numpy


with open('input.dat','r') as infile:
  coord = []
  energy = []
  data = infile.readlines()

plot_title = data[0].strip()
x_axis_name = data[1].strip()
y_axis_name = data[2].strip()
if '#' not in data[3].strip():
  axes_scale = data[3].strip().split()
  x1 = float(axes_scale[0])
  x2 = float(axes_scale[1])
  y1 = float(axes_scale[2])
  y2 = float(axes_scale[3])

sec_count = 0
start_sec = []
end_sec = []

for i in range(5, len(data)):
  if data[i].strip() != '':
    if '$start' in data[i]:
      sec_count = sec_count + 1
      start_sec.append(i + 1)
    if '$end' in data[i]:
      end_sec.append(i - 1)

fig = plt.figure() 
gr = fig.add_subplot(111)

for i in range(0, sec_count):
  coord = []
  energy = [] 
  for j in range(start_sec[i], end_sec[i]):
    tmp = data[j].strip().split()
    if 'bohr' in data[-1]:
      coord.append(float(tmp[0]) * 0.529177)
    else:
      coord.append(float(tmp[0]))
    energy.append(float(tmp[1]))
  min_energy = min(energy)
  for j in range(len(energy)):
    if 'noscale' in data[-1]:
      pass
    elif 'inkcal' in data[-1]:
      energy[j] = ( energy[j] - min_energy ) 
    else:
      energy[j] = ( energy[j] - min_energy ) * 627.5095

  max_energy = max(energy)
  if i == 0:
    plt.plot(coord, energy, 'mo--', label='Electrostatic')
    #plt.plot(coord, energy, 'k--')
  if i == 1:
    plt.plot(coord, energy, 'bo--', label='Exchange')
  if i == 2:
    plt.plot(coord, energy, 'go--', label='Induction')
  if i == 3:
    plt.plot(coord, energy, 'ro--', label='Dispersion')
  if i == 4:
    plt.plot(coord, energy, 'ko--', label='Total SAPT2+3')
  if i == 5:
    plt.plot(coord, energy, 'go--')

plt.title(plot_title, y = 1.06)
plt.xlabel(x_axis_name)
plt.xlim(coord[0], coord[-1])
#plt.xticks(np.arange(0,coord[-1],0.1))
plt.ylabel(y_axis_name)
plt.ylim(-1, max_energy)
#plt.yticks(np.arange(0,coord[-1],0.25))
if 'legend' in data[-1]:
  plt.legend(loc='lower left', prop={'size':10})
if 'horiz' in data[-1]:
  plt.axhline(y=0, linewidth=1, color='r')
  plt.axhline(y=energy[-1], linewidth=1, color='m')
  plt.text(coord[0]+0.1, energy[-1] + 0.1, energy[-1], weight='bold', horizontalalignment='left')
if 'dashzero' in data[-1]:
  plt.axhline(y=0, linewidth=1, color='k')#, ls='dashed')
if 'lrp' in data[-1]:
  plt.annotate('C5', xy=(coord[0],energy[0]), xytext=(coord[0]-0.1,1.0), arrowprops=dict(arrowstyle='->'))
  plt.annotate('C7', xy=(coord[-1],energy[-1]), xytext=(45,energy[-1]), arrowprops=dict(arrowstyle='->'))
  plt.annotate('TS???', xy=(37,max(energy)), xytext=(37,(max(energy)+0.2)), arrowprops=dict(arrowstyle='->'))
if '#' not in data[3]:
  plt.xlim(x1,x2)
  plt.ylim(y1,y2)
#pnt.set_clip_on(False)
plt.savefig('pes.pdf')


os.system('evince pes.pdf')
