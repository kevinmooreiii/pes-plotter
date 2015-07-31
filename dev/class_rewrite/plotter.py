"""
  This Class handles the set-up and creation of the plot to be generated.
  All of the parameters for the plot are stored here.
  Additionally, it handles placing all of the objects onto the plot.
"""
#from input_processor import Input_Processor
from molecule import Molecule
import matplotlib.pyplot as plt

class ThePlot:
    """ Handles options of the entire plot created, not specific to a single molecule. """

    def __init__(self, num_ground, max_energy, min_energy):
      self.name = 'pes.pdf'
      self.width = 16
      self.height = 9
      self.dpi = 1000   
      #self.x_axis_label = 'Reaction Coordinate' # Not used 
      self.x_axis_extension = 1.5
      self.x_axis_max, self.x_axis_min = self.set_x_axis_limits(num_ground) 
      self.y_axis_label = 'Relative Energy (kcal/mol)'
      self.y_axis_min_extension = 2.5
      self.y_axis_max_extension = 2.5
      self.y_axis_max, self.y_axis_min = self.set_y_axis_limits(max_energy, min_energy)

    def set_x_axis_limits(self, num_ground):
      """ Determine the maximum of the y limits. """

      x_axis_min = 0.0
      x_axis_max = num_ground + self.x_axis_extension # Need to take account other spacing

      return x_axis_max, x_axis_min
    

    def set_y_axis_limits(self, max_energy, min_energy):
      """ Determine the maximum of the y limits. """

      y_axis_min = min_energy - self.y_axis_min_extension
      y_axis_max = max_energy + self.y_axis_max_extension

      return y_axis_max, y_axis_min


    def gen_plot_axes(self):
        """ Makes the axes with the parameters computed earlier. """

        plt.axes(frameon=False)
        plt.axvline(0, self.y_axis_min, self.y_axis_max, color='k')
        plt.tick_params(which='both', bottom='off', top='off', right='off', labelbottom='off')
        plt.xlim(self.x_axis_min, self.x_axis_max)
        plt.ylim(self.y_axis_min, self.y_axis_max)
        plt.ylabel(self.y_axis_label)

        return None

    def plt_molecule_lines(self, molec_dict, min_energy, max_energy):
        """ Plot the lines that correspond to the molecular species. """
   
        # Loop thorugh the molecule dictionary
        for molecule_name, molecule in molec_dict.items():      
            mid_line = molecule.calc_midpoint(molecule.x1, molecule.x2)
            energy_shift, name_shift = molecule.vert_shift_name_and_energy(min_energy, max_energy)

            plt.plot([molecule.x1, molecule.x2], [molecule.energy, molecule.energy],
                     color=molecule.linecolor, lw=molecule.linewidth, linestyle='-')
            plt.text(mid_line, energy_shift, molecule.energy, weight='bold', horizontalalignment='center',
                     fontsize=molecule.energy_font_size)
            plt.text(mid_line, name_shift, molecule.name, weight='bold', horizontalalignment='center',
                     fontsize=molecule.name_font_size)

    def plt_connector_lines(self, connector_dict):
        """ Plot the lines that connect the species lines showing establishing a relationship of two molecular species
            in a reaction mechanism.
        """
    
        for key, connector in connector_dict.items():      
            plt.plot([connector.x1, connector.x2], [connector.y1, connector.y2], color=connector.linecolor,
                     lw=connector.linewidth, linestyle=connector.linestyle)
    
        return None
    
    
    def create_pdf(self):
        """ Creates the outgoing plot in the format requested by the user. """
    
        fig = plt.gcf()
        fig.set_size_inches(self.width, self.height)
        fig.savefig(self.name, dpi=self.dpi)
    
        return None




