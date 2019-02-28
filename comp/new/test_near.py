import sys
import numpy as np

f1 = sys.argv[1]
f2 = sys.argv[2]


def get_vals(fname):

    x, y, z = [], [], []
    with open(fname,'r') as efile:
        for line in efile:
            tmp = line.strip().split()
            x.append(float(tmp[0]))
            y.append(float(tmp[1]))
            z.append(float(tmp[2]))
    
    return x, y, z


def calc_dist(xa, ya, xb, yb):

    dist = np.sqrt( (xb-xa)**2 + (yb-ya)**2 )

    return dist


x1, y1, z1 = get_vals(f1)
x2, y2, z2 = get_vals(f2)


short_dist = None
dif = 0.0
all_difs = []
for i in range(len(x1)):
    for j in range(len(x2)):
        distance = calc_dist(x1[i], y1[i], x2[j], y2[j])
        if distance < short_dist or short_dist is None:
            short_dist = distance
            idx = j
    z1val = z1[i]         
    z2val = z2[idx]
    dif = abs(z1val - z2val)
    print('{0:>8.4f} {1:>8.4f} {2:>8.2f} {3:>8.2f} {4:>8.2f}'.format(x1[i], y1[i], x2[idx], y2[idx], dif))
    all_difs.append(dif)
    short_dist = None

print('\n\n')
print(max(all_difs))
print(sum(all_difs)/len(all_difs))
        
