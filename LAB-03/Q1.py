class Environment:
    def __init__(self, beds):
        self.beds = beds

    def get_precept(self, i):
        return self.beds[i]
    
    def get_number_states(self):
        return len(self.beds)

    def display(self):
        for i in range(len(self.beds)):
            print(f"Bed {i + 1}: {self.beds[i]}")

class SimpleReflexAgent:
    def __init__(self):
        self.index = 0

    def act(self, state, grid):
        if(state == "Dry"):
            grid[self.index] = "Moist"
            return "Watered"
        return "Skip"
    
    def move(self):
        self.index += 1

def run_agent(environment, agent):
    for i in range(environment.get_number_states()):
        state = environment.get_precept(i)
        action = agent.act(state, environment.beds)   
        print(f"Step {i + 1}: Position {i} -> Percept - {state}, Action - {action}")    
        agent.move()

    print()
    environment.display()

a = SimpleReflexAgent()
e = Environment(["Moist", "Dry", "Moist", "Moist", "Dry", "Moist", "Dry", "Moist", "Dry"])

run_agent(e, a)