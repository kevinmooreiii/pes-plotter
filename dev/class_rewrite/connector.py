class Connector(Molecule):

  def __init__(self,pos,name,energy):
    self.pos = pos
    self.energy = energy
    self.linecolor = 'black'
    self.linewidth = 4 
    #self.x1 = x1
    #self.x2 = x2
    #self.texthoriz = texthoriz
    #self.textvert = textvert
    #self.textfontsize = textfontsize    

    
  def print_linecolor(self):
    print(self.linecolor)

  def get_name(self):
    return self.name
