A,B,C=map(int,input().split())
S=(A+B+C)/2
t=(S*(S-A)*(S-B)*(S-C))**0.5
print('{0:.2f}'.format(t))