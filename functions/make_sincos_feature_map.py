import numpy as np




def make_sincos_feature_map(n, d, x=None):

    # in case of no specification I choose equispaced arms
    if x == None:
        x = np.linspace(-1,1,n)


    feature_matrix = np.zeros((n, d))

    # build linear features from the arms
    for j in range(d):
        if j == 0:
            # the constant tem is normalized to have L2 norm equal to one on [-1, 1]
            feature_matrix[:,j] = (1/2)**0.5
        elif j%2 == 1:
            eta = j//2+1
            feature_matrix[:,j] = np.sin(np.pi*eta*x)
        else:
            eta = j//2
            feature_matrix[:,j] = np.cos(np.pi*eta*x)

    return feature_matrix