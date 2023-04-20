##Create a function that takes two numbers as arguments and returns their sum.
##Examples
##addition(3, 2) ➞ 5
 ##addition(-3, -6) ➞ -9


def sum_number(num1,num2):
    result=num1+num2
    return result
num1=int(input("enter number:"))
num2=int(input("enter number:"))
print(sum_number(num1,num2))