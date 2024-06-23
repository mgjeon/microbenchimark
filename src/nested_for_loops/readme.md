# Environment
Windows 11 (23H2), PowerShell, AMD Ryzen 5 5600X, NVIDIA RTX 3060

[setup](env.md)

# Psuedo Code

```
Program NestedLoops
    Set n = 100000
    Set result = 0.0

    For i = 1 to n do
        For j = 1 to n do
            result = result + 0.00001
        End For
    End For

    Print the result: result
End Program
```

Result = 100000\*100000\*0.00001 = 100000

## Fortran 90

```
> gfortran -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    100000.02193264633
Ticks             : 260444774
TotalDays         : 0.000301440710648148
TotalHours        : 0.00723457705555556
TotalMinutes      : 0.434074623333333
TotalSeconds      : 26.0444774
TotalMilliseconds : 26044.4774
```

```
> gfortran -O3 -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    100000.02193264633
Ticks             : 65366842
TotalDays         : 7.56560671296296E-05
TotalHours        : 0.00181574561111111
TotalMinutes      : 0.108944736666667
TotalSeconds      : 6.5366842
TotalMilliseconds : 6536.6842
```

```
> gfortran -Ofast -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    100000.02193264633
Ticks             : 65269219
TotalDays         : 7.55430775462963E-05
TotalHours        : 0.00181303386111111
TotalMinutes      : 0.108782031666667
TotalSeconds      : 6.5269219
TotalMilliseconds : 6526.9219
```

```
> ifx -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 2548151
TotalDays         : 2.94924884259259E-06
TotalHours        : 7.07819722222222E-05
TotalMinutes      : 0.00424691833333333
TotalSeconds      : 0.2548151
TotalMilliseconds : 254.8151
```

```
> ifx /O3 -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 2505836
TotalDays         : 2.90027314814815E-06
TotalHours        : 6.96065555555555E-05
TotalMinutes      : 0.00417639333333333
TotalSeconds      : 0.2505836
TotalMilliseconds : 250.5836
```

```
> ifx /Ofast -o main .\main.f90
> Measure-Command { .\main.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 2478418
TotalDays         : 2.86853935185185E-06
TotalHours        : 6.88449444444444E-05
TotalMinutes      : 0.00413069666666667
TotalSeconds      : 0.2478418
TotalMilliseconds : 247.8418
```

## Fortran 90 (With OpenMP)

```
> gfortran -fopenmp -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.997473787516
Ticks             : 24242581
TotalDays         : 2.80585428240741E-05
TotalHours        : 0.000673405027777778
TotalMinutes      : 0.0404043016666667
TotalSeconds      : 2.4242581
TotalMilliseconds : 2424.2581
```

```
> gfortran -fopenmp -O3 -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.997473787516
Ticks             : 6269447
TotalDays         : 7.25630439814815E-06
TotalHours        : 0.000174151305555556
TotalMinutes      : 0.0104490783333333
TotalSeconds      : 0.6269447
TotalMilliseconds : 626.9447
```

```
> gfortran -fopenmp -Ofast -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.997473787516
Ticks             : 6085612
TotalDays         : 7.04353240740741E-06
TotalHours        : 0.000169044777777778
TotalMinutes      : 0.0101426866666667
TotalSeconds      : 0.6085612
TotalMilliseconds : 608.5612
```

```
> ifx /Qopenmp -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 727030
TotalDays         : 8.41469907407407E-07
TotalHours        : 2.01952777777778E-05
TotalMinutes      : 0.00121171666666667
TotalSeconds      : 0.072703
TotalMilliseconds : 72.703
```

```
> ifx /Qopenmp /O3 -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 691564
TotalDays         : 8.00421296296296E-07
TotalHours        : 1.92101111111111E-05
TotalMinutes      : 0.00115260666666667
TotalSeconds      : 0.0691564
TotalMilliseconds : 69.1564
```

```
> ifx /Qopenmp /Ofast -o main_openmp .\main_openmp.f90
> Measure-Command { .\main_openmp.exe | Out-Default }
Result:    99999.9974737875
Ticks             : 732488
TotalDays         : 8.47787037037037E-07
TotalHours        : 2.03468888888889E-05
TotalMinutes      : 0.00122081333333333
TotalSeconds      : 0.0732488
TotalMilliseconds : 73.2488
```

## C

```
> gcc -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 263443985
TotalDays         : 0.000304912019675926
TotalHours        : 0.00731788847222222
TotalMinutes      : 0.439073308333333
TotalSeconds      : 26.3443985
TotalMilliseconds : 26344.3985
```

