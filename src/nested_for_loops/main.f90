program NestedLoops
    implicit none
    integer :: n, i, j
    real(8) :: result

    n = 100000
    result = 0.0

    do i = 1, n
        do j = 1, n
            result = result + 0.00001
        end do
    end do

    print *, "Result: ", result
end program NestedLoops