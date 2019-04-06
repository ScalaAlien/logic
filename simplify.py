"""This module -- Simplify logic program."""
from log_out import *
from sympy.abc import a, b, c, d, e, f
from sympy.logic import *
from sympy import S


def logic_out(arg):
    """logic_out -- logic output function."""
    log_out('input', S(arg))
    log_out('dnf', simplify_logic(arg, form='dnf'))
    log_out('cnf', simplify_logic(arg, form='cnf'))


logic = ((a & b) | ((a | c) & d) & e)
logic_out(logic)
