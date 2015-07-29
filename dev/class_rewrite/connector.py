from molecule import Molecule

class Connector(Molecule):

  connector_dict = {}

  def __init__(self, molec_dict, mol1, mol2):
    self.linecolor = 'black'
    self.linewidth = 4 
    self.x1, self.x2, self.y1, self.y2 = self.get_connector_coords(molec_dict, mol1, mol2)

  def make_connector(connector_lines, molec_dict, connector_dict):
    """ Make the connector objects. """
   
    for i in range(len(connector_lines)):
      # Split the connector lines
      # input for line mol1 - mol2
      tmp = connector_lines[i].strip().split()
      mol1 = tmp[0]
      mol2 = tmp[2]     

      # Create a connector object stored in a dictionary
      connector_dict[i] = Connector(molec_dict, mol1, mol2)    

    return None


  def get_connector_coords(self, molec_dict, mol1, mol2):
    """ Define the coordinates of the connectors. """   
    
    # Get the x and y coordinates of the molecule objects
    x1 = molec_dict[mol1].x2
    x2 = molec_dict[mol2].x1
    y1 = molec_dict[mol1].energy
    y2 = molec_dict[mol2].energy

    return x1, x2, y1, y2

