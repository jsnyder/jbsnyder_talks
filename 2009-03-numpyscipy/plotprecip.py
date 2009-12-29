from mpl_toolkits.basemap import Basemap, cm, NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import rcParams

# plot rainfall from NWS using special precipitation
# colormap used by the NWS, and included in basemap.

#data from http://water.weather.gov/download.php
#nc = NetCDFFile('nws_precip_conus_20090312.nc')
nc = NetCDFFile('nws_precip_conus_20090311.nc')

# extract precipitation value
prcpvar = nc.variables['amountofprecip']
data = 0.01*prcpvar[:]

# get corners of the map
latcorners = nc.variables['lat'][:]
loncorners = -nc.variables['lon'][:]

plottitle = prcpvar.long_name+' (mm) for period ending '+prcpvar.dateofdata

# get location where position is true in map
lon_0 = -nc.variables['true_lon'].getValue()
lat_0 = nc.variables['true_lat'].getValue()

# create polar stereographic Basemap instance.
m = Basemap(projection='stere',lon_0=lon_0,lat_0=90.,lat_ts=lat_0,\
            llcrnrlat=latcorners[0],urcrnrlat=latcorners[2],\
            llcrnrlon=loncorners[0],urcrnrlon=loncorners[2],\
            rsphere=6371200.,resolution='l',area_thresh=1000)

# create figure
fig = plt.figure(figsize=(6,5))
ax = plt.gca()

# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# project data
ny = data.shape[0]; nx = data.shape[1]
lons, lats = m.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.

# draw filled contours.
clevs = np.array([0,1,2.5,5,7.5,10,15,20,30,40,50,70,100,150,200,250,300,400,500,600,750])
cs = m.contourf(x,y,data,clevs,cmap=cm.s3pcpn)

# new axis for colorbar
pos = ax.get_position()
l, b, w, h = pos.bounds
cax = plt.axes([l+w+0.025, b, 0.025, h]) # setup colorbar axes

# draw colorbar.
plt.colorbar(cs, cax, format='%g', ticks=clevs, drawedges=False) 
plt.axes(ax)  # make the original axes current again

# plot title
plt.title(plottitle,fontsize=10)
plt.show() # display onscreen.
