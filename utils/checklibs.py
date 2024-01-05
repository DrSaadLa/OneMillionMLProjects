"""
This module is used to check whether the working libraries are installed.
"""

import importlib
import subprocess
import sys
import re


def get_pip_version():
    result = subprocess.run([sys.executable, '-m', 'pip', '--version'],
                            capture_output=True, text=True)
    
    match = re.search(r'pip (\d+\.\d+\.\d+)', result.stdout)
    return match.group(1) if match else None


def update_pip():
    current_version = get_pip_version()
    if current_version is None:
        print("Unable to determine the current version of pip.")
        return

    # Get the latest version of pip from pypi
    latest_version = subprocess.run([sys.executable, '-m', 'pip', 'index', 'versions', 'pip'],
                                    capture_output=True, text=True).stdout.split()[-1]

    if current_version == latest_version:
        print("pip is already up-to-date.")
    else:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'],
                stdout=subprocess.DEVNULL,  
                stderr=subprocess.DEVNULL   
            )
            print(f"pip has been successfully updated from {current_version} to {latest_version}.")
        except subprocess.CalledProcessError:
            print("Failed to update pip.")
            

def install_libraries(working_libs):

    already_installed = []
    newly_installed = []

    for lib_name in working_libs:
        if lib_name!="scikit-learn":
            try:
                importlib.import_module(lib_name)
                already_installed.append(lib_name)
            except ImportError:
                # If the library is not installed, install it in the current 
                # environment
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade",
                                       lib_name])
                newly_installed.append(lib_name)
        else:
            try:
                importlib.import_module("sklearn")
                already_installed.append("sklearn")
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-U",
                                       lib_name])
                newly_installed.append(lib_name)
                
    if len(working_libs) == len(already_installed):
        print("....................................................... ")
        print("Your working space has all the necessary working libs.")
    else:
        print(f"The already install libraries: {already_installed}")
    if newly_installed:
        print(f"The newly installed libraries: {newly_installed}")
    else:
        print("....................................................... ")
    print()












