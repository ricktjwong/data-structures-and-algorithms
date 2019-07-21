def selection_sort(A: list, n: int):
    for i in range(n-1):
        min_idx = i
        # Find minimum in list at each iteration
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A
