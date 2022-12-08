import numpy as np
import time
from ezGraph import * 
from jStats import * 
# Finite Difference Model

#PARAMETERS
dt = 10
nsteps = 120

mh = 28 #max height 
l = 50 #length 
w = 25 #width
q = 0.011 #inflow rate cm/sec (volume)
h = 0 #intial height (cm)
k = -0.0115 #outflow rate 

# EXPERIMENTAL DATA
x_measured = [97.14, 187.82, 278, 382.88, 466.56, 560.2, 659.41, 748.09, 835.63, 923.19, 1007.6, 1099.21, 1188.98]
y_measured = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
y_modeled = []

# GRAPH
graph = ezGraphMM (xmin=0, xmax=100, xLabel= "Time (s)", yLabel= "Height (cm)", x_measured = x_measured, y_measured = y_measured)

graph.addModeled (0, h) # add intial vaules 


# TIME LOOP
for t in range (1, nsteps) :
    modelTime = t * dt 
    if modelTime < 660:
        h = q * dt + h 
    else:
        h = k * dt + h 


    graph.addModeled (t * dt, h)
    graph.wait 

   #dh/dt = K

# DRAW GRAPH
graph.keepOpen ()