#!usr/bin/python3

import numpy as np
import settings.detector as setdet
import settings.screen   as setscr
import params.constants  as cts

### DEFINITION OF FUNCTIONS TO COMPUTE PHYSICAL VARIABLES




def PADDELAY(coord):
	"""
	Function to compute the delays between two hits. Calculated as the difference between the
	real time and the time that would be needed from the first hit to the point
	INPUTS:  	-> coord:  list or array with the coordinates of the hits for one event
	                       [[x1,y1,z1]...[xn,yn,zn]]
	"""
	
	firstplane = np.min(coord[:,0])
	ts = [coord[i,4] for i in range(len(coord)) if coord[i,0] == firstplane]
	firsthit = np.argmin(ts)
	x0 = coord[firsthit][1] ;  y0 = coord[firsthit][2] ;  z0 = coord[firsthit][3] ;  t0 = coord[firsthit][4]
	
	Dt_list = []
	for arr in coord:
		xh = arr[1] ;  yh = arr[2] ;  zh = arr[3] ;  th = arr[4]
		dist = np.sqrt((xh-x0)**2+(yh-y0)**2+(zh-z0)**2)
		#tc = np.abs(zh-z0)/c # time at light speed
		tc = dist/cts.c      # time at light speed
		tr = (th-t0)         # real time from initial hit
		Dt = tr-tc           # delay between the two times
		Dt_list.append(Dt)
		
	return Dt_list



def TRACKREJ(coord,N):
	"""
	Function to determine the rejection or not of tracks depending on their velocity
	INPUTS:		-> coord:     list or array with the coordinates of the hits for one event [[x1,y1,z1]...[xn,yn,zn]]
				-> N:         number of planes that can be traversed after the first to be shown
				-> style:     string with line style to plot
				-> alfa:      number of line opacity
				-> pltden:    logical to show denied tracks
				-> pltacc:    logical to show accepted tracks
	OUTPUTS:	-> acc:       list with information for each accepted track [[plane start, plane end], velocity, [x start point, x end point], [y sp, y ep], [z sp, z ep], [t sp, t ep]]
				-> den:       list with information for each denied track [[plane start, plane end], velocity, [x sp, x ep], [y sp, y ep], [z sp, z ep], [t sp, t ep]]
				-> new_coord: array with only coordinates which were not achieved by any accepted track
	"""
	
	acc = [] ; den = []
	ind_to_del = []             # list with indices to delete in new_coord list
	for i in range(len(setdet.Zplates)-N):
		indices1 = np.where(coord[:,3]==setdet.Zplates[i])[0]
		indices2 = np.where(coord[:,3]==setdet.Zplates[i+N])[0]
		for indx1 in indices1:
			h1 = int(coord[indx1,0]) ;  x1 = coord[indx1,1] ;  y1 = coord[indx1,2] ;
			z1 = coord[indx1,3] ;  t1 = coord[indx1,4]
			for indx2 in indices2:
				h2 = int(coord[indx2,0]) ;  x2 = coord[indx2,1] ;  y2 = coord[indx2,2] ;
				z2 = coord[indx2,3] ;  t2 = coord[indx2,4]
				dR = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
				dt = t2-t1
				v = dR/dt
				if (v < cts.c*(1-setdet.tol_lo)) or (v > cts.c*(1+setdet.tol_up)):
					den.append([[h1,h2],v, [x1,x2],[y1,y2],[z1,z2],[t1,t2]])
				else:
					acc.append([[h1,h2],v, [x1,x2],[y1,y2],[z1,z2],[t1,t2]])
					ind_to_del.append(indx2)
	new_coord = np.delete(coord,ind_to_del,0)  # array with only coordinates which were not achieved by any track

	return acc, den, new_coord
