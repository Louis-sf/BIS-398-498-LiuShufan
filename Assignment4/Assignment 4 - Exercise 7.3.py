#Create a 3-by-3 array
#containing the even integers from 2 through 18. Create a second 3-by-3
#array containing the integers from 9 down to 1, then multiply the first
#array by the second.
import numpy as np

array1 = np.array([i for i in range (2,19,2)])
array1 = array1.reshape(3,3)
array2 = np.array([i for i in range (9,0,-1)])
array2 = array2.reshape(3,3)

array1 * array2
