print("Please enter the number you want to check ends with 0 or 5 or other:")

index = int(input())

if (index % 10 == 0) :
    print(index, "ends with 0.")
elif (index % 10 == 5)    :
    print(index, "ends with 5.")
else :
    print(index, "ends with something other than 0 or 5.")   