# --------------------------------------------------
#
# Program by R. Kholmurotov.
#
#
#  Version        Date           Info
#  1.0            2023      Autumn Version
#
# --------------------------------------------------



# before = [9, 45, 23, 11, 21, -5, 26]
#
# def bubble_sort(mylist):
#     last_item = len(before) - 1
#     for z in range(0, last_item):
#         for x in range(0, last_item - z):
#             print(mylist)
#             if mylist[x] > mylist[x+1]:
#                 mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
#
#     return mylist
#
# print("before: ", before)
# after = bubble_sort(before).copy()
# print("after: ", after)

#---------------------------------------------------------

# n = int(input())
# mylist = list(map(int, input()))
# count = 0
# for x in range(n - 1):
#     for z in range(n-1-x):
#         # print(f"now comparing: {mylist[z]} and {mylist[z+1]}")
#         if mylist[z] > mylist[z+1]:
#             count += 1
#             mylist[z], mylist[z+1] = mylist[z+1], mylist[z]
#
# print(*mylist)
# print(count)

#--------------------------------------------------------------

