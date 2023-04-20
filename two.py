##Problem (Problem Code: BATTERY LOW)
##The chef's phone shows a Battery Low notification if the battery level is 15% or less. 
# Given that the battery level of Chef's phone is X%, 
# determine whether it would show a Battery low notification.


n=int(input("enter no. of inputs:"))
i=0
while i<n:
    n1=int(input("enter battery percentage:"))
    if n1<=15:
        print("low battery")
    else:
        print("NO")
    i+=1
