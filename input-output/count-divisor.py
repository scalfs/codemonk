l,r,k = list(map(int,input().split()))

n=0

for i in range(l,r+1):
    if not (i%k):
        n+=1
print(n)