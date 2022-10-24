#   MAS dfab - Week 6 - Compas

---
Contents
- [Compas installation](#compas-installation)


---

## Compas installation
```
    Windows PowerShell
    版权所有（C） Microsoft Corporation。保留所有权利。

    安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

    PS C:\Users\Zac> pip install cython --install-option="--no-cython-compile"
    WARNING: Disabling all use of wheels due to the use of --build-option / --global-option / --install-option.
    Collecting cython
    Downloading Cython-0.29.32.tar.gz (2.1 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 6.0 MB/s eta 0:00:00
    Preparing metadata (setup.py) ... done
    Skipping wheel build for cython, due to binaries being disabled for it.
    Installing collected packages: cython
    Running setup.py install for cython ... done
    Successfully installed cython-0.29.32

    [notice] A new release of pip available: 22.2.2 -> 22.3
    [notice] To update, run: C:\Users\Zac\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    PS C:\Users\Zac> pip install compas
    Collecting compas
    Downloading COMPAS-1.17.0-py2.py3-none-any.whl (5.2 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 4.9 MB/s eta 0:00:00
    Collecting matplotlib>=3.1
    Downloading matplotlib-3.6.1-cp310-cp310-win_amd64.whl (7.2 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 10.0 MB/s eta 0:00:00
    Collecting scipy>=1.1
    Downloading scipy-1.9.3-cp310-cp310-win_amd64.whl (40.1 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.1/40.1 MB 14.5 MB/s eta 0:00:00
    Collecting pycollada
    Downloading pycollada-0.7.2.tar.gz (107 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 107.6/107.6 kB ? eta 0:00:00
    Preparing metadata (setup.py) ... done
    Collecting typing-extensions
    Downloading typing_extensions-4.4.0-py3-none-any.whl (26 kB)
    Requirement already satisfied: cython in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas) (0.29.32)
    Collecting watchdog
    Downloading watchdog-2.1.9-py3-none-win_amd64.whl (78 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.4/78.4 kB ? eta 0:00:00
    Collecting networkx
    Downloading networkx-2.8.7-py3-none-any.whl (2.0 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 18.5 MB/s eta 0:00:00
    Collecting sympy
    Downloading sympy-1.11.1-py3-none-any.whl (6.5 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.5/6.5 MB 15.3 MB/s eta 0:00:00
    Collecting imageio>=2.7
    Downloading imageio-2.22.2-py3-none-any.whl (3.4 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 21.5 MB/s eta 0:00:00
    Requirement already satisfied: pillow in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas) (9.2.0)
    Collecting schema
    Downloading schema-0.7.5-py2.py3-none-any.whl (17 kB)
    Requirement already satisfied: numpy>=1.15.4 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas) (1.23.4)
    Collecting jsonschema
    Downloading jsonschema-4.16.0-py3-none-any.whl (83 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.1/83.1 kB 4.9 MB/s eta 0:00:00
    Collecting contourpy>=1.0.1
    Downloading contourpy-1.0.5-cp310-cp310-win_amd64.whl (164 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 164.1/164.1 kB 9.6 MB/s eta 0:00:00
    Collecting cycler>=0.10
    Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
    Collecting kiwisolver>=1.0.1
    Downloading kiwisolver-1.4.4-cp310-cp310-win_amd64.whl (55 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.3/55.3 kB 2.8 MB/s eta 0:00:00
    Collecting packaging>=20.0
    Using cached packaging-21.3-py3-none-any.whl (40 kB)
    Collecting fonttools>=4.22.0
    Downloading fonttools-4.38.0-py3-none-any.whl (965 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 965.4/965.4 kB 20.3 MB/s eta 0:00:00
    Collecting pyparsing>=2.2.1
    Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas) (2.8.2)
    Collecting attrs>=17.4.0
    Using cached attrs-22.1.0-py2.py3-none-any.whl (58 kB)
    Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
    Downloading pyrsistent-0.18.1-cp310-cp310-win_amd64.whl (61 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.6/61.6 kB ? eta 0:00:00
    Collecting contextlib2>=0.5.5
    Downloading contextlib2-21.6.0-py2.py3-none-any.whl (13 kB)
    Collecting mpmath>=0.19
    Downloading mpmath-1.2.1-py3-none-any.whl (532 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 532.6/532.6 kB 32.6 MB/s eta 0:00:00
    Requirement already satisfied: six>=1.5 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from python-dateutil>=2.7->matplotlib>=3.1->compas) (1.16.0)
    Using legacy 'setup.py install' for pycollada, since package 'wheel' is not installed.
    Installing collected packages: mpmath, watchdog, typing-extensions, sympy, scipy, pyrsistent, pyparsing, networkx, kiwisolver, imageio, fonttools, cycler, contourpy, contextlib2, attrs, schema, pycollada, packaging, jsonschema, matplotlib, compas
    WARNING: The script watchmedo.exe is installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The script isympy.exe is installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The scripts imageio_download_bin.exe and imageio_remove_bin.exe are installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Running setup.py install for pycollada ... done
    WARNING: The script jsonschema.exe is installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The script compas_rpc.exe is installed in 'C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Successfully installed attrs-22.1.0 compas-1.17.0 contextlib2-21.6.0 contourpy-1.0.5 cycler-0.11.0 fonttools-4.38.0 imageio-2.22.2 jsonschema-4.16.0 kiwisolver-1.4.4 matplotlib-3.6.1 mpmath-1.2.1 networkx-2.8.7 packaging-21.3 pycollada-0.7.2 pyparsing-3.0.9 pyrsistent-0.18.1 schema-0.7.5 scipy-1.9.3 sympy-1.11.1 typing-extensions-4.4.0 watchdog-2.1.9

    [notice] A new release of pip available: 22.2.2 -> 22.3
    [notice] To update, run: C:\Users\Zac\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    PS C:\Users\Zac>
    PS C:\Users\Zac>
    PS C:\Users\Zac> cd path/to/compas
    cd : 找不到路径“C:\Users\Zac\path\to\compas”，因为该路径不存在。
    所在位置 行:1 字符: 1
    + cd path/to/compas
    + ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : ObjectNotFound: (C:\Users\Zac\path\to\compas:String) [Set-Location], ItemNotFoundException
        + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

    PS C:\Users\Zac> pip install -e .
    Obtaining file:///C:/Users/Zac
    ERROR: file:///C:/Users/Zac does not appear to be a Python project: neither 'setup.py' nor 'pyproject.toml' found.

    [notice] A new release of pip available: 22.2.2 -> 22.3
    [notice] To update, run: C:\Users\Zac\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    PS C:\Users\Zac> pip install compas[planarity]
    Requirement already satisfied: compas[planarity] in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (1.17.0)
    Requirement already satisfied: jsonschema in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (4.16.0)
    Requirement already satisfied: watchdog in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (2.1.9)
    Requirement already satisfied: imageio>=2.7 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (2.22.2)
    Requirement already satisfied: networkx in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (2.8.7)
    Requirement already satisfied: scipy>=1.1 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (1.9.3)
    Requirement already satisfied: schema in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (0.7.5)
    Requirement already satisfied: typing-extensions in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (4.4.0)
    Requirement already satisfied: pillow in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (9.2.0)
    Requirement already satisfied: cython in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (0.29.32)
    Requirement already satisfied: sympy in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (1.11.1)
    Requirement already satisfied: pycollada in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (0.7.2)
    Requirement already satisfied: matplotlib>=3.1 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (3.6.1)
    Requirement already satisfied: numpy>=1.15.4 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from compas[planarity]) (1.23.4)
    Collecting planarity
    Downloading planarity-0.4.1.zip (193 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 193.2/193.2 kB 1.7 MB/s eta 0:00:00
    Preparing metadata (setup.py) ... done
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (2.8.2)
    Requirement already satisfied: pyparsing>=2.2.1 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (3.0.9)
    Requirement already satisfied: fonttools>=4.22.0 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (4.38.0)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (1.4.4)
    Requirement already satisfied: packaging>=20.0 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (21.3)
    Requirement already satisfied: contourpy>=1.0.1 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (1.0.5)
    Requirement already satisfied: cycler>=0.10 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from matplotlib>=3.1->compas[planarity]) (0.11.0)
    Requirement already satisfied: attrs>=17.4.0 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from jsonschema->compas[planarity]) (22.1.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from jsonschema->compas[planarity]) (0.18.1)
    Requirement already satisfied: setuptools in c:\program files\windowsapps\pythonsoftwarefoundation.python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\site-packages (from planarity->compas[planarity]) (63.2.0)
    Requirement already satisfied: contextlib2>=0.5.5 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from schema->compas[planarity]) (21.6.0)
    Requirement already satisfied: mpmath>=0.19 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from sympy->compas[planarity]) (1.2.1)
    Requirement already satisfied: six>=1.5 in c:\users\zac\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from python-dateutil>=2.7->matplotlib>=3.1->compas[planarity]) (1.16.0)
    Using legacy 'setup.py install' for planarity, since package 'wheel' is not installed.
    Installing collected packages: planarity
    Running setup.py install for planarity ... error
    error: subprocess-exited-with-error

    × Running setup.py install for planarity did not run successfully.
    │ exit code: 1
    ╰─> [22 lines of output]
        running install
        C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
            warnings.warn(
        running build
        running build_py
        creating build
        creating build\lib.win-amd64-cpython-310
        creating build\lib.win-amd64-cpython-310\planarity
        copying planarity\planarity_functions.py -> build\lib.win-amd64-cpython-310\planarity
        copying planarity\planarity_networkx.py -> build\lib.win-amd64-cpython-310\planarity
        copying planarity\__init__.py -> build\lib.win-amd64-cpython-310\planarity
        creating build\lib.win-amd64-cpython-310\planarity\tests
        copying planarity\tests\test.py -> build\lib.win-amd64-cpython-310\planarity\tests
        copying planarity\tests\test_planarity.py -> build\lib.win-amd64-cpython-310\planarity\tests
        copying planarity\tests\test_planarity_networkx.py -> build\lib.win-amd64-cpython-310\planarity\tests
        copying planarity\tests\__init__.py -> build\lib.win-amd64-cpython-310\planarity\tests
        running build_ext
        cythoning planarity/planarity.pyx to planarity\planarity.c
        C:\Users\Zac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\Cython\Compiler\Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: C:\Users\Zac\AppData\Local\Temp\pip-install-lka9qw6g\planarity_72c595de180445349a28375597ae64d9\planarity\planarity.pyx
            tree = Parsing.p_module(s, pxd, full_module_name)
        building 'planarity.planarity' extension
        error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
        [end of output]

    note: This error originates from a subprocess, and is likely not a problem with pip.
    error: legacy-install-failure

    × Encountered error while trying to install package.
    ╰─> planarity

    note: This is an issue with the package mentioned above, not pip.
    hint: See above for output from the failure.

    [notice] A new release of pip available: 22.2.2 -> 22.3
    [notice] To update, run: C:\Users\Zac\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    PS C:\Users\Zac> pip install -e .[planarity]
    Obtaining file:///C:/Users/Zac
    ERROR: file:///C:/Users/Zac does not appear to be a Python project: neither 'setup.py' nor 'pyproject.toml' found.

    [notice] A new release of pip available: 22.2.2 -> 22.3
    [notice] To update, run: C:\Users\Zac\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    PS C:\Users\Zac>
```