##Suppose Andy and Doris want to choose a restaurant for dinner, 
# and they both have a list of favorite restaurants represented by strings.
##You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.
## eg: Input: 
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]

# Input:list1=["Shogun","Tapioca Express","Burger King","KFC"],
# list2=["KFC","Shogun","Burger King"]
#Output:["Shogun"]
##Explanation:The restaurant they both like and have the least index sum is "Shogun" 
# with index sum 1 (0+1).

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
list1=["Shogun","Tapioca Express","Burger King","KFC"],
list2=["KFC","Shogun","Burger King"]
i=0
index_sum=0
while i<len(list1):
    if list1[i] in list2:
        print(str(i))
    i+=1

        



# grocery_list=['flour','cheese','carrot']
# length=len(grocery_list)
# i=0
# while i<length:
#     print(str(i),":",grocery_list[i])
#     i+=1