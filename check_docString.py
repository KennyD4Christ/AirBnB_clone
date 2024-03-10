import inspect
from models.place import Place  # Adjust this import according to your project structure

def print_method_docstrings(cls):
    """Prints the documentation strings of all methods in the given class."""
    
    print(f"Documentation for all methods of {cls.__name__}:")
    print("-" * 40)
    
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if method.__doc__:  # Check if the method has a docstring
            print(f"Method: {name}\nDocstring: {method.__doc__}\n")
        else:
            print(f"Method: {name} has no docstring.\n")

# Example usage:
print_method_docstrings(Place)
