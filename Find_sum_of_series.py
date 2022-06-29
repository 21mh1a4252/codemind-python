n=int(input())
su=0
for i in range(n,0,-1):
    r=1/i
    su+=r
print('{0:.2f}'.format(su))