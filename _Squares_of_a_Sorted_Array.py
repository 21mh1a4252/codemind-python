x=int(input())
y=list(map(int,input().split()))
I=[]
for i in y:
    m=i**2
    I.append(m)
I=sorted(I)
for j in I:
    print(j,end=" ")