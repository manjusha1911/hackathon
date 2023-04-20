##Create a function that takes a number num and returns its length.
##Examples
##number_length(10) ➞ 2
##number_length(5000) ➞ 4


def length(num):
    a=[]
    b=str(num)
    a.extend(b)
    i=0
    count=0
    while i<len(a):
        count+=1
        i+=1
    print(count)
num=int(input("enter number:"))
length(num)

