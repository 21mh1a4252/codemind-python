x=int(input())
y=list(map(int,input().split()))
I=[]
for i in range(len(y)):
    s=0
    for j in range(len(y)):
        if y[i]>y[j]:
            s+=1
    I.append(s)
    s=0
for a in I:
    print(a,end=' ')