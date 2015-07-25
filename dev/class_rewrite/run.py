from input_processor import Input_Processor
from molecule import Molecule
#from connector import Connector
#from plotter import ThePlot
 
# Create an Input Processor object 
proc = Input_Processor()

# Use the Input Processor to parse the input file
proc.cmdline_parser()
proc.input_file_parser()

# Create all of the molecule onjects; all stored in dictionary in Molecule class
Molecule.make_molecule(Input_Processor.molecule_lines, Molecule.molec_dict)
# Compute values needed for plotting
Molecule.energy_lim(Molecule._energy_list)
# Compute and then change program neccessary attributes of each molecule 

# Change any attributes that are requested by the user


# Loop through the molecule lines and generate each of the connector objects; store in dictionary
#for i in range(len(Input_Processor.connector_lines)):
#  tmp = Input_Processor.molecule_lines[i].strip().split()
#  Connector.connect_dict[] = Connecter()

# Augment all of the molecule and connector objects to the users specifications
# Some function....

# Create the plot object
#plotter.gen_plot_axes()

# Place all the objects onto the plot object
#plotter.plt_molecule_lines()
#plotter.plt_connector_lines()

# Create the total plot that has been created
#plotter.create_pdf()
