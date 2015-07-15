import sys

inputfilename = sys.argv[1]
outfilename = sys.argv[2]

with open(inputfilename, 'r') as infile:
  data = infile.readlines()

newlines = []

for i in range(0,9):
  newlines.append(data[i])

for i in range(9,len(data)):
  if '$end' in data[i]:
    break
  else: 
    tmp = data[i].strip().split() 
    newval = str(float(tmp[1]) * 0.5)
    newstr = tmp[0]+'\t\t'+newval+'\t\t'+tmp[2]+'\n'
    newlines.append(newstr)

newlines.append('$end')

with open(outfilename,'w') as convfile:
  convfile.writelines(newlines)

