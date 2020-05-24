"""
Tests the differente selection strategies available
"""

import ga_solver.pop_selectors as selectors


def test_build_roullete():
    """
    Tests if build_roullete works with a simple population
    """
    population = {"a": 10, "b": 10, "c": 20}
    roullete = selectors.build_roullete(population)

    assert repr(roullete) == "{(0, 0.25): 'a', (0.25, 0.5): 'b', (0.5, 1.0): 'c'}"
