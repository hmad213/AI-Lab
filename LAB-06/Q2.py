import random
import math

def get_neighbors(x: int):
    values = []
    if(x + 1 <= 100):
        values.append(x + 1)
    if(x - 1 >= 0):
        values.append(x - 1)
    return values

def get_value(x: int):
    return pow(x, 2) + 10 * x + 5

def hill_climbing(x: int):
    current_cost = get_value(x)
    current_state = x

    while True:
        print(f"{current_state}, {current_cost}")
        next_state = None
        next_cost = current_cost
        for neighbor in get_neighbors(current_state):
            new_cost = get_value(neighbor)
            if new_cost > next_cost:
                next_cost = new_cost
                next_state = neighbor

        if next_cost <= current_cost:
            break

        current_cost = next_cost
        current_state = next_state

    return current_state, current_cost

state, cost = hill_climbing(random.randint(0, 100))
print(f"X: {state}, Value: {cost}")