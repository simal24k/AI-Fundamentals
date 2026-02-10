class TrafficSystem:
    def __init__(self, current_flow):
        self.flow = current_flow

    def sense(self):
        return self.flow

class TrafficAgent:
    def decide(self, data):
        return "Extend Green Time" if data == "Heavy Traffic" else "Normal Green"

def execute():
    for traffic in ["Heavy Traffic", "Light Traffic"]:
        context = TrafficSystem(traffic)
        bot = TrafficAgent()
        info = context.sense()
        result = bot.decide(info)
        print(f"Percept: {info} -> Action: {result}")

execute()
