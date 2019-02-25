import numpy

p1 = []
with open('all_all.dat', 'r') as e1file:
    for line in e1file:
        p1.append(line.strip().split()[2])
p2 = []
with open('all_deg2.dat', 'r') as e1file:
    for line in e1file:
        p2.append(line.strip().split()[2])
p3 = []
with open('p050_deg2.dat', 'r') as e1file:
    for line in e1file:
        p3.append(line.strip().split()[2])
p4 = []
with open('p050_all.dat', 'r') as e1file:
    for line in e1file:
        p4.append(line.strip().split()[2])

p5 = []
with open('p01_deg4.dat', 'r') as e1file:
    for line in e1file:
        p5.append(line.strip().split()[2])

x = range(1,146,1)

for i in range(len(x)):
    prstr = '{0}  {1}  {2}  {3}  {4}  {5}'.format(x[i], p1[i], p2[i], p3[i], p4[i], p5[i])
    print(prstr)


