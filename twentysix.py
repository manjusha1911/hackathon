##Write a function that takes an integer minute and converts it to seconds.
##Examples
##convert(5) ➞ 300
##convert(3) ➞ 180
##convert(2) ➞ 120


def second(minutes):
    sec=60
    result=minutes*sec
    return result
minutes=int(input("enter minutes:"))
print(second(minutes))