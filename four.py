##There are N bikes and M cars on the road.
##Each bike has 2 tyres.
##Each car has 4 tyres.
##Find the total number of tyres on the road.


n=int(input("enter no. of bikes:"))
m=int(input("enter no. of cares:"))
bike_tyre=2*n
car_tyre=4*m
total_tyres=bike_tyre+car_tyre
print(total_tyres)