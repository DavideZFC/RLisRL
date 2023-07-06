from functions.make_sincos_feature_map import make_sincos_feature_map
import numpy as np

def compute_singular_value():
    dmin = 2
    dmax = 9
    nmin = 2
    nmax = 8
    for d in range(dmin, dmax):
        #for n in range(nmin, nmax):

        A = make_sincos_feature_map(2**d+2, 2**d)
        _, s, _ = np.linalg.svd(A)
        print('the least singular value for d={} and n={} is {}, the largest is {}'.format(2**d,2**d+2,s[-1], s[0]))