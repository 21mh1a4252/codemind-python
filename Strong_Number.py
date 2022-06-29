def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
N=int(input())
s=0
temp=N
while temp:
    r=temp%10
    s+=fact(r)
    temp//=10
if s==N:
    print('The number',N,'is a strong number')
else:
    print('The number',N,'is not a strong number')