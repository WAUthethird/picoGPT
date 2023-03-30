"""
NumPy Replacement Functions, written in pure Python
Please don't use these for anything remotely serious
"""

#import numpy as np
import math

def matmul(inputarray1, inputarray2):
    return([[sum(a * b for a, b in zip(i, f)) for f in zip(*inputarray2)] for i in inputarray1])

def matmul_elem(inputarray1, inputarray2):
    if not isinstance(inputarray1[0], list):
        return([[inputarray1[f] * inputarray2[i][f] for f in range(len(inputarray1))] for i in range(len(inputarray2))])
    elif not isinstance(inputarray2[0], list):
        return([[inputarray2[f] * inputarray1[i][f] for f in range(len(inputarray2))] for i in range(len(inputarray1))])
    else:
        return([[inputarray1[i][f] * inputarray2[i][f] for f in range(len(inputarray2[0]))] for i in range(len(inputarray1))])

def matadd(inputarray1, inputarray2):
    if not isinstance(inputarray1[0], list):
        return([[inputarray1[f] + inputarray2[i][f] for f in range(len(inputarray1))] for i in range(len(inputarray2))])
    elif not isinstance(inputarray2[0], list):
        return([[inputarray2[f] + inputarray1[i][f] for f in range(len(inputarray2))] for i in range(len(inputarray1))])
    else:
        return([[inputarray1[i][f] + inputarray2[i][f] for f in range(len(inputarray2[0]))] for i in range(len(inputarray1))])
    
def matsub(inputarray1, inputarray2):
    return([[inputarray1[i][f] - inputarray2[i][0] for f in range(len(inputarray1[i]))] for i in range(len(inputarray1))])

def matdiv(inputarray1, inputarray2):
    return([[inputarray1[i][f] / inputarray2[i][0] for f in range(len(inputarray1[i]))] for i in range(len(inputarray1))] if len(inputarray2) > 1 else [[inputarray1[i][f] / inputarray2[0][0] for f in range(len(inputarray1[i]))] for i in range(len(inputarray1))])

def matmax(inputarray):
    return([[max(i)] for i in inputarray])

def matsum(inputarray):
    return([[sum(i)] for i in inputarray])

def matexp(inputarray):
    return([matexp(i) for i in inputarray] if isinstance(inputarray, list) else math.exp(inputarray))

def matmean(inputarray):
    return([[sum(i) / len(i)] for i in inputarray])

def matvar(inputarray):
    return([[sum((f - (sum(i) / len(i))) ** 2 for f in i) / len(i)] for i in inputarray])

def matsplit(inputarray, indices):
    return([[[f[q:q + (len(f) // indices)] for q in range(0, len(f), (len(f) // indices))][i] for f in inputarray] for i in range(indices)])

def mattranspose(inputarray):
    return([list(i) for i in zip(*inputarray)] if len(inputarray) > 1 else [[f] for f in inputarray[0]])

def mattri(size):
    return([[-0.e+00 if j <= i - 0 else -1.e+10 for j in range(size)] for i in range(size)]) # I know I'm cheesing this one by combining multiple operations - thing is, it's only used once. Lemme have this one.

def main():
    testmat1 = [[1, 1, 1, 5, 5], [1, 1, 1, 5, 5], [1, 2, 1, 5, 5.7], [1, 2, 3, 5, 5]]
    testmat2 = [[1, 1, 1, 5, 5], [1, 1, 1, 5, 5], [1, 2, 1, 5, 5], [1, 2, 3, 5, 5]]
    testmat3 = [1, 2, 43, 4, 432]


if __name__ == "__main__":
    main()