#!usr/bin/python3

import numpy as np
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d
import settings.detector as setdet
import settings.screen   as setscr
import modules.timing    as tim
import params.constants  as cts


### DEFINITION OF FUNCTIONS TO MAKE THE 3D REPRESENTATIONS




def PADPAINT(ax,coord,delays):
	"""
	Function to paint pads which are hit in one event. If pad_colours==True, the colour depends
	on the time delay w.r.t. speed of light
	INPUTS:       -> ax:     axis to plot
	              -> coord:  list or array with the coordinates of the hits for one event
	                       [[x1,y1,z1]...[xn,yn,zn]]
	"""
	
	
	if setscr.colpads:
		
		for i in range(len(delays)):
			xh = coord[i][1] ;  yh = coord[i][2] ;  zh = coord[i][3]
			icol = int(delays[i]/setscr.tstcol)
			if icol<20 and icol>=0:
				R = Rectangle(xy=(xh-setdet.WPADX/2,yh-setdet.WPADY/2),width=setdet.WPADX,
				height=setdet.WPADY,alpha=0.5,facecolor=setscr.rbcolors[icol],
				edgecolor='black',fill=True)
			elif icol<0 and icol>-20:
				R = Rectangle(xy=(xh-setdet.WPADX/2,yh-setdet.WPADY/2),width=setdet.WPADX,
				height=setdet.WPADY,alpha=0.5,facecolor='lightgrey',
				edgecolor=setscr.rbcolors[icol],fill=True)
			else:
				R = Rectangle(xy=(xh-setdet.WPADX/2,yh-setdet.WPADY/2),width=setdet.WPADX,
				height=setdet.WPADY,alpha=0.5,facecolor='lightgrey',edgecolor='grey',fill=True)
				print('WARNING. Delay out of colour limits. Pad painted in grey instead')
			ax.add_patch(R)
			art3d.pathpatch_2d_to_3d(R, z=zh, zdir="z")
		return
	
	
	else:
	
		#ax,nPADSX,WPADX,nPADSY,WPADY = config
		for arr in coord:
			xh = arr[1] ;  yh = arr[2] ;  zh = arr[3]
			R = Rectangle(xy=(xh-setdet.WPADX/2,yh-setdet.WPADY/2),width=setdet.WPADX,
			height=setdet.WPADY,alpha=0.5,facecolor='blue',edgecolor='black',fill=True)
			ax.add_patch(R)
			art3d.pathpatch_2d_to_3d(R, z=zh, zdir="z")
		return



def TRACKLINES(axs,coord,style='-',alfa=1.0,line_st='col'):
    """
    Function to plot tracklines given their start and end points, and their velocity
    INPUTS:      -> ax:     axis to plot
                 -> coord:  list or array with the coordinates of the hits for one event
                           [[x1,y1,z1]...[xn,yn,zn]]
    """
	
	
    if line_st == 'acc':
        for item in coord:
            axs.plot(item[2],item[3],item[4],color='red',alpha=alfa)
	
    if line_st == 'den':
        for item in coord:
            axs.plot(item[2],item[3],item[4],color='green',alpha=alfa)
		
    if line_st == 'col':
        for item in coord:
            icol = int((item[1]-(1-setdet.tol_lo)*cts.c)/(setscr.vstcol))
            if icol<20 and icol>=0:
                axs.plot(item[2],item[3],item[4],color=setscr.ifcolors[icol],alpha=alfa)
            else:
                axs.plot(item[2],item[3],item[4],color='red',alpha=alfa)
                print('WARNING. Velocity out of colour limits. Track painted in red instead')
	
    return



def DETECTOR_DRAW(ax):
	"""
	Functions to plot the detector
	"""
	xINI = -(setdet.nPADSX/2)*setdet.WPADX ;  yINI = -(setdet.nPADSY/2)*setdet.WPADY
	for zp in setdet.Zplates:
		for i in range(setdet.nPADSX):
			for j in range(setdet.nPADSY):
				xp = xINI+i*setdet.WPADX ;  yp = yINI+j*setdet.WPADY
				PAD = Rectangle(xy=(xp,yp),width=setdet.WPADX,height=setdet.WPADY,alpha=0.1,
							facecolor='grey',edgecolor='darkgrey',fill=True)
				ax.add_patch(PAD)
				art3d.pathpatch_2d_to_3d(PAD, z=zp, zdir="z")
	return




