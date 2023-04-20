##(i)  list1=[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
     ##output => [8,-50]
##(ii) list=[1]
     ##Output => [1,0]
##(iii) list=[-1]
      #3Output => [0,-1]

list=[0,2,3,0,5,6,7,8,9,10,-11,-12,-13,-14]
count_p=0
sum_n=0
i=0
while i<len(list):
    if list[i]<=0:
        sum_n=sum_n+list[i]
    if list[i]>0:
        count_p+=1
    i+=1
print(count_p,",",sum_n)


