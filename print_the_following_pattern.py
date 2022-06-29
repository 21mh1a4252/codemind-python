N=int(input())
for i in range(N,0,-1):
    for j in range(1,N+1):
        if i==j or i>j:
            print(chr(64+i),end=' ')
    print()