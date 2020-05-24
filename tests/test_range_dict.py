"""
Unit tests for the RangeDict
"""
from pytest import fixture

from ga_solver import RangeDict

# pylint: disable=redefined-outer-name
@fixture
def r_dict():
    """
    Provides a dummy RangeDict for testing
    """
    r_dict = RangeDict()
    r_dict[(0, 10)] = "a"
    r_dict[(10, 20)] = "b"
    r_dict[(20, 50)] = "c"

    return r_dict


def test_initialize():
    """
    Basic initialization test
    """

    r_dict = RangeDict()
    r_dict[(0, 10)] = "a"


def test_lower_bounds(r_dict):
    """
    Tests if the lower bounds are respected
    """
    assert r_dict[0] == "a"
    assert r_dict[10] == "b"
    assert r_dict[20] == "c"


def test_upper_bounds(r_dict):
    """
    Tests if the upper bounds are respected
    """
    assert r_dict[10 - 0.001] == "a"
    assert r_dict[20 - 0.001] == "b"
    assert r_dict[50 - 0.001] == "c"
