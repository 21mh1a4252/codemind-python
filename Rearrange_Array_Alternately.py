x=int(input())
for i in range(x):
    a=int(input())
    I=sorted(list(map(int,input().split())))
    n=len(I)//2
    m=len(I)
    s=[]
    if m%2==1:
        for j in range(n):
            s.append(I[m-(j+1)])
            s.append(I[j])
        s.append(I[n])
        print(*s)
    else:
        for j in range(n):
            s.append(I[m-(j+1)])
            s.append(I[j])
        print(*s)
    