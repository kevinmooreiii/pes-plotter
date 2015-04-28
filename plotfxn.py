from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
import pyparsing
from specs import Input
from specs import Molecule
from specs import PlotParameter
from specs import OutFileParameter


def format_axes():
    """ Format the x- and y-axes. Default scaling factors defined in llama.py are used, unless user specifies a
        value in the input file.
    """

    plt.axes(frameon=False)
    plt.axvline(0, PlotParameter.y_axis_bot_lim, PlotParameter.y_axis_top_lim, color='k')
    plt.tick_params(which='both', bottom='off', top='off', right='off', labelbottom='off')
    plt.xlim(0, PlotParameter.x_axis_right_lim)
    plt.ylim(PlotParameter.y_axis_bot_lim, PlotParameter.y_axis_top_lim)
    plt.ylabel(PlotParameter.y_axis_label)


def generate_xcoords():
    """ Generates a list of the coordinates for the left and right endpoints of each of the horizontal lines
        corresponding to a molecular species.
    """

    for i in range(0, Molecule.ground_species_count):
        tmp1 = (PlotParameter.species_line_spacing * i) + 0.25
        tmp2 = tmp1 + PlotParameter.species_line_length
        Molecule.left_endpt.append(tmp1)
        Molecule.right_endpt.append(tmp2)

    for i in range(0, Molecule.excited_species_count):
        tmp1 = Molecule.left_endpt[Molecule.excited_state[i] - 1]
        tmp2 = Molecule.right_endpt.append[Molecule.excited_state[i] - 1]
        Molecule.left_endpt.append(tmp1)
        Molecule.right_endpt.append(tmp2)

    return None


def plt_spec_lines():
    """ Plot the lines that correspond to the molecular species. """

    for i in range(0, Molecule.species_count):

        mid_line = (Molecule.right_endpt[i] + Molecule.left_endpt[i]) / 2
        shift1 = Molecule.energy[i] - PlotParameter.energy_vshift
        shift2 = Molecule.energy[i] + PlotParameter.name_vshift

        plt.plot([Molecule.left_endpt[i], Molecule.right_endpt[i]], [Molecule.energy[i], Molecule.energy[i]],
                    color=PlotParameter.species_line_color, lw=PlotParameter.species_line_width, linestyle='-')
        plt.text(mid_line, shift1, Molecule.energy[i], weight = 'bold', horizontalalignment='center',
                    fontsize=PlotParameter.energy_font_size)
        plt.text(mid_line, shift2, Molecule.name[i], weight='bold', horizontalalignment='center',
                    fontsize=PlotParameter.name_font_size)


def plt_connecting_lines():
    """ Plot the lines that connect the species lines showing establishing a relationship of two molecular species
        in a reaction mechanism.
    """

    for i in range(0, Molecule.connection_count):

        tmp1 = Molecule.right_endpt[Molecule.left_connection[i] - 1]
        tmp2 = Molecule.left_endpt[Molecule.right_connection[i] - 1]
        tmp3 = Molecule.energy[Molecule.left_connection[i] - 1]
        tmp4 = Molecule.energy[Molecule.right_connection[i] - 1]

        plt.plot([tmp1, tmp2], [tmp3, tmp4], color=PlotParameter.connection_line_color,
                    lw=PlotParameter.connection_line_width, linestyle='--')

    return None

def create_pdf():
    """ Creates the outgoing plot in the format requested by the user. """

    fig = plt.gcf()
    fig.set_size_inches(OutFileParameter.width, OutFileParameter.height)
    fig.savefig(OutFileParameter.name, dpi=OutFileParameter.dpi)
    #plt.show()

    return None


def print_outgoing_msg():
    """ Prints a message which signals successful completion of program as well as program information. """

    print("""
      A LOVELY little potential energy surface has been successfully generated by the
      Lim, Launder, and Moore auto-plotter (LLAMA) vers. 0.3!

      ############################################################################### 
         LLAMA 0.3 written By:
         [a] Andrew Launder and Kevin Moore
             Center for Computational Quantum Chemistry, 
             Dept. of Chemistry, Univ. of Georgia, Athens, GA, United States
         [b] Victoria Lim
             Dept. of Chemistry, Belmont University, Nashville, TN, United States
      ###############################################################################

      Thank you for very much for plotting with us today! Please do so again soon!
          """)

    return None

### Funcion that needs to be added into the program ###

#def plot_gr_state_images():
#  """ Upload images for each species and place them in plot above corresponding species line. Current memory issues restrict this function to the plotting of only 3-5 images. """  
      #img = plt.imread(IMNAME[i])
      #plt.imshow(img, aspect = 'auto', extent = (x1[i],x2[i],Energy[i],Energy[i] + text_vert_shift * 3))

#  return None


