s = "tHiS is My bLog."

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.swapcase())
print(s.title())

print(s.islower())
print(s.isupper())
print(s.istitle())

s = '123'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
s = 'abc'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
s = '12ab'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())

s = '-----Gang-----'
print(s.strip('-'))
print(s.lstrip('-'))
print(s.rstrip('-'))

s = 'Babygirl'
print(s.startswith('B'))
print(s.startswith('b'))
print(s.endswith('l'))
print(s.endswith('L'))

s = 'No bandana thas no problem'
print(s.count('a'))
print(s.count('N'))
print(s.index('a'))
print(s.index('n'))
print(s.replace('N', 'n'))
print(s.replace('b', 'B'))