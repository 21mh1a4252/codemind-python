N=int(input())
for i in range(0,N):
    for j in range(1,N+1):
        if(i+j)==N or (i+j)<N:
            print(j+i,end=' ')
    print()