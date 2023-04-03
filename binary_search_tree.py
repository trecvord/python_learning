# --------------------------------------------------
#
# Program by R. Kholmurotov.
#
#
#  Version        Date           Info
#  1.0            2023      Autumn Version
#
# --------------------------------------------------

def binarysearch(mylist, s, start, stop):

    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if s == mylist[mid]:
            return mid
        elif s < mylist[mid]:
            return binarysearch(mylist, s, start, mid - 1)
        else:
            return binarysearch(mylist, s, mid + 1, stop)



mylist = [11, 13, 20, 33, 34, 45, 46, 66, 67, 68, 76, 97, 98, 99]
s = 13
start = 0
stop = len(mylist)

x = binarysearch(mylist, s, start, stop)

if not x:
    print("bratan, item ", s, " not found!")
else:
    print("bushman, item on ", x, " index!")