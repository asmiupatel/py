#dynamic typing
#things can change

n = 10
print(type(n))
print(n)
n = n/2
print(type(n)) #would be float as the division function always gives float number as a result
print(n) 
n = 10
print(type(n))
print(n)
n = n/1
print(type(n)) #would also result in float cuz dividing by any number, be it 1 or any other number, the result will always be a float number
print(n)