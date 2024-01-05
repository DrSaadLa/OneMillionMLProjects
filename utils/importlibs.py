"""
Check not installed libraries and install them automatically
then import the working libraries in this project
"""

import os
import sys
import time
import tempfile
import shutil
import pathlib

# Processing libs
import pandas as pd
import numpy as np
import polars as pl
# import tqdm

# Visualization Libs
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Time Series Libs
# import pyts
# import sktime
# import aeon

# Ml Libs
import sklearn
import statsmodels


# Dl Libs
from checklibs import install_libraries, update_pip

# Prompt the libs to be installed
# ...

__working_libs__ = [
    "pandas",
    "polars",
    "numpy",
    "matplotlib",
    "seaborn",
    # "aeon",
    # "pyts",
    # "sktime",
    "sklearn",
    "statsmodels"    
]

__all__ = [
    'os',
    'sys',
    'time',
    'shutil',
    'tempfile',
    'pathlib',
    'plt',
    'sns',
    'pd',
    'pl',
    'np',
    'lib_versions',
    'python_version',
    'executable_path',
    # 'pyts',
    # 'sktime',
    # 'aeon',
    'sklearn',
    'matplotlib',
    'statsmodels'
    # 'tqdm'
]

__importlibs__ = [
    'matplotlib',
    'plt',
    'sns',
    'pd',
    'pl',
    'np',
    # 'pyts',
    # 'sktime',
    'sklearn',
    'statsmodels'
    # 'aeon',
    # 'tqdm'
]

__builtin_libs__ = [
    'os',
    'sys',
    "time",
    "shutil",
    "tempfile"
]


# Update pip 
update_pip()

# Check the installation the working libs
install_libraries(__working_libs__)


def lib_versions(char="=", nchar=72):
    """
    Display the imported libraries to the wrospace versions.
    """
    VERSION = "version is"
    
    print(char * nchar)
    print("The imported libraries with their versions are".center(72))
    print(char * nchar)
    
    for libname in __importlibs__:
        if libname != 'plt':
            print(f"{eval(libname).__name__:<12} {VERSION:<10} : "
                  F"{eval(libname).__version__}")
    print(char * nchar)

    
def python_version():
    """
    Display the Python version information.
    """
    ver_info = sys.version_info
    print((f"Python version is: {ver_info.major}.{ver_info.minor}."
           f"{ver_info.micro}"))

    
def executable_path():
    """
    Display the executable path of the Python interpreter.
    
    Returns:
    None
    """
    print("Python executable path:", sys.executable)

    
print("Information about the working space".center(72))

lib_versions()
python_version()
executable_path()
print("="*72)


# Setting Data Paths

import_path = "../Data/Raw/"
export_path = "../Data/Preprocessed/"