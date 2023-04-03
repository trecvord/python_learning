# --------------------------------------------------
#
# Program by R. Kholmurotov.
#
#
#  Version        Date           Info
#  1.0            2023      Autumn Version
#
# -----------------PRACTICE-------------------------






# def outer(func):
#     def inner(*args, **kwargs):
#         print("Advertisement")
#         return func(*args, **kwargs)
#
#     return inner
#
# @outer
# def fak(a, b):
#     return a / b
#
#
# print(fak(2, 2))

def my_decor(func):
    def wrapper(n):
        print('start')
        func(n)
        print('end')
    return wrapper


@my_decor
def my_func(number):
    print(number ** 2)

my_func(10)