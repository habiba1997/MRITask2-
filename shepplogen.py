import numpy as np
from matplotlib import pyplot as plt

import numpy as np
import math
from matplotlib import pyplot as plt
# a function that returns T1 ( recovery time ) based on the intensity
def createT1(intensity):

    if intensity == 100: #Gray matter
        T1=900
        
    elif intensity == 255: #white matter
        T1= 510
       
    elif intensity == 200: #muscle
        T1=900
       
    elif intensity == 120 : #fat
        T1=300
        
    elif intensity == 25: #protein
        T1=250
        
    #elif intensity == 0: #Black => air
    #    T1=1
        
    else: # general case for any phantom whatever its intensity 
        T1 = (7.5*intensity) + 50

    return T1

def createPD(intensity):
        if intensity ==0:
            return 1
        else:
            return (1/255)*intensity 

# a function that returns T2 ( decay time ) based on the intensity
def createT2(intensity):

    if intensity == 100: #Gray matter
        T2 =90
   
    elif intensity == 255: #white matter       
        T2 =70

    elif intensity == 200: #muscle        
        T2 = 50

    elif intensity == 120 : #fat        
        T2 = 100

    elif intensity == 25: #protein       
        T2 = 30

    #elif intensity == 0: #Black => air        
    #    T2=0

    else: # general case for any phantom whatever its intensity 
        T2 = 0.5*intensity+10

    return T2


#self.pixmap5 = QtGui.QPixmap(self.fileName4)
#                self.ui.image.setPixmap(self.pixmap5)
# self.img[self.x, self.y]

def rotationAroundYaxisMatrix(theta,vector):
            vector = vector.transpose()
            theta = (math.pi / 180) * theta
            R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
            R = np.dot(R, vector)
            R = R.transpose()
            return np.matrix(R)


def rotationAroundZaxisMatrixXY(theta,vector): #time = self.time
            vector = vector.transpose()
            theta = (math.pi / 180) * theta
            XY = np.matrix([[np.cos(theta),-np.sin(theta),0], [np.sin(theta), np.cos(theta),0],[0, 0, 1]])
            XY = np.dot(XY,vector)
            XY = XY.transpose()
            return np.matrix(XY) 


def recoveryDecayEquation(T1,T2,PD,vector,time):
            vector = vector.transpose()
            Decay =np.matrix([[np.exp(-time/T2),0,0],[0,np.exp(-time/T2),0],[0,0,np.exp(-time/T1)]])
            Decay = np.dot(Decay,vector)
        
            Rec= np.dot(np.matrix([[0,0,(1-(np.exp(-time/T1)))]]),PD)
            Rec = Rec.transpose()
            Decay = np.matrix(Decay)
            Rec =  np.matrix(Rec)    
        
            RD  = Decay + Rec
            RD = RD.transpose()
            return RD

