N=int(input())
a,b=0,1
print(a,b,end=' ')
i=2
for i in range(3,N+1):
    c=a+b
    print(c,end=' ')
    a,b=b,c
    i+=1
    