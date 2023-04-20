##Create a function that takes a number as an argument, increments the number by +1, 
# and returns the result.
##Examples
##addition(0) ➞ 1
 ##addition(9) ➞ 10


def next_number(number):
    number+=1
    return number
number=int(input("enter number:"))
print(next_number(number))