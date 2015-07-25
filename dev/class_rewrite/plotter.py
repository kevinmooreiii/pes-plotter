"""
  This Class handles the set-up and creation of the plot to be generated.
  All of the parameters for the plot are stored here.
  Additionally, it handles placing all of the objects onto the plot.
"""

from molecule import Molecule

class ThePlot:
    """ Handles options of the entire plot created, not specific to a single molecule. """

    def __init__(self):
      self.plot_name = pes.pdf
      self.width = 16
      self.height = 9
      self.dpi = 1000   
      #self.x_axis_label = 'Reaction Coordinate' # Not used 
      self.x_axis_spacing = 1.00
      self.x_axis_extension = 0.75
      self.x_axis_min = 0.0
      self.x_axis_max = set_x_axis_limits() 
      self.y_axis_label = 'Relative Energy (kcal/mol)'
      self.y_axis_min_extension = 2.5
      self.y_axis_max_extension = 2.5
      self.y_axis_min, self.y_axis_max = set_y_axis_limits()

    def set_x_axis_limits(self, num_species_ground):
      """ Determine the maximum of the y limits. """

      x_axis_min = 0
      x_axis_max = num_species_ground - x_axis_max_extension

      return x_axis_min, x_axis_max
    

    def set_y_axis_limits(self):
      """ Determine the maximum of the y limits. """

      y_axis_min = min_energy - y_axis_min_extension
      y_axis_max = max_energy - y_axis_max_extension

      return y_axis_min, y_axis_max


    def gen_plot_axes(self):
        """ Makes the axes with the parameters computed earlier. """

        plt.axes(frameon=False)
        plt.axvline(0, self.y_axis_min, self.y_axis_max, color='k')
        plt.tick_params(which='both', bottom='off', top='off', right='off', labelbottom='off')
        plt.xlim(self.x_axis_min, self.x_axis_max)
        plt.ylim(self.y_axis_min, self.y_axis_max)
        plt.ylabel(self.y_axis_label)

        return None

    def plt_spec_lines(self, molec_dict):
        """ Plot the lines that correspond to the molecular species. """
    
        # Loop thorugh the molecule dictionary
        for molecule_name, molecule in molec_dict.items():      
            mid_point = Molecule.calc_midpoint(molecule.x1, molecule.x2)
            name_shift = Molecule.vert_shift_name(molecule.name_shift)
            energy_shift = Molecule.vert_shift_energy(molecule.energy_shift)
    
            plt.plot([Molecule.left_endpt[i], Molecule.right_endpt[i]], [Molecule.energy[i], Molecule.energy[i]],
                     color=PlotParameter.species_line_color, lw=PlotParameter.species_line_width, linestyle='-')
            plt.text(mid_line, shift1, Molecule.energy[i], weight='bold', horizontalalignment='center',
                     fontsize=PlotParameter.energy_font_size)
            plt.text(mid_line, shift2, Molecule.name[i], weight='bold', horizontalalignment='center',
                     fontsize=PlotParameter.name_font_size)
    
    
    def plt_connector_lines():
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
        fig.savefig(Input.output_file_name, dpi=OutFileParameter.dpi)
    
        return None




