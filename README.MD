# GA Solver

[![Build Status](https://travis-ci.org/fbidu/simple-ga-solver.svg?branch=master)](https://travis-ci.org/fbidu/simple-ga-solver)
[![Documentation Status](https://readthedocs.org/projects/simple-ga-solver/badge/?version=latest)](https://simple-ga-solver.readthedocs.io/en/latest/?badge=latest)

Uma forma _pythonica_ de usar Algoritmos Genéticos.

## Uso

Instale com `pip install ga-solver`

```python

def goal(x):
    # Defina uma função-objetivo

def mutation(x):
    # Defina uma função que faz a mutação

def crossover(x, y):
    # Defina uma função que faz o cruzamento de duas soluções

initial_pop = [] # defina uma população inicial

# Você pode montar seu próprio seletor de população ou usar algum já embutido
from ga_solver.pop_selectors import roulette
from ga_solver import GASolver

# A instância GASolver aceita diversos argumentos para customizar sua solução
problem = GASolver(
    initial_pop,
    goal=goal,
    target_value=1000,
    mutation=mutation,
    prob_mutation=0.4,
    crossover_=crossover,
    selector=roullete,
    max_steps=2000
)

for state in problem:
    best_solution = problem.best_solution
    print(f"Tentando solução #{problem.steps}")
    print(f"O melhor encaixe até agora tem valor {best_solution[1]}")
    print(f"O estado atual é {state}")
    print(f"A população tem tamanho {len(problem)})

if problem.solution_found:
    print(f"A solução encontrada é {problem.solution}")
```
