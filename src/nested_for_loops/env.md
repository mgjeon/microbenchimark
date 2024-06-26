# Environment

Windows 11

# Fortran, C/C++

## GNU Compiler (gfortran, gcc, g++)

Install [MSYS2](https://www.msys2.org/) and run `pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain` & `pacman -S mingw-w64-ucrt-x86_64-gcc-fortran` in MSYS2 UCRT64 terminal. Add `C:\msys64\ucrt64\bin` to the system PATH.

[Fortran tutorial](https://fortran-lang.org/learn/os_setup/install_gfortran/)

[C/C++ tutorial](https://code.visualstudio.com/docs/cpp/config-mingw)

## Intel Compiler (ifx, icx)

[Intel oneAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html)

[Intel oneAPI HPC Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html)

Run `"C:\Program Files (x86)\Intel\oneAPI\setvars.bat"` to set the environment variables.

In Windows, you need to install `Desktop development with C++` in [Visual Studio](https://visualstudio.microsoft.com/) before installing Intel oneAPI.

# Python

Install [Miniconda](https://docs.anaconda.com/miniconda/)

# Julia

Install [Julia](https://julialang.org/downloads/)

If you use julia in Anaconda prompt in Windows, you may need to create a separate environment for Julia where `SSL_CERT_FILE` is removed using `conda env config vars set SSL_CERT_FILE=`. If not, you may see `GitError(Code:ERROR, ...` error when adding packages.