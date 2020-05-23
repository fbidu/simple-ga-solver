"""
Defines the main Genetic Algorithm Solver class
"""
from random import random, seed

# pylint: disable=too-many-instance-attributes
class GASolver:
    """
    A simple Genetic Algorithm Solver. It accepts an initial population, and several
    callables to define goal, mutation and crossovers.

    Args:

        initial_pop (list): The elements of the initial population.
        goal (function): A function that accepts one member of the population
            and returns its current value.
        target_value (numeric): The value you're looking for. When the goal(x)
            for any member x of the population is equal to this, the solution
            has been found.
        mutation (function): A callable that accepts one member of the population
            and returns a mutated value of that member.
        prob_mutation (float, 0 <= prob_mutation <= 1)): The probability of a
            mutation occur in any individual. Every time that the `mutation`
            function is invoked, there's `prob_mutation` chance of it actually
            DOING anything.
        crossover_: (function): A callable that takes 2 arguments that are current
            solutions and crosses them over, returning a new one
        random_seed (int, optional): If provided, the seed of Python's PRNG will
            be set to this. In practice you _only_ want to set this value when
            you need reproducible runs. Useful for testing
    """

    __current_state = []

    # pylint: disable=too-many-arguments, bad-continuation
    def __init__(
        self,
        initial_pop,
        goal,
        target_value,
        mutation,
        prob_mutation,
        crossover_,
        random_seed=None,
    ):
        self.population = initial_pop

        self.goal = goal
        self.target_value = target_value

        self.mutation = mutation
        self.prob_mutation = prob_mutation

        self.crossover_ = crossover_

        self.random_seed = random_seed

    @property
    def current_state(self):
        """
        Current state computes the status of the current
        population by applying the goal function to
        all of its members
        """
        self.__current_state = [self.goal(indiv) for indiv in self.population]

        return self.__current_state

    @property
    def solution_found(self):
        """
        Returns True if any member of the current population
        has goal(x) == target_value
        """
        meets_target = [x == self.target_value for x in self.current_state]
        return any(meets_target)

    def mutate(self, individual):
        """
        Mutate tries to apply the mutation function, but it actually
        does anything only a few times, determined by `prob_mutation`
        """
        seed(self.random_seed)
        if random() < self.prob_mutation:
            return self.mutation(individual)

        return individual

    def mutate_pop(self):
        """
        Runs the entire population through `mutate`. Note that not _every_ time
        that mutate is called it actually does anything. Check `mutate's` doc
        for details
        """
        self.population = [self.mutate(x) for x in self.population]

    def crossover(self, sol_a, sol_b):
        """
        Calls the crossover function with the parameters
        `sol_a` and `sol_b` and returns the given sibling
        """
        return self.crossover_(sol_a, sol_b)
