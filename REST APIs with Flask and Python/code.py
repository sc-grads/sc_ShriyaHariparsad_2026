from mymodule import divide

print(divide(10, 2))

print(__name__)

# -- importing with names --

import mymodule

print("code.py: ", __name__)

# How does Python know where `mymodule` is?
# Answer, it looks at the paths in sys.path in order:

import sys

print(sys.path)

# -- importing from a folder --

import mymodule

print("code.py: ", __name__)

import sys

print(sys.modules)

