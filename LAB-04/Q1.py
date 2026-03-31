class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal found"
        return "Searching"
    
    def bfs_search(self, graph, start, goal):
        visited = [start]
        queue = [start]

        while(queue):
            current = queue.pop(0)
            print(f"Visiting: {current}")

            if current == goal:
                return f"Goal {self.goal} found!"
            
            for state in graph.get(current, []):
                if state not in visited:
                    visited.append(state)
                    queue.append(state)

        return "Goal not found!"


            

    def act(self, precept, graph):
        goal_status = self.formulate_goal(precept)
        if goal_status == "Goal found":
            return f"Goal {self.goal} found!"
        else:
            return self.bfs_search(graph, precept, self.goal)

def run_agent(environment: Environment, agent: GoalBasedAgent):
    percept = environment.get_percept("Tehran")
    action = agent.act(percept, environment.graph)
    print(action)

e = Environment({
    "Tehran": ["Baghdad", "Istanbul"],
    "Baghdad": ["Cairo"],
    "Istanbul": ["Berlin"],
    "Cairo": ["Washington"],
    "Berlin": ["Washington"],
})
a = GoalBasedAgent("Washington")

run_agent(e, a)