from input_processor import Input_Processor
from molecule import Molecule
from connector import Connector
from plotter import ThePlot
 
# Create an Input Processor object 
proc = Input_Processor()

# Use the Input Processor to parse the input file
proc.cmdline_parser()
proc.input_file_parser()

# Create all of the molecule onjects; all stored in dictionary in Molecule class
Molecule.make_molecule(Input_Processor.molecule_lines, Molecule.molec_dict)
Connector.make_connector(Input_Processor.connector_lines, Molecule.molec_dict, Connector.connector_dict)

# Augment all of the molecule and connector objects to the users specifications
# Some function....

# Compute values from Molecule that are needed to instantiate the plot object
num_ground, max_energy, min_energy = Molecule.get_energy_param(Molecule.energy_list)

# Create the plot object
aplot = ThePlot(num_ground, max_energy, min_energy)

# Generate the plot's axes
aplot.gen_plot_axes()

# Place all the objects onto the plot object
aplot.plt_molecule_lines(Molecule.molec_dict, max_energy, min_energy)
aplot.plt_connector_lines(Connector.connector_dict)

# Create the total plot that has been created
aplot.create_pdf()
