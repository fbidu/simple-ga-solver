"""
Provides basic unitary tests for the solver
"""
from random import uniform
from sys import maxsize

from pytest import fixture
from ga_solver import GASolver
from ga_solver.pop_selectors import roullete


@fixture
def eq_solver():
    """
    Offers a GASolver for a second-degree equation
    """

    # pylint: disable=invalid-name
    def goal(x):
        """
        In order to find the root of an equation, we need to goal to
        increase as the result approaches 0.
        """
        result = x ** 2 - 49
        if result == 0:
            return maxsize

        return abs(1 / result)

    mutation = lambda x: x + uniform(-1, 1)
    crossover = lambda x, y: (x * y) ** 0.5
    gas = GASolver(
        initial_pop=[0, 2, 4, 6],
        goal=goal,
        target_value=maxsize,
        mutation=mutation,
        prob_mutation=0.7,
        crossover_=crossover,
        selector=roullete,
        random_seed=0,
    )

    return gas


# pylint: disable=redefined-outer-name
def test_current_state_eval(eq_solver):
    """
    Tests if the GA solver correctly computes the current state
    """
    assert eq_solver.current_state == {
        0: 0.02040816326530612,
        2: 0.022222222222222223,
        4: 0.030303030303030304,
        6: 0.07692307692307693,
    }
    assert not eq_solver.solution_found


def test_solver_notes_correct_solution(eq_solver):
    """
    Tests if the solver really determines when a solution has been found
    """
    eq_solver.population.append(7)

    assert 0 in eq_solver.current_state
    assert eq_solver.solution_found


def test_solver_honors_mutation_prob(eq_solver):
    """
    Tests if the solver actually respects the given mutation probability
    """
    # pylint: disable=invalid-name
    eq_solver.random_seed = 4242424242
    x = 10
    for _ in range(10):
        x = eq_solver.mutate(x)

    assert x == 2.733731801703599


def test_solver_mutates_all_pop(eq_solver):
    """
    Tests if the solver mutate all the population correctly
    """
    eq_solver.random_seed = 4242424242

    for _ in range(10):
        eq_solver.mutate_pop()

    assert eq_solver.current_state == {
        -7.266268198296398: 0.2632511736631728,
        -5.266268198296398: 0.047022490603815664,
        -3.2662681982963973: 0.026088209624562805,
        -1.2662681982963981: 0.021098575459321596,
    }


def test_crossover_works(eq_solver):
    """
    Tests if the solver correctly crosses over two solutions
    """
    eq_solver.random_seed = 4242424242

    sibling = eq_solver.crossover(10, 20)

    assert sibling == 14.142135623730951


def test_selection_works(eq_solver):
    """
    Tests if the solver correctly selects the solutions
    """
    assert eq_solver.select(replace=False) == [6, 6]
