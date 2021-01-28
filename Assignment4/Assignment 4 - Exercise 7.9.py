# 7.9 (Indexing and Slicing arrays) Create an array containing the
#values 1–15, reshape it into a 3-by-5 array, then use indexing and
#slicing techniques to perform each of the following operations:


import numpy as np

numbers = np.array([i for i in range(1,16)]).reshape(3,5)

#1. Select row 2.
numbers[2]
#2. Select column *4.
numbers[:, 4]
#3. Select rows 0 and 1.
numbers[0:2]
#4. Select columns 2–4.
numbers[:,2:5]
#5. Select the element that is in row 1 and column 4.
numbers[1,4]
#6. Select all elements from rows 1 and 2 that are in columns 0, 2
#and 4.
numbers[1:3, [0,2,4]]

#I am strictly follow the index number the question provided, for example, 
# row 1 is row[1], instead of row[0] which I normally interpreted as row1