##Chef wants to reach home as soon as possible. He has two options:
##Travel with his BIKE which takes X minutes.
##Travel with his CAR which takes Y minutes.
##Which of the two options is faster or do they both take the same time?


x=int(input("enter miniutes taken by bike:"))
y=int(input("enter miniutes taken by car:"))
if x==y:
    print("SAME")
elif x<y:
    print("BIKE")
else:
    print("CAR")