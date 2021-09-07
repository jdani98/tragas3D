# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:05:24 2021

@author: dviqu
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import os
import datetime

import settings.detector as setdet
import settings.data     as setdat
import settings.saving   as setsav
import settings.screen   as setscr
import modules.represent as rep
import modules.timing    as tim
import modules.reading   as rd
import modules.topology  as top

dia = datetime.datetime.today()
strday = dia.strftime("%y%m%d")

if   setdat.dtread=='mode1': data = rd.DATA_READING1(setdat.fname)
elif setdat.dtread=='mode2': data = rd.DATA_READING2(setdat.fname)

print('***************************************************************************')
print('############# SHOWER TRACKS RECONSTRUCTION IN TRAGALDABAS #################')
print('***************************************************************************')
print('\n  //// DETECTOR CONFIGURATION')
print('    - Size      %f mm x %f mm'   %(setdet.lenX,setdet.lenY))
print('    - Pads      %i mm x %i mm'   %(setdet.nPADSX,setdet.nPADSY))
print('    - Situation of planes:  '    %setdet.Zplates)
print('    - Tolerance:  -%4.2f +%4.2f' %(setdet.tol_lo,setdet.tol_up))
print('\n  //// PLOTS CONFIGURATION')
print('    - Save all plots?', setsav.savefgr)
print('    - Save tracks?   ', setsav.saveinf)
print('    - What transitions to show? (0,1 or 2 intermediate planes)  ', 
setscr.plane1,setscr.plane2,setscr.plane3)
print('\n  //// DATA CONTENT')
print('    - Total number of events: %i' %len(data))


if setsav.saveinf or setsav.savefgr:
    print('\n  Save figures/tracks option is activated')
    savedir = input('     Write the name of the directory to save or press ENTER to name as default: ')
    if len(savedir) == 0: savedir = setsav.preffix + strday

    cwd = os.getcwd()  # main current working directory
    print(cwd)
	
    os.chdir(cwd+'/'+setsav.savedrt)
    print(cwd)
    list_dir = os.listdir()
    print(list_dir)
    if savedir not in list_dir:
        os.mkdir(savedir)
        print(' New directory created in %s: %s' %(cwd,savedir))

print('\n   MODE OF VISUALIZATION: HITS AND RECONSTRUCTION')
print('\n  Introduce MODE OF SELECTION for plots')
print('    MODE A - Selection by event number')
print('    MODE B - Selection by topology')
plotmode = input('  > Introduce <A> or <B>: ')

#### PLOT MODE A ######################################################
if plotmode =='A' or plotmode =='a':
    print('\n   SELECTION BY EVENT NUMBER')
    print('  *** Introduce one event')
    ev = int(input('  >>>  '))


#### PLOT MODE B ######################################################
if plotmode == 'B' or plotmode == 'b':
    print('\n   SELECTION BY EVENT TOPOLOGY')
    print('    Computing topologies ...')
    topo_list = []
    for ev in range(len(data)):
        dat   =  data[ev]
        coord = np.array(dat[1:])
        acc, den, new_coord = tim.TRACKREJ(coord,1)
        code = top.CREATE_CODE((top.NOH,top.NOT,top.NOV,top.NOP,top.P1H,top.PLH),dat,acc)
        topo_list.append(code)
    sort_topo = Counter(topo_list)
    sort_topo = sorted(sort_topo.items())
		
    printable = ''
    for i in range(len(sort_topo)):
        printable += '   %6s: %3i' %(sort_topo[i][0],sort_topo[i][1])
        if (i+1)%3==0: printable += '\n'
    print('\n Sorted topologies and frequencies')
    print(printable)
		
    print('\n  *** Introduce topology. ')
    print('      [Introduce only those digits of interest. The rest can be filled by dash]')
    print('      [Examples: 3----- returns all events with this first digit;')
    print('                 31---- returns all events with these two first digits')
    print('                 -4-1-0 returns all events with these second, fourth and sixth digits]')
    print('      Remember that the code has 6 digits')
    topology = input('  >>>  ')


    accepted_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ichars = [index for index,element in enumerate(topology) if element in accepted_digits]
    events = []
    for i in range(len(topo_list)):
        item = topo_list[i]
        valid = True
        for indx in ichars:
            if item[indx] == topology[indx]:
                valid = valid * True
            else:
                valid = valid * False
        if valid:
            events.append(i+1)
    print('    -> Found ', len(events), ' events: ', events)
    ev = int(input('Introduce number of event '))


fig = plt.figure('3D representation for event '+str(int(ev)),figsize=(8,8))
ax  = fig.gca(projection='3d')
		
xINI = -(setdet.nPADSX/2)*setdet.WPADX ;  yINI = -(setdet.nPADSY/2)*setdet.WPADY
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_xticks(np.arange(xINI,xINI+setdet.WPADX*setdet.nPADSX+1,setdet.WPADX))
ax.set_yticks(np.arange(yINI,yINI+setdet.WPADY*setdet.nPADSY+1,setdet.WPADY))
ax.set_zticks(setdet.Zplates)
ax.set_xlim(xINI,xINI+setdet.lenX)
ax.set_ylim(yINI,yINI+setdet.lenY)
ax.set_zlim(0,setdet.Zplates[0])
ax.grid(False)
plt.tick_params(labelsize = 7.5)

