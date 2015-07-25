import argparse

class Input_Processor(object):
  """ Class of methods to: (1) accept command line arguments from the user,
                           (2) read the input file, and
                           (3) Store all the information in variables to pass to other classes. """

  infile_name = ''      # Name of the input file
  outfile_name = ''     # Name of the output file

  molecule_lines = []   # List to hold all the lines from the molecule section
  connector_lines = []  # List to hold all the lines from the connector section
  options_lines = []    # List to hold all the lines from the options section


  def __init__(self):
    """ No objects will be used, so the __init__ function does not need to do anything. """
    pass


  @classmethod
  def cmdline_parser(cls):
    """ Function uses the argparse module to take in options the user specifies on the command line. """

    # Add arguments that user can specify and put info you can discuss what each options are 
    parser = argparse.ArgumentParser(description="Produces a plot of a computed potential energy surface.")
    parser.add_argument('-i', '--input', type=str, default='input.dat', help="Name of the input file to be read in")
    parser.add_argument('-o', '--output', type=str, default='pes.pdf', help="Name of the output file to be created.")

    # Store all the arguments from argparse into class variabes
    args = parser.parse_args()
    cls.infile_name = args.input
    cls.outfile_name = args.output

    return None 


  @classmethod
  def input_file_parser(cls):
    """ Opens the input file and stores each of the lines of each section into """
 
    # Loop through the file and store lines in an appropriate list that is passed to other class functions
    with open(cls.infile_name,'r') as infile:
      for line in infile:                     # Loop through the whole file
        if '$molecule' in line:              # Search for a section header
          for line in infile:                 # Enter second loop over the lines in the section
            if '$end' in line:                # If you find $end, stop loop as the section is finished
              break
            else:                             # Otherwise add the line to a list
              cls.molecule_lines.append(line.strip())
        if '$connection' in line:            # Continue for other sections...
          for line in infile:
            if '$end' in line:
              break
            else:
              cls.connector_lines.append(line.strip())
        if '$options' in line:                # Continue for other sections...
          for line in infile:
            if '$end' in line:
              break
            else:
              cls.options_lines.append(line.strip())
