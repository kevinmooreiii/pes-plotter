class Molecule(object):

  _energy_list = []
  molec_dict = {}

  def __init__(self,pos,name,energy):
    self.pos = pos
    self.name = name
    self.energy = energy
    self.linecolor = 'black'
    self.linewidth = 5
    self.linethickness = 4
    self.x1, self.x2 = self.generate_xcoords(self.pos, self.linethickness) 
    self.name_font_size = 10
    self.energy_font_size = 10
    type(self).molec_dict[self.name] = self
    type(self)._energy_list.append(weakref.ref(self.energy))


  def generate_xcoords(self, pos, linethickness):
    """ Generates a list of the coordinates for the left and right endpoints of each of the horizontal lines
        corresponding to a molecular species.
    """

    # line_sep should be mae into a plot class variable
    linesep = 5

    x1 = (linesep * pos) + 0.25
    x2 = x1 + linethickness

    return x1, x2


  def calc_midpoint(self, x1, x2):
      """ Names of molecules are specified over the middle of the line. This function computes the midpoint for this. """

      midpoint = (x2 - x1) / 2

      return midpoint


  def vert_shift_name(self, name):
      """ Calculate how far below the molecule line the name will be shown. """

      PlotParameter.name_vshift = PlotParameter.name_vshift_scale_fact * Molecule.range_name

      return name_vshift


  def vert_shift_energy(self energy):
      """ Calculate how far above the molecule line the energy will be shown. """

      PlotParameter.energy_vshift = PlotParameter.energy_vshift_scale_fact * Molecule.range_energy

      return energy_vshift


  def latexify_name(self,name):
      """ Convert the name into a format to make it in LaTEX style. """

      self.name = '$' + self.name + '$'

      return self.name

# Code to implement

#    for i in range(0, Molecule.excited_species_count):
#        tmp1 = Molecule.left_endpt[Molecule.excited_state[i] - 1]
#        tmp2 = Molecule.right_endpt[Molecule.excited_state[i] - 1]
#        Molecule.left_endpt.append(tmp1)
#        Molecule.right_endpt.append(tmp2)

#    return None

#    for key, value in mol_dict.items():      
#      if tmp[0] == mol_dict[key].get_name(): 
#        mol_dict[key].print_linecolor()      
#        mol_dict[key].linecolor = tmp[1]     
#        mol_dict[key].print_linecolor() 