```
> gcc -O3 -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 69182992
TotalDays         : 8.00729074074074E-05
TotalHours        : 0.00192174977777778
TotalMinutes      : 0.115304986666667
TotalSeconds      : 6.9182992
TotalMilliseconds : 6918.2992
```

```
> gcc -Ofast -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 69253153
TotalDays         : 8.01541122685185E-05
TotalHours        : 0.00192369869444444
TotalMinutes      : 0.115421921666667
TotalSeconds      : 6.9253153
TotalMilliseconds : 6925.3153
```

```
> icx -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10256507
TotalDays         : 1.18709571759259E-05
TotalHours        : 0.000284902972222222
TotalMinutes      : 0.0170941783333333
TotalSeconds      : 1.0256507
TotalMilliseconds : 1025.6507
```

```
> icx /O3 -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10256812
TotalDays         : 1.18713101851852E-05
TotalHours        : 0.000284911444444444
TotalMinutes      : 0.0170946866666667
TotalSeconds      : 1.0256812
TotalMilliseconds : 1025.6812
```

```
> icx /Ofast -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10200478
TotalDays         : 1.18061087962963E-05
TotalHours        : 0.000283346611111111
TotalMinutes      : 0.0170007966666667
TotalSeconds      : 1.0200478
TotalMilliseconds : 1020.0478
```

## C (With OpenMP)

```
> gcc -fopenmp -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 24285886
TotalDays         : 2.81086643518519E-05
TotalHours        : 0.000674607944444444
TotalMinutes      : 0.0404764766666667
TotalSeconds      : 2.4285886
TotalMilliseconds : 2428.5886
```

```
> gcc -fopenmp -O3 -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 6385499
TotalDays         : 7.39062384259259E-06
TotalHours        : 0.000177374972222222
TotalMinutes      : 0.0106424983333333
TotalSeconds      : 0.6385499
TotalMilliseconds : 638.5499
```

```
> gcc -fopenmp -Ofast -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 5790856
TotalDays         : 6.70237962962963E-06
TotalHours        : 0.000160857111111111
TotalMinutes      : 0.00965142666666667
TotalSeconds      : 0.5790856
TotalMilliseconds : 579.0856
```

```
> icx /Qiopenmp -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 680190
TotalDays         : 7.87256944444444E-07
TotalHours        : 1.88941666666667E-05
TotalMinutes      : 0.00113365
TotalSeconds      : 0.068019
TotalMilliseconds : 68.019
```

```
> icx /Qiopenmp /O3 -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 704999
TotalDays         : 8.15971064814815E-07
TotalHours        : 1.95833055555556E-05
TotalMinutes      : 0.00117499833333333
TotalSeconds      : 0.0704999
TotalMilliseconds : 70.4999
```

```
> icx /Qiopenmp /Ofast -o main_openmp main_openmp.c
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 670927
TotalDays         : 7.7653587962963E-07
TotalHours        : 1.86368611111111E-05
TotalMinutes      : 0.00111821166666667
TotalSeconds      : 0.0670927
TotalMilliseconds : 67.0927
```

## C++

```
> g++ -o main main.cpp
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 264012190
TotalDays         : 0.000305569664351852
TotalHours        : 0.00733367194444444
TotalMinutes      : 0.440020316666667
TotalSeconds      : 26.401219
TotalMilliseconds : 26401.219
```

```
> g++ -O3 -o main main.cpp
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 69196242
TotalDays         : 8.00882430555556E-05
TotalHours        : 0.00192211783333333
TotalMinutes      : 0.11532707
TotalSeconds      : 6.9196242
TotalMilliseconds : 6919.6242
```

```
> g++ -Ofast -o main main.cpp
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.022073
Ticks             : 69220773
TotalDays         : 8.01166354166667E-05
TotalHours        : 0.00192279925
TotalMinutes      : 0.115367955
TotalSeconds      : 6.9220773
TotalMilliseconds : 6922.0773
```

```
> icx -o main main.cpp
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10162431
TotalDays         : 1.17620729166667E-05
TotalHours        : 0.00028228975
TotalMinutes      : 0.016937385
TotalSeconds      : 1.0162431
TotalMilliseconds : 1016.2431
```

```
> icx /O3 -o main main.cpp
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10250595
TotalDays         : 1.18641145833333E-05
TotalHours        : 0.00028473875
TotalMinutes      : 0.017084325
TotalSeconds      : 1.0250595
TotalMilliseconds : 1025.0595
```

```
> icx /Ofast -o main main.c
> Measure-Command { .\main.exe | Out-Default }
Result: 100000.000554
Ticks             : 10419863
TotalDays         : 1.20600266203704E-05
TotalHours        : 0.000289440638888889
TotalMinutes      : 0.0173664383333333
TotalSeconds      : 1.0419863
TotalMilliseconds : 1041.9863
```

