import numpy as np

def difdiv(x,y) :
    x = np.array(x)
    y = np.array(y)
    x.astype(float)
    y.astype(float)
    n = len(x)
    F = np.zeros((n,n), dtype=float)
    b = np.zeros(n) 
    for i in range(0,n):
        F[i,0]=y[i]

    for j in range(1, n):
        for i in range(j,n):
            F[i,j] = float(F[i,j-1]-F[i-1,j-1])/float(x[i]-x[i-j])

    for i in range(0,n):
        b[i] = F[i,i]

    return np.array(b) # return an array of coefficient

def Eval(a, x, r):
    x.astype(float)
    n = len( a ) - 1
    temp = a[n]
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp # return the y_value interpolation
