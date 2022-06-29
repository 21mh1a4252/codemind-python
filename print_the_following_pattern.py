N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print("*",end=' ')
        elif(j==1 and i<=N) or(j==N and i<=N):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()