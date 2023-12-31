import re
m,n = tuple(map(int, input().split()))
a=[]
for i in range(m):
    a.append(list(input().rstrip('\n')))
s=""
for i in range(n):
    for j in range(m):
        s+=a[j][i]
p = re.compile(r'([a-zA-z0-9][\$\#\!\@\ \%\&]{1,99}[a-zA-Z0-9])')
matches = list(map(lambda x: x[1:-1],re.findall(p, s)))
b=s[:]
for i in matches:
    b=b.replace(i, " ", 1)

print(b)

