import weakref

Class InputParser():
  """ Class handles the parsing of the input file and storage of information. """

  _input_file_content = []

  @staticmethod
  def read_input(input_file_name):
    """ Open input file and store the information in a list to read through. """
    with open(input_file_name,'r') as infile:
      _input_file_content = infile.readlines()

    return None

  @staticmethod
  def get_section_lines(_input_file_content):
    """ Read through the content list and determine where each section of the input file begins and ends. This will be used for later loops. """ 
    
    sections = {
      'Number': 0,
      'Start Lines': [],
      'End Lines': [],
      'Plot Start': 0,
      'Plot End': 0
    }
 
    for i in range(0, len(_input_file_content)):   
      if '$plot_start' in content[i]:
        sections['Plot Start'] = i 
      if '$plot_end' in content[i]:
        sections['Plot End'] = i 
      if '$data_start' in content[i]:
        sections['Data Number'] = sections['Number'] + 1 
        sections['Start Lines'].append(int(i))
      if '$data_end' in content[i]:
        sections['End Lines'].append(int(i))
  

    return sections

  @staticmethod
  def get_data(_input_file_content, **sections)
    """ Store coordinate and energy in lists. """
   
    coord = [[]] * sections['Number']
    energy = [[]] * sections['Number']
   
    for i in range(0, sections['Number']):
      for j in range(sections['Start Lines'][i],sections['End Lines'][i]):
        coord[i].append(content[j].strip().split()[0])
        energy[i].append(content[j].strip().split()[1])
 
    return coord, energy

  @staticmethod
  def get_plot_params(_input_file_content, **sections)
    """ Get information that plot the parameters. """
    
    plot_specs = {}
    
    for i in range(0,len(_input_file_content)):
      tmp = _input_file_content[i].strip().split('=')  
      plot_specs[tmp[0].lower()].append(tmp[i])


    if title :
        plot_specs['Title'] = content[0].strip()
      if  
        plot_specs['X-axis Label'] = content[1].strip()
      if
        plot_specs['Y-axis Label'] = content[2].strip()
      if
        plot_specs['X-axis Min'] = float(content[3].strip().split()[0])
      if 
        plot_specs['X-axis Max'] = float(content[3].strip().split()[1])
      if 
        plot_specs['Y-axis Min'] = float(content[3].strip().split()[2])
      if 
        plot_specs['Y-axis Max'] = float(content[3].strip().split()[3])


### Class definition over ###


Class DataSet(InputParser):
  """ Each instance of this class pertains to a set of data to be included into the plot. """

  #_x_vals = []
  #_y_vals = []
  
  def __init__(self, x, y, rep, label)
    self.x
    self.y
    self.rep
    self.label
  #  type(self)._x_vals.append(weakref.ref(self.x))
  #  type(self)._y_vals.append(weakref.ref(self.y))

  #def reverse_data(self,x,y):
  #  _x_vals = reversed(_x_vals)
  #  _y_vals = reversed(_y_vals)

  #def every_other(self,x,y):
  #  for i in range(0,len(_x_vals)):
  #    if i % 2 != 0:
  #      _x_vals.remove

  #def plot_data(self,x,y,rep,label):
  #  plt.plot(self.x, self.y, self.rep, label=self.label)

  #@classmethod 
  #max_enegy(cls):
  #min_energy(cls):
  #max_coord(cls):  


### Class definition over ###


Class Plot:
  ''' Class creates the plot using the information obtained and manipulated by the earlier classes. '''
 
  def __init__(self,title,xaxislabel,yaxislabel,xmin,xmax,ymin,ymax):
    self.title = title
    self.xaxislabel = xaxislabel
    self.yaxislabel = yaxislabel
    self.xmin = xmin
    self.xmax = xmax
    self.ymin = ymin
    self.ymax = ymax
    self.specialoptions = specialoptions

  def plot_necc(self,title, xaxislabel, yaxislabel,xmin,xmax,ymin,ymax):
    plt.title(plot_specs['Title'], y = 1.06)
    plt.xlabel(plot_specs['X-axis Label'])
    plt.ylabel(plot_specs['Y-axis Label'])
    plt.xlim(coord[0], coord[-1])
    plt.xlim(coord[0], coord[-1])

  def plot_optional():
    if horizline true:
      plot horizline
    if legen true:
      plot legend


