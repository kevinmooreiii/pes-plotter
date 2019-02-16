
class Estimation():
    def __init__(self,datax,datay,dataz):
        self.x = datax
        self.y = datay
        self.v = dataz

    def estimate(self,x,y,using='ISD'):
        """
        Estimate point at coordinate x,y based on the input data for this
        class.
        """
        if using == 'ISD':
            return self._isd(x,y)

    def _isd(self,x,y):
        d = np.sqrt((x-self.x)**2+(y-self.y)**2)
        if d.min() > 0:
            v = np.sum(self.v*(1/d**2)/np.sum(1/d**2))
            return v
        else:
            return self.v[d.argmin()]

# example
#z2_est = Estimation(np.array(x), np.array(y), np.array(z2rel))
#with open('seam_e.dat', 'w') as efile:
#    for i in range(len(xv[1])):
#        zv = z2_est.estimate(xv[1][i], yv[1][i])
#        efile.write('{0:>12.4f}   {1:>8.4f}   {2:>8.4f}\n'.format(xv[1][i], yv[1][i], zv))

