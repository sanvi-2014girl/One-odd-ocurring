def oneodd(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res
arr = []
n= int(input("Enter the number of elements to be added: "))
while n:
    num = int(input("Enter number: "))
    arr.append(num)
    n = n-1
    print("one odd occuring num is;",oneodd(arr))
    