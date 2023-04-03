# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# -------------------------------------------------------------------------------


# def count_sheeps(x):
#     return x.count(True)

# def make_negative(number):
#     return number*-1 if number > 0 else number

# -------------------------------------------------------------------------------


# def summation(num):
#     result = 0
#     count = 1
#
#     while count <= num:
#         result += count
#         count += 1
#
#     return result
#
# if __name__ == '__main__':
#
#     assert summation(1) == 1
#
#     assert summation(8) == 36

# -------------------------------------------------------------------------------
# total = 90
# #country = "LV"
# country = "UZB"
# if country == "LV":
#     if total <= 50:
#         print("Shipping cost is $50")
# elif total <= 90:
#     print("Shipping cost is $25")
# elif total <=150:
#     print("Shipping cost is $5")
# else:
#     print("FREE")
# if country == "UZB":
#     if total <= 50:
#         print("Shipping cost is $100")
# else:
#         print("FREE")

# -------------------------------------------------------------------------------

# def my_func():
#     print("Hello Python!")
#
# my_func()

# def somenum(num1, num2):
#     print(num1 + num2)
#
#
# somenum(2, 4)

# def multiply(num1):
#     return num1 * 5
#
#
# result = multiply(8)
# print(result)

# -------------------------------------------------------------------------------

# def my_func(fullname):
#     print(fullname + " Bushman")
#
#
# my_func("Max")
# my_func("Richardo")
# my_func("Rakha")
# ------------------------------------------------

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#   print("The youngest child is " + kids[1])
#
# my_function("Emil", "Tobias", "Linus")

# -----------------------------------------------

# def my_func(food):
#     for x in food:
#         print(x)
#
#
# fruits = ["banana", "cherry", "pineapple"]
#
# my_func(fruits)

#-----------------------------------------------------------RECURSION!!!!

# def tri_recurs(x):
#     if(x > 0):
#         result = x + tri_recurs(x - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("\n\nRecursion results: ")
# tri_recurs(20)

#-----------------------------------------------------------

# a = input("write your line: ")
# stack = []
# y = True
#
# for x in a:
#     if x in "([{":
#         stack.append(x)
#     elif x in ")]}":
#         if len(stack) == 0:
#             y = False
#             break
#
#         br = stack.pop()
#         if br == "(" and x == ")":
#             continue
#         if br == "[" and x == "]":
#             continue
#         if br == "{" and x == "}":
#             continue
#
#         y = False
#         break
#
# if y and len(stack) == 0:
#     print("Yes")
# else:
#     print("No")

#-------------------------------------------------------------------------


#   STACK

# s = []
#
# s.append("eat")
# s.append("sleep")
# s.append("code")
# s.append("repeat")
# s.pop()
#      just lists

# from collections import deque
# s = deque()
# s.append("eat")
# s.append("sleep")
# s.append("code")
# s.append("repeat")
# s
#                                 deque (better use this method)

#   QUEUES

#   just lists (recommended with only short lists)

# s = []
# s.append("eat")
# s.append("sleep")
# s.append("code")
# s.append("repeat")
# s.pop(0)

#    deque (recommended)

# from collections import deque
# s = deque()
# s.append("eat")
# s.append("sleep")
# s.append("code")
# s.append("repeat")
# s.popleft()

#----------------------------------------------

