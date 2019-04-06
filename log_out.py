"""This module -- Simplify logic program."""

from logging import *
from sys import *


def log_out(name, out):
    """log_out -- log output function."""
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    logger.addHandler(FileHandler('%s.log' % name))
    logger.addHandler(StreamHandler(stdout))
    logger.debug(out)
    return logger
