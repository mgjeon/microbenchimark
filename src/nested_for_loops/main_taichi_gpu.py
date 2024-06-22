import taichi as ti

ti.init(arch=ti.gpu)

n = 100000
result = ti.field(dtype=ti.f64, shape=())

@ti.kernel
def nested_loops(n: ti.i32):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result[None] += 0.00001

nested_loops(n)

print("Result: ", result[None])
