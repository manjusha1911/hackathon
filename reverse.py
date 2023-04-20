##Problem statement:
##(i)digit=7567
##Output should be=>[7,6,5,7]
##(ii) digit=4523
##Output should=> [3,2,5,4]

a=7567
i=0
while i<a:
    b=[int(i) for i in str(a)]
    i+=1
    j=-1
    while j<len(b):
        print(b[j],end=",")
        j-=1

