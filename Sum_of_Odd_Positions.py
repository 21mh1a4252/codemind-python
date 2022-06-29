N=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(1,N,2):
    sum+=a[i]
print(sum)