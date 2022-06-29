n=int(input())
sq=pow(n,2)
r=0
x=0
i=10
while r!=sq:
    r=sq%i
    if n==r:
        print('Automorphic Number')
        x=1
        break
    i*=10
if x==0:
    print('Not an Automorphic Number')