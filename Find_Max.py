#Write a program which finds the largest element in the array.
my_list = [1,22,3,4,5,99]

def my_max(my_list):
    for a in range(len(my_list)-1,-1,-1):
        largest = my_list[0]
        for a in my_list:
            if a > largest:
                largest = a
    return(largest)

m = my_max(my_list)
print(f"{m} is the largest number")