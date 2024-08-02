# #super()- метод.
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = mod
#         self.color = color
#         self.year = year
# class SupperCar(Car):
#
#     def __init__(self, model, color, year,sponsor):
#
#         super().__init__(model, color,year)
#         self.sponsor = sponsor

# class MyClass:
#     @classmethod
#     def class_info(cls):
#         return f"this is the {cls.__name__} class"
# print(MyClass.class_info())

#dream Team:

# class Player:
#     def __init__(self, run, goal):
#         self.run = run
#         self.goal = goal
#
# class Protector(Player):
#     def __init__(self, run, goal):
#         super().__init__(run, goal)
#         self.smth = smth
# class MidFielder(Protector):
#     def __init__(self, run, goal, smth):
#         super().__init__(run, goal, smth, smth2)
#         self.smth2 = smth2
# class GoalKipper(MidFielder):
#     def __init__(self, run, goal, smth, touch):
#         super().__init__(run, goal, smth)
#         self.touch = touch
