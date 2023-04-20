###(i) get_average=[2, 2, 2, 2]
##output= 2
##(ii) get_average=[1, 5, 87, 45, 8, 8]
##output= 25
##(iii) get_average=[2,5,13,20,16,16,10]
##output= 11
##(iv) get_average=[1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]
##output= 11

# a=[2,2,2,2]
# i=0
# sum=0
# mean=0
# while i<len(a):
#     sum=sum+a[i]
#     mean=sum//len(a)
#     i+=1
# print(mean)

a=[1,5,87,45,8,8]
i=0
sum=0
mean=0
while i<len(a):
    sum=sum+a[i]
    mean=sum//len(a)
    i+=1
print(mean)