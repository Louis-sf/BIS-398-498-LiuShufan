#  5.28 (Intro to Data Science: Survey Response Statistics) Twenty students
#were asked to rate on a scale of 1 to 5 the quality of the food in the student
#cafeteria, with 1 being “awful” and 5 being “excellent.” Place the 20
#responses in a list
#   1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3,
#   3, 2, 3, 3, 2, 5
#Determine and display the frequency of each rating. Use the built-in
#functions, statistics module functions and NumPy functions
#demonstrated in Section 5.17.2 to display the following response statistics:
#minimum, maximum, range, mean, median, mode, variance and standard
#deviation.

import numpy as np
import statistics as st
Survey  = [ 1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3,3, 2, 3, 3, 2, 5]

np.unique(Survey, return_counts= True)

minimum = min(Survey)
maximum = max(Survey)
Range = maximum-minimum
mean = np.mean(Survey)
median = np.median(Survey)
mode = st.mode(Survey)
varriance = np.var(Survey)
standard_deviation = np.std(Survey)

print('Minimum is: ', minimum)
print('Maximum is: ', maximum)
print('Range is: ', Range)
print('Mean is: ', mean)
print('Median is: ', median)
print('Mode is: ', mode)
print('Varriance is: ', varriance)
print('Standard deviation is: ', standard_deviation)
