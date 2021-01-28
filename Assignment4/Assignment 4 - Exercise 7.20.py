# 7.20 (Performance Analysis) 
import timeit
import random
import numpy
counts = [10**x for x in range(0,7)];
def gen_list(size):
   l = []
   for i in range(size):
       l.append(random.randint(0,7))

def gen_array(size):
   l = numpy.random.rand(size)

print("Number of values\tList average execution time\tarray average execution time")
for i in counts:
  
   list_timer = timeit.Timer(lambda: gen_list(i))
   array_timer = timeit.Timer(lambda: gen_array(i))
   print(f"{i}\t\t\t{list_timer.timeit(5)}\t\t{array_timer.timeit(5)}"


























import random
import numpy as np

counts = [10**x for x in range(0,7)];


def gen_list(size):
   l = []
   for i in range(size):
       l.append(random.randint(0,7))

def gen_array(size):
   l = np.random.rand(size)

print("Number of values\tList average execution time\tarray average execution time")
for i in counts:
   list_timer = %timeit gen_list(i)
   array_timer = %timeit.Timer(lambda: gen_array(i))
   print(f"{i}\t\t\t{list_timer.timeit(5)}\t\t{array_timer.timeit(5)}")