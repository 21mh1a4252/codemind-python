import math
n=int(input())
for i in range(1,n+1):
    m=int(input())
    a=math.floor(m**0.5)
    sq=a*a
    if int(m-sq)==0:
        print('True')
    else:
        print('False')