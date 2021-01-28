#  (Horizontal and Vertical Stacking) Create the two-dimensional arrays
import numpy as np
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

#1. Use vertical stacking to create the 4-by-2 array named
#array3 with array1 stacked on top of array2.
array3 = np.vstack((array1,array2))

#2. Use horizontal stacking to create the 2-by-4 array named
#array4 with array2 to the right of array1.
array4 = np.hstack((array1, array2))

#3. Use vertical stacking with two copies of array4 to create a 4-
#by-4 array5.
array5 =np.vstack((array4,array4))

#4. Use horizontal stacking with two copies of array3 to create a
#4-by-4 array6.
array6 = np.hstack((array3,array3))
