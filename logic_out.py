from sympy.logic import *
from sympy import S
from logging import *
from sys import *


def log_out(name, out):
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    logger.addHandler(FileHandler('%s.log' % name))
    logger.addHandler(StreamHandler(stdout))
    logger.debug(out)
    return logger


def logic_out(arg):
    log_out('input', S(arg))
    log_out('dnf', simplify_logic(arg, form='dnf'))
    log_out('cnf', simplify_logic(arg, form='cnf'))
