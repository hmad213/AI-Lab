class Environment:
    def __init__(self, path):
        self.path = path

    def get_percept(self, i):
        return self.path[i]
    
    def get_path_size(self):
        return len(self.path)

class GoalBasedAgent:
    def __init__(self):
        self.goal = "Red House"
    
    def formulate_goal(self):
        return self.goal
    
    def act(self, percept):
        if percept == self.goal:
            return "Found! Exiting..."
        return "Not Found"
    
def run_agent(environment: Environment, agent: GoalBasedAgent):
    for i in range(environment.get_path_size()):
        percept = environment.get_percept(i)
        action = agent.act(percept)

        print(f"Step {i + 1}: Position {i} -> Percept - {percept}, Action - {action}") 
        if(action != "Not Found"):
            return 
        
e = Environment(['Blue House', 'Green House', 'Red House', 'Yellow House', 'White House'])
a = GoalBasedAgent()

run_agent(e, a)