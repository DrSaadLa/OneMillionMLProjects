def import_libraries(dependencies):
    imported_libraries = {}
    
    for lib in dependencies:
        # Adjust for scikit-learn which is imported as sklearn
        if lib == 'scikit-learn':
            lib_name = 'sklearn'
        else:
            lib_name = lib

        try:
            imported_libraries[lib_name] = __import__(lib_name)
            print(f"Successfully imported {lib_name}")
        except ImportError as e:
            print(f"Error importing {lib_name}: {e}")

    return imported_libraries


# List of project dependencies
project_dependencies = [
    "pandas",
    "polars",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn"  
]

# Importing the libraries
imported_libraries = import_libraries(project_dependencies)

