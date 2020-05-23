"""
Provides basic unitary tests for the solver
"""
from random import uniform

from pytest import fixture
from ga_solver import GASolver


@fixture
def eq_solver():
    """
    Offers a GASolver for a second-degree equation
    """
    goal = lambda x: x * x - 49
    mutation = lambda x: x + uniform(-1, 1)
    gas = GASolver(
        initial_pop=[0, 2, 4, 6],
        goal=goal,
        target_value=0,
        mutation=mutation,
        prob_mutation=0.7,
        random_seed=0,
    )

    return gas


# pylint: disable=redefined-outer-name
def test_initialization():
    """
    Tests if a correct initialization is possible
    """

    goal = lambda x: x ^ 2 + 10
    mutation = lambda x: x + uniform(-1, 1)
    gas = GASolver(
        initial_pop=[0, 2, 4, 6],
        goal=goal,
        target_value=0,
        mutation=mutation,
        prob_mutation=0.7,
        random_seed=0,
    )

    assert gas


def test_current_state_eval(eq_solver):
    """
    Tests if the GA solver correctly computes the current state
    """
    assert eq_solver.current_state == (-49, -45, -33, -13)
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
