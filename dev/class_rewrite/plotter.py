class ThePlot:
    """ Handles options of the entire plot created, not specific to a single molecule. """
    
    # Parameters for axes set-up
    y_axis_top_lim = 0
    y_axis_bot_lim = 0
    y_axis_top_extend = 2.5
    y_axis_bot_extend = 2.5
    x_axis_right_lim = 0
    x_axis_right_extend = 0.75

    # Parameters for name and energy labels
    name_vshift = 0
    name_vshift_scale_fact = 0.04
    energy_vshift = 0
    energy_vshift_scale_fact = 0.04

    def __init__(self):
      self.plot_name = pes.pdf
      self.width = 16
      self.height = 9
      self.dpi = 1000   
      self.x_axis_name = 
      self.x_axis_spacing = 1.00
      self.x_axis_min = 0.0
      self.x_axis_max = 'Reaction Coordinate'
      self.y_axis_name = 'Relative Energy (kcal/mol)'
      self.y_axis_min =
      self.y_axis_max =



    @staticmethod
    def y_axis_maximum(self):
        PlotParameter.y_axis_top_lim = Molecule.max_energy + PlotParameter.y_axis_top_extend
        return y_axis_max

    @staticmethod
    def y_axis_minimum(self):
        PlotParameter.y_axis_bot_lim = Molecule.min_energy - PlotParameter.y_axis_bot_extend
        return y_axis_min

    @staticmethod
    def x_axis_extent(self):
        PlotParameter.x_axis_right_lim = Molecule.ground_species_count + PlotParameter.x_axis_right_extend
        return x_axis_extent

    def gen_plot_axes(self):
        plt.axes(frameon=False)
        plt.axvline(0, PlotParameter.y_axis_bot_lim, PlotParameter.y_axis_top_lim, color='k')
        plt.tick_params(which='both', bottom='off', top='off', right='off', labelbottom='off')
        plt.xlim(0, PlotParameter.x_axis_right_lim)
        plt.ylim(PlotParameter.y_axis_bot_lim, PlotParameter.y_axis_top_lim)
        plt.ylabel(PlotParameter.y_axis_label)


    def plt_spec_lines():
        """ Plot the lines that correspond to the molecular species. """
    
        for i in range(0, Molecule.species_count):
            mid_line = (Molecule.right_endpt[i] + Molecule.left_endpt[i]) / 2
            shift1 = Molecule.energy[i] - PlotParameter.energy_vshift
            shift2 = Molecule.energy[i] + PlotParameter.name_vshift
    
            plt.plot([Molecule.left_endpt[i], Molecule.right_endpt[i]], [Molecule.energy[i], Molecule.energy[i]],
                     color=PlotParameter.species_line_color, lw=PlotParameter.species_line_width, linestyle='-')
            plt.text(mid_line, shift1, Molecule.energy[i], weight='bold', horizontalalignment='center',
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
        fig.savefig(Input.output_file_name, dpi=OutFileParameter.dpi)
        # plt.show()
    
        return None




