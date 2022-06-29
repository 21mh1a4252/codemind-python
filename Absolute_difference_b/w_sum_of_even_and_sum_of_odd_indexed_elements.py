N=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,N):
    if i%2==0:
        s1+=a[i]
    else:
        s2+=a[i]
res=abs(s1-s2)
print(res)