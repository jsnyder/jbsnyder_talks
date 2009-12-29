import numpy as np
from scipy import random, optimize, interpolate
import matplotlib.pyplot as plt

# Generate oscillating signal on -2pi,2pi with noise
x = np.arange(-np.pi*2,np.pi*2,0.5)
x += random.standard_normal(np.shape(x))*0.1
y = np.sin(x) + random.standard_normal(np.shape(x))*0.1

# Model signal with spline interp (smoothing set to 0.5)
interp_function = interpolate.UnivariateSpline(x,y,s=0.5)

# New x range for data
newx = np.arange(-np.pi*2, np.pi*2, 0.1)
newy = interp_function(newx)

# Plot Data
plt.figure()
plt.plot(newx, newy,'b-',label='interp')
plt.plot(x, y, 'ko',label='raw data')
plt.legend()
plt.show()

# ... or fit the data
fitfunc = lambda p, x: p[0]*np.sin(2*np.pi/p[1]*x+p[2])
errfunc = lambda p, x, y: fitfunc(p, x) - y

p0 = [1., 5., 0.] # Initial guess for the parameters
p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))

plt.figure()
plt.plot(newx, newy,'b-',label='interp')
plt.plot(x, y, 'ko',label='raw data')
plt.plot(newx, fitfunc(p1, newx),'k:',label='fit',linewidth=3)
plt.legend()
plt.show()