n=int(input())
if n<3 or n>100:
    print('The pattern is not possible')
else:
    for i in range(1,2*n):
        for j in range(1,n+1):
            if i==n or i==j or (i+j<=2*n and i>j):
                print('*',end='')
        print()
        
        
