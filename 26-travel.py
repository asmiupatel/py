print("Travel from city A to city B")

time = int(input("Enter time: "))
longer = int(input("Define longer: "))

if (time >= longer) :
    price = int(input("Enter price: "))
    higher = int(input("Define higher: "))
    if (price >= higher) :
        print("Train")
    else :
        print("Coach")
else :
    price = int(input("Enter price:"))
    higher = int(input("Define higher:"))
    if (price >= higher) :
        print("Daytime Flight")
    else :
        print("Red Eye Flight")

print("Ariive city B")
    