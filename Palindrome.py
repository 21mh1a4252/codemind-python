def rev(n):
    re=0
    while n:
        r=n%10
        re=re*10+r
        n//=10
    return re
a=int(input())
b=rev(a)
if b==a:
    print('True')
else:
    print('False')