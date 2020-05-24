"""
Tests the differente selection strategies available
"""

from pytest import fixture

import ga_solver.pop_selectors as selectors

# pylint: disable=redefined-outer-name
@fixture
def population():
    """
    Provides a simple population for testing
    """
    pop = {"a": 10, "b": 10, "c": 10, "d": 10}
    return pop


@fixture
def pop_range(population):
    """
    Provides a RangeDict for a demo pop
    """
    return selectors.build_roullete(population)


def test_build_roullete(population):
    """
    Tests if build_roullete works with a simple population
    """
    roullete = selectors.build_roullete(population)

    assert (
        repr(roullete)
        == "{(0, 0.25): 'a', (0.25, 0.5): 'b', (0.5, 0.75): 'c', (0.75, 1.0): 'd'}"
    )


def test_roullete(pop_range):
    """
    Tests if the roullete selection works as expected
    """
    selected = set(selectors.roullete(pop_range, random_seed=42424) for _ in range(10))
    assert selected == {"d"}
