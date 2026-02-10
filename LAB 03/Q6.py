class FireEnvironment:
    def __init__(self):
        self.grid = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def display(self):
        nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        for i in range(0, 9, 3):
            row = [("🔥" if self.grid[nodes[j]] == "fire" else " ") for j in range(i, i+3)]
            print(f"| {' | '.join(row)} |")
        print("-" * 13)

class FireRobot:
    def run(self, env):
        path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        for room in path:
            print(f"Robot moved to {room}")
            if env.grid[room] == 'fire':
                print(f"Fire detected in {room}! Extinguishing...")
                env.grid[room] = 'safe'
            env.display()
        print("Final Status: All fires extinguished.")
        env.display()

env = FireEnvironment()
robot = FireRobot()
robot.run(env)
