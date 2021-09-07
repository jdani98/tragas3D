import numpy as np
#******* Detector configuration *******************************************************************

nPADSX = 12    # -!- number of pads in X direction
nPADSY = 10    # -!- number of pads in Y direction

Zplates = np.array([1826.,924.,87.]) # -!- z positions of the detector planes

# Tolerance to accept or reject track in function of its velocity w.r.t. that of light
tol_up  = 0.1  # -!- tolerance upper limit
tol_lo  = 0.5  # -!- tolerance lower limit

WPADX = 12.6   # pad width (pitch) in X direction
WPADY = 12.1   # pad width (pitch) in Y direction

lenX = nPADSX*WPADX # -!- detector length in X direction
lenY = nPADSY*WPADY # -!- detector length in Y direction

nplanes = len(Zplates) # number of planes
