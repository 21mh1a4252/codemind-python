N=int(input())
a=list(map(int,input().split()))
so=0
for i in range(0,N):
    if a[i]%2!=0:
        so+=a[i]
print(so)
