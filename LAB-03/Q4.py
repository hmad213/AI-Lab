import math

class Environment:
    def __init__(self, rocks):
        self.rocks = rocks

    def get_percept(self):
        return self.rocks
    
class UtilityBasedAgent:
    def __init__(self):
        pass

    def utility(self, rock):
        return rock['value'] * 2 - rock["cost"]
    
    def act(self, percept):
        best_rock = None
        best_utility = -math.inf

        for rock in percept:
            rock_utility = self.utility(percept[rock])
            if rock_utility > best_utility:
                best_rock = rock
                best_utility = rock_utility

        return f"{best_rock} is the best rock"
    
def run_agent(environment: Environment, agent: UtilityBasedAgent):
    percept = environment.get_percept()
    action = agent.act(percept)

    print(f"Percept - {percept}\nAction - {action}")


e = Environment({
    "Rock A": {
        "value": 5,
        "cost": 2
    },
    "Rock B": {
        "value": 9,
        "cost": 8
    },
    "Rock C": {
        "value": 6,
        "cost": 3
    }
})

a = UtilityBasedAgent()

run_agent(e, a)