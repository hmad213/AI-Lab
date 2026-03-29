import random

class Environment:
    def __init__(self):
        self.path = ["Start", "Empty", "Cheese", "Trap"]
        self.rewards = {
            "Start": 0,
            "Empty": -1,
            "Cheese": 10,
            "Trap": -10
        }

    def get_precept(self):
        return [1, 2, 3]
    
    def move(self, index):
        state = self.path[index]
        reward = self.rewards[state]
        return (state, reward)
    
class LearningAgent:
    def __init__(self):
        self.knowledge = {}

    def select_action(self, actions):
        return random.choice(actions)
    
    def act(self, actions):
        action = self.select_action(actions)
        return action

    def learn(self, state, reward):
        self.knowledge[state] = reward
        print(f"Learned that moving to {state} gives {reward} points!")

def run_agent(environment: Environment, agent: LearningAgent):
    actions = environment.get_precept()

    action = agent.act(actions)

    state, reward = environment.move(action)

    agent.learn(state, reward)
    
e = Environment()
a = LearningAgent()

run_agent(e, a)