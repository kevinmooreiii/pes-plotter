
with open('gd_seam1.dat', 'r') as infile:
    data = infile.readlines()

count = 0
for i in range(len(data)):
    if (i+1) % 8 == 0:
        count += 1
        print(str(count)+'\t'+data[i].strip())    


with open('gd_seam2.dat', 'r') as infile:
    data = infile.readlines()

count = 0
for i in range(len(data)):
    if (i+1) % 6 == 0:
        count += 1
        print(str(count)+'\t'+data[i].strip())    
