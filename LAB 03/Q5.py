class QBot:
    def __init__(self):
        self.values = {"Play": 0, "Rest": 0}

    def learn_step(self, act, rwd):
        self.values[act] = self.values[act] + 0.1 * (rwd - self.values[act])

def simulate():
    q_agent = QBot()
    count = 1
    while count <= 10:
        a, r = "Play", 5
        q_agent.learn_step(a, r)
        if count in [1, 5, 10]:
            print(f"Step {count}: Action {a} Reward {r}")
        count += 1
    print("Q-table Updated:", q_agent.values)

simulate()
