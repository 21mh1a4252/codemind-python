x=int(input())
b=list(map(int,input().split()))
c=0
I=[]
for i in range(len(b)):
    for j in range(len(b)):
        if b[i]==b[j]:
            c+=1
    if c==1:
        I.append(b[i])
    c=0
if len(I)==0:
    print('-1')
elif I!=0:
    print(max(I))