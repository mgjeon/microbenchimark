from numba import cuda
import numpy as np

@cuda.jit
def nested_loops_kernel(result_arr, n):
    i, j = cuda.grid(2)

    if i < n and j < n:
        cuda.atomic.add(result_arr, (0, 0), 0.00001)

n = 100000

result_arr = np.zeros((1, 1), dtype=np.float64)
d_result_arr = cuda.to_device(result_arr)

threadsperblock = (16, 16)
blockspergrid_x = int(np.ceil(n / threadsperblock[0]))
blockspergrid_y = int(np.ceil(n / threadsperblock[1]))
blockspergrid = (blockspergrid_x, blockspergrid_y)

nested_loops_kernel[blockspergrid, threadsperblock](d_result_arr, n)

result_arr = d_result_arr.copy_to_host()

print(f"Result: {result_arr[0, 0]}")