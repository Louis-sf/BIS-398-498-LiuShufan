# (Flattening arrays with flatten vs. ravel) Create a 2-by-3
#array containing the first six powers of 2 beginning with 2 . Flatten the
#array first with method flatten, then with ravel. In each case,
#display the result then display the original array to show that it was
#unmodified.

import numpy as np

twoexp = np.array([ 2 ** i for i in range(1,7)]).reshape(2,3)

#flatten

flattened = twoexp.flatten()

print('Flattened: \n', flattened)
print('Original: \n', twoexp)

#ravel

raveled  = twoexp.ravel()

print('Raveled: \n', raveled)
print('Original: \n', twoexp)