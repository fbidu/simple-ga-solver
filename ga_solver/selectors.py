"""
Provides different strategies for population selection
"""
from random import seed, random


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