rep.DETECTOR_DRAW(ax)

dat   =  data[ev-1]
coord = np.array(dat[1:])
		
hplanes = [dati[0] for dati in dat[1:]]

accepted = [] ; denied = []
		
delays = tim.PADDELAY(coord)
rep.PADPAINT(ax,coord,delays)


def subroutine_for_lines(ax,coord,N,style,k_alfa):
	acc, den, new_coord = tim.TRACKREJ(coord,N)
	if not setscr.plttrc:
		if setscr.pltacc:
			rep.TRACKLINES(axs=ax,coord=acc,style='-',alfa=1.0*k_alfa,line_st='acc')
		if setscr.pltden:
			rep.TRACKLINES(axs=ax,coord=den,style='-',alfa=1.0*k_alfa,line_st='den')
	if setscr.plttrc:
		if setscr.pltacc:
			rep.TRACKLINES(axs=ax,coord=acc,style='-',alfa=1.0*k_alfa,line_st='col')
		if setscr.pltden:
			rep.TRACKLINES(axs=ax,coord=den,style='-',alfa=0.6*k_alfa,line_st='col')
	return acc,den,new_coord


plan1 = setscr.plane1 ;  plan2 = setscr.plane2 ;  plan3 = setscr.plane3	
if plan1:
	accepted1,denied1,new_coord1 = subroutine_for_lines(ax,coord,1,'-',1.0)
	accepted = accepted1 ;  denied = denied1
topcode = top.CREATE_CODE((top.NOH,top.NOT,top.NOV,top.NOP,top.P1H,top.PLH),dat,accepted1)    # CREATION OF TOPOLOGY CODE

if plan2:
	accepted2,denied2,new_coord2 = subroutine_for_lines(ax,coord,2,'--',0.9)
	accepted = accepted + accepted2 ;  denied = denied + denied2

if plan3:
	accepted3,denied3,new_coord3 = subroutine_for_lines(ax,coord,3,'dotted',0.8)
	accepted = accepted + accepted3 ;  denied = denied + denied3

header1 = ' ---> EVENT NUMBER '+str(ev)
header2 = '       A/D     Planes    v (mm/ns)     t coords (ns)       X coords (mm)       Y coords (mm)       Z coords (mm)'
if setscr.prinlog: print('\n '+header1); print(' '+header2)
if setsav.saveinf:
    svname = setsav.preffix+str(ev)+'.dat'
    svfile = open(cwd+'/'+setsav.savedrt+'/'+savedir+'/'+svname, "a")
    svfile.write('#'+header1+'\n')
    svfile.write('#'+('Detector sizes: %5.1f mm X %5.1f mm and %i planes' %(setdet.lenX,setdet.lenY,setdet.nplanes))+'\n')
    svfile.write('#'+('Tolerance= -%5.2f +%5.2f' %(setdet.tol_lo,setdet.tol_up))+'\n')
    svfile.write('#'+header2+'\n')
		
for line in accepted:
    p1=line[0][0]; p2=line[0][1] ;  v=line[1] ;  t1=line[5][0]; t2=line[5][1] 
    x1=line[2][0]; x2=line[2][1] ;  y1=line[3][0]; y2=line[3][1]  ;  z1=line[4][0]; z2=line[4][1]
    info1 = f"         A      {p1:2} {p2:2}     {v:7.1f}     {t1:7.1f} {t2:7.1f}"
    info2 = f"     {x1:7.1f} {x2:7.1f}     {y1:7.1f} {y2:7.1f}     {z1:7.1f} {z2:7.1f}"
    info = info1 + info2  # info about the accepted tracks
    if setscr.prinlog: print(info)
    if setsav.saveinf: svfile.write(info+'\n')
for line in denied:
    p1=line[0][0]; p2=line[0][1] ;  v=line[1] ;  t1=line[5][0]; t2=line[5][1] 
    x1=line[2][0]; x2=line[2][1] ;  y1=line[3][0]; y2=line[3][1]  ;  z1=line[4][0]; z2=line[4][1]
    info1 = f"         D      {p1:2} {p2:2}     {v:7.1f}     {t1:7.1f} {t2:7.1f}"
    info2 = f"     {x1:7.1f} {x2:7.1f}     {y1:7.1f} {y2:7.1f}     {z1:7.1f} {z2:7.1f}"
    info = info1 + info2  # info about the denied tracks
    if setscr.prinlog: print(info)
    if setsav.saveinf: svfile.write(info+'\n')
			
strcod = 'Topological classification: '+topcode
if setscr.prinlog: print('       '+strcod)
		
if setsav.saveinf: svfile.write('#'+strcod)
if setsav.saveinf: svfile.close() ;  print('    File saved!')

plt.suptitle('Data from '+setdat.fname+'\n'+'EVENT NUMBER '+str(ev)+'\n'+'Topology '+topcode)

if setsav.savefgr:
    figname = setsav.preffix+str(ev)+'.png'
    plt.savefig(cwd+'/'+setsav.savedrt+'/'+savedir+'/'+figname,dpi=setsav.resol)
    print('   Figure saved!')