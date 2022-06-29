N=int(input())
max=0
temp=N
while temp:
    r=temp%10
    temp//=10
    if r>max:
        max=r
print(max)