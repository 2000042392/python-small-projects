# 4. Shape Calculator — Abstraction + Menu ⭐⭐⭐⭐⭐
#
# Create an abstract class:
#
# Shape
#
# with an abstract method:
#
# area()
#
# Create two subclasses:
#
# Shape
#  ├── Circle
#  └── Rectangle
# Menu:
# 1. Circle
# 2. Rectangle
# 3. Exit
#
# If Circle:
#
# Enter radius: 5
# Area: 78.5
#
# If Rectangle:
# #
# # Enter length: 10
# # Enter width:
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class circle(shape):
#     def __init__(self):
#         self.radius=int(input("enter the radius of the circle: "))
#     def area (self):
#         self.area=3.14*(self.radius)**2
#         print(self.area)
# class rectangle(shape):
#     def __init__(self):
#         self.length=int(input("enter the length of the rectangle: "))
#         self.width=int(input("enter the width of the rectangle: "))
#     def area(self):
#             self.area=(self.length*self.width)
#             print(self.area)
# while True:
#     print(1,"circle")
#     print(2,"rectangle")
#     print(3,"exit")
#     choice=int(input("enter your choice: "))
#     if choice==1:
#         c=circle()
#         c.area()
#     elif choice==2:
#         r=rectangle()
#         r.area()
#     elif choice==3:
#         print("exit")
#     else:
#         print("enter valid choice")


