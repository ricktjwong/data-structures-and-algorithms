def bubble_sort(A: list, n: int):
    for j in range(1, n):
        swapped = 0
        for i in range(n-j):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = 1
        if not swapped: break
    return A
