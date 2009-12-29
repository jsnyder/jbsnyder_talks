from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
# don't plot features that are smaller than 1000 square km.
map = Basemap(projection='tmerc',lat_0=41.908682,lon_0=-87.649250,
              resolution='h', width=1e5, height=1e5, lat_ts=41.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines()
map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary()
# draw lat/lon grid lines every 30 degrees.
#map.drawmeridians(np.arange(0,360,30))
#map.drawparallels(np.arange(-90,90,30))
map.drawstates()
map.drawrivers()
plt.show()