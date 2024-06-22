using Base.Threads

function nested_loops(n)
    result = Atomic{Float64}(0.0)

    @threads for i in 1:n
        local_result = 0.0
        @inbounds @simd for j in 1:n
            local_result += 0.00001
        end
        atomic_add!(result, local_result)
    end

    return result[]
end

n = 100000
result = nested_loops(n)

println("Result: ", result)