## C++ (With OpenMP)

```
> g++ -fopenmp -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 24134914
TotalDays         : 2.79339282407407E-05
TotalHours        : 0.000670414277777778
TotalMinutes      : 0.0402248566666667
TotalSeconds      : 2.4134914
TotalMilliseconds : 2413.4914
```

```
> g++ -fopenmp -O3 -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 6407591
TotalDays         : 7.41619328703704E-06
TotalHours        : 0.000177988638888889
TotalMinutes      : 0.0106793183333333
TotalSeconds      : 0.6407591
TotalMilliseconds : 640.7591
```

```
> g++ -fopenmp -Ofast -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 99999.999159
Ticks             : 6015819
TotalDays         : 6.96275347222222E-06
TotalHours        : 0.000167106083333333
TotalMinutes      : 0.010026365
TotalSeconds      : 0.6015819
TotalMilliseconds : 601.5819
```

```
> icx /Qiopenmp -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 723325
TotalDays         : 8.37181712962963E-07
TotalHours        : 2.00923611111111E-05
TotalMinutes      : 0.00120554166666667
TotalSeconds      : 0.0723325
TotalMilliseconds : 72.3325
```

```
> icx /Qiopenmp /O3 -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 681450
TotalDays         : 7.88715277777778E-07
TotalHours        : 1.89291666666667E-05
TotalMinutes      : 0.00113575
TotalSeconds      : 0.068145
TotalMilliseconds : 68.145
```

```
> icx /Qiopenmp /Ofast -o main_openmp main_openmp.cpp
> Measure-Command { .\main_openmp.exe | Out-Default }
Result: 100000.000023
Ticks             : 702521
TotalDays         : 8.13103009259259E-07
TotalHours        : 1.95144722222222E-05
TotalMinutes      : 0.00117086833333333
TotalSeconds      : 0.0702521
TotalMilliseconds : 70.2521
```

## Python 3.11
```
> Measure-Command { python main.py | Out-Default }
Result: 100000.02207306116
Ticks             : 6023268111
TotalDays         : 0.00697137512847222
TotalHours        : 0.167313003083333
TotalMinutes      : 10.038780185
TotalSeconds      : 602.3268111
TotalMilliseconds : 602326.8111
```

## PyPy 3.9
```
> Measure-Command { pypy main.py | Out-Default }
Result:  100000.02207306116
Ticks             : 264979164
TotalDays         : 0.000306688847222222
TotalHours        : 0.00736053233333333
TotalMinutes      : 0.44163194
TotalSeconds      : 26.4979164
TotalMilliseconds : 26497.9164
```

## Python 3.11 (With Cython)

```
> python setup.py build_ext --inplace
> Measure-Command { python main_cython.py | Out-Default }
Result:  100000.02207306116
Ticks             : 65555665
TotalDays         : 7.58746122685185E-05
TotalHours        : 0.00182099069444444
TotalMinutes      : 0.109259441666667
TotalSeconds      : 6.5555665
TotalMilliseconds : 6555.5665
```

## Python 3.11  (With Taichi)

```
> Measure-Command { python main_taichi.py | Out-Default }
[Taichi] version 1.7.1, llvm 15.0.1, commit 0f143b2f, win, python 3.11.9
[Taichi] Starting on arch=x64
Result:  99999.99747378752
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 825
Ticks             : 8254668
TotalDays         : 9.55401388888889E-06
TotalHours        : 0.000229296333333333
TotalMinutes      : 0.01375778
TotalSeconds      : 0.8254668
TotalMilliseconds : 825.4668
```

```
> Measure-Command { python main_taichi_gpu.py | Out-Default }
[Taichi] version 1.7.1, llvm 15.0.1, commit 0f143b2f, win, python 3.11.9
[Taichi] Starting on arch=cuda
Result:  99999.99747378752
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 1
Milliseconds      : 192
Ticks             : 11928701
TotalDays         : 1.38063668981481E-05
TotalHours        : 0.000331352805555556
TotalMinutes      : 0.0198811683333333
TotalSeconds      : 1.1928701
TotalMilliseconds : 1192.8701
```

## Python 3.11 (With Numba)
```
> Measure-Command { python main_numba_jit.py | Out-Default }
Result:  100000.02207306116
Ticks             : 72332068
TotalDays         : 8.37176712962963E-05
TotalHours        : 0.00200922411111111
TotalMinutes      : 0.120553446666667
TotalSeconds      : 7.2332068
TotalMilliseconds : 7233.2068
```

