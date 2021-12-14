import numpy as np

def Newton_method(F, DF, x, num_steps):
    """ Applies the Newton's method FPI num_steps
    times to F with initial guess x0. """
    for k in range(num_steps):
        x = x- np.linalg.solve(DF(x), F(x)) #use numpy's solve command
        print(k, x)
        
#input to Newton's method
# a function F(x); its Jacobian DF
# and an initial guess x = x0

def F(x):
    """ F is the function whose roots we will approximate """
    return np.array([x[0]**2 - 2*x[0] - x[1] + 1, x[0]**2 + x[1]**2 - 1])

def J(x):
    """ J is the Jacobian matrix of F. """
    return np.array([[2*x[0] - 2, -1],
                     [2*x[0], 2* x[1]]])

x = np.array([1,3])

Newton_method(F, J, x, 5)
        
            