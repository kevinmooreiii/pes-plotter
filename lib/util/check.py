with open('energies.dat', 'r') as energyfile:
    lines = energyfile.readlines()

for line in lines:
    tmp = line.strip().split()
    if tmp[1] in ('90.0'):
        print(tmp[0]+'   '+tmp[1])
print('\n\n')
for line in lines:
    tmp = line.strip().split()
    if tmp[1] in ('92.0'):
        print(tmp[0]+'   '+tmp[1])
print('\n\n')
for line in lines:
    tmp = line.strip().split()
    if tmp[1] in ('94.0'):
        print(tmp[0]+'   '+tmp[1])




