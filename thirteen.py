##13. Move Zeroes
##Given an integer array nums, move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.
##Note that you must do this in-place without making a copy of the array.
 
##Example 1:
##Input: nums = [0,1,0,3,12]
##Output: [1,3,12,0,0]

##Example 2:
##Input: nums = [0]
##Output: [0]

def move_zero(list):
    i=0
    a=[]
    b=[]
    while i<len(list):
        if list[i]==0:
            a.append(list[i])
        else:
            b.append(list[i])
        i+=1
    b.extend(a)
    print(b)
list=[0,1,0,3,12]
move_zero(list)
