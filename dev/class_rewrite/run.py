from input_processor import Input_Processor
from molecule import Molecule
#import connector
#import plotter
 
# Process the input file
proc = Input_Processor()
proc.cmdline_parser()
proc.input_file_parser()

#molec.generate_xcoord()

for i in range(len(Input_Processor.molecule_lines)):
  tmp = Input_Processor.molecule_lines[i].strip().split()
  Molecule.molec_dict[tmp[0]] = Molecule( (i+1), tmp[0], tmp[2])
Molecule.print_dict(Molecule.molec_dict)

# Create the molecule objects needed for the plot
#molec.make_molecules()

# Create the connector objects needed for the plot
#connect.make_connectors()

# Create the plot object
#plotter.make_plot()

