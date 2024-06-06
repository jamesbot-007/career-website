# from abc import xyz
# Check wheather "xyz" is function or a class

import inspect
from flask import Flask

if inspect.isfunction(Flask):
    print("Flask is a function")
elif inspect.isclass(Flask):
    print("Flask is a class")
else:
    print("Flask is something else")

# Run this file using : python check.py 
