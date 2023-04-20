##In computing, the collection of four bits is called a nibble. Chef defines a program as:
##Good, if it takes exactly X nibbles of memory, where X is a positive integer.
##Not Good, otherwise. Given a program that takes N bits of memory, 
# determines whether it is Good or Not Good.

x=int(input("enter no. of nibbles:"))
bits_per_nibble=4
if x%bits_per_nibble==0:
    print("GOOD")
else:
    print("NOT GOOD")