from numba import njit

@njit(fastmath=True)
def compute_result(n):
    result = 0.0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += 0.00001
    return result

n = 100000
result = compute_result(n)

print("Result: ", result)