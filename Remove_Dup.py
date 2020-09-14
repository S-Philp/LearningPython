#Write a program which will remove duplicates from the array.
names = ["Alex","John","Mary","Steve","John", "Steve"] 
names = list(dict.fromkeys(names))
print(names)
