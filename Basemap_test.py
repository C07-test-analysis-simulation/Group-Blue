from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


#Map Projection

m = Basemap(projection='cyl', 
            llcrnrlat = -90, 
            urcrnrlat = 90,
            llcrnrlon = -180,
            urcrnrlon = 180,
            resolution = 'c')

m.drawcoastlines()
# m.drawcountries(color='tomato')
# m.drawrivers(color = 'blue')
# m.drawmapboundary(fill_color = 'aqua')
# m.fillcontinents(color='lightgreen')
m.drawlsmask(land_color='lightgreen', ocean_color='aqua', lakes = True)
# m.etopo()
#m.bluemarble()

m.drawparallels(np.arange(-90, 90, 10), labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,30),labels=[0,0,0,1])

#Example function
t_start = 0
t_end = 60 * 60 *24
dt = 60


def lat_func(t):
    return np.sin(t / 10000) * 40

def lon_func(t):
    return np.cos(t / 10000) * 40

#from Interpolation_test import f_latt, f_long, f_alt

time = np.arange(t_start,t_end,dt)
lon = lon_func(time)
lat = lat_func(time)

#lat = f_latt(time)
#lon = f_long(time)

x, y = m(lon,lat)
m.plot(x, y, marker=None, color='red', linewidth=2)

plt.title('Orbit Visualisation',fontsize = 20)
plt.show()
print('limburhg')