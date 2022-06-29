a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    re=0
    while i:
        r=i%10
        re=re*10+r
        i//=10
    if(temp==re):
        print(temp,end=' ')