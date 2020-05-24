"""
Unit tests for the RangeDict
"""
from pytest import fixture, mark, raises

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


def test_decimals_works():
    """
    We should be able to use decimals as ranges
    """
    r_dict = RangeDict()
    r_dict[(0.42, 7.42)] = "a"
    assert r_dict[0.42] == "a"
    assert r_dict[0.52] == "a"
    assert r_dict[0.72] == "a"
    assert r_dict[1] == "a"
    assert r_dict[1.000001] == "a"
    assert r_dict[2] == "a"
    assert r_dict[3] == "a"
    assert r_dict[7] == "a"
    assert r_dict[7.42 - 0.0001] == "a"


@mark.xfail
def test_overlapping_ranges_are_forbidden():
    """
    Tests if overlaps raises error
    """
    r_dict = RangeDict()
    r_dict[(0, 10)] = "a"

    with raises(ValueError):
        r_dict[(1, 3)] = "b"
