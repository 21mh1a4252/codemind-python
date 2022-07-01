x=int(input())
I=list(map(int,input().split()))
y=int(input())
m=max(I)
Ik=[]
for i in I:
    if(y+i)>=m:
        print('True',end=" ")
    else:
        print("False",end=' ')