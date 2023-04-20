##Problem (Problem Code: FBC, fill the buckets)
##Chef has a bucket having a capacity of K liters. 
# It is already filled with X liters of water.
# Find the maximum amount of extra water in liters that Chef can fill in the bucket
#  without overflowing.

k=int(input("enter capacity of water in litres:"))
x=int(input("enter litres of water in bucket k:"))
if k<x:
    print("overflow")
elif k==x:
    print("water is full")
else:
    water=k-x
    print(water)