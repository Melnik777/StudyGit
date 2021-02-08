import numpy as np


def MatriX(A):
    A = list(A)
    if len(A[0]) == 2:
        deter = (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
        return deter
    else:
        c = 0
        for i in range(len(A[0])):
            G = [np.delete(s, [i]) for s in A[1:len(A[0])]]
            c += (A[0][i] * ((-1) ** (i + 2)) * (MatriX(G)))
            H = c
        return H


tor = 0
np.random.seed(7)

M = np.random.randint(5, size=(5, 5))
print(M)
print(MatriX(M))

