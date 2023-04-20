##Given an integer n, return true if it is a power of four. Otherwise, return false.
##An integer n is a power of four, if there exists an integer x such that n == 4x.

# n=int(input("enter number:"))
# power=n*4
# i=0
# while i<n:


def power(num):
    if num==0:
        return False
    elif num==1:
        return True
    elif num%4!=0:
        return False
    else:
        return True
num=int(input("enter number:"))
print(power(num))


