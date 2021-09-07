#!usr/bin/python3

#import numpy as np
import settings.detector as setdet
#import settings.screen   as setscr
#import modules.timing    as tim
#import params.constants  as cts

def DATA_READING1(fname):
	"""
	subroutine to read data in format <<simple_electrons_at_100MeV.txt>>
	"""
	DATA = open('simple_electrons_at_100MeV.txt').readlines()[4:]
	data = []
	i=0
	for line in DATA:
		sline = line.split()
		if len(sline) == 8:
			data.append([])
			Event_number  = int(sline[0])
			Ini_E         = float(sline[1])
			Ini_X         = float(sline[2])
			Ini_Y         = float(sline[3])
			Ini_Z         = float(sline[4])
			Ini_Theta     = float(sline[5])
			Ini_Phi       = float(sline[6])
			Number_of_hits= int(sline[7])
			data[i].append([Event_number,Ini_E,Ini_X,Ini_Y,Ini_Z,Ini_Theta,Ini_Phi,Number_of_hits])
			i+=1
		else:
			Plane_h = int(sline[0])
			X_h     = float(sline[1])
			Y_h     = float(sline[2])
			Z_h     = float(sline[3])
			Time_h  = float(sline[4])
			data[i-1].append([Plane_h,X_h,Y_h,Z_h,Time_h])
	return data



def DATA_READING2(fname):
	"""
	subroutine to read data in format <<tragas_sample.txt>>
	"""
	nheader = 4
	DATA = open(fname).readlines()[nheader:]
	data = [[]]

	nTRBs = [2,0,1]   # correspondence between nTRB and Ti
	#Ti   = [1,2,3]   # here we consider the three planes that work. 3 is really the plane T4

	NLINES = len(DATA)
	iline = 0
	nevent = 1
	data[0].append([nevent, 0, 0, 0, 0, 0, 0, 0])
	nhits = 0
	while iline < NLINES:
		sline = (DATA[iline]).split()
		curevnt = int(sline[0]) ;  nTRB = int(sline[1])
		row = int(sline[2]) ;  col = int(sline[3])
		time = float(sline[4]) ;  charge = float(sline[5])
		if curevnt == nevent:
			iP = nTRBs.index(nTRB)
			z = setdet.Zplates[iP]
			x = (col-setdet.nPADSX/2-1./2.)*setdet.WPADX
			y = (row-setdet.nPADSY/2-1./2.)*setdet.WPADY  # here the centre of each plane is in (0,0)
			data[nevent-1].append([iP+1,x,y,z,time])
			iline += 1
			nhits += 1
		else:
			data[nevent-1][0][7] = nhits
			nevent = curevnt
			data.append([])
			data[nevent-1].append([nevent, 0, 0, 0, 0, 0, 0, 0])
			nhits = 0
	data[nevent-1][0][7] = nhits
	return data


"""
MODE of STORAGE:
[ [ [Event_Number 1,Ini_E[MeV],Ini_X[mm],Ini_Y[mm],Ini_Z[mm],Ini_Theta,Ini_Phi,Number_of_hits],
    [Plane_h,X_h[mm],Y_h[mm],Z_h[mm],Time_h[ns]]
    .
    .
    .
    [Plane_i,X_i[mm],Y_i[mm],Z_i[mm],Time_i[ns]]
  ]
  .
  .
  .
  [ [Event_Number N,Ini_E[MeV],Ini_X[mm],Ini_Y[mm],Ini_Z[mm],Ini_Theta,Ini_Phi,Number_of_hits],
    [Plane_h,X_h[mm],Y_h[mm],Z_h[mm],Time_h[ns]]
    .
    .
    .
    [Plane_i,X_i[mm],Y_i[mm],Z_i[mm],Time_i[ns]]
  ]
]
"""
