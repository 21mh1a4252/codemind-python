def fact(n):
    s=1
    for i in range(1,n+1):
        r=i%10
        s*=r
        i//=10
    return s
T=int(input())
for i in range(1,T+1):
    N=int(input())
    print(fact(N))