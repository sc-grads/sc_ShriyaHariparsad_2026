from math import isclose

a: float = .1 + .2
b: float = .3

print(f'{a}) == {b}?' , isclose(a, b, rel_tol=0.001))






