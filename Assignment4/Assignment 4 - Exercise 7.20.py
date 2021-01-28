# 7.20 (Performance Analysis) 



import numpy as np
# for only one repetition

%timeit rolls_array = np.random.randint(1, 7, 1)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1)]

# for 10
%timeit rolls_array = np.random.randint(1, 7, 10)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0,10)]
# for 100
%timeit rolls_array = np.random.randint(1, 7, 100)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 100)]
# for 1000
%timeit rolls_array = np.random.randint(1, 7, 1000)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1000)]
#for 10,000
%timeit rolls_array = np.random.randint(1, 7, 10000)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 10000)]

#for 100,000 
%timeit rolls_array = np.random.randint(1, 7, 100000)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 100000)]

#for 1,000,000
%timeit rolls_array = np.random.randint(1, 7, 1000000)
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1000000)]

