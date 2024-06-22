function nested_loops(n)
    result = 0.0

    for i in 1:n
        for j in 1:n
            result += 0.00001
        end
    end

    return result
end

n = 100000
result = nested_loops(n)

println("Result: ", result)