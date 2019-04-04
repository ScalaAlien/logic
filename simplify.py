from logic_out import *
from sympy.abc import a, b, c, d, e, f

logic = ((a & b) | ((a | c) & d) & e)
logic_out(logic)
