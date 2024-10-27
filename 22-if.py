print("Enter your marks in maths exam.")

marks = int(input())

if (marks > 100) :
    print("Please enter a valid input")
elif (marks < 33) :
    print("You have failed. Better luck next time.")
else :
    print("You have passed. Congratulations!")    