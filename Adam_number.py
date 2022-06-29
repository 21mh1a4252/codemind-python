def rev(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
N=int(input())
sqo=N*N
sqr=rev(N)*rev(N)
if sqo==rev(sqr):
    print('True')
else:
    print('False')