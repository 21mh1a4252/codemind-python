n=int(input())
i=0
while n!=1 and n!=7:
    su=0
    temp=n
    while temp:
        r=temp%10
        su+=r**2
        temp//=10
    n=su
    i+=1
    if i>50:
        break
if n==1 or n==7:
    print('True')
else:
    print('False')