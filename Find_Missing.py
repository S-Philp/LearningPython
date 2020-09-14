my_num = [0,2,3,4,5]
good_num = [0,1,2,3,4,5]

for a in good_num:
    if a not in my_num:
        my_num.append(a)
        print("In this array " + str(a) + " was missing and has been added.")
my_num.sort()
print(my_num)

