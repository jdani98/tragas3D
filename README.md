# tragas3D
##### Program for the 3D visualization of high multiplicity showers hitting a TRASGO detector

## 1. How to run tragas3D
It is neccessary to have installed the latest version of python, _python 3_.
To run tragas3D in a command prompt, use as pwd tragas3D directory and type **python3 main.py**.
The directory must contain a file with data formatted with one of the formats that is supported by the routines inside _modules/reading.py_.

## 2. Modes of visualization
Once the program has started, the user must choose the mode of visualization:
  * **Mode A. Selection by event number**: The events are enumerated one by one in the data file and the user can choose one or more events when asked. To introduce the desired numbers, one can introduce the both the limits of an interval separated by dashes and a list of single events. For example,
  ```
   > 6         : returns event 6
   > 6,8       : returns events 6 and 8
   > 6,8-10    : returns events 6,8,9 and 10
  ```
  * **Mode B. Selection by topology**: The events can be classified by a 6-digit code which basically determines the number of hits and tracks and the planes. _modules/topology.py_ contains the subroutines to compute each digit and the 6 digits which shape the code are indicated in _main.py_. The selection can restrict only some digits, thus the user can let be free the rest of them by writing a non-alphanumeric character. For example,
  ```
   > 3----- returns all events with this first digit
   > 31---- returns all events with these two first digits
   > -4-1-0 returns all events with these second, fourth and sixth digits
  ```

## 3. Settings
The directory _settings_ contains all the files with the previous configuration that can be changed.

### 3.1. Detector
The detector consists on several parallel planes, each one composed by a 2D array of cells ("pads"). Each hit will be assumed to be produced at the center of one cell. The variables to configure the detector are located at _settings/detector.py_. The user should make sure that the configuration corresponds with the real detector of the data. The following variables can be changed: number of pads and dimension of pads in X and Y dimension, array with position of each plane in the _z_ direction, total number of planes, total length of the detector in both directions and tolerance. The _tolerance_ is understood as the fraction of the speed of light until which a track can travel to be accepted.

### 3.2. Data
Go to _settings/data.py_ to introduce the name of the file with the data and select the mode of lecture. Recall that the formats must coincide.

### 3.3. Outputs by screen
Go to _settings/screen.py_ to determine the appearance of the outputs by screen. The user can activate and desactivate the graphics and some elements of them. The hit pads can be coloured in function of their delay. The _delay_ is defined as the time difference between the real hit and a hypothetical hit that came from the first hit at the speed of light. The tracks can be configured to be painted with colour which depends on their velocity. If the velocity is out of the limits given by the tolerance, the track is denied. The user can decide to watch those denied tracks or not.
To desactivate the options write _False_.

### 3.4. Saving files
The plots and the information about the computed tracks can be saved in a folder named _OUTPUTS_ by default. To determine the preffix of the name of the output files and the resolution of the graphics go to _settings/saving.py_. If some option of saving files is activated, at the beginning of the program the name of the directory to save will be requested.

## 4. More about tracks
The tracks are simply straight segments which join two hits. The first hits which are joined are those from adjacent planes, as a particle is not supossed to transverse a plane without being detected. The hits that cannot be joined by tracks between adjacent planes are matched by tracks traversing some plane, if _plane2 _and _plane3_ are activated at _settings/screen.py_.

## 5. To be continue...
This program is susceptible to more changes...