def phantom (n = 256, p_type = 'Modified Shepp-Logan', ellipses = None):
	"""
	 phantom (n = 256, p_type = 'Modified Shepp-Logan', ellipses = None)
	
	Create a Shepp-Logan or modified Shepp-Logan phantom.

	A phantom is a known object (either real or purely mathematical) 
	that is used for testing image reconstruction algorithms.  The 
	Shepp-Logan phantom is a popular mathematical model of a cranial
	slice, made up of a set of ellipses.  This allows rigorous 
	testing of computed tomography (CT) algorithms as it can be 
	analytically transformed with the radon transform (see the 
	function `radon').
	
	Inputs
	------
	n : The edge length of the square image to be produced.
	
	p_type : The type of phantom to produce. Either 
	  "Modified Shepp-Logan" or "Shepp-Logan".  This is overridden
	  if `ellipses' is also specified.
	
	ellipses : Custom set of ellipses to use.  These should be in 
	  the form
	  	[[I, a, b, x0, y0, phi],
	  	 [I, a, b, x0, y0, phi],
	  	 ...]
	  where each row defines an ellipse.
	  I : Additive intensity of the ellipse.
	  a : Length of the major axis.
	  b : Length of the minor axis.
	  x0 : Horizontal offset of the centre of the ellipse.
	  y0 : Vertical offset of the centre of the ellipse.
	  phi : Counterclockwise rotation of the ellipse in degrees,
	        measured as the angle between the horizontal axis and 
	        the ellipse major axis.
	  The image bounding box in the algorithm is [-1, -1], [1, 1], 
	  so the values of a, b, x0, y0 should all be specified with
	  respect to this box.
	
	Output
	------
	P : A phantom image.
	
	Usage example
	-------------
	  import matplotlib.pyplot as pl
	  P = phantom ()
	  pl.imshow (P)
	
	References
	----------
	Shepp, L. A.; Logan, B. F.; Reconstructing Interior Head Tissue 
	from X-Ray Transmissions, IEEE Transactions on Nuclear Science,
	Feb. 1974, p. 232.
	
	Toft, P.; "The Radon Transform - Theory and Implementation", 
	Ph.D. thesis, Department of Mathematical Modelling, Technical 
	University of Denmark, June 1996.
	
	"""
	
	if (ellipses is None):
		ellipses = _select_phantom (p_type)
	elif (np.size (ellipses, 1) != 6):
		raise AssertionError ("Wrong number of columns in user phantom")
	
	# Blank image
	p = np.zeros ((n, n))

	# Create the pixel grid
	ygrid, xgrid = np.mgrid[-1:1:(1j*n), -1:1:(1j*n)]

	for ellip in ellipses:
		I   = ellip [0]
		a2  = ellip [1]**2
		b2  = ellip [2]**2
		x0  = ellip [3]
		y0  = ellip [4]
		phi = ellip [5] * np.pi / 180  # Rotation angle in radians
		
		# Create the offset x and y values for the grid
		x = xgrid - x0
		y = ygrid - y0
		
		cos_p = np.cos (phi) 
		sin_p = np.sin (phi)
		
		# Find the pixels within the ellipse
		locs = (((x * cos_p + y * sin_p)**2) / a2 
              + ((y * cos_p - x * sin_p)**2) / b2) <= 1
		
		# Add the ellipse intensity to those pixels
		p [locs] += I

	return p


def _select_phantom (name):
	if (name.lower () == 'shepp-logan'):
		e = _shepp_logan ()
	elif (name.lower () == 'modified shepp-logan'):
		e = _mod_shepp_logan ()
	else:
		raise ValueError ("Unknown phantom type: %s" % name)
	
	return e


def _shepp_logan ():
	#  Standard head phantom, taken from Shepp & Logan
	return [[   2,   .69,   .92,    0,      0,   0],
	        [-.98, .6624, .8740,    0, -.0184,   0],
	        [-.02, .1100, .3100,  .22,      0, -18],
	        [-.02, .1600, .4100, -.22,      0,  18],
	        [ .01, .2100, .2500,    0,    .35,   0],
	        [ .01, .0460, .0460,    0,     .1,   0],
	        [ .02, .0460, .0460,    0,    -.1,   0],
	        [ .01, .0460, .0230, -.08,  -.605,   0],
	        [ .01, .0230, .0230,    0,  -.606,   0],
	        [ .01, .0230, .0460,  .06,  -.605,   0]]

def _mod_shepp_logan ():
	#  Modified version of Shepp & Logan's head phantom, 
	#  adjusted to improve contrast.  Taken from Toft.
	return [[   1,   .69,   .92,    0,      0,   0],
	        [-.80, .6624, .8740,    0, -.0184,   0],
	        [-.20, .1100, .3100,  .22,      0, -18],
	        [-.20, .1600, .4100, -.22,      0,  18],
	        [ .10, .2100, .2500,    0,    .35,   0],
	        [ .10, .0460, .0460,    0,     .1,   0],
	        [ .10, .0460, .0460,    0,    -.1,   0],
	        [ .10, .0460, .0230, -.08,  -.605,   0],
	        [ .10, .0230, .0230,    0,  -.606,   0],
	        [ .10, .0230, .0460,  .06,  -.605,   0]]

