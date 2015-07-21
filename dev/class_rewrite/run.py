import input_processor as proc 
import molecule as molec
import connector
import plotter
 
# Process the input file

proc.cmdline_parser()
proc.input_file_parser()
proc.section_checker()

# Create the molecule objects needed for the plot

molec.generate_xcoord()
molec.make_molecules()

# Create the connector objects needed for the plot

connect.make_connectors()

# Create the plot object

plotter.make_plot()


