list=[1,3,8,1,8]
i=0
a=[]
sum=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        sum=sum+list[i]
    i+=1
print(a)
print(sum)
print("seminao")