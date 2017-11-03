from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x=Symbol('x')
s=str(input())
parse_expr(s)
print(diff(s,x))
