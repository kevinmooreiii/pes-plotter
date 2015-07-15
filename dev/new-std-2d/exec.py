import sys

# Open the file and read in the input.
# InputParser will then manipulate the data to instantiate other classe.

InputParser.read_input(sys.argv[1])
sections = InputParser.get_section_lines()
data = InputParser.get_data()
plotparams = InputParser.get_plot_params() 

# Create an object of using the information from the InputParser class.
