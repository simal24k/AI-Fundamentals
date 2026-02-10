class StudyBot:
    def __init__(self, todo):
        self.todo_list = todo

    def execute_plan(self):
        for item in list(self.todo_list):
            print(f"Studying {item}")
            self.todo_list.remove(item)
        if not self.todo_list:
            print("Goal Achieved: All subjects completed")

planner = StudyBot(["AI", "Math", "Physics"])
planner.execute_plan()
