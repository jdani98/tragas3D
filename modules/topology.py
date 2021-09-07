# FUNCTIONS FOR TOPOLOGY

import numpy as np
import settings.detector as setdet

def CREATE_CODE(digits,data,coord):
	"""
	Function to create code from the selected digits
	INPUTS:    -> digits: tuple with name of digits to make the code
	           -> coord:  array with coordinates of hits
	           -> data:   array with coordinates of tracks
	OUTPUT:    -> code:   string with the code
	"""
	
	code = ''
	for function in digits:
		digit = function(data,coord)
		code += str(hex(digit)[-1])
	
	return code



def NOH(dat,coord):
	"""
	Number of hits
	"""
	return dat[0][7]



def N2P(dat,coord):
	"""
	Total number of tracks between two adjacent planes
	"""
	return len(coord)



def P1H(dat,coord):
    """
    First plane with hits
    """
    hplanes = np.array(dat[1:])[:,0]
    return int(np.min(hplanes))



def PLH(dat,coord):
    """
    Last plane with hits
    """
    hplanes = np.array(dat[1:])[:,0]
    return int(np.max(hplanes))


def NOV(dat,coord):
	"""
	Number of vertices
	"""
	points1 = [[coordi[2][0],coordi[3][0],coordi[4][0]] for coordi in coord]
	no_rep = []
	for item in points1:
		if item not in no_rep:
			no_rep.append(item)
	return len(points1) - len(no_rep)



def NOHLP(dat,coord):
	"""
	Number of hits in the last plane
	"""
	number = 0
	for item in dat[1:]:
		if item[0] == setdet.nplanes: number += 1
	return number



def NOH1P(dat,coord):
    """
    Number of hits in the first plane
    """
    number = 0
    for item in dat[1:]:
        if item[0] == 1: number += 1
    return number



def NOH3P(dat,coord):
    """
    Number of hits in the third plane
    """
    number = 0
    for item in dat[1:]:
        if item[0] == 3: number += 1
    return number



def NOH4P(dat,coord):
    """
    Number of hits in the fourth plane
    """
    number = 0
    for item in dat[1:]:
        if item[0] == 4: number += 1
    return number



def NOT(dat,coord):
	"""
	Number of tracks
	"""
	return len(coord)



def NOP(dat,coord):
	"""
	Number of hit planes
	"""
	hplanes = [dati[0] for dati in dat[1:]]
	return len(set(hplanes))



