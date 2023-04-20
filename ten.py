##Vasya likes the number 239. Therefore, he considers a number pretty if its last digit is 
# 2, 3 or 9. Vasya wants to watch the numbers between L and R (both inclusive), 
# so he asked you to determine how many pretty numbers are in this range. Can you help him?

# l=int(input("enter start number:"))
# r=int(input("enter end number:"))
# pretty_count=0
# for i in range(l,r+1):
#     if i%10==2 or i%10==3 or i%10==9:
#         pretty_count+=1
# print(pretty_count)
    


# def pretty_count(l,r):
#     count=0
#     for i in range(l,r+1):
#         if i%10==2 or i%10==3 or i%10==9:
#             count+=1
#     print(count)
# l=int(input("enter start number:"))
# r=int(input("enter end number:"))
# pretty_count(l,r)


l=int(input("enter start number:"))
r=int(input("enter end number:"))
pretty_count=0
i=l
while i<=r:
    if i%10==2 or i%10==3 or i%10==9:
        pretty_count+=1
    i+=1
print(pretty_count)

