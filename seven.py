##anmansh received X coins of 10 rupees and Y coins of 5 rupees from Chingari. 
# Since he is weak in math, can you find out how much total money does he have?

x=int(input("enter no. of 10 rupees coins:"))
y=int(input("enter no. of 5 rupees coins:"))
if x>0 and y>0:
    ten=x*10
    five=y*5
    total_amount=ten+five
    print(total_amount)
elif x>0 and y<=0:
    print(x*10)
elif x<=0 and y>0:
    print(y*5)