```
> Measure-Command { python main_numba_njit.py | Out-Default }
Result:  100000.02207306116
Ticks             : 72360433
TotalDays         : 8.37505011574074E-05
TotalHours        : 0.00201001202777778
TotalMinutes      : 0.120600721666667
TotalSeconds      : 7.2360433
TotalMilliseconds : 7236.0433
```

```
> Measure-Command { python main_numba_njit_fastmath.py | Out-Default }
Result:  99999.99991278863
Ticks             : 7631187
TotalDays         : 8.83239236111111E-06
TotalHours        : 0.000211977416666667
TotalMinutes      : 0.012718645
TotalSeconds      : 0.7631187
TotalMilliseconds : 763.1187
```

```
> Measure-Command { python main_numba_njit_parallel.py | Out-Default }
Result:  99999.99915876485
Ticks             : 15879350
TotalDays         : 1.83788773148148E-05
TotalHours        : 0.000441093055555556
TotalMinutes      : 0.0264655833333333
TotalSeconds      : 1.587935
TotalMilliseconds : 1587.935
```

```
> Measure-Command { python main_numba_njit_parallel_fastmath.py | Out-Default }
Result:  99999.99998854523
Ticks             : 10922346
TotalDays         : 1.26416041666667E-05
TotalHours        : 0.0003033985
TotalMinutes      : 0.01820391
TotalSeconds      : 1.0922346
TotalMilliseconds : 1092.2346
```

```
> Measure-Command { python main_numba_cuda.py | Out-Default }
Result: 100000.02207306116
Ticks             : 176345317
TotalDays         : 0.000204103376157407
TotalHours        : 0.00489848102777778
TotalMinutes      : 0.293908861666667
TotalSeconds      : 17.6345317
TotalMilliseconds : 17634.5317
```

## Julia

`> $Env:JULIA_NUM_THREADS = "auto"`

```
> Measure-Command { julia main.jl | Out-Default }
Result: 100000.02207306116
Ticks             : 67472503
TotalDays         : 7.80931747685185E-05
TotalHours        : 0.00187423619444444
TotalMinutes      : 0.112454171666667
TotalSeconds      : 6.7472503
TotalMilliseconds : 6747.2503
```

```
> Measure-Command { julia main_simd.jl | Out-Default }
Result: 100000.00137956644
Ticks             : 6864702
TotalDays         : 7.94525694444444E-06
TotalHours        : 0.000190686166666667
TotalMinutes      : 0.01144117
TotalSeconds      : 0.6864702
TotalMilliseconds : 686.4702
```

```
> Measure-Command { julia main_fastmath.jl | Out-Default }
Result: 99999.99991278863
Ticks             : 3132524
TotalDays         : 3.62560648148148E-06
TotalHours        : 8.70145555555556E-05
TotalMinutes      : 0.00522087333333333
TotalSeconds      : 0.3132524
TotalMilliseconds : 313.2524
```

```
> Measure-Command { julia main_threads.jl | Out-Default }
Result: 99999.99999991048
Ticks             : 8966069
TotalDays         : 1.03773946759259E-05
TotalHours        : 0.000249057472222222
TotalMinutes      : 0.0149434483333333
TotalSeconds      : 0.8966069
TotalMilliseconds : 896.6069
```

```
> Measure-Command { julia main_threads_fastmath.jl | Out-Default }
Result: 99999.99999999999
Ticks             : 3424389
TotalDays         : 3.96341319444444E-06
TotalHours        : 9.51219166666667E-05
TotalMinutes      : 0.005707315
TotalSeconds      : 0.3424389
TotalMilliseconds : 342.4389
```

```
> Measure-Command { julia main_threads_inbounds.jl | Out-Default }
Result: 99999.99999991048
Ticks             : 8966765
TotalDays         : 1.03782002314815E-05
TotalHours        : 0.000249076805555556
TotalMinutes      : 0.0149446083333333
TotalSeconds      : 0.8966765
TotalMilliseconds : 896.6765
```

```
> Measure-Command { julia main_threads_simd.jl | Out-Default }
Result: 100000.00000000036
Ticks             : 3843874
TotalDays         : 4.44892824074074E-06
TotalHours        : 0.000106774277777778
TotalMinutes      : 0.00640645666666667
TotalSeconds      : 0.3843874
TotalMilliseconds : 384.3874
```

```
> Measure-Command { julia main_threads_inbounds_simd.jl | Out-Default }
Result: 100000.00000000036
Ticks             : 3814411
TotalDays         : 4.4148275462963E-06
TotalHours        : 0.000105955861111111
TotalMinutes      : 0.00635735166666667
TotalSeconds      : 0.3814411
TotalMilliseconds : 381.4411
```