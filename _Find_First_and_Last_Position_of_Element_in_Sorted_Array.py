x=int(input())
I=list(map(int,input().split()))
y=int(input())
c=-1
d=-1
for i in range(x):
    if I[i]==y and c==-1:
        c=i
    if I[i]==y:
        d=i
print(c,d)