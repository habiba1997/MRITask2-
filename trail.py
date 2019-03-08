import numpy as np
import matplotlib.pyplot as plt
import math

"""rr = np.arange(-5, 20, 1)

def y(o): 
    return np.sin(o / 2.) * np.exp(o / 4.) + 6. * np.exp(-o / 4.)

plt.plot(rr, y(rr).astype(np.int))"""

"""
plt.show() 
a = np.matrix([[1, 2]])
b = np.matrix([[4, 1], [2, 2]])
c = np.matrix([5 , 3])
d = np.matrix ([0,0,4])

time  = np.arange(0, 20,1) #in sec but step in 1 msec
print(time[0])
print(time[15])

tryy =[]
a = np.append(tryy,1)
a = np.append(a,2)
a = np.append(a,3)


print(a)
tryy = np.matrix(a)

print(a)

print(a[1])"""

array = np.arange(0,30,1)
print(array)

array = array.reshape(10,3)
print(array)
print(array.transpose())
print(array[:,0])

print(array[0,:])

#array = np.matrix(array)
#print(array)