#def ?? ():
#	# Add any further phantoms of interest here
#	return np.array (
#	 [[ 0, 0, 0, 0, 0, 0],
#	  [ 0, 0, 0, 0, 0, 0]])

def createT1(intensity):

    if intensity == 100: #Gray matter
        T1=900
        
    elif intensity == 255: #white matter
        T1= 510
       
    elif intensity == 200: #muscle
        T1=900
       
    elif intensity == 120 : #fat
        T1=300
        
    elif intensity == 25: #protein
        T1=250
        
    #elif intensity == 0: #Black => air
    #    T1=1
        
    else: # general case for any phantom whatever its intensity 
        T1 = (7.5*intensity) + 50

    return T1

def createPD(intensity):
        if intensity ==0:
            return 1
        else:
            return (1/255)*intensity 

# a function that returns T2 ( decay time ) based on the intensity
def createT2(intensity):

    if intensity == 100: #Gray matter
        T2 =90
   
    elif intensity == 255: #white matter       
        T2 =70

    elif intensity == 200: #muscle        
        T2 = 50

    elif intensity == 120 : #fat        
        T2 = 100

    elif intensity == 25: #protein       
        T2 = 30

    #elif intensity == 0: #Black => air        
    #    T2=0

    else: # general case for any phantom whatever its intensity 
        T2 = 0.5*intensity+10

    return T2

def mappingT1 (T1): #T1 in msec assumption
        return (T1-500)/6

def mappingT2 (T2):  #T1 in msec assumption
        return (T2-20)/2


img = phantom(n=64)
T1 = np.zeros((img.shape[0],img.shape[1]))
T2= np.zeros((img.shape[0],img.shape[1]))


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        T1[i,j]=mappingT1(createT1(img[i,j]))
        T2[i,j]=mappingT2(createT2(img[i,j]))


import scipy.io

output = {
		"Phantom" : img,
        "T1": T1,
        "T2":T2,
	}
scipy.io.savemat('shapeloggin64', output)






TE = 50
vector= np.matrix ([0,0,1]) #da range sabt
theta = 90 
TR = 3000


Kspace =  np.zeros((9,9),dtype=np.complex_)

signal = [[[0 for k in range(3)] for j in range(img.shape[0])] for i in range(img.shape[1])]
start = True

for Ki in range(Kspace.shape[0]):
    #move in each image pixel
    print('Ki: ',Ki)
    
    if start :
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                signal[i][j] =  rotationAroundYaxisMatrix(theta,vector)
                signal[i][j] = signal[i][j] * np.exp(-TE/createT2(img[i,j]))
    else:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                signal[i][j] =  rotationAroundYaxisMatrix(theta,np.matrix(signal[i][j]))
                signal[i][j] =  signal[i][j] * np.exp(-TE/createT2(img[i,j]))
    
    # for kspace column
    for Kj in range (Kspace.shape[1]):
        print('Kj: ',Kj)
        GxStep = ((2 * math.pi) / Kspace.shape[0]) * Kj
        GyStep = ((2 * math.pi) /Kspace.shape[1]) * Ki
        
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                totalTheta = (GxStep*j)+ (GyStep*i)
                z = abs(complex(np.ravel(signal[i][j])[0],np.ravel(signal[i][j])[1]))
                Kspace[Ki,Kj]= Kspace[Ki,Kj] + (z * np.exp(1j*totalTheta))
       


    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            signal[i][j] =  rotationAroundYaxisMatrix(theta, vector)
            signal[i][j] = recoveryDecayEquation(createT1(img[i,j]),createT2(img[i,j]),1,np.matrix(signal[i][j]),TR)
            signal[i][j] = [[0,0,np.ravel(signal[i][j])[2]]]
            start = False
    
plt.imshow(img, cmap="gray")
plt.show()
plt.imshow(abs(Kspace), cmap="gray")
plt.show()

print(Kspace)
Kspacefft = np.fft.fft2(Kspace)
Kspaceifft = np.fft.ifft2(Kspace)

plt.imshow(abs(Kspacefft),cmap="gray" )
plt.show()

    


plt.imshow(abs(Kspaceifft), cmap="gray")
plt.show()

