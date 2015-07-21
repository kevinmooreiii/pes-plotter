import argparse

class Input_Processor():
""" Handles the input of the input file. """

  # List to hold all the lines we will loop through to pull out additional info.
  infile_lines = []
  # Dictionary to hold the beginning and ending line numbers of a section
  sections = {}
  #    'molecules':  [],
  #    'connections: [],
  #    'options':    []
  #}

  def __init__(self):
    """ No objects will be used, so the __init__ function does not need to do anything. """
    pass

  @staticmethod
  def cmdline_parser():
    """ Function uses the argparse module to take in options the user specifies on the command line. """

    parser = argparse.ArgumentParser(description="Produces a plot of a computed potential energy surface.")

    parser.add_argument('-i', '--input', type=str, default='input.dat', help="Name of the input file to be read in")
    parser.add_argument('-o', '--output', type=str, default='pes.pdf', help="Name of the output file to be created.")

    args = parser.parse_args()

    Input.input_file_name = args.input
    Input.output_file_name = args.output

    return None


  @staticmethod
  def read_input_file():
    """ Open the input file and parse the info. """
     
    with open(, 'r') as infile:
        infile_lines = infile.readlines()

    return infile_lines 


  @staticmethod
  def input_file_parser():
    """ Figures out what sections are in the input file and figures out where they begin and end. """
      
    for i in range(len(infile_lines)):
      if '$molecules' in infile_lines[i]: 
        sections['molecules'].append(i)
        for j in range(i, infile_lines)):
          if '$end' in infile_lines[j]:
            sections['molecules'].append(j)
            break
        molecule_section_parser(
      elif '$connections' in infile_lines[i]: 
        sections['connections'].append(i)
        for j in range(i, infile_lines)):
          if '$end' in infile_lines[j]:
            sections['connections'].append(j)
            break
      elif '$options' in infile_lines[i]: 
        sections['options'].append(i)
        for j in range(i, infile_lines)):
          if '$end' in infile_lines[j]:
            sections['connections'].append(j)
            break

    return None

    @staticmethod
    def molecule_section_parser(sec_start, sec_end):
      """ Reads through the molecule section and stores all the appropriate information as molecule objects. """

      a = []
      for i in range(sec_start, sec_end):
        a.append(infile_lines[i].strip().split())
        
      return a

    @staticmethod
    def connection_section_parser(sec_start, sec_end):
      """ Reads through the connection section and stores all the appropriate information as connector objects. """
     
      a = []
      for i in range(sec_start, sec_end):
        a.append(infile_lines[i].strip().split())
        
      return a

    @staticmethod
    def options_section_parser(sec_start, sec_end):
      """ Reads through the options section and stores all the appropriate information as a list. """
     
      a = []
      for i in range(sec_start, sec_end):
        a.append(infile_lines[i].strip().split())
        
      return a





