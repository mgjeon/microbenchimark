def compute_result(int n):
    cdef int i, j
    cdef double result = 0.0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            result += 0.00001

    return result