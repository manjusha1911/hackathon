##Two strings are anagrams if you can make one from the other by rearranging the letters.
##Write a function named is_anagram that takes two strings as its parameters.
#  Your function should return True if the strings are anagrams, and False otherwise.
##For example, the call is_anagram("typhoon", "opython") should return True 
# while the call is_anagram("Alice", "Bob") should return False.

def anagram(a,b):
    if len(a)==len(b):
        i=0
        while i<1:
            if a[i] in b:
                print(a, "and",b ,"are anagram")
            else:
                print("not anagram")
            i+=1
    else:
        print("not anagram")
a=input("enter string:")
b=input("enter string:")
anagram(a,b)