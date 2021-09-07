# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:02:32 2021

@author: dviqu
"""

formats= '\n(i)          -> simple_electrons_at_100MeV.txt: mode1'+\
'\n(i)          -> tragas_sample.txt: mode2'

description = '\n       *****\n'+\
'(i)tragas3D is developed for the 3D visualization of showers hitting a trasgo'+\
' detector. Each hit is represented by colouring the corresponding cell of the detector, and the'+\
' possible tracks of the particles are represented by straight lines.'+\
' \n(i) More information in <<README.md>>'+\
' \n \n(i) -- Developed by Daniel Viqueira at the IGFAE (Universidade de Santiago de Compostela) -- \n       *****\n'

message1 = '\n(i) MODE A. SELECTION BY EVENT NUMBER'+\
'\n(i) Separate single events by commas and indicate intervals by dash'+\
'\n(i) Examples:'+\
'\n(i)   -> 6         : returns event 6'+\
'\n(i)   -> 6,8       : returns events 6 and 8'+\
'\n(i)   -> 6,8-10    : returns events 6,8,9 and 10 \n'

message2 = '\n(i) MODE B. SELECTION BY TOPOLOGY'+\
'\n(i)    Introduce only those digits of interest. The rest can be filled by dash'+\
'\n(i)    Examples:'+\
'\n(i)    -> 3----- returns all events with this first digit;'+\
'\n(i)    -> 31---- returns all events with these two first digits'+\
'\n(i)    -> -4-1-0 returns all events with these second, fourth and sixth digits'+\
'\n(i)    Remember that the code has 6 digits \n'

message3 = '\n(i) Go to folder <<settings>> for configuration'+\
'\n(i)    -> <<detector.py>> contains the size and number of plates of the TRASGO detector'+\
'\n(i)       and the tolerances which determine the interval of velocities at which a track can be'+\
'\n(i)       accepted.'+\
'\n(i)    -> <<data.py>> contains the name of the file with data to read and the format of lecture.'+\
'\n(i)       Format of lecture and format of file must coincide:'+formats+\
'\n(i)    -> <<screen.py>> allows to activate or desactivate outputs by screen (prints and plots)'+\
'\n(i)       and style of tracks and pads'+\
'\n(i)    -> <<saving.py>> allows to activate saving of files with information of tracks and plots \n'


def help_menu():
	message = input(' Press ENTER to see main description of the program, <mode> for help about'+
	' modes of visualization, <config> for help about settings ')
	if message == '':
		print(description)
	if message == 'mode':
		print(message1)
		control = input(' Press ENTER')
		print(message2)
	if message == 'config':
		print(message3)
	return
