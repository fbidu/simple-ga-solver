Welcome to GASolver's documentation!
====================================

Introduction
^^^^^^^^^^^^

GASolver is a simple and pure-Python framework for solving problems with `genetic
algorithms <https://natureofcode.com/book/chapter-9-the-evolution-of-code/>`_.
With its *pythonic* interface, it allows for a clean implementation of the
necessary steps.

It also provides selectors for your population. Currently, the only one available
is the `Roulette Wheel Selection <https://en.wikipedia.org/wiki/Fitness_proportionate_selection>`_

Example
^^^^^^^

Suppose you have defined the necessary attributes for a Genetic Algorithm, that
is:

* A **mutation** function e.g.: ``mutation(x)``
* A **crossover** function e.g.: ``crossover(x, y)``
* An **initial population** e.g.: ``[1, 2, 3]``
* A **fitness function** e.g.: ``fitness(x)``
* A **goal value** e.g.: ``42``

You can easily create a new instance of ``GAsolver``:

.. code-block:: python
   :linenos:

   from ga_solver import GASolver

   solver = GASolver(
        initial_pop=initial_pop,
        goal=fitness,
        target_value=maxsize,
        mutation=mutation,
        prob_mutation=0.7,
        crossover_=crossover,
        selector=roullete
    )

   for state in solver:  # GASolvers are iterable
      print(f"The current step is {solver.steps}")
      print(f"The best fit so far has value of {solver.best_solution[1]}")
      print(f"The current state is {state}")
      print(f"Population has size {len(problem)}")


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   ga_solver



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
