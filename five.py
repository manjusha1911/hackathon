##Chef wants to gift C chocolates to Botswal on his birthday. 
# However, he has only X chocolates with him. The cost of 1 chocolate is Y rupees.
##Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.


choco=int(input("enter no. of choco chef needs:"))
choco1=int(input("enter no. of choco chef have:"))
cost=int(input("enter cost of one choco:"))
if choco1>choco:
    print("excess")
else:
    r=choco-choco1
    money=cost*r
    print(money)