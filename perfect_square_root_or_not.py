import math
n=int(input())
a=math.floor(n**0.5)
sq=int(a*a)
if n-sq==0:
    print('True')
else:
    print('False')