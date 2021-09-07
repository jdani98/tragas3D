import numpy as np
import matplotlib.cm as cm
import settings.detector as setdet
import params.constants as cts


#******* Plots and screen configuration ***********************************************************
showlog = False       # -!- True to show all plots
prinlog = False       # -!- True to print information about tracks
colpads = True        # -!- True to color pads in function of their delay
plane1  = True        # -!- True to show possible tracks between two adjacent planes
plane2  = True        # -!- True to show tracks between two separated planes (discontinuous lines)
plane3  = True        # -!- True to show tracks between two doubly-separated planes (disc. lines)
pltacc  = True        # -!- True to show all accepted (green) tracks
pltden  = False       # -!- True to show all denied (red) tracks
plttrc  = True        # -!- True to show track velocity by a scale of colors
tstcol  = 0.2         # -!- time-step to change color in pads (rainbow scale)
vstcol  = (setdet.tol_up+setdet.tol_lo)*cts.c/20         # -!- time-step to change color in tracklines (inferno scale)

rbcolors = cm.rainbow(np.linspace(0,1,20)) # scale of colors: 20 different colors. Each color change means a time-step with value tstcol
ifcolors = cm.inferno(np.linspace(0,1,20))
