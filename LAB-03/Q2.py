class Environment:
    def __init__(self, path):
        self.path = path
    
    def get_precept(self, i):
        return self.path[i]
    
    def get_path_size(self):
        return len(self.path)
    
class ModelBasedAgent:
    def __init__(self):
        self.__has_key = False

    def act(self, precept):
        if precept == 'D' and not self.__has_key:
            return f"Access denied to room {precept}"
        
        s = ""
        if precept == 'B' and not self.__has_key:
            self.update_key()
            s = f", Key acquired in room {precept}"

        return f"Access granted to room {precept}" + s

    def update_key(self):
        self.__has_key = True

def run_agent(environment: Environment, agent: ModelBasedAgent):
    for i in range(environment.get_path_size()):
        percept = environment.get_precept(i)
        action = agent.act(percept)

        print(f"Step {i + 1}: Position {i} -> Percept - {percept}, Action - {action}")   

e = Environment(["A", "C", "D", "B", "D"])
a = ModelBasedAgent()

run_agent(e, a)