
# LLAMA version 2.0
# Authors: Andrew Launder, Victoria Lim, and Kevin Moore
# Center for Computational Quantum Chemistry (CCQC)

# Last updated on 10/07/2014 by Kevin Moore.

# Program designed to plot the 1-D potential energy surface of a reaction coordinate, 
# using as input, the relative energies for each species in the reaction. All plots
# are generated using the matplotlib module of Python. llama.py uses to read and process
# the input file - plotting done with functions listed in plot_fxn.py

import os
import sys
import plotfxn as plot

# Print program header to screen.

print('''
  ##################################################### 
    Generation of Potential Energy Surfaces via LLAMA
    Andrew Launder, Victoria Lim, Kevin Moore
    Center for Computational Quantum Chemistry (CCQC)
  ##################################################### 
      ''')

# Check if command line input was entered correctly.

if len(sys.argv) != 2:
    print('Expecting input file as an argument')
    sys.exit()

if not os.path.exists(sys.argv[1]):
    print('Could not locate file: '+sys.argv[1])
    sys.exit()
else:
    print('Input file '+sys.argv[1]+' found. Opening file...\n\n')
    infile = open(sys.argv[1], 'r').readlines()
    print('Processing input...\n\n')

# Initialize variables for storing plotting information read from input file.

num = []
name = []
energy = []

ex_rel = []
ex_surf = []

con_cnt = 0

lft_connect = []
rgt_connect = []

img_num = []
img_name = []

tmp = ' '

# Initialize check variables which change based on input from the user.

check_energies = -1
check_excite = -1
check_image = -1
check_latex = -1

# Setting default values for formatting the plot axes.

y_top_ext = 2.5
y_bot_ext = 2.5
x_rgt_ext = 0.75
y_axis_label = 'Relative Energy (kcal/mol)'

# Setting default values for formatting the lines of the plot.

nm_vshift_fact = 0.04
en_vshift_fact = 0.04
sp_lin_len = 0.50
sp_lin_spc = 1.00
sp_lin_wid = 4.5
sp_lin_clr = 'k'
cn_lin_wid = 1.5
cn_lin_clr = 'k'
nm_fsize = 10
en_fsize = 10
ex_clr1 = 'b'
ex_clr2 = 'm'
ex_clr3 = 'g'
ex_clr4 = 'r'

# Setting default values for the parameters of the pdf output by the script.

pdf_width = 16
pdf_height = 9
pdf_dpi = 1000
pdf_name = 'pes.pdf'

# Store information of input file.

for i in range(0, len(infile)):
    if '$energies' in infile[i]:
      check_energies = 0
      for j in range(i + 1, len(infile)):
        if '#' not in infile[j]:
          if '$end' in infile[j]:
            break
          elif 'excite' not in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            num.append(int(tmp[0]))
            name.append(str(tmp[2]))
            energy.append(float(tmp[4]))
          else:
            check_excite = 0
            tmp = infile[j].lstrip().rstrip().split()
            num.append(int(tmp[0]))
            name.append(str(tmp[2]))
            energy.append(float(tmp[4]))
            ex_rel.append(int(tmp[8]))
            ex_surf.append(int(tmp[10]))
    if '$connect' in infile[i]:
      if 'numbers' in infile[i+1]:
        for j in range(i + 2, len(infile)):
          if '#' not in infile[j]:
            if '$end' in infile[j]:
              break
            else:
              con_cnt += 1
              tmp = infile[j].lstrip().rstrip().split()
              lft_connect.append(int(tmp[0]))
              rgt_connect.append(int(tmp[2]))
      elif 'names' in infile[i+1]:
        for j in range(i + 2, len(infile)):
          if '#' not in infile[j]:
            if '$end' in infile[j]:
              break
            else:
              con_cnt += 1
              tmp = infile[j].lstrip().rstrip().split()
              if check_excite == 0:
                for k in range(0, len(energy)):
                  if name[k] == tmp[0]:
                    lft_connect.append(int(num[k]))
                  if name[k] == tmp[2]:
                    rgt_connect.append(int(num[k]))
      else:
        print('Connect section formatted improperly.')
        sys.exit()
    if '$images' in infile[i]:
      check_energies = 0
      for j in range(i + 1, len(infile)):
        if '#' not in infile[j]:
          if '$end' in infile[j]:
            break
          else:
            check_image = 0
            tmp = infile[j].lstrip().rstrip().split()
            img_num.append(int(tmp[0]))
            img_name.append(str(tmp[2]))
    if '$plot_format' in infile[i]:
      for j in range(i + 1, len(infile)):
        if '#' not in infile[j]:
          if '$end' in infile[j]:
            break
          if 'y_top_ext' in infile[j]:  
            tmp = infile[j].lstrip().rstrip().split()
            y_top_ext = float(tmp[2])
          if 'y_bot_ext' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            y_bot_ext = float(tmp[2])
          if 'x_rgt_ext' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            x_rgt_ext = float(tmp[2])
          if 'y_axis_label' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            y_axis_label = str(tmp[2])
          if 'nm_vshift' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            nm_vshift_fact = float(tmp[2])
          if 'en_vshift' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            en_vshift_fact = float(tmp[2])
          if 'sp_lin_len' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            sp_lin_len = float(tmp[2])
          if 'sp_lin_spc' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            sp_lin_spc = float(tmp[2])
          if 'sp_lin_wid' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            sp_lin_wid = float(tmp[2])
          if 'sp_lin_clr' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            sp_lin_clr = str(tmp[2])
          if 'cn_lin_wid' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            cn_lin_wid = float(tmp[2])
          if 'cn_lin_clr' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            cn_lin_clr = str(tmp[2])
          if 'nm_fsize' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            nm_fsize = int(tmp[2])
          if 'en_fsize' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            en_fsize = int(tmp[2])
          if 'ex_clr1' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            ex_clr1 = str(tmp[2])
          if 'ex_clr2' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            ex_clr2 = str(tmp[2])
          if 'ex_clr3' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            ex_clr3 = str(tmp[2])
          if 'ex_clr4' in infile[j]:
            tmp = infile[j].lstrip().rstrip().split()
            ex_clr4 = str(tmp[2])
          if 'latex_text = on' in infile[j]:
            check_latex = -0
    if '$pdf' in infile[i]:
      for j in range(i + 1, len(infile)):
        if '#' not in infile[j]:
          if '$end' in infile[j]:
            break
          if 'width' in infile[j]:
            tmp = infile[j].lstrip.rstrip.split()
            pdf_width = int(tmp[2])
          if 'height' in infile[j]:
            tmp = infile[j].lstrip.rstrip.split()
            pdf_length = int(tmp[2])
          if 'name' in infile[j]:
            tmp = infile[j].lstrip.rstrip.split()
            pdf_name = str(tmp[2])
          if 'dpi' in infile[j]:
            tmp = infile[j].lstrip.rstrip.split()
            pdf_dpi = int(tmp[2])
        
# Check to see if neccessary sections are in the input file.  

if check_energies == -1:
  print('Expecting an $energies section.')
  sys.exit()
else:
  print('Energies sections found.\n\n')
  print('Storing input values and computing useful quantities for plotting...\n\n')


# Format input data and compute useful values to pass to plotting functions.

spc_count = len(energy)
ex_count = len(ex_rel)
gr_count = spc_count - len(ex_rel)

y_top = max(energy) + y_top_ext
y_bot = min(energy) - y_bot_ext
nm_shift = nm_vshift_fact * (max(energy) - min(energy))
en_shift = en_vshift_fact * (max(energy) - min(energy))

x_rgt = gr_count + x_rgt_ext

if check_latex == 0:
    for k in range(0, len(gr_name)):
        tmp = '$'+name[k]+'$'
        name[k] = tmp
    for k in range(0, len(ex_name)):
        tmp = '$'+name[k]+'$'
        name[k] = tmp

# Call functions to run matplotlib and create pdf of potential energy surface plot.

plot.format_axes(y_top, y_bot, x_rgt, y_axis_label)

lft_endpt, rgt_endpt = plot.generate_xcoords(gr_count, sp_lin_len, sp_lin_spc, ex_rel)

plot.plt_spec_lines(spc_count, lft_connect, rgt_connect, lft_endpt, rgt_endpt, energy, sp_lin_clr, sp_lin_wid, en_shift, en_fsize, nm_shift, name, nm_fsize)

plot.plt_connecting_lines(con_cnt, lft_connect, rgt_connect, lft_endpt, rgt_endpt, energy, cn_lin_clr, cn_lin_wid)

plot.create_pdf(pdf_width, pdf_height, pdf_name, pdf_dpi)

# Print outgoing messages to screen

print('\n\n------------------------------------------------------------------------------\n\n')
print('Everything seems to have gone hunky-dorey!!!\n\n') 
print('Please check the plot to see if you need to adjust parameters to get what you need.\n\n')
print('Thank you for plotting with us today! We hope you will do so again very soon!!!\n\n')




