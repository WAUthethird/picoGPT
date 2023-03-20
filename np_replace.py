"""
NumPy Replacement Functions, written in pure Python
Please don't use these for anything remotely serious
"""
import numpy as np

def matmul(inputmatrix1, inputmatrix2):
    return([[sum(a * b for a, b in zip(i, f)) for f in zip(*inputmatrix2)] for i in inputmatrix1])

def matadd(inputmatrix1, inputmatrix2):
    if not isinstance(inputmatrix1[0], list):
        return([[inputmatrix1[f] + inputmatrix2[i][f] for f in range(len(inputmatrix1))] for i in range(len(inputmatrix2))])
    elif not isinstance(inputmatrix2[0], list):
        return([[inputmatrix2[f] + inputmatrix1[i][f] for f in range(len(inputmatrix2))] for i in range(len(inputmatrix1))])
    else:
        return([[inputmatrix1[i][f] + inputmatrix2[i][f] for f in range(len(inputmatrix2[0]))] for i in range(len(inputmatrix1))])


def main():
    testmat1 = [[1, 1, 1, 5, 5], [1, 1, 1, 5, 5], [1, 2, 1, 5, 5.7], [1, 2, 3, 5, 5], [1, 2, 3, 5, 5]]
    testmat2 = [[1, 1, 1, 5, 5], [1, 1, 1, 5, 5], [1, 2, 1, 5, 5], [1, 2, 3, 5, 5], [1, 2, 3, 5, 5]]
    print(matadd(testmat1, testmat2))
    print(np.array(testmat1) + np.array(testmat2))
    print(matmul(testmat1, testmat2))
    print(np.array(testmat1) @ np.array(testmat2))


if __name__ == "__main__":
    main()