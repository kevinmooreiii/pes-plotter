
# Run a loop to store the lines from each section of the input file into separate lists

mol_lines = []
con_lines = []
opt_lines = []

with open('input.dat','r') as infile:
  for line in infile:                     # Loop through the whole file
    if '$mol' in line:                    # Search for a section header
      for line in infile:                 # Enter second loop over the lines in the section
        if '$end' in line:                # If you find $end, stop loop as the section is finished
          break
        else:                             # Otherwise add the line to a list
          mol_lines.append(line.strip())   
    if '$con' in line:                    # Continue for other sections...
      for line in infile:
        if '$end' in line:
          break
        else:
          con_lines.append(line.strip())   
    if '$opt' in line:                    # Continue for other sections...
      for line in infile:
        if '$end' in line:
          break
        else:
          opt_lines.append(line.strip())   

for i in range(len(mol_lines)):
  print(mol_lines[i])
print('\n\n')
for i in range(len(con_lines)):
  print(con_lines[i])
print('\n\n')
for i in range(len(opt_lines)):
  print(opt_lines[i])
print('\n\n')



