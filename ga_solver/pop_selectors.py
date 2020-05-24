"""
Provides different strategies for population selection
"""
from random import seed, random

from .range_dict import RangeDict


def build_roullete(population):
    """
    Returns a RangeDict with keys related to the value's probability of
    being chosen in a Roullete Selection

    >>> build_roullete({"a": 10, "b": 10, "c": 20})
    {(0, 0.25): "a", (0.25, 0.5): "b", (0.5, 1): "c"}
    """
    sum_probabilities = sum(population.values())
    averaged_probs = {k: v / sum_probabilities for k, v in population.items()}

    start = 0
    result = RangeDict()

    for value, prob in averaged_probs.items():
        result[(start, start + prob)] = value
        start += prob

    return result


def roullete_selection(population, random_seed=None):
    """
    Uses a classic roullete strategy for selection. Every individual has a
    probability of being selected equal to

    (its goal value)/(the sum of all goal values)

    Args:
        population (dict): a dictionary containing the elements as key and their
            fitness as values.
        random_seed (int, optional): if supplied, Python PRNG's seed is set to
            it. Use **only** if you need a total reproducible behavior such
            as in testing.

    Returns:
        A list containing the selected members
    """
    # This is safe because if the seed is None, Python will use a default behavior
    seed(random_seed)
    total_fitness = sum(population.values())

    selected = []

    for item, fitness in population.items():
        if random() < fitness / total_fitness:
            selected.append(item)

    return selected
