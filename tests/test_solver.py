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
    crossover = lambda x, y: (x * y) ** 0.5
    gas = GASolver(
        initial_pop=[0, 2, 4, 6],
        goal=goal,
        target_value=0,
        mutation=mutation,
        prob_mutation=0.7,
        crossover_=crossover,
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
    crossover = lambda x, y: (x * y) ** 0.5
    gas = GASolver(
        initial_pop=[0, 2, 4, 6],
        goal=goal,
        target_value=0,
        mutation=mutation,
        prob_mutation=0.7,
        crossover_=crossover,
        random_seed=0,
    )

    assert gas


def test_current_state_eval(eq_solver):
    """
    Tests if the GA solver correctly computes the current state
    """
    assert eq_solver.current_state == [-49, -45, -33, -13]
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

    assert eq_solver.current_state == [
        3.798653529573585,
        -21.266419263612008,
        -38.33149205679761,
        -47.39656484998319,
    ]


def test_crossover_works(eq_solver):
    """
    Tests if the solver correctly crosses over two solutions
    """
    eq_solver.random_seed = 4242424242

    sibling = eq_solver.crossover(10, 20)

    assert sibling == 14.142135623730951
