from input_processor import Input_Processor
from molecule import Molecule
#import connector
#import plotter
 
# Process the input file
proc = Input_Processor()
proc.cmdline_parser()
proc.input_file_parser()
#proc.checker(proc.molecule_lines, proc.connector_lines, proc.options_lines)

# Create the molecule objects needed for the plot
#molec.generate_xcoord()
#molec.make_molecules()

# Create the connector objects needed for the plot
#connect.make_connectors()

# Create the plot object
#plotter.make_plot()

