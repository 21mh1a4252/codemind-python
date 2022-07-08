x=int(input())
for i in range(x):
    if i*(i+1)==x:
        print('YES')
        break
else:
    print('NO')