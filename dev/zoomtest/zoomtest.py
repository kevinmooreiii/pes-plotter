import pylab as pl
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

x=np.linspace(0,1,100)
y=x**2
z = x**4

ax=pl.subplot(1,1,1)
ax.plot(x,y)

axins = zoomed_inset_axes(ax, 2, loc=3,bbox_to_anchor=(0.2, 0.55),bbox_transform=ax.figure.transFigure) # zoom = 6

axins.plot(x,y)

x1, x2= .4, .6
y1, y2 = x1**2, x2**2
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
mark_inset(ax, axins, loc1=1, loc2=3, fc='none', ec="0.5")

pl.savefig('zoom.pdf')
