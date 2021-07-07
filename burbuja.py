def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def burbuja_optimizado(A):
    i = 0
    n = len(A)
    ordered = False
    while i < n and not ordered:
        i = i + 1
        ordered = True
        for j in range(n-i):
            if A[j] > A[j+1]:
                ordered = False
                swap(A, j, j+1)


array1 = [8, 3, 1 ,56, 2, 43, 656, 7]

array2 = [8, 3, 1 ,56, 2, 43, 656, 7]

burbuja(array1)

print('Resultado de burbuja normal es de:    ', array1)

burbuja_optimizado(array2)

print('Resultado de burbuja optimizada es de ', array2)

