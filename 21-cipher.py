a = 'abcdefghijklmnopqrstuvwxyz'

s = 'superb'

i = 0
k = 3
t = ''
t = t + (a[((a.index(s[i])) +k) %26])
t = t + (a[((a.index(s[i + 1])) +k) %26])
t = t + (a[((a.index(s[i + 2])) +k) %26])
t = t + (a[((a.index(s[i + 3])) +k) %26])
t = t + (a[((a.index(s[i + 4])) +k) %26])
t = t + (a[((a.index(s[i + 5])) +k) %26])
print(t)