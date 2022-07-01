x=int(input())
I=list(map(int,input().split()))
n=[]
c=0
for i in list(set(I)):
    for j in I:
        if i==j:
            c+=1
    n.append([c,i])
    c=0
m=max(n)
print(m[1])
