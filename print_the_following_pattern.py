N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if(j==1 and i<=N) or(i==N and j<=N):
            print('*',end='')
        elif(i==j):
            print('*',end='')
        else:
            print(' ',end='')
    print()