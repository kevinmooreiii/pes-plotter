class Molecule(object):

  _energy_list = []

  #_classdic = {}

  def __init__(self,pos,name,energy):
    self.pos = pos
    self.name = name
    self.energy = energy
    self.linecolor = 'black'
    self.linewidth = 4 
    #self.x1 = x1
    #self.x2 = x2
    #self.texthoriz = texthoriz
    #self.textvert = textvert
    #self.textfontsize = textfontsize    


   @staticmethod
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
           tmp2 = Molecule.right_endpt[Molecule.excited_state[i] - 1]
           Molecule.left_endpt.append(tmp1)
           Molecule.right_endpt.append(tmp2)

       return None

  def make_molecules():
    """ """

    # Open up input file and create file objects for plotting 
    mol_dict = {}                                                          
    i = 0                                                                                            
                                                                                                 
    with open('in.txt','r') as infile:                                                               
      for line in infile:                                                                            
        i = i + 1                                           # Loop Counter                           
        tmp = line.strip().split()                          # Create split up the lines of the input file
        key = 'molecule'+str(i)                             # Cenerate dictionary key for each molecule
        mol_dict[key] = Molecule(tmp[0], tmp[1], tmp[2])    # Store each molecule object into a dictionary          

        
        tmp = line.strip().split()                                                                   
      for key, value in mol_dict.items():      
        if tmp[0] == mol_dict[key].get_name(): 
          mol_dict[key].print_linecolor()      
          mol_dict[key].linecolor = tmp[1]     
          mol_dict[key].print_linecolor() 

    return None      

   def calc_midpoint(self, x1, x2):
       midpoint = (x2 - x1) / 2
       return midpoint

   def vert_shift_name(self):
       PlotParameter.name_vshift = PlotParameter.name_vshift_scale_fact * Molecule.range_energy
       return name_vshift

   def vert_shift_energy(self):
       PlotParameter.energy_vshift = PlotParameter.energy_vshift_scale_fact * Molecule.range_energy
       return energy_vshift

   def latexify_name(self,name):
       self.name = '$' + self.name + '$'

