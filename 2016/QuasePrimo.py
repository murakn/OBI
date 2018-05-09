n = [int(x) for x in input().split()][0]
k = [int(x) for x in input().split()]
c = 0
for e in range(n+1,1,-1):
    temp = True
    for i in k:
        if e%i == 0:
            temp = False
            break
    if temp:
        c += 1
print(c)
