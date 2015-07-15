
### Matplotlib 2-D plot generator
### Kevin Moore - Center for Computational Chemistry
### Last Edited June 18, 2015

import sys
import os
import numpy
from pylab import *
import matplotlib.pyplot as plt

### BEGIN FUNCTION DECLARATIONS ###

def parse_input(inputfilename):
  """ Open in the input file and store the neccessary variables. """

  # Read in all the lines of the file and store in a list
  with open(inputfilename,'r') as infile:
    content = infile.readlines()

  # Store the Basic plot specifications as well as options in a dictionary
  plot_specs = {}
  plot_specs['Title'] = content[0].strip()
  plot_specs['X-axis Label'] = content[1].strip()
  plot_specs['Y-axis Label'] = content[2].strip()
  plot_specs['X-axis Min'] = float(content[3].strip().split()[0])
  plot_specs['X-axis Max'] = float(content[3].strip().split()[1])
  plot_specs['Y-axis Min'] = float(content[3].strip().split()[2])
  plot_specs['Y-axis Max'] = float(content[3].strip().split()[3])
  plot_specs['Special Options'] = 'dog' 
  
      
  # To generate multiple plots, we need to know where each data section begins and ends in a list
  sections = {
    'Number': 0,
    'Start Lines': [],
    'End Lines': [],
    'Plot Start': 0,
    'Plot End': 0
  }
   

  # Loop through content of input file to find the lines where all sections begin and end 
  for i in range(0,len(content)):
    if '$start' in content[i]:
      sections['Number'] = sections['Number'] + 1 
      sections['Start Lines'].append(int(i + 1))
    if '$end' in content[i]:
      sections['End Lines'].append(int(i - 1))
    if '$plot' in content[i]:
      sections['Plot Start'] = i + 1
  
  # Last element of endlines may contain an extra $end if a $plot section is included 
  if sections['Plot Start'] != 0: 
    sections['Plot End'] = sections['End Lines'][-1]
    del sections['End Lines'][-1]


  # Rerun through content to parse through the options block; starting scan at final location of $end in file
  special_options = {
    'Legend': [ 'upper right', 10 ],                # [0] = legend location, [1] = legend size
    'HorizLine': [ 0, 1, 'k', False ],              # [0] = y-coordinate, [1] = linewidth, [2] = linecolor, [3] = bool to determine  
    'Reverse': False,                               # Determine whether to reverse the order of the points plotted
    'Point Labels': [ 'Label', [0.0,0.0], [0,0] ],  # [0] = Point Label, [1] = Coord where arrow points, [2] = Coord arrow originates
    'Every Other': [ False, 2 ]                     # Skip over a certain number of points in the plot
  } 

  for i in range(sections['Plot Start'], sections['Plot End']+1):
    if '$end' in content[i]:
      break
    else:
      tmp = content[i].strip().split()
      special_options[str(tmp[0])] = tmp[1:] 
  else:
    pass

  return plot_specs, sections


def generate_lists_for_each_plot(inputfilename, **sections):
  """ Create a list to hold all the other lists for the plot information """

  # Read in all the lines of the file and store in a list
  with open(inputfilename,'r') as infile:
    content = infile.readlines()
 
  # Break up each set of data and store in their respective
  coord = [[]] * sections['Number']
  energy = [[]] * sections['Number']
  for i in range(0, sections['Number']):
    for j in range(sections['Start Lines'][i],sections['End Lines'][i]):
      coord[i].append(content[j].strip().split()[0])
      energy[i].append(content[j].strip().split()[1])

  return coord, energy


def create_options(opts):
  """ Create variables to store the options for the plot. """

  #if 'legend' in data[-1]:
  #  plt.legend(loc='lower left', prop={'size':10})

  #if 'horiz' in data[-1]:
  #  plt.axhline(y=0, linewidth=1, color='r')
  #  plt.axhline(y=energy[-1], linewidth=1, color='m')
  #  plt.text(coord[0]+0.1, energy[-1] + 0.1, energy[-1], weight='bold', horizontalalignment='left')

  #if 'dashzero' in data[-1]:
  #  plt.axhline(y=0, linewidth=1, color='k')#, ls='dashed')

  #if 'lrp' in data[-1]:
  #  plt.annotate('C5', xy=(coord[0],energy[0]), xytext=(coord[0]-0.1,1.0), arrowprops=dict(arrowstyle='->'))
  #  plt.annotate('C7', xy=(coord[-1],energy[-1]), xytext=(45,energy[-1]), arrowprops=dict(arrowstyle='->'))
  #  plt.annotate('TS???', xy=(37,max(energy)), xytext=(37,(max(energy)+0.2)), arrowprops=dict(arrowstyle='->'))

  #if '#' not in data[3]:
  #  plt.xlim(x1,x2)
  #  plt.ylim(y1,y2)
  #
  ##pnt.set_clip_on(False)

  return None

def energy_converter(energy, **plot_specs):
  """ Determine units of the energy """
  
  min_energy = min(energy)
  if 'rel' in plot_specs['Special Options']:
    for i in range(0, len(energy)):
      for j in range(0, len(energy[i])):
        energy[i][j] = ( energy[i][j] - min_energy ) 
    return energy
  elif 'kcal' in plot_specs['Special Options']:
    for i in range(0,len(energy)):
      for j in range(0,len(energy[i])):
        energy[i][j] = energy[i][j] * 627.5095
    return energy 
  elif 'kcalrel' in plot_specs['Special Options']: 
    for i in range(0,len(energy)):
      for j in range(0,len(energy[i])):
        energy[i][j] = ( energy[i][j] - min_energy ) * 627.5095 
    return energy
  else:
    pass 


def create_plot(coord, energy):
  """ Take all the information and options obtained above and create a plot. """

  fig = plt.figure() 
  gr = fig.add_subplot(111)

  plt.title(plot_specs['Title'], y = 1.06)
  plt.xlabel(plot_specs['X-axis Label'])
  plt.xlim(coord[0], coord[-1])
  #plt.xticks(np.arange(0,coord[-1],0.1))
  plt.ylabel(plot_specs['Y-axis Label'])
  plt.ylim(-1, max_energy)
  #plt.yticks(np.arange(0,coord[-1],0.25))

  if i == 0:
    plt.plot(coord, energy, 'mo--', label='Electrostatic')
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
  
  return 

### END FUNCTION DECLARATIONS

inputfile = sys.argv[1]

plot_specs, sections = parse_input(inputfile)
coord,energy = generate_lists_for_each_plot(inputfile, **sections)
#energy_converter(energy, **plot_specs)
#create_options(plot_specs['Special Options'])
create_plot(coord,energy)#, **plot_specs)

# Save the neccessary pdf and open it with gnome terminal
plt.savefig('pes.pdf')
os.system('gnome-open pes.pdf')


# ---

### Error messages for input
# Check various error possibilities
#if len(sections["Start Lines"]) != len(sections["End Lines"]):
#  raise ValueError('There is a mismatched $start or $end')
#if '$start' in content[0:6]:
#  raise ValueError('$start appearing too early in file. One or more required plot option lines are missing')
#if plot_specs["Special Options"] = content[4].strip().split():
#  raise ImportError('The keyword x does not represent a feature in this program')
#if len(content[3].strip().split()) != 4:
#  raise ValueError('The specifications of the x and y axis limits are wrong')



