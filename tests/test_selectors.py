"""
Tests the differente selection strategies available
"""
from ga_solver.selectors import *


def test_roullete_selection():
    options = {1: 10, 2: 4, 3: 200, 9: 20}
    selected = roullete_selection(options, random_seed=4242424242)

    assert selected == [3]